# Changelog — plugin rapido-lovable

## 1.1.0 — 2026-07-10

- Premier agent du plugin : `chef-produit-web` — cadre le brief AVANT de
  construire (chaque message Lovable consomme des crédits), charge la
  marque (sync-marque-lovable), route vers le bon skill, pilote par
  itérations économes (plan_mode sur l'ambigu), valide preview + get_diff
  avant tout déploiement (accord explicite). tests/evals.md créé.

## 1.0.0 — 2026-07-06

- Première version publique.

## 0.4.0 — 2026-07-06

- Intégration de 2 skills anthropics/skills (Apache 2.0, LICENSE.txt propre à
  chaque skill conservé) : `frontend-design` (direction esthétique,
  typographie — description enrichie : se combine avec ui-ux-pro-max pour le
  choix des styles) et `web-artifacts-builder` (artifacts HTML multi-
  composants React/Tailwind/shadcn ; scripts nécessitant Node/pnpm — voir
  ATTRIBUTIONS.md).
- ATTRIBUTIONS.md créé, avec entrées rétroactives pour ui-ux-pro-max et
  ui-styling (MIT, nextlevelbuilder).

## 0.3.0 — 2026-07-06

- Intégration de 2 skills externes MIT depuis
  github.com/nextlevelbuilder/ui-ux-pro-max-skill (LICENSE copiée dans chaque
  dossier de skill, artefacts .coverage purgés) :
  - `ui-ux-pro-max` : intelligence design UI/UX (50+ styles, 161 palettes,
    57 paires de polices, 99 guidelines UX, 10 stacks) avec scripts de
    recherche Python stdlib ;
  - `ui-styling` : shadcn/ui + Tailwind + designs canvas (références,
    polices OFL embarquées, scripts de génération de config).
  Dépendances externes NON installées (signalées) : python3 sur le PATH ;
  Node.js 18+ / npm / npx pour le script shadcn_add.py (ui-styling) ;
  pytest/pytest-cov/pytest-mock uniquement pour les tests dev.

## 0.2.0 — 2026-07-06

- Passe de portabilité : section « dégradation propre » dans les directives (Lovable absent → explication + initial_message préparé).

## 0.1.0 — 2026-07-06

- Version initiale : `.mcp.json` (lovable + foodeatup + rapidocms + rapidocrm
  + rapidorh).
- Références : `architecture-lovable.md` (mode A build-time connecteurs via
  dashboard ; mode B runtime API Anthropic /v1/messages + mcp_servers, blocs
  parsés par type, clé API côté serveur ; pièges : enable_database avant
  query_database, query_database = production, set_*_knowledge remplace tout,
  crédits via get_workspace, plan_mode, deploy = URL publique),
  `directives-outils.md` (IDs, KB, confirmations, crédits).
- Skills : `site-restaurant` (contenu réel FoodEatUp, résa mode B
  availability→create, QR carte digitale), `usine-a-landing` (campagne CRM +
  KB, formulaire → prospect mode B, boucle analytics↔stats campagne),
  `agent-ia-produit` (rôle, system prompt dérivé des personas/KB, plan mode,
  autonomie héritée : lecture libre / écriture confirmée, tests guidés avant
  deploy), `sync-marque-lovable` (KB → workspace knowledge fusionné + skill
  charte-<société>).
