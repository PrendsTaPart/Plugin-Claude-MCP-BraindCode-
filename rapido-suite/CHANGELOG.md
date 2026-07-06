# Changelog — plugin rapido-suite

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
