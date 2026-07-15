#!/usr/bin/env python3
"""PreToolUse — garde argent réel TikTok Ads (le plus strict du marketplace).

TikTok Ads (MCP officiel récent) est en lecture/écriture sur tout le cycle
campagne. Règles :
  - CRÉATION avec un état ACTIF détecté → DENY (exit 2). On ne crée jamais une
    entité TikTok directement active : elle doit être inactive/brouillon.
  - ACTIVATION (enable/activate) ou présence d'un BUDGET → ASK (confirmation
    écrite, coût max annoncé, plafond ./rapido-kb/).
  - Lecture / création en état inactif → allow.

Contrat hook : deny = exit 2 + stderr ; ask = exit 0 + stdout JSON ;
allow = exit 0 sans stdout. Stdlib uniquement, sans réseau.
"""
import json
import sys

CREATION = ("create", "add")
ACTIVATION = ("activate", "enable", "update_status", "set_status", "publish")
ETATS_ACTIFS = {"active", "enable", "enabled", "delivery", "deliver", "on"}


def suffixe(tool):
    return tool.split("__")[-1] if tool else ""


def valeurs(obj, acc):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, str) and k.lower() in ("status", "operation_status",
                                                    "opt_status", "state", "delivery"):
                acc.append(v.lower())
            valeurs(v, acc)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            valeurs(v, acc)


def a_budget(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if "budget" in k.lower() and v not in (None, "", 0):
                return True
            if a_budget(v):
                return True
    elif isinstance(obj, (list, tuple)):
        return any(a_budget(v) for v in obj)
    return False


def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    tool = data.get("tool_name", "") or ""
    if "tiktok" not in tool.lower():
        return 0  # allow — pas TikTok
    ti = data.get("tool_input") or {}
    s = suffixe(tool).lower()

    etats = []
    valeurs(ti, etats)
    etat_actif = any(e in ETATS_ACTIFS for e in etats)

    # 1) Création avec état actif → DENY
    if any(k in s for k in CREATION) and etat_actif:
        sys.stderr.write(
            f"⛔ Création TikTok en état ACTIF refusée ({tool}). Règle verrouillée : "
            "une entité TikTok se crée INACTIVE/brouillon, jamais active. Relancer sans "
            "l'état actif (status inactif), puis activer séparément sur confirmation écrite.\n"
        )
        return 2

    # 2) Activation ou budget → ASK
    if any(k in s for k in ACTIVATION) or etat_actif or a_budget(ti):
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "ask",
                "permissionDecisionReason": (
                    f"💸 Action TikTok à argent réel ({tool}) : confirmation écrite requise. "
                    "Annoncer le budget/coût MAX, respecter le plafond ./rapido-kb/ "
                    "(jamais plus de X €/jour sans validation), activation séparée et explicite."
                ),
            }
        }, ensure_ascii=False))
        return 0

    return 0  # allow — lecture ou création inactive


if __name__ == "__main__":
    sys.exit(main())
