#!/usr/bin/env python3
"""Garde-fou ARGENT RÉEL (Meta Ads) :
- ask forcé sur : ads_activate_entity (début de dépense), ads_boost_ig_post
  UNIQUEMENT si confirmed=true (le plan confirmed=false passe librement),
  ads_update_entity UNIQUEMENT si la mise à jour touche un budget,
  ads_delete_custom_audience (met en pause les ad sets liés),
  ads_experiment_lift_create_test (étude payante).
Exit 0 + JSON = ask ; exit 0 sans sortie = allow. Aucun appel réseau."""
import json
import sys


def contient_budget(objet):
    """Cherche récursivement une clé contenant 'budget' ou 'spend_cap'."""
    if isinstance(objet, dict):
        for cle, valeur in objet.items():
            if "budget" in str(cle).lower() or "spend_cap" in str(cle).lower():
                return True
            if contient_budget(valeur):
                return True
    elif isinstance(objet, list):
        return any(contient_budget(v) for v in objet)
    elif isinstance(objet, str):
        # fields peut être une chaîne JSON sérialisée
        try:
            return contient_budget(json.loads(objet))
        except (ValueError, TypeError):
            return "budget" in objet.lower() or "spend_cap" in objet.lower()
    return False


def ask(raison):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": raison,
        }
    }))
    sys.exit(0)


try:
    data = json.load(sys.stdin)
except Exception:
    data = {}

tool = data.get("tool_name", "")
tool_input = data.get("tool_input") or {}

if tool.endswith("ads_activate_entity"):
    ask("💸 ACTIVATION = début de dépense réelle. Confirmer uniquement après "
        "récapitulatif : budget/jour, durée, cible, coût maximum estimé. "
        "Rappel : activer campagne → ad set → ad (top-down).")

if tool.endswith("ads_boost_ig_post"):
    if tool_input.get("confirmed"):
        ask("💸 Boost Instagram CONFIRMÉ (confirmed=true) : création réelle "
            "d'une promotion payante. Vérifier que le plan (confirmed=false) "
            "a été montré et approuvé, avec le budget dans la devise du compte.")
    sys.exit(0)  # plan (confirmed=false) : libre

if tool.endswith("ads_update_entity"):
    if contient_budget(tool_input):
        ask("💸 Modification de BUDGET sur une entité publicitaire : "
            "confirmer avec l'ancien et le nouveau budget (devise du compte) "
            "et le nouveau coût maximum estimé.")
    sys.exit(0)  # autre mise à jour (nom, statut pause…) : libre

if tool.endswith("ads_delete_custom_audience"):
    ask("⚠️ Suppression d'audience : les ad sets qui l'utilisent seront MIS "
        "EN PAUSE. Vérifier ads_get_custom_audience_adsets et prévenir "
        "l'utilisateur avant de confirmer.")

if tool.endswith("ads_experiment_lift_create_test"):
    ask("💸 Étude de lift = test PAYANT. Confirmer le coût et le périmètre "
        "avant création.")

sys.exit(0)
