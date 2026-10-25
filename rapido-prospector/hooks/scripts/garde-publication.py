#!/usr/bin/env python3
"""Hook PreToolUse — publications visibles et écritures de configuration.

Ask quand l'appel rend quelque chose PUBLIC ou change la configuration :
- add_webinar / update_webinar avec is_active à vrai (page publique) ;
- add/update_blog_post, add/update_calendar_post, add/update_video_post
  avec le statut « publie » ;
- prospection_terms avec add_kind (ajout d'un terme de prospection) ;
- add_linkedin_account / update_linkedin_account (comptes d'envoi).

Silence sinon (brouillons, lectures). Fail-closed : table
reference/outils-sensibles.json illisible → ask pour tout outil matché.
"""
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
PLUGIN = os.path.dirname(os.path.dirname(ICI))
RX_OUTIL = re.compile(r"^mcp__(?:plugin_[\w-]+_)?[Pp]rospect__([A-Za-z0-9_]+)$")


def ask(raison):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": "ask",
        "permissionDecisionReason": f"[garde-publication] {raison}"}}))
    sys.exit(0)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        data = {}
    m = RX_OUTIL.match(data.get("tool_name", ""))
    if not m:
        sys.exit(0)
    outil, entree = m.group(1), data.get("tool_input") or {}
    try:
        table = json.load(open(os.path.join(
            PLUGIN, "reference", "outils-sensibles.json"), encoding="utf-8"))
        publications = table["publications"]
        configuration = table["ecritures_configuration"]
    except Exception:  # noqa: BLE001
        ask("table des outils sensibles illisible (fail-closed) — "
            "confirmer cette écriture et relire reference/outils-sensibles.json")

    if outil in publications:
        regle = publications[outil]
        if entree.get(regle["champ"]) in regle["valeurs"]:
            ask(f"{outil} rend un contenu VISIBLE ({regle['champ']}="
                f"{entree.get(regle['champ'])!r} : {regle['raison']}). "
                "Montrer l'aperçu et confirmer la mise en ligne.")
        sys.exit(0)  # brouillon ou simple mise à jour : rien à bloquer

    if outil in configuration:
        declencheur = configuration[outil].get("champ_declencheur")
        if declencheur and not entree.get(declencheur):
            sys.exit(0)  # prospection_terms sans add_kind = lecture
        ask(f"{outil} : {configuration[outil].get('raison', 'écriture de configuration')}. "
            "Confirmer — la configuration engage tous les envois suivants.")
    sys.exit(0)


if __name__ == "__main__":
    main()
