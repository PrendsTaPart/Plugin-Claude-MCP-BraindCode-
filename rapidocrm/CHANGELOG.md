# Changelog — plugin rapidocrm

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
