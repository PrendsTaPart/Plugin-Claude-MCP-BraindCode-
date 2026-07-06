# Changelog — plugin rapidocrm

## 0.4.0 — 2026-07-06

- Script de calcul `skills/coaching-pipeline/scripts/funnel_metrics.py`
  (stdlib) : conversions par étape, maillon faible, deals dormants, valeur
  brute/pondérée — le skill impose « utiliser le script pour tout calcul ;
  ne jamais calculer de tête ».
- `reference/pieges-outils.md` : tableau des pièges (transitions DGFiP,
  company_id/user_id de session, confirm=true pour suppressions, formats de
  dates, message vs template SMS…), référencé par les directives.

## 0.3.0 — 2026-07-06

- Hooks déterministes (`hooks/hooks.json` + `hooks/scripts/`) :
  - PreToolUse `garde-destructif` : confirmation forcée (ask) sur `delete_*`,
    `update_contrat_status`, `close_opportunity` et `update_invoice_status` ;
    refus (deny) de toute transition de facture vers un statut non autorisé par
    la table DGFiP encodée dans le script (cibles valides : en_attente, payee,
    en_retard — jamais de retour à brouillon). `update_invoice_status` est
    matché défensivement (outil non exposé par le serveur à ce jour) ;
  - Stop `récap-actions` (hook prompt) : bloque la fin de tour si des écritures
    MCP ont eu lieu sans récapitulatif des IDs dans la réponse.

## 0.2.0 — 2026-07-06

- Ajout de la couche métier :
  - Agents : `directeur-commercial` (funnel, qualification BANT avant devis,
    relances J+3/J+7/J+15, pilotage par objectifs) et `sdr-prospection`
    (ciblage, personnalisation, cadence multicanal, qualification, passage de
    relais au closing).
  - Skills d'expertise : `coaching-pipeline` (revue de deals — dormants, devis
    expirants, étapes engorgées, une action par deal) et
    `redaction-commerciale` (AIDA/PAS, objet < 50 caractères, 1 CTA,
    personnalisation obligatoire, ton par étape du funnel).
- Les agents connaissent et invoquent les skills du plugin au bon moment.

## 0.1.0 — 2026-07-06

- Version initiale : `.mcp.json` (serveur rapidocrm), références
  `directives-outils.md` et `charte-graphique.md`, skills workflow
  `prospection-pipeline`, `campagne-marketing`, `devis-facture-relance`,
  `communication-client`, `performance-commerciale`.
