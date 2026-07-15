# Changelog — plugin rapido-lovable

## 1.5.2 — 2026-07-15 — hooks (garde + récap IDs) — série FINITION F2

- hook PreToolUse `garde-lovable` (ask) sur deploy_project / create·update·delete_workspace_skill / set_workspace_knowledge (périmètre large) + hook Stop récap-IDs/URLs. Testés au testeur.

## 1.5.1 — 2026-07-15 — articulation avec le pipeline rapido-design

- `mvp-lovable` : quand un travail de design précède le build, **le MVP démarre du design
  system Lovable** produit par `rapido-design:studio-maquette` (`create_project` avec
  `design_systems`) et reprend **les mêmes tokens** — zéro divergence. Passerelle ajoutée.
- `ui-ux-pro-max` : articulation écrite — ce skill est la **bibliothèque de styles**,
  `rapido-design` est le **pipeline** qui l'exploite de bout en bout (DA → maquettes → DS → MVP).

## 1.5.0 — 2026-07-15 — workspace sync + agent architecte-lovable (LV4)

- `sync-marque-lovable` : **volet kit** — pousse le connecteur en **workspace skill**
  Lovable (`create_workspace_skill` « rapido-mcp-connect », condensé du kit ≤ 100k) +
  `set_workspace_knowledge` (méthode maison ≤ 10k), **versionné** (numéro du kit), push
  **sur confirmation** (touche tous les projets).
- Agent **`architecte-lovable`** : orchestre brief → spec (`mvp-lovable`) → prompts →
  branchement (`connecteur-mcp-lovable`) → recette + gate. Interdits (clé en dur/BraindCode,
  client-side, mise en ligne sans confirmation, hors scope, sauter le gate).
- Patchs : `agent-ia-produit` (consomme le kit, mode C canonisé), `usine-a-landing` &
  `site-restaurant` (« ajouter l'agent embarqué » → `connecteur-mcp-lovable`).
- Évals : agent + volet sync.

## 1.4.0 — 2026-07-15 — mvp-lovable (spec-driven, série P1-P8, LV3)

- Skill **`mvp-lovable`** — du brief au MVP multi-pages : **SPEC d'abord**
  (`templates/spec-mvp.md` → `docs/specs/{projet}.md`, validée avant tout prompt),
  design system (charte + `ui-ux-pro-max`), **série P1-P8** (fondations → pages →
  données/formulaires mode B → agent embarqué délégué à `connecteur-mcp-lovable` →
  SEO/perfs/a11y → recette + gate sécurité + mise en ligne confirmée), exécution
  assistée optionnelle, capitalisation KB. Frontière : one-shot = `prompt-lovable`,
  verticaux = `usine-a-landing`/`site-restaurant`.
- `templates/spec-mvp.md` (méthode spec-driven, cf. NOTICE).
- Évals : 4 cas (spec d'abord, délégation MCP, routage vertical, mise en ligne
  confirmée).

## 1.3.0 — 2026-07-15 — connecteur-mcp-lovable (kit → prompts étagés, LV2)

- Skill **`connecteur-mcp-lovable`** — LE skill « connecte le MCP X au site » :
  Étape 0 (fiche kit du MCP + gate sécurité + règles stack + contexte projet),
  qualification (MCP, projet neuf/existant, périmètre, credentials CLIENT),
  génération des **prompts Lovable étagés P1-P5** (secrets/env noms immuables ;
  edge function scope serveur ; chat UI carte de confirmation ; system prompt +
  knowledge ; tests d'acceptation), exécution assistée optionnelle (send_message +
  vérif entre chaque + gate + recette démo), livraison (doc client +
  connecteurs-installes.md).
- Interdits : jamais de clé BraindCode chez un client, jamais d'appel client-side,
  jamais d'écriture sans confirmation UI, pas de promesse d'isolation multi-tenant
  avant le token par tenant.
- Évals : 4 cas (chaîne, refus clé BraindCode, refus client-side, multi-tenant
  honnête) + anti-collisions.

## 1.2.0 — 2026-07-15 — kit connecteur MCP canonique (v2, LV1)

- `reference/kit-connecteur-mcp/` (kit v1) — source de vérité versionnée : `_commun.md`
  (template edge function canonisé depuis academyrapido:execute-prompt — API Anthropic +
  mcp_servers type url, beta mcp-client-2025-04-04, parsing PAR TYPE, rate-limits, filtre
  injection, scope injecté serveur, écritures confirmées, 7 points sécurité, versioning) +
  une fiche par MCP (`foodeatup`, `crm`, `cms`, `rh` : env immuables, familles d'outils
  autorisées, system prompt, scope).
- `reference/regles-stack-lovable.md` (awesome-cursorrules CC0, francisé) : règles
  React/TS/Tailwind/shadcn/Supabase injectées dans chaque prompt.
- `reference/gate-securite.md` (VibeSec Apache-2.0, adapté/modifié) : checklist bloquante
  « agent + clés MCP » (secrets hors bundle, appels serveur, scope, écritures confirmées).
- `NOTICE.md` (CC0/Apache-2.0/MIT, modifications VibeSec signalées) ; patch
  `architecture-lovable.md` (section kit canonique).
- Fondé sur l'audit LV0 (`docs/REFERENCE-AGENT-LOVABLE.md`, `docs/IMPORTS-LOVABLE-V2.md`)
  et la spec auth multi-tenant (`docs/OUTILS-MCP-MANQUANTS.md` §11). Skills LV2→LV5 à venir.

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
