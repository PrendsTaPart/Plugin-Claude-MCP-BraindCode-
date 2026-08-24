#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest import mock


SCRIPT = Path(__file__).with_name("generate_mcp_config.py")
SPEC = importlib.util.spec_from_file_location("generate_mcp_config", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

REPO = Path(__file__).resolve().parents[2]


class GenerateMcpConfigTests(unittest.TestCase):
    def test_core_config_is_deduplicated_and_oauth_enabled(self) -> None:
        result = MODULE.build_config(
            REPO,
            list(MODULE.CORE_PLUGINS),
            core_only=True,
            expand_url_env=False,
        )
        self.assertEqual(
            list(result["servers"]),
            ["foodeatup", "rapidocms", "rapidocrm", "rapidorh"],
        )
        for server in result["servers"].values():
            self.assertEqual(server["transport"], "streamable-http")
            self.assertEqual(server["auth"], "oauth")
            self.assertNotIn("cwd", server)
            self.assertNotIn("command", server)
        self.assertEqual(result["skipped"], [])
        static_core = json.loads(
            (Path(__file__).with_name("core-mcp.json")).read_text(encoding="utf-8")
        )
        self.assertEqual(static_core, result)

    def test_unresolved_satellite_url_is_reported_without_secret_expansion(self) -> None:
        with mock.patch.dict(os.environ, {}, clear=True):
            result = MODULE.build_config(
                REPO,
                ["rapido-suite"],
                core_only=False,
                expand_url_env=False,
            )
        skipped = {item["server"]: item for item in result["skipped"]}
        self.assertIn("n8n", skipped)
        self.assertEqual(skipped["n8n"]["variables"], ["N8N_MCP_URL"])
        self.assertNotIn("n8n", result["servers"])

    def test_url_expansion_is_opt_in(self) -> None:
        with mock.patch.dict(
            os.environ, {"N8N_MCP_URL": "https://n8n.example.test/mcp"}, clear=True
        ):
            unresolved = MODULE.build_config(
                REPO,
                ["rapido-suite"],
                core_only=False,
                expand_url_env=False,
            )
            expanded = MODULE.build_config(
                REPO,
                ["rapido-suite"],
                core_only=False,
                expand_url_env=True,
            )
        self.assertNotIn("n8n", unresolved["servers"])
        self.assertEqual(
            expanded["servers"]["n8n"]["url"], "https://n8n.example.test/mcp"
        )

    def test_conflicting_duplicate_names_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / ".claude-plugin").mkdir()
            for plugin in ("one", "two"):
                (root / plugin).mkdir()
            (root / ".claude-plugin" / "marketplace.json").write_text(
                json.dumps(
                    {
                        "plugins": [
                            {"name": "one", "source": "./one"},
                            {"name": "two", "source": "./two"},
                        ]
                    }
                ),
                encoding="utf-8",
            )
            (root / "one" / ".mcp.json").write_text(
                json.dumps(
                    {"mcpServers": {"same": {"type": "http", "url": "https://a.test/mcp"}}}
                ),
                encoding="utf-8",
            )
            (root / "two" / ".mcp.json").write_text(
                json.dumps(
                    {"mcpServers": {"same": {"type": "http", "url": "https://b.test/mcp"}}}
                ),
                encoding="utf-8",
            )
            with self.assertRaises(MODULE.ConfigError):
                MODULE.build_config(
                    root,
                    ["one", "two"],
                    core_only=False,
                    expand_url_env=False,
                )


if __name__ == "__main__":
    unittest.main()
