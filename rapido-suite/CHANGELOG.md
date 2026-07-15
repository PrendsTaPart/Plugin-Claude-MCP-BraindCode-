# Changelog — plugin rapido-suite

## 1.4.0 — 2026-07-14

Branchement de la base de connaissance sur la couche marque RapidoCMS (la KB
reste PRIORITAIRE ; le CMS est le miroir d'exécution) :

- `onboarding-entreprise` : nouvelle Phase 3 bis « Miroir CMS » (optionnelle,
  non bloquante) — après la charte, proposer la création de la marque via le
  skill `gestion-marques` (rapidocms), mapping validé par l'utilisateur, puis
  écrire `> Miroir CMS : brand_id <id> — dernière sync <date>` dans
  `charte-graphique.md`. Plugin rapidocms absent / MCP indisponible → signalé,
  on continue.
- `mise-a-jour-kb` : sync DESCENDANTE — quand une modif touche
  charte-graphique.md (couleurs/logo/slogan/fonts) et qu'un brand_id est en KB,
  proposer `edit_brand` des seuls champs modifiés après confirmation, puis
  mettre à jour la date de sync. Jamais de sync silencieuse.
- `onboarding-client-360` : acte CMS crée aussi la marque du client
  (`create_brand`) + importe le logo via `bibliotheque-assets`, brand_id et
  asset_id consignés au récapitulatif.
- `reference/sync-marque.md` (nouveau) : note courte renvoyant à
  `rapidocms/reference/outils-marque.md` (règles non dupliquées).
- tests/evals.md : 5 scénarios de sync (dont dégradé sans rapidocms et
  frontière sans brand_id).

## 1.3.0 — 2026-07-11

- Nouveau skill `pilotage-entreprise` : « Pilote mon entreprise » — le
  prompt maître du kit (`rapido-kb-template/PROMPT-PILOTAGE.md`) encodé
  en skill. Étape 0 obligatoire (KB entière + autonomie.md + vérif
  serveurs), puis Sense → Plan → Act → Feed → Report sur TOUS les
  domaines (finance, ventes, marketing, équipe, resto, automatisations) ;
  KPI via catalogue-kpi uniquement, récap groupé avant toute écriture,
  report une page. Frontières documentées vers monday-brief,
  business-pulse, comite-de-direction, R4-R9 et lancement-projet-360.
  tests/evals.md : 3 scénarios P1-P3.

## 1.2.0 — 2026-07-10

- Nouveau skill `lancement-projet-360` : l'orchestrateur « je lance un
  nouveau SaaS » de bout en bout — 5 actes (Penser via rapido-forge →
  Structurer RH + prévisionnel → Construire landing/marque/visuels →
  Vendre & raconter → Automatiser & mesurer), validation OBLIGATOIRE entre
  chaque acte, livrables méthodo en KB avant exécution, récapitulatif par
  acte avec IDs réels ; ads toujours en PAUSED (argent réel, accord
  explicite). tests/evals.md créé (3 déclenchements + non-régression).

## 1.1.0 — 2026-07-10

- Serveur n8n déclaré dans `.mcp.json` (`${N8N_MCP_URL}`, optionnel —
  dégradation propre) : comite-de-direction et revue-hebdo-business
  citaient `search_workflows`/`search_executions` via « plugin rapido-n8n
  co-installé » — le serveur est désormais porté par le plugin lui-même,
  même pattern que rapido-direction. Formulations ajustées.

## 1.0.1 — 2026-07-10

- Corrections documentaires (audit) : dossier-startup-360 —
  `upload_file_tool` `type: "document"` → `type: "doc"` (enum réel vérifié
  serveur : image, video, doc ; écart ouvert depuis le 06/07, aucune autre
  occurrence dans le dépôt).
- pieges-outils : ligne `update_invoice_status` (FoodEatUp) — enum élargi,
  transitions DGFiP validées PAR LE SERVEUR, ne pas pré-filtrer côté skill.
- Hook anti-donnee-inventee (copie locale) aligné sur foodeatup 1.2.1 :
  refus de tout `add_temperature` sans `equipment_id` (requis par le schéma
  serveur, résolution via `search_entities`) — testé stdin.

## 1.0.0 — 2026-07-06

- Première version publique.

## 0.14.0 — 2026-07-06

- Skill `dossier-startup-360` : la mémoire de l'entreprise pour les agents
  IA — dossier `./rapido-kb/startup/` en 8 fichiers (vision, persona,
  marché, offre, identité, traction, pitch, roadmap), interview guidée,
  chiffres sourcés MCP, publication en bibliothèque CMS
  (`upload_file_tool`) et projets RH (`create-project-link-tool`), règle
  transverse de lecture par tous les agents Rapido.
- Agent `directeur-general` : lit `./rapido-kb/startup/` (01-vision,
  02-persona, 05-identite) avant toute production quand il existe ;
  06-traction ou 08-roadmap datés de plus de 30 jours déclenchent une
  proposition de mise à jour via `mise-a-jour-kb`.

## 0.13.0 — 2026-07-06

- Intégration du skill `skill-creator` d'anthropics/skills (Apache 2.0,
  LICENSE.txt conservé, entrée ATTRIBUTIONS.md) : création, amélioration et
  évaluation des skills maison de la marketplace. Premier usage :
  `onboarding-restaurateur` (plugin foodeatup).

## 0.12.0 — 2026-07-06

- Intégration de 4 skills Apache 2.0 du pack small-business
  d'anthropics/knowledge-work-plugins (LICENSE dans chaque dossier,
  provenance dans ATTRIBUTIONS.md) : `monday-brief` (brief prospectif du
  lundi), `business-pulse` (snapshot une-page à la demande, renvoi croisé
  vers revue-hebdo-business), `cash-flow-snapshot` (projection de trésorerie
  30/60/90 j), `invoice-chase` (relances d'impayés avec ton gradué).
- `friday-brief` FUSIONNÉ dans revue-hebdo-business au lieu d'être copié
  (recoupement trop fort) : chiffres clés comparés à la période précédente,
  top ventes, section « Wins & watches ».
- Adaptation : mention MCP/KB en description + section « Adaptation Rapido »
  dans chaque skill copié (mapping des outils US vers les équivalents Rapido).

## 0.11.0 — 2026-07-06

- Passe de portabilité : devise lue depuis la KB ou le compte connecté ; `onboarding-entreprise` gagne le bloc « réglages techniques » (fuseau horaire, devise, establishment_id FoodEatUp, plafond budget pub/jour, rappel N8N_MCP_URL).

## 0.10.0 — 2026-07-06

- Agent `directeur-general` : devient l'orchestrateur A→Z — délègue aux
  agents de domaine (chef-restaurateur, directeur-commercial,
  responsable-marketing, studio-creatif, chef-de-projet/responsable-rh,
  media-buyer, assistant-direction, workflows n8n), consolide en une
  synthèse, tranche selon la KB.

## 0.9.0 — 2026-07-06

- Domaine « Automatisations » ajouté à `revue-hebdo-business` et
  `comite-de-direction` (si le plugin rapido-n8n est installé et N8N_MCP_URL
  définie) : workflows actifs vs registre KB, taux de succès, échecs à
  traiter.

## 0.8.0 — 2026-07-06

- Domaine « Acquisition payante » ajouté à `revue-hebdo-business` et
  `comite-de-direction` (si le plugin rapido-meta-ads est installé) :
  dépense, coût par résultat (`ads_get_ad_entities` avec période), anomalies,
  lu en coût par CLIENT via les leads CRM.

## 0.7.0 — 2026-07-06

- Domaine « Web / Produits » ajouté à `revue-hebdo-business` et
  `comite-de-direction` (si le plugin rapido-lovable est installé) :
  `list_projects` publiés + `get_project_analytics` (RFC 3339, même période),
  croisés avec `get_stats_campagne` (le trafic vient-il des campagnes ?).

## 0.6.0 — 2026-07-06

- Règle de chargement KB enrichie dans les directives (routage fichier par
  type de production ; hiérarchie : opérationnel = MCP live d'abord, marque =
  KB d'abord avec API en vérification) ; agent `directeur-general` cite ses
  sources KB. Évals « avec KB vs sans KB » ajoutées au dépôt (tests/evals.md).

## 0.5.0 — 2026-07-06

- Système d'onboarding entreprise → base de connaissance `./rapido-kb/`
  (8 fichiers markdown dans le RÉPERTOIRE DE TRAVAIL du client, jamais dans le
  plugin : versionnable, éditable, survit aux mises à jour) :
  - skill `onboarding-entreprise` : collecte auto via les 4 MCP (jamais
    demander ce que les serveurs savent), interview guidée par blocs de 3-4
    questions, rédaction + validation, câblage ; « je ne sais pas » =
    `### À COMPLÉTER`, jamais de données inventées ;
  - skill `mise-a-jour-kb` : table changement → fichier, relecture avant
    modification, questions ciblées, datation en tête de fichier ;
  - hook SessionStart : détecte `./rapido-kb/` — absent → suggère
    l'onboarding ; présent → liste les fichiers disponibles ;
  - directives et charte : hiérarchie des sources MCP live > KB > références
    génériques du plugin ; l'agent `directeur-general` ancre ses arbitrages
    dans les seuils maison de la KB.

## 0.4.0 — 2026-07-06

- `reference/pieges-outils.md` : condensé multi-serveurs (establishment_id
  FoodEatUp vs session CRM/CMS/RH, deux create_campagne différents, formats de
  dates divergents CRM/CMS, DGFiP, priorités RH…), référencé par les
  directives.

## 0.3.0 — 2026-07-06

- Hooks déterministes (`hooks/hooks.json` + `hooks/scripts/`) :
  - PreToolUse `garde-destructif` : union des gardes des 4 plugins (delete_*
    foodeatup ; delete_*/update_invoice_status/update_contrat_status/
    close_opportunity rapidocrm avec table DGFiP ; delete_*/
    cancel_schedules_post/remove_post_campagne rapidocms ; delete-user-tool/
    delete-project-link-tool rapidorh). La vérification DGFiP ne s'applique
    qu'aux factures CRM (statuts FoodEatUp non vérifiés, schéma différent) ;
  - PreToolUse `anti-donnee-inventee` : plage plausible sur `add_temperature`
    (serveur foodeatup) ;
  - Stop `récap-actions` (hook prompt) : récapitulatif PAR SERVEUR exigé en fin
    de tour après toute écriture ;
  - SessionStart `contexte` : injecte le rappel de la politique d'autonomie et
    du chargement des directives.
- Nouveau fichier `reference/autonomie.md` : politique d'autonomie détaillée
  (lecture libre, écriture par système, destructif unitaire, échec transverse).

## 0.2.0 — 2026-07-06

- Ajout de la couche métier :
  - Agent : `directeur-general` (vision transverse par croisement de signaux —
    acquisition, organisation, delivery, conversion —, délégation
    systématique aux agents spécialistes des autres plugins, données réelles
    uniquement).
  - Skill d'expertise : `comite-de-direction` (orchestre revue-hebdo-business,
    restitution CODIR : 1 page par domaine — chiffre clé, tendance, alerte,
    décision proposée — + arbitrages inter-domaines, 3 décisions maximum).

## 0.1.0 — 2026-07-06

- Version initiale : `.mcp.json` (4 serveurs), références
  `directives-outils.md` et `charte-graphique.md`, skills transverses
  `onboarding-client-360` et `revue-hebdo-business`.
