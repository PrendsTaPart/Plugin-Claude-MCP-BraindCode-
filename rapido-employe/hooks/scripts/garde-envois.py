#!/usr/bin/env python3
"""Garde des envois et publications (PreToolUse) — l'aperçu, c'est nous.

Plusieurs serveurs (Prospector Hub en tête) n'ont NI aperçu NI confirmation :
un send_email part tout de suite. Ce garde impose donc, quel que soit le
niveau d'autonomie :

- DENY sur l'envoi Gmail direct (send_message, reply, forward, send_draft du
  serveur Gmail) : le brouillon Gmail (create_draft) le remplace, l'humain
  envoie ;
- DENY quand le QUOTA du jour est atteint (envois / publications / réponses —
  quotas relus dans le cadre .claude/state/cadre-employe.json, compteurs
  tenus par le hook journal-ecritures dans .claude/state/compteurs-envois.json) ;
- ask systématique sur tout envoi, publication ou réponse publique (listes
  `envois_ask` + quotas de reference/familles-outils.json) : destinataires,
  objet et texte se montrent AVANT, sur un modèle validé, avec l'expéditeur
  et un moyen de refuser.

Clés racine de test CI : `cadre_test`, `compteurs_test`. Aucun appel réseau.
"""
import datetime
import json
import os
import re
import sys

RACINE_PLUGIN = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
TABLE = os.path.join(RACINE_PLUGIN, "reference", "familles-outils.json")
ETAT_CADRE = os.path.join(".claude", "state", "cadre-employe.json")
ETAT_COMPTEURS = os.path.join(".claude", "state", "compteurs-envois.json")
RX_MCP = re.compile(r"^mcp__(.+)__([A-Za-z0-9_-]+)$")
QUOTAS = (("quota_envois", "envoisJour", "envois"),
          ("quota_publications", "publicationsJour", "publications"),
          ("quota_reponses", "reponsesJour", "reponses"))


def ask(raison):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "ask",
        "permissionDecisionReason": raison,
    }}, ensure_ascii=False))
    sys.exit(0)


def deny(raison):
    print(f"garde-envois : {raison}", file=sys.stderr)
    sys.exit(2)


def charger(chemin, cle_test, payload):
    if payload.get(cle_test) is not None:
        return payload[cle_test]
    try:
        with open(chemin, encoding="utf-8") as f:
            return json.load(f)
    except Exception:  # noqa: BLE001
        return {}


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        sys.exit(0)
    m = RX_MCP.match(payload.get("tool_name", ""))
    if not m:
        sys.exit(0)
    serveur_brut, outil = m.group(1).lower(), m.group(2)
    try:
        with open(TABLE, encoding="utf-8") as f:
            table = json.load(f)
    except Exception:  # noqa: BLE001
        table = {}

    if "gmail" in serveur_brut and f"gmail:{outil}" in set(
            table.get("envois_deny_direct", [])):
        deny(f"l'envoi Gmail direct est interdit : préparer un BROUILLON "
             f"(create_draft) à la place de « {outil} » — l'humain envoie.")

    concernes = set(table.get("envois_ask", []))
    for liste, _, _ in QUOTAS:
        concernes |= {c.split(":", 1)[-1] for c in table.get(liste, [])}
    if outil not in concernes:
        sys.exit(0)

    cadre = charger(ETAT_CADRE, "cadre_test", payload)
    compteurs = charger(ETAT_COMPTEURS, "compteurs_test", payload)
    jour = datetime.date.today().isoformat()
    du_jour = compteurs.get(jour, {}) if isinstance(compteurs, dict) else {}
    quotas = (cadre or {}).get("quotas_jour", {})
    for liste, cle_quota, cle_compteur in QUOTAS:
        noms = {c.split(":", 1)[-1] for c in table.get(liste, [])}
        if outil in noms and cle_quota in quotas:
            if int(du_jour.get(cle_compteur, 0)) >= int(quotas[cle_quota]):
                deny(f"quota du jour atteint ({cle_compteur} : "
                     f"{du_jour.get(cle_compteur, 0)}/{quotas[cle_quota]}, "
                     f"cadre get_work_plan) — « {outil} » attendra demain ou "
                     "une décision du responsable.")
    ask(f"« {outil} » part vers l'extérieur : montrer destinataires, objet et "
        "texte (modèle validé, expéditeur nommé, moyen de refuser), puis "
        "attendre l'accord. Les outils de ce serveur n'ont pas d'aperçu : "
        "l'aperçu, c'est nous.")


if __name__ == "__main__":
    main()
