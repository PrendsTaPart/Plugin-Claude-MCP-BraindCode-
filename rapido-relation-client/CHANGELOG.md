# Changelog — plugin rapido-relation-client

## 0.1.0 — 2026-07-15 — Service client & fidélité (5 skills, 3 routines)

- Nouveau plugin **rapido-relation-client** (21e du marketplace) — service client,
  fidélité et santé client **en boucle**, orchestré sur RapidoCRM/FoodEatUp. **Délègue**
  triage/rédaction/animation/réclamations aux skills existants.
- `.mcp.json` : rapidocrm, foodeatup, rapidocms, rapidorh.
- `reference/kb-templates/` : `sla.md`, `sante-client.md` (pondérations health score),
  `fidelite.md` (seuils NPS, segments RFM).
- **5 skills** : `pilotage-service-client` (Sense→…→Report, SLA×valeur, récurrences →
  Kanban ; anti-collision ticket-triage), `boucle-nps` (mesure + actions par segment ;
  promoteurs → ambassadeurs), `sante-client` (health score `scripts/health_score.py`,
  formule affichée, vert/orange/rouge), `cent-premiers-jours` (8 phases → jalons
  J+1…J+90 Kanban ; J+60 → ambassadeur ; réécrit, aucun verbatim), `segmentation-rfm`
  (`scripts/rfm.py`, quintiles → segments).
- **Hooks** : `garde-envois` (ask sur envois client) + `Stop` (récap IDs/statuts/scores/
  sources). **Scores par script**, calculs KPI via `catalogue-kpi`.
- Routines `RC-HEBDO` / `RC-NPS-TRIMESTRE` / `RC-SANTE-MENSUEL` au registre unifié +
  `rapido-n8n/reference/recettes-relation-client.md`.
