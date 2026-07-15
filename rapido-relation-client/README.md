# rapido-relation-client

**Service client, fidélité et santé client en boucle** : SLA, CSAT/NPS, health score,
sauvetages et 100 premiers jours — orchestré sur **RapidoCRM** et **FoodEatUp**. Ce
plugin **orchestre** la relation client ; il **délègue** le triage et la rédaction aux
skills existants (`rapidocrm:ticket-triage`, `rapidocrm:draft-response`,
`rapidocrm:animation-client`, `foodeatup:handle-complaint`).

## Connecteurs (`.mcp.json`)
`rapidocrm` · `foodeatup` · `rapidocms` · `rapidorh` (Kanban) — URLs produit, auth par utilisateur.

## Skills
- **`pilotage-service-client`** — orchestrateur support (Sense→Plan→Act→Feed→Report) : SLA, priorisation SLA×valeur, récurrences → Kanban.
- **`boucle-nps`** — NPS mesuré et actionné (détracteurs→sauvetage, promoteurs→ambassadeurs).
- **`sante-client`** — health score composite (`scripts/health_score.py`, formule affichée) → portefeuille vert/orange/rouge.
- **`cent-premiers-jours`** — les 8 phases (Assess→Advocate) en jalons J+1…J+90 (Kanban RH).
- **`segmentation-rfm`** — RFM sur factures/commandes (`scripts/rfm.py`) → champions/à risque/endormis…

## Routines (registre unifié)
`RC-HEBDO` (pilotage-service-client), `RC-NPS-TRIMESTRE` (boucle-nps), `RC-SANTE-MENSUEL`
(sante-client) — recettes n8n dans `rapido-n8n/reference/recettes-relation-client.md`.

## Garde-fous
`reference/kb-templates/` (sla, sante-client, fidelite — seuils en KB, jamais en dur) ;
hook `garde-envois` (ask sur tout envoi client) + `Stop` (récap IDs/statuts/scores) ;
**scores par script** (formule affichée), calculs KPI via `catalogue-kpi` ; tout envoi
en **brouillon confirmé** ; ne duplique pas triage/rédaction (délégation).
