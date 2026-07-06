# Changelog — plugin rapido-suite

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
