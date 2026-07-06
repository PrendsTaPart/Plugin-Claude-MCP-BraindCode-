# Changelog — plugin rapidocrm

## 0.9.0 — 2026-07-06

- Intégration de 3 skills wondelai/skills (MIT, contenu non modifié — skills
  basés sur des livres ; LICENSE dans chaque dossier, provenance ajoutée à
  skills/ATTRIBUTIONS.md) : `predictable-revenue` (machine outbound B2B),
  `negotiation` (empathie tactique, questions calibrées, Ackerman),
  `mom-test` (interviews clients sans biais).

## 0.8.0 — 2026-07-06

- Intégration de 6 skills externes Apache 2.0 depuis
  anthropics/knowledge-work-plugins (commit 564d560c, LICENSE copiée dans
  chaque dossier, provenance tracée dans skills/ATTRIBUTIONS.md) :
  - vente : `pipeline-review-methodo` (renommé depuis pipeline-review pour ne
    pas confondre avec coaching-pipeline), `draft-outreach`,
    `account-research`, `forecast` ;
  - support : `ticket-triage`, `draft-response`.
- Chaque description se termine par « (utilise les données du MCP rapidocrm
  quand elles sont disponibles) » pour croiser la méthode avec les vraies
  données CRM.

## 0.7.0 — 2026-07-06

- Passe de portabilité : devise lue depuis la KB (défaut euros signalé).

## 0.6.0 — 2026-07-06

- Couverture des outils orphelins — 3 nouveaux skills :
  - `contrats-clients` : `create_contrat_template` → `create_contrat`
    (⚠️ send_email TRUE par défaut : validation du destinataire avant appel) →
    `update_contrat_status` (brouillon/en_attente/signe), relance des
    non-signés à la cadence maison ;
  - `agenda-rdv` : `create_rdv` (Visioconférence/Téléphonique/Présentiel avec
    champs conditionnels, mode_envoi SMS/Email confirmé avant),
    `get_today_schedule` (vérification de conflits), `create_evenement` ;
  - `studio-templates` : `create_editor_template` appelé DIRECTEMENT avec le
    HTML (jamais de widget intermédiaire), charte KB imposée dans le HTML/CSS,
    contraintes email-safe pour les newsletters.

## 0.5.0 — 2026-07-06

- Utilisation de la base de connaissance `./rapido-kb/` : règle de chargement
  dans les directives ; `directeur-commercial` : cadence de relance maison
  (processus-internes.md) sinon défaut J+3/J+7/J+15 signalé ;
  `coaching-pipeline` : seuil dormant et cadences maison ;
  `devis-facture-relance` : escalade d'impayés maison sinon J+7/J+21/J+45 ;
  `redaction-commerciale` : arguments depuis propositions-valeur.md,
  objections/parades depuis concurrents.md, ton depuis ton-et-accroches.md.

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
