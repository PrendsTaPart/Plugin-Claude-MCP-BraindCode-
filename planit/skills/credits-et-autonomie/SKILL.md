---
name: credits-et-autonomie
description: Utiliser quand les crédits Plan'It se pilotent, que l'utilisateur dit « combien me coûtent mes routines », « il me reste combien de jours de crédits », « lesquelles coûtent le plus cher », « et si je passais celle-ci en hebdo ». Calcule par script la consommation par routine, le classement, les jours d'autonomie et l'effet d'un changement de fréquence — formule affichée.
---

# Crédits et autonomie (les comptes, formule affichée)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow

1. **Collecter** : `get_kpi_home` (solde, jours d'autonomie annoncés),
   `list_routines` (coût mensuel estimé par routine), et `get_routine_report`
   sur les routines coûteuses (crédits réels consommés, moyenne par tour).
2. **Calculer, par script** : enregistrer les JSON et lancer
   `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/credits_autonomie.py bilan
   <home.json> <routines.json> [reports.json]` — il produit :
   - la consommation mensuelle par routine (mesurée quand le report la
     donne, estimée sinon — base dite) ;
   - le classement des plus coûteuses ;
   - les jours d'autonomie restants = solde / consommation quotidienne
     (formule affichée dans la sortie) ;
   - l'effet d'un changement de fréquence (option `--si <routine>
     <nouvelle_freq>`), à CONFIRMER par `estimate_routine_cost` avant toute
     proposition.
3. **Restituer** : le bilan + le widget `credits-par-routine` en option ;
   pour agir (changer une fréquence), passer par une proposition
   d'amélioration (skill `auditer-mes-routines`) — jamais un update direct.
4. Promotions de crédits : `list_promotions` (surface credits) — rien
   d'autre.

## Garde-fous

- Toute division et toute projection viennent du script, formule affichée —
  jamais de tête.
- Une estimation flat_price/default se distingue d'une consommation
  mesurée, ligne par ligne.
- Les jours d'autonomie du serveur (get_kpi_home) priment : notre calcul
  les recoupe, il ne les remplace pas (un écart se dit).
