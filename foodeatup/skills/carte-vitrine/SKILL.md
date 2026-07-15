---
name: carte-vitrine
description: Utiliser quand l'utilisateur veut construire ou mettre à jour sa carte en ligne (vitrine web), ses catégories de carte ou ses formules. Bâtit toute la carte vitrine en un appel avec import_storefront_menu.
---

# Carte vitrine (carte en ligne)

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
   règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).
2. S'assurer d'avoir l'`establishment_id` (le demander si absent) avant tout appel.

## Principe — une seule source de vérité

La carte vitrine et le menu imprimable (skill `menu-restaurant-design` du plugin
rapido-canva) partagent la MÊME source : les plats de l'établissement
(`list_dishes`). Avant de construire la vitrine, vérifier l'existant avec
`list_dishes` + `list_categories` — `import_storefront_menu` est IDEMPOTENT sur
les noms (catégories/plats existants réutilisés, pas dupliqués), mais un nom
mal orthographié crée un doublon : reprendre les noms EXACTS de `list_dishes`.

## Workflow

1. **État des lieux** — `list_dishes` + `list_categories` : plats et catégories
   existants. Annoncer ce qui sera réutilisé vs créé.
2. **Composer la structure** avec l'utilisateur :
   - catégories sur 2 niveaux max (`categories[].children`), avec
     `show_on_storefront` pour piloter la visibilité ;
   - plats par nom (`dishes` : `name`, `description`, `price` — prix issus de
     `list_dishes`/`get_recipe`, jamais de tête) ;
   - formules éditoriales (`formules` : `title`, `subtitle`, `price` +
     `price_suffix` ex. « /personne », `sections` > `groups` > `items`, et
     `notes` pour les conditions : minimum de commande, zones, délais).
3. **Valider la structure complète** avec l'utilisateur (arborescence + prix +
   formules) AVANT l'appel — c'est toute la carte en un coup.
4. **Construire** — `import_storefront_menu` (`establishment_id`, `categories`,
   `formules`).
5. **Récapituler** : catégories créées/réutilisées, plats créés/reliés,
   formules ; proposer ensuite le menu imprimable assorti
   (`menu-restaurant-design`, plugin rapido-canva) pour garder les deux
   supports synchrones.

## Garde-fous

- Prix et plats STRICTEMENT issus de FoodEatUp ou fournis par l'utilisateur.
- Un changement de prix se fait dans la fiche du plat (`update_dish` /
  `update_recipe`) — la vitrine et le menu imprimé doivent rester cohérents :
  proposer de mettre à jour les deux.
- Ne pas cacher une catégorie (`show_on_storefront: false`) sans confirmation.
- **Photos de plats premium** (packshots 4K de la carte) → mode « carte en photos »
  de `rapido-higgsfield:studio-image-pro` **si installé** (`list_dishes` → packshot
  par plat, coût du lot confirmé) ; rapatriement puis liaison à la vitrine.
