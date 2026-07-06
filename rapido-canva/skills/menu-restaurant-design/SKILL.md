---
name: menu-restaurant-design
description: Utiliser quand l'utilisateur veut créer son menu, un menu imprimable ou une carte à imprimer pour son restaurant. Compose le contenu depuis FoodEatUp puis génère le design dans Canva et l'exporte en PDF.
---

# Menu restaurant (FoodEatUp × Canva)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`,
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-canva.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/CONFORMITE.md`. Obtenir l'`establishment_id`
(FoodEatUp) avant tout appel.

## Workflow

1. **Contenu du menu (FoodEatUp)** — `list_dishes` + `list_categories` :
   plats par catégorie, prix. Vérifier la cohérence TVA (nature du plat :
   immediate 10 %, conservable 10 %/5,5 %, alcohol 20 %) et signaler toute
   incohérence de prix AVANT le design. Faire valider la sélection (tout le
   menu ? une carte du midi ? sans les plats épuisés ?).
2. **Charte** — demander si design « on-brand » : `list-brand-kits` et faire
   choisir le `brand_kit_id` ; sinon injecter la palette et le ton de
   `./rapido-kb/charte-graphique.md` dans la query.
3. **Générer** — `generate-design` (`design_type` : `flyer` pour un menu
   simple, `poster` pour un affichage) avec une query DÉTAILLÉE : nom du
   restaurant, style, catégories et plats avec prix en euros, ambiance,
   palette. Rappel : l'outil est sans mémoire — tout le contexte à chaque
   itération.
4. **Candidats** — présenter les candidats à l'utilisateur, faire choisir,
   puis `create-design-from-candidate` (`job_id`, `candidate_id`) — obligatoire
   avant export.
5. **Retouches éventuelles** — transaction d'édition complète (start →
   operations → preview → accord → commit ; voir pieges-canva.md §3), ex.
   corriger un prix ou un accent.
6. **Export PDF** — `get-export-formats` d'abord, puis `export-design`
   (`format.type: "pdf"`, `size` a4 par défaut) et AFFICHER l'URL de
   téléchargement.
7. **QR de la carte digitale (option)** — proposer d'ajouter le QR code de la
   carte digitale CMS (`list_digital_card` / `list_card_page` côté rapidocms)
   sur le menu : insérer l'image du QR via la transaction d'édition
   (`insert_fill` avec un asset uploadé), ou le signaler comme étape manuelle
   si l'asset n'est pas disponible.

## Variante — mise à jour du menu (changement de prix)

1. Identifier le design existant (`search-designs` par titre, ou demander le
   lien) et le nouveau prix (source : `list_dishes` / `get_recipe` — jamais de
   tête).
2. Transaction d'édition : `find_and_replace_text` sur l'ancien prix (confirmer
   les occurrences si le montant apparaît plusieurs fois) → preview → accord →
   commit → ré-export PDF (get-export-formats puis export-design).

## Garde-fous

- Prix et plats STRICTEMENT issus de FoodEatUp — aucun plat ou prix inventé ;
  citer la source (« prix de list_dishes »).
- Pas de données personnelles clients sur un menu (CONFORMITE.md).
- Jamais d'export d'un candidat non converti ; jamais de commit sans accord.
