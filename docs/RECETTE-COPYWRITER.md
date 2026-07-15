# Recette réelle — rapido-copywriter (runbook)

Une idée FoodEatUp déclinée sur 4 réseaux :
**« Le coût caché des ruptures de stock dans un restaurant »**.

> **Statut : à exécuter côté opérateur.** Les 4 pièces de copy se produisent au fil de
> l'eau (texte — le vrai livrable du plugin). Le seul **write réel** est
> `create_draft_tool` (crée des **brouillons dans le CMS du client** + une campagne test) :
> déféré ici pour ne pas polluer le CMS de prod sans accord. **Aucune publication** —
> brouillons uniquement. Ci-dessous le mode opératoire + la grille de relevé.

## Prérequis

- MCP RapidoCMS connecté (comptes sociaux liés — `list_connected_accounts`) ; charte
  FoodEatUp (`get_brand`). Preuves chiffrées **réelles** (stocks/coûts) via CRM/CMS/FoodEatUp.

## Déroulé

| # | Étape | Skill | Attendu | À relever |
|---|---|---|---|---|
| a | **Déclinaison** | `declinaison-multi-reseaux` | Idée-noyau → 4 déclinaisons **natives** | idée-noyau retenue |
| b | **LinkedIn** | `copy-linkedin` | Post page FoodEatUp (hook, 900-1 300 car., CTA question) — 3 variantes | hook L# utilisé |
| c | **Facebook** | `copy-meta` | Post **local** 40-120 mots | hook F# |
| d | **Instagram** | `copy-meta` | **Carrousel 7 slides** (structure + brief visuel délégué) | hook I# |
| e | **TikTok** | `copy-tiktok` | **Script 30 s** (générique, production différée) | hook T# |
| f | **Gates** | anti-voix-IA + `brand-review` | Les 2 passes tracées sur chaque pièce | verdicts |
| g | **Brouillons + calendrier** | `create_draft_tool` + `calendrier-editorial` | 4 brouillons CMS rattachés à une **campagne test** + calendrier 1 semaine | IDs brouillons, campagne |

## Grille de relevé (à remplir à l'exécution)

| Réseau | Hook utilisé | Anti-voix-IA | brand-review | ID brouillon | Qualité perçue |
|---|---|---|---|---|---|
| LinkedIn | L# | passé | passé | | |
| Facebook | F# | passé | passé | | |
| Instagram | I# | passé | passé | | |
| TikTok | T# | passé (parlé) | passé | (ou export) | |

## Garde-fous rappelés

- **Brouillons uniquement**, jamais de publication directe.
- **Preuves réelles** (coûts/stocks du CRM/CMS), **anti-clickbait** (le hook « coût caché »
  est tenu par le contenu).
- **Anti-voix-IA** + **brand-review** avant chaque brouillon ; hooks **consignés** au
  compteur de `reference/banque-hooks.md`.
- Après publication (plus tard) : `scripts/score_hooks.py` sur les insights réels
  (liked/shares/comments/views) → tags GAGNANT/NEUTRE.

> Une fois la grille remplie sur un run réel, le passage **1.0.0** est justifié. Jusque-là,
> livré **0.5.0** feature-complete (4 skills + 1 agent + boucle) ; recette **déférée**.
