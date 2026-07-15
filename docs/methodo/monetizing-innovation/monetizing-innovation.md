# Monetizing Innovation — concevoir le produit autour du prix

> **Idées** : Madhavan Ramanujam & Georg Tacke, *Monetizing Innovation* (2016).
> **Distillation source** : founder-playbook (MIT © 2026 AgentSeal).
> Reformulation FR intégrale, aucun extrait. Licence :
> `docs/methodo/100m-leads/NOTICE.md`. Comble la compétence **Pricing Strategy**.

## L'inversion
La plupart des produits fixent le prix **juste avant le lancement**, une fois
tout construit — trop tard. Le principe : **parler prix tôt** et concevoir le
produit **autour** de ce que le client est prêt à payer.

## Willingness-to-pay (WTP) — 5 méthodes de question
Du simple à l'avancé : (1) questions directes (prix acceptable / cher /
prohibitif — type Van Westendorp), (2) probabilité d'achat à un prix donné,
(3) analyse « le plus / le moins » (most-least), (4) build-your-own, (5)
simulations d'achat (conjoint). Règle : cadrer en **conversation de valeur**,
pas de prix ; ~1 question sur 4 est un « pourquoi ? » ; regarder la
**distribution**, pas la moyenne.

## Segmentation par la valeur (pas par la démographie)
Segmenter par **besoins, valeur et WTP** — deux clients au même profil
démographique peuvent avoir des WTP opposés. Viser 3-4 segments.

## Packaging & bundling
- **Leaders / Fillers / Killers** : un « killer » est valorisé par une minorité et
  rejeté par une autre → à sortir du bundle commun.
- **Good / Better / Best** avec des **barrières (fences)** claires ; distribution
  saine ≈ ≤ 25 % Good, gros du volume en Better/Best.

## Modèle de tarification (« comment » > « combien »)
Le **mode de facturation** (abonnement, à l'usage, par résultat…) pèse plus que
le montant. 5 modèles types ; attention au freemium (conversion souvent faible).

## Stratégie de prix — 3 types
**Maximisation** / **Pénétration** (prix bas pour la part de marché, le plus
risqué) / **Écrémage** (prix haut sur les early adopters). À décider **avant** le
lancement. **Intégrité du prix** : ne pas brader après lancement ; avant toute
baisse, tenter **3 actions non-prix** (plus de preuve, plus de valeur, montée en
gamme au même prix).

## Exemple Rapido / FoodEatUp
Un SaaS resto qui teste 3 points de prix par sondage WTP auprès de 10 clients,
puis packe en Good/Better/Best avec fences (nb d'établissements) — au lieu d'un
prix unique décidé « au feeling ».

## Articulation avec nos skills (pas de doublon)
- `scale-pricing-strategy` (rapido-forge) couvre **3 modèles (freemium /
  usage / flat) + un test WTP** : cette fiche **ajoute** la segmentation par la
  valeur, le packaging Leaders/Fillers/Killers + Good/Better/Best/fences, le
  pricing comportemental et l'intégrité du prix.
- `money-math-acquisition` (LTGP:CAC) et `catalogue-kpi` restent les **calculs
  par script** ; cette fiche est la **méthode de fixation du prix** en amont.

## Outils MCP Rapido pressentis
Produits/prix → `list_products`/`create_product`, devis → `create_devis` ;
revenus par offre → `get_revenue_summary` ; sondage WTP client → RapidoCRM
(`lancer_sondage_entreprise`). Chiffres par script (`catalogue-kpi`).
