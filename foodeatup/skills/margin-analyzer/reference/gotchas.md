# Pièges (gotchas)

Sources de revenus et de coûts **réelles** : FoodEatUp uniquement
(`finance_summary`, `list_orders`, `list_invoices`, `list_expenses`) — le plugin
est découplé de RapidoCRM. Aucun connecteur PayPal / QuickBooks / Square ici —
ne jamais citer d'outil qui n'existe pas côté serveur.

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

## Piège : périmètre du chiffre d'affaires (restaurant vs B2B)

Ce plugin analyse le CA **restaurant** (FoodEatUp). Si l'exploitant a aussi une
facturation B2B/prestations dans un CRM, elle est HORS périmètre ici — l'analyse
ne la voit pas. Les listes FoodEatUp sont **paginées** (`limit`) — parcourir
plusieurs pages ne doit pas double-compter.

**Pourquoi c'est important :** présenter une marge « globale » calculée sur le
seul restaurant, sans le dire, trompe l'exploitant qui a d'autres revenus.

### ✗ Mauvais
Annoncer « ta marge totale » alors que seul le CA restaurant a été lu.

### ✓ Bon
Dire explicitement le périmètre (« CA restaurant FoodEatUp uniquement ») et, si
l'exploitant a une activité B2B, la signaler comme non couverte (plugin
rapidocrm, hors périmètre de ce skill).

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
