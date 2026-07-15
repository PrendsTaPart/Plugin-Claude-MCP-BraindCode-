---
name: site-vitrine-foodeatup
description: Utiliser quand l'utilisateur veut gérer son site vitrine FoodEatUp — « mon site », « publie ma page », « change le thème du site », « applique un template », « mes leads du site », « statut de mon site ». Pilote la vitrine web FoodEatUp (pages, thème, templates, leads, stats). À NE PAS utiliser pour la carte des plats (carte-vitrine) ni un MVP/app sur mesure (rapido-lovable).
---

# Site vitrine FoodEatUp (pages, thème, templates, leads)

Gère la **vitrine web** de l'établissement. La charte (couleurs/typo) suit le **fil des
tokens** de la marque — pont `rapido-design`/`rapido-lovable`. Rien d'inventé.

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et l'appliquer.
2. S'assurer d'avoir l'`establishment_id` (le demander si absent).
3. **État d'abord** : `get_site_status` (pages publiées/brouillon, URL publique, domaine)
   avant toute modification.

## 1. Structure & contenu

- `get_page_content` (`page_slug`) : relire une page (sections + props) avant de la
  modifier.
- `toggle_site_page` (paramètres `page_slug` + publier/dépublier) : bascule **une** page.
- Ajout d'une page du catalogue (about, faq, allergens, gallery, jobs, boissons…) et
  édition fine d'une section : `add_site_page` / `update_section` — **schémas à finaliser
  (réintrospection)**, ne pas inventer leurs paramètres.

## 2. Thème & templates

- `list_site_templates` : galerie des templates métiers du Studio.
- `apply_site_template` (`slug`, `confirm`) : **REMPLACE pages et thème** → le serveur
  **exige `confirm:true`** ; le skill **résume le changement** (ce qui sera écrasé)
  **puis** confirme.
- `set_site_theme` (`tokens`) : **fusion partielle** des design tokens (couleurs,
  polices). Reprendre les **tokens de la charte** (via `rapido-design` / la marque du
  CMS), pas de valeur en dur inventée.

## 3. Mise en ligne

Publier l'ensemble des pages brouillon : `publish_site` (**`confirm:true` exigé côté
serveur** — schéma exact à finaliser). Récapituler les pages concernées **puis** publier.
Vérifier le domaine (DNS/SSL) via `get_domain_status` (schéma à finaliser).

## 4. Performance & leads

- `get_site_stats` : commandes web, CA, leads, avis, jeux (30 j).
- `list_site_leads` (`source` optionnel) : leads captés (contact, roue, privatisation).
  **Router les leads vers le CRM** (`rapidocrm:prospection-pipeline` / `enregistrer_prospect`).
- `get_wheel_stats` (`wheel_id`) : lancers, lots, leads d'un jeu de roue.

## Passerelles

- Carte des plats / boissons / happy hours → `carte-vitrine`. App/MVP sur mesure →
  `rapido-lovable:mvp-lovable`. Charte & tokens → `rapido-design`. Avis clients →
  volet avis de `handle-complaint`.

## Règles

- **Confirmation** : `apply_site_template` et `publish_site` **confirmés** (serveur
  `confirm:true` + hook `garde-destructif`) ; `confirm:true` **jamais** posé d'office.
- **Fil des tokens** : le thème reprend la charte de la marque, zéro valeur en dur inventée.
- **Leads → CRM** ; **rien d'inventé** (stats, leads, pages viennent du serveur).
- Outils à schéma non finalisé (`add_site_page`, `update_section`, `publish_site`,
  `get_domain_status`) : **réintrospecter avant d'en fixer les paramètres**.
