---
name: sites-et-jeux-express
description: Utiliser quand l'utilisateur veut un « microsite de campagne », une « page concours », un « jeu concours jouable », un « mini-jeu » ou un « site express ». Crée des microsites jetables et des jeux jouables Higgsfield, branchés sur la mécanique concours du CRM, avec routage explicite vers Lovable pour tout ce qui est connecté au CRM.
---

# Sites & jeux express (Higgsfield)

Microsites de campagne **jetables** et **jeux jouables**. **Jamais** l'outil pour
une app métier connectée au CRM.

## Règle de routage (EN TÊTE)
- **Landing / app connectée au CRM** (formulaires, prospects, données) → **`rapido-lovable:usine-a-landing`** (PRIORITAIRE).
- **Microsite jetable, page événement, JEU** → **ici**.

## Étape 0 — Charger
- `${CLAUDE_PLUGIN_ROOT}/reference/routage-media.md` + `garde-fous-media.md`.
- `gouvernance-credits` (déploiements = coût à mesurer → chiffrer/confirmer).

## Sites
1. Lire **d'abord** les instructions officielles (get_website_creation_instructions —
   stack, contrat de design, règles) — **requis avant** toute création/édition.
2. Créer le site (create_website : `type` = website ou app = **choix utilisateur**,
   `subdomain` court = slug) → `website_repo_access` (git URL + token, cloner/éditer/pousser).
3. **`deploy_website`** (CI) : **chaque déploiement ship en live, pas de preview**
   → donc **métadonnées OG complètes AVANT** ; re-déployer après tout changement
   (publish ne déploie pas, il ne fait que lister). Secrets via `website_secrets` ;
   **`website_db` en LECTURE seule** ; slug via le `subdomain`.

## Jeux
1. Lire **d'abord** get_game_creation_instructions (**requis**).
2. Build local (`logic.js`/`server.js` + `index.html`) → **zip** → `media_upload`
   → PUT bytes → `media_confirm` type=`file`.
3. **`deploy_game`** (`source_game` = URL du zip ; **thumbnail 16:9 + favicon 1:1
   requis** — les générer d'abord via l'image si absents ; title/description).
   **MAJ = TOUJOURS repasser le `game_id`** exact retourné au 1er déploiement
   (piège : sans lui, un **nouveau jeu** est créé silencieusement — ne jamais
   réessayer un update sans `game_id`).

## Croisement CRM (jeu concours)
- La **mécanique officielle** (participants, points fidélité) reste
  `lancer_jeu_concours_entreprise` (RapidoCRM, `modele_jeu_id` + `entreprise_id`) ;
  le **jeu Higgsfield est la surface jouable**. Injecter l'**URL du jeu** dans la
  campagne CMS et les posts.

## Registre
Chaque site/jeu consigné dans `./rapido-kb/marketing/tunnels.md` (nom, IDs —
`website_id`/`game_id` —, URL, campagne).

## Garde-fous
Routage respecté (**CRM connecté → Lovable**) ; instructions officielles lues
**avant** création ; **OG complètes avant déploiement** (ship = live) ; update de
jeu **avec `game_id`** (jamais inventé) ; `website_db` lecture seule ; coûts de
déploiement chiffrés ; IDs consignés dans `tunnels.md`.
