---
name: etude-de-marche-terrain
description: Utiliser quand on va chercher la vérité sur le terrain, que l'utilisateur dit « prépare l'étude de marché », « fais-moi la grille d'entretien des restaurateurs », « saisis les résultats de mes visites ». Prépare les entretiens depuis le gabarit Academy, consigne les résultats réels et en tire la synthèse.
---

# Étude de marché terrain (préparer, consigner, synthétiser)

Familles engagées : **apprendre** (gabarit, synthèse) + **configurer**
(`submit_market_study_results`).

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow

1. **`get_market_study_template`** — le gabarit maison : qui interroger,
   combien, quelles questions, comment noter.
2. **Préparer les entretiens** : la grille par cible (depuis le gabarit, et
   les personas de `get_onglet` personas), le planning des visites, le
   script d'approche — tout en brouillon remis à l'humain : c'est LUI qui va
   sur le terrain.
3. **Consigner** : après chaque vague, **`submit_market_study_results`**
   avec les réponses RÉELLES rapportées (aperçu → accord → confirm) — un
   entretien non fait n'est jamais « reconstitué ».
4. **La synthèse** : `get_market_study_summary` — restituée telle quelle,
   avec les trous dits ; en tirer les ajustements du plan (skill
   `business-plan`, hypothèses) et des personas de prospection.

KPI : `taux-prospection-rdv` (une étude juste améliore le ciblage).
Formations : `personas`, `prospection`, `business-plan`.

## Garde-fous

- Les résultats saisis sont ceux du terrain, mot pour mot quand c'est
  possible — aucun verbatim inventé, aucun « ressenti » transformé en
  donnée.
- La synthèse sert le plan ; elle ne se publie nulle part sans accord.
