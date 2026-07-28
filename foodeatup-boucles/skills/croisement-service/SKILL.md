---
name: croisement-service
description: Utiliser quand l'utilisateur veut croiser gestion et vente — « détecte mes incohérences », « croise mes boucles », « est-ce que ma com et mon stock racontent la même histoire », « audit du croisement », « qu'est-ce qui cloche entre ma cuisine et mes campagnes ». Le seul skill qui lit les deux familles de boucles en même temps pour détecter les contradictions.
---

# Croisement du 8 — le service, où les deux familles de boucles se rencontrent

## Quand l'utiliser

Le point de croisement du 8 est LE service : quatre flux le traversent
(commande, encaissement, carte, marge). Les boucles de gestion (①–④) et de
vente (⑤–⑧) peuvent chacune être vertes tout en se contredisant : c'est ici
qu'on le voit. Personne d'autre ne lit les deux côtés en même temps — ni un
skill de boucle (un seul côté), ni le briefing du jour (photo, pas croisement).

## Enchaînement d'outils MCP (l'ordre compte)

Lecture des deux côtés AVANT toute analyse — aucune écriture dans ce skill :

1. Côté vente : `list_campaigns` (actives), `list_orders` (période),
   `list_reservations` (à venir), `get_loyalty_program`, `list_loyalty_rewards`.
2. Côté gestion : `list_low_stocks`, `list_stocks`, `list_production_plans`,
   `list_dishes`, `list_recipes` (+ `get_recipe` pour les coûts des plats cités
   en campagne).
3. Croiser, détection par détection (ci-dessous), en citant les données
   observées — jamais « il semble que ».

## Détections (au minimum ces cinq)

1. **Campagne × stock** : un plat mis en avant dans une campagne active alors
   que son ingrédient principal est dans `list_low_stocks` → promettre ce qu'on
   ne peut pas servir.
2. **Production × demande** : un plan de production (`list_production_plans`)
   sans demande correspondante — couverts prévus (`list_reservations`) ou
   commandes — → gaspillage planifié.
3. **Campagne × marge** : un plat à marge négative (coût recette ≥ prix de
   vente, via `get_recipe` et `list_dishes`) présent dans une campagne active
   → on paie pour vendre à perte.
4. **Jour creux × échantillon** : un « jour creux » identifié sur moins de
   3 commandes → signaler l'échantillon insuffisant AU LIEU de recommander une
   action (voir contrainte forte).
5. **Fidélité éteinte × récompenses actives** : `get_loyalty_program` avec
   `active: false` alors que `list_loyalty_rewards` contient des récompenses
   actives → moteur débranché, catalogue qui tourne à vide.

Toute autre incohérence observée en lisant (réservations > capacité, happy hour
sur plat épuisé…) s'ajoute au tableau, avec les mêmes exigences de preuve.

## Contrainte forte — seuils d'échantillon

Ce skill ne recommande RIEN si l'échantillon est sous le seuil. Il écrit
« données insuffisantes » et indique combien il en faudrait :

- tendance par jour de semaine : minimum **3 commandes par jour observé** et
  **2 semaines** de données ;
- popularité d'un plat : minimum **10 ventes** du plat sur la période ;
- performance d'une campagne : campagne **terminée** ou ≥ 7 jours d'activité.

Sous le seuil, la seule recommandation admise est : « collecter davantage de
données » (et comment).

## Sortie attendue

Un tableau `[incohérence | boucles concernées | données observées | action proposée]`,
les incohérences les plus coûteuses d'abord. Si aucune incohérence : le dire,
avec la liste des vérifications faites (preuve du travail, pas silence).

## Ce que ce skill NE fait PAS

- Corriger lui-même : chaque action proposée renvoie vers le skill de la boucle
  concernée (`boucle-3-stock-production`, `boucle-6-communication`,
  `boucle-7-fidelite`…) qui porte les garde-fous d'écriture.
- Le point quotidien sans croisement → skill `briefing-du-jour` (plugin
  foodeatup).
- L'analyse de rentabilité de toute la carte → skill `analyse-rentabilite-carte`.
