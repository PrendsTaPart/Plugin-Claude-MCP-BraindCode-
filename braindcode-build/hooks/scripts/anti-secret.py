#!/usr/bin/env python3
"""Hook PreToolUse — aucun secret ne quitte la session.

Deny si l'entrée de send_message, create_project, request_human_validation,
report_blocker, save_project_progress, set_project_knowledge ou
publish_project contient un motif de secret : clé API, jeton Bearer ou JWT,
service_role, clé Stripe sk_, mot de passe en clair. Les secrets se règlent
dans l'éditeur Lovable ou le tableau de bord — jamais dans une demande, un
blocage, un message ou une trace. Le refus ne RECOPIE jamais le secret :
il nomme le motif détecté.
"""
import json
import re
import sys

OUTILS = {"send_message", "create_project", "request_human_validation",
          "report_blocker", "save_project_progress", "set_project_knowledge",
          "publish_project"}
RX_OUTIL = re.compile(
    r"^mcp__(?:plugin_[\w-]+_)?(?:[Ll]ovable|[Bb]raindcode[-_][Bb]uild)__"
    r"([A-Za-z0-9_]+)$")
MOTIFS = [
    ("clé Stripe sk_", re.compile(r"\bsk_(?:live|test)_[A-Za-z0-9]{8,}")),
    ("jeton JWT", re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}")),
    ("jeton Bearer", re.compile(r"\bBearer\s+[A-Za-z0-9_\-.]{16,}", re.I)),
    ("service_role", re.compile(r"service_role", re.I)),
    ("clé API affectée", re.compile(
        r"(?:api[_-]?key|apikey|secret[_-]?key|access[_-]?token)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{12,}",
        re.I)),
    ("mot de passe en clair", re.compile(
        r"(?:password|mot de passe|passwd)\s*[:=]\s*\S{6,}", re.I)),
]


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        sys.exit(0)
    m = RX_OUTIL.match(data.get("tool_name", ""))
    if not m or m.group(1) not in OUTILS:
        sys.exit(0)
    texte = json.dumps(data.get("tool_input") or {}, ensure_ascii=False)
    for nom, rx in MOTIFS:
        if rx.search(texte):
            print(f"[anti-secret] REFUS : motif « {nom} » détecté dans "
                  f"l'entrée de {m.group(1)}. Aucun secret ne part dans une "
                  "demande, un blocage, un message Lovable, un knowledge ou "
                  "une trace : règle-le dans l'éditeur Lovable ou le tableau "
                  "de bord, et reformule l'entrée sans le secret.",
                  file=sys.stderr)
            sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
