# Pièges (gotchas)

Sources de revenus et de coûts **réelles** de l'écosystème Rapido : FoodEatUp
(`finance_summary`, `list_orders`, `list_invoices`, `list_expenses`) et RapidoCRM
(`get_revenue_summary`, `list_factures`, `list_depenses`). Aucun connecteur PayPal /
QuickBooks / Square ici — ne jamais citer d'outil qui n'existe pas côté serveur.

## Piège : confondre chiffre d'affaires et bénéfice

L'exploitant voit le CA encaissé (`finance_summary`) et croit que c'est ce qu'il
a gagné. Non : c'est ce qu'il a **collecté**, pas ce qu'il lui **reste**.

**Pourquoi c'est important :** afficher un CA sans le mettre immédiatement en face
des coûts laisse croire à une santé qui n'existe peut-être pas.

### ✗ Mauvais
« Ton CA du trimestre était de 50 000 €. »

### ✓ Bon
« Ton CA du trimestre était de 50 000 €. Après coûts directs de 31 000 €, ta marge
brute est de 19 000 € — soit 38 %. »

---

## Piège : prix affiché au lieu du prix effectif

Remises, avoirs et promotions réduisent ce qui est réellement encaissé par vente.
`finance_summary` et `list_invoices` reflètent les montants **réels** ; la carte
(`list_dishes`) montre le prix **affiché**.

**Pourquoi c'est important :** calculer une marge sur le prix affiché la surestime.

### ✗ Mauvais
Prendre le prix de `list_dishes` comme revenu par vente.

### ✓ Bon
Partir des montants encaissés (`finance_summary` / `list_invoices`) et signaler
l'écart avec le prix affiché quand il y a beaucoup de remises.

---

## Piège : élasticité déduite d'un seul changement de prix

Un seul historique de hausse ne suffit pas à prévoir la réaction du volume.

**Pourquoi c'est important :** une élasticité tirée d'un point est du bruit, pas un
signal.

### ✗ Mauvais
« Tu as monté les prix de 5 % une fois, le volume a baissé de 2 %, donc à +10 % il
baissera de 4 %. »

### ✓ Bon
Présenter la sensibilité comme une **hypothèse** signalée, avec une fourchette, et
dire que la vraie réponse dépend de la concurrence et de la clientèle.

---

## Piège : ignorer les coûts de service (prestations)

Pour une prestation (traiteur, événement), le coût inclut le temps de travail et la
logistique, pas seulement les ingrédients.

**Pourquoi c'est important :** une marge « produit » qui oublie la main-d'œuvre
surestime la rentabilité réelle.

### ✗ Mauvais
Calculer la marge d'un menu traiteur sur le seul coût matière.

### ✓ Bon
Ajouter le temps de préparation (fiches recettes, `get_recipe`) et la logistique ;
si la donnée manque, la demander à l'exploitant et le signaler dans la sortie.

---

## Piège : coût de revient absent quand la recette n'est pas saisie

Le coût par produit vient des **recettes** (ingrédients × prix, `get_recipe` /
`recette-cout-marge`). Sans recette rattachée, FoodEatUp ne connaît pas le coût
matière du plat.

**Pourquoi c'est important :** on ne peut pas calculer une marge par produit si le
coût de revient n'est pas renseigné.

### ✗ Mauvais
Diviser un coût total (`list_expenses`) sur tous les plats → chiffres sans valeur.

### ✓ Bon
Si un plat n'a pas de recette, le dire : « Ce plat n'a pas de fiche recette, donc
son coût matière n'est pas connu. Veux-tu qu'on la saisisse, ou tu me donnes une
estimation ? » Marquer la limite dans la sortie.

---

## Piège : deux sources de revenus (FoodEatUp + RapidoCRM)

Le chiffre d'affaires peut venir de **deux serveurs** : FoodEatUp (activité
restaurant) et RapidoCRM (facturation commerciale / prestations). Les listes sont
**paginées** (`limit`) — parcourir plusieurs pages ne doit pas double-compter.

**Pourquoi c'est important :** additionner les deux sources aveuglément gonfle le
CA ; n'en interroger qu'une en oublie une partie.

### ✗ Mauvais
Prendre `finance_summary` (FoodEatUp) **et** `get_revenue_summary` (CRM) et les
additionner sans vérifier les périmètres.

### ✓ Bon
Choisir la source qui fait foi pour le périmètre analysé (restaurant → FoodEatUp ;
prestations facturées → CRM), le **dire** dans la sortie, et ne croiser que si les
périmètres sont disjoints. En cas de doute, demander à l'exploitant quelle source
reflète ses ventes.

---

## Piège : présenter des scénarios comme des prévisions

Les tableaux de scénarios de prix sont des **calculs**, pas des prédictions.

**Pourquoi c'est important :** l'exploitant pourrait agir comme si c'était garanti,
puis se sentir trompé quand le réel diffère.

### ✗ Mauvais
« Si tu montes les prix de 10 %, tu feras 55 000 € le trimestre prochain. »

### ✓ Bon
« Si tu montes les prix de 10 % et que le volume baisse d'environ 5 % (d'après
l'historique disponible), le CA serait d'environ 53 000 €. C'est une projection —
le réel dépendra de tes clients et de la concurrence. »
