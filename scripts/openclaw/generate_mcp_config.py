#!/usr/bin/env python3
"""Convert Claude marketplace .mcp.json files to OpenClaw MCP entries.

The converter is deliberately deterministic and never resolves credentials.
Environment variables are expanded only in server URLs, and only when
``--expand-url-env`` is explicitly requested. Header and process environment
placeholders stay as ``${NAME}`` so secrets never transit through stdout.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import sys
from typing import Any


CORE_PLUGINS = (
    "rapido-suite",
    "rapidocrm",
    "rapidocms",
    "rapidorh",
    "foodeatup",
)

CORE_SERVERS = frozenset(("rapidocrm", "rapidocms", "rapidorh", "foodeatup"))

# Sources documented by the marketplace as OAuth-first. URL-based/private
# gateways are intentionally not guessed here.
OAUTH_SERVERS = frozenset(
    (
        "canva",
        "facebook-ads",
        "foodeatup",
        "gmail",
        "google-calendar",
        "google-drive",
        "hyperframes",
        "lovable",
        "rapidocms",
        "rapidocrm",
        "rapidorh",
        "stripe",
    )
)

ENV_PATTERN = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)\}")


class ConfigError(ValueError):
    """Raised when marketplace MCP declarations are ambiguous or invalid."""


def _load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ConfigError(f"Fichier introuvable : {path}") from exc
    except json.JSONDecodeError as exc:
        raise ConfigError(f"JSON invalide dans {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ConfigError(f"Objet JSON attendu dans {path}")
    return value


def marketplace_plugins(repo: Path) -> dict[str, Path]:
    manifest_path = repo / ".claude-plugin" / "marketplace.json"
    manifest = _load_json(manifest_path)
    result: dict[str, Path] = {}
    for item in manifest.get("plugins", []):
        if not isinstance(item, dict):
            continue
        name = item.get("name")
        source = item.get("source")
        if isinstance(name, str) and isinstance(source, str):
            result[name] = (repo / source).resolve()
    return result


def _resolve_url(
    raw_url: str, *, expand_url_env: bool
) -> tuple[str | None, list[str]]:
    variables = ENV_PATTERN.findall(raw_url)
    if not variables:
        return raw_url, []

    missing = [name for name in variables if not os.environ.get(name)]
    if missing or not expand_url_env:
        return None, missing or variables

    return ENV_PATTERN.sub(lambda match: os.environ[match.group(1)], raw_url), []


def normalize_server(
    name: str, raw: dict[str, Any], *, expand_url_env: bool
) -> tuple[dict[str, Any] | None, list[str]]:
    """Return one OpenClaw server entry and unresolved URL variables."""

    if "url" in raw:
        url = raw.get("url")
        if not isinstance(url, str) or not url.strip():
            raise ConfigError(f"URL MCP invalide pour {name}")
        resolved_url, unresolved = _resolve_url(
            url.strip(), expand_url_env=expand_url_env
        )
        if resolved_url is None:
            return None, unresolved

        raw_type = raw.get("type", "http")
        if raw_type not in ("http", "sse"):
            raise ConfigError(f"Transport MCP distant non supporté pour {name}: {raw_type}")

        entry: dict[str, Any] = {
            "url": resolved_url,
            "transport": "streamable-http" if raw_type == "http" else "sse",
        }
        headers = raw.get("headers")
        if headers is not None:
            if not isinstance(headers, dict):
                raise ConfigError(f"Headers MCP invalides pour {name}")
            entry["headers"] = headers
        if name in OAUTH_SERVERS:
            entry["auth"] = "oauth"
        return entry, []

    command = raw.get("command")
    if not isinstance(command, str) or not command.strip():
        raise ConfigError(f"URL ou commande MCP requise pour {name}")
    entry = {"command": command.strip()}
    for optional_key in ("args", "env"):
        if optional_key in raw:
            entry[optional_key] = raw[optional_key]
    return entry, []


def build_config(
    repo: Path,
    selected_plugins: list[str],
    *,
    core_only: bool,
    expand_url_env: bool,
) -> dict[str, Any]:
    known_plugins = marketplace_plugins(repo)
    unknown = sorted(set(selected_plugins) - set(known_plugins))
    if unknown:
        raise ConfigError("Plugin(s) inconnu(s) : " + ", ".join(unknown))

    servers: dict[str, dict[str, Any]] = {}
    origins: dict[str, str] = {}
    skipped: list[dict[str, Any]] = []

    for plugin_name in selected_plugins:
        mcp_path = known_plugins[plugin_name] / ".mcp.json"
        if not mcp_path.is_file():
            continue
        document = _load_json(mcp_path)
        declared = document.get("mcpServers", {})
        if not isinstance(declared, dict):
            raise ConfigError(f"mcpServers doit être un objet dans {mcp_path}")

        for server_name, raw_server in declared.items():
            if core_only and server_name not in CORE_SERVERS:
                continue
            if not isinstance(server_name, str) or not isinstance(raw_server, dict):
                raise ConfigError(f"Déclaration MCP invalide dans {mcp_path}")

            normalized, unresolved = normalize_server(
                server_name, raw_server, expand_url_env=expand_url_env
            )
            if normalized is None:
                skipped.append(
                    {
                        "server": server_name,
                        "plugin": plugin_name,
                        "reason": "unresolved_url_environment",
                        "variables": sorted(set(unresolved)),
                    }
                )
                continue

            if server_name in servers and servers[server_name] != normalized:
                raise ConfigError(
                    f"Conflit MCP '{server_name}' entre {origins[server_name]} "
                    f"et {plugin_name}"
                )
            servers[server_name] = normalized
            origins[server_name] = plugin_name

    unique_skipped: dict[tuple[str, str, tuple[str, ...]], dict[str, Any]] = {}
    for item in skipped:
        if item["server"] in servers:
            continue
        key = (
            item["server"],
            item["reason"],
            tuple(item["variables"]),
        )
        unique_skipped.setdefault(key, item)

    return {
        "schemaVersion": 1,
        "servers": dict(sorted(servers.items())),
        "skipped": sorted(
            unique_skipped.values(), key=lambda item: (item["server"], item["plugin"])
        ),
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Génère les entrées MCP OpenClaw depuis la marketplace Rapido."
    )
    parser.add_argument(
        "--repo",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Racine du clone de la marketplace.",
    )
    parser.add_argument(
        "--plugin",
        action="append",
        dest="plugins",
        help="Plugin à lire (répétable). Par défaut : noyau Rapido.",
    )
    parser.add_argument(
        "--include-satellites",
        action="store_true",
        help="Inclut les MCP satellites déclarés par les plugins sélectionnés.",
    )
    parser.add_argument(
        "--expand-url-env",
        action="store_true",
        help="Résout explicitement ${VAR} dans les URL (jamais dans les secrets).",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        result = build_config(
            args.repo.resolve(),
            args.plugins or list(CORE_PLUGINS),
            core_only=not args.include_satellites,
            expand_url_env=args.expand_url_env,
        )
    except ConfigError as exc:
        print(f"ERREUR: {exc}", file=sys.stderr)
        return 2
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
