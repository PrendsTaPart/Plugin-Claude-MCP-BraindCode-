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

---

## Run 2026-07-15 — copy produite (le vrai livrable du plugin)

> **Contexte confirmé** : le MCP RapidoCMS connecté est le compte **PRODUCTION** de Mo
> (`company_id 321`, admin). **Aucune écriture test** (`create_draft_tool`, `create_campagne`)
> n'est lancée dessus — cela polluerait le CMS de prod (règle maison). Les chiffres
> spécifiques restent `[à lire via foodeatup: finance_summary / list_low_stocks]`, non
> inventés. La copy ci-dessous est le **livrable réel** ; le rattachement CMS (brouillons)
> attend un **run supervisé** ou une **marque de test**.

### LinkedIn — hook **L2** (chiffre-preuve), famille « chiffre-preuve »
```
Une rupture sur un plat qui tourne coûte bien plus que l'ingrédient manquant.
La plupart des restaurateurs ne comptent que l'ingrédient.

Le coût réel, c'est :
– la vente perdue sur le plat… et souvent sur le menu entier de la table,
– l'achat d'urgence au prix fort (parfois +40 % vs le fournisseur habituel),
– le client déçu qui ne revient pas — le plus cher, et le plus invisible,
– le temps de l'équipe passé à « gérer » au lieu de servir.

Un plat à [marge réelle] € qui saute 8 fois par semaine, c'est [calcul] € par mois
qui ne reviendront jamais. Pas l'ingrédient à 2 €.

Ce qui change tout : des seuils d'alerte par ingrédient et un réappro anticipé —
pas « quand c'est vide », mais « quand ça va l'être ».

Vous suivez vos seuils de rupture à l'œil, ou vous êtes déjà passés à l'anticipation ?

#restauration #gestion #foodcost
```

### Facebook — hook **F4** (rappel utile local), court
```
Petit rappel utile pour les restaurateurs : une rupture de stock coûte bien plus
que l'ingrédient qui manque.

La vente perdue, l'achat d'urgence au prix fort, le client déçu qui ne revient pas…
c'est là que part la marge — pas dans les 2 € de l'ingrédient.

La parade : un seuil d'alerte par produit, un réappro anticipé. Comment vous gérez
les ruptures, vous ? 👇
```

### Instagram — carrousel (hook dans les 125 premiers car.), CTA « enregistre »
```
Caption : Ce que coûte VRAIMENT une rupture de stock (spoiler : pas l'ingrédient). Enregistre pour ton prochain inventaire 📌
Slide 1 : « Le vrai coût d'une rupture »
Slide 2 : La vente perdue (le plat + souvent la table)
Slide 3 : L'achat d'urgence au prix fort
Slide 4 : Le client déçu qui ne revient pas (le plus cher)
Slide 5 : Le temps de l'équipe à gérer l'imprévu
Slide 6 : La parade → seuil d'alerte + réappro anticipé
Slide 7 : « Anticipe, ne subis pas » — enregistre ce post
Hashtags : #restauration #restaurateur #foodcost #gestionresto
```

### TikTok — SCRIPT (hook < 3 s, boucle ouverte, sous-titres, payoff, CTA)
```
[0-3 s] (face cam, cuisine) « Une rupture de stock, ça te coûte 2 € ? Non. Ça peut t'en coûter 200. »
[3-8 s] Boucle ouverte : « Et le pire coût, tu le vois jamais passer. »
[8-20 s] Valeur : « La vente perdue sur le plat + la table, l'achat d'urgence au prix fort,
         et LE truc : le client déçu qui revient pas. Ça, aucun logiciel te le facture. »
[20-28 s] Payoff : « La parade en 10 s : un seuil d'alerte par produit, un réappro AVANT le vide. »
[28-30 s] CTA : « Abonne-toi si tu gères un resto, j'en fais d'autres. »
Sous-titres : obligatoires · Son : tendance · #restauration #resto #foodcost
```

### Gates (tracés)

| Réseau | Hook | Anti-voix-IA (`anti-voix-ia.md`) | brand-review | ID brouillon |
|---|---|---|---|---|
| LinkedIn | L2 | passé (pas de tics FR : « à l'ère de », « plongeons », emoji-puces) | à passer sur la vraie charte | — (prod, différé) |
| Facebook | F4 | passé | à passer | — |
| Instagram | carrousel | passé | à passer | — |
| TikTok | T (curiosité/enjeu) | passé (ton créateur, pas corporate) | à passer | — |

**Hooks consignés** : L2, F4 (+ variantes IG/TikTok) — compteur d'usage à incrémenter
**par script** (`score_hooks.py`) après un run publié réel, jamais à la main.

## Verdict

- **Livrable copy = PRODUIT** (4 réseaux, méthode maison appliquée, gate anti-voix-IA passé).
- **Écriture CMS** (`create_draft_tool` + `create_campagne` + `brand-review` sur charte
  réelle) = **STOP** : le CMS connecté est la **PROD de Mo** (company 321) → à jouer sur une
  **marque de test** ou en **run supervisé**, jamais de test dans le CMS de prod.
- **Bump 1.0.0 : STOP** tant que le run CMS (brouillons + insights via `score_hooks.py`)
  n'est pas passé sur une cible de test. Plugin reste **0.6.0** (feature-complete).
