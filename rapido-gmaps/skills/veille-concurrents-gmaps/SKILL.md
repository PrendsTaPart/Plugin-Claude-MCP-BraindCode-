---
name: veille-concurrents-gmaps
description: Utiliser quand l'utilisateur veut analyser la concurrence d'une zone depuis Google Maps — « scrape les concurrents de [client] », « veille concurrentielle zone », « que proposent les concurrents dans [ville] », « comment se situe mon resto face aux voisins ». Scrape les établissements concurrents (même catégorie, même zone) → rapport de positionnement (notes, prix, affluence, canaux) dans la KB. À NE PAS utiliser pour sourcer des prospects (sourcing-gmaps) ni traiter les avis clients FoodEatUp (foodeatup handle-complaint).
---

# Veille concurrentielle Google Maps

Situer un établissement FoodEatUp face à ses **concurrents directs** d'une zone :
notes, gamme de prix, affluence, canaux (livraison/réservation) — pour nourrir la
stratégie (offre, publicité). **Données publiques d'agrégat**, pas de ciblage des
avis individuels.

## Étape 0 — contexte

Lire `reference/modes-execution.md`, `reference/garde-fous-scraping.md`,
`rapido-kb/entreprise.md` (catégorie, ville de l'établissement) et
`rapido-kb/marketing/icp.md` si présent. Sans mode d'exécution : le dire, s'arrêter.

## 1. Cadrer l'établissement cible

Identifier la **catégorie** et la **ville/zone** de l'établissement FoodEatUp
(depuis `rapido-kb/entreprise.md` ; en complément `list_dishes` pour la gamme de
l'offre et `get_order` pour le panier moyen si utile). Définir le **rayon** de
veille (configurable, défaut : ville / arrondissement).

## 2. Scraper les concurrents

Construire `"{catégorie} in {ville}"` et lancer le scrape (voir
`reference/modes-execution.md`). **Filtrer les concurrents directs** : même
catégorie, dans le rayon. Exclure l'établissement lui-même.

## 3. Rapport de positionnement

Produire un rapport d'**agrégat** (jamais nominatif-diffamatoire) :

- distribution des **notes** et du **nombre d'avis** (où se situe le client) ;
- **gamme de prix** (`price_range`) moyenne de la zone ;
- **heures d'affluence** (`popular_times`) dominantes ;
- **canaux** : part des concurrents avec livraison / réservation en ligne
  (`order_online` / `reservations`) — révèle la maturité numérique de la zone ;
- **visuels** : `thumbnail` uniquement, à titre d'inventaire — **aucune
  reproduction** ni republication.

Consigner dans `rapido-kb/marketing/veille-concurrents.md` (daté, par zone).

## 4. Passerelles

Proposer des angles pour `rapido-meta-ads:veille-ads-concurrents` (les concurrents
bien notés **sans publicité** = cibles de conquête). Croiser l'affluence avec
`foodeatup:reservation_availability` pour optimiser les créneaux proposés.

## Règles (éthique de veille)

- **JAMAIS** scraper les avis pour les **critiquer/republier** publiquement — les
  avis servent l'analyse de positionnement, pas du contenu diffamatoire.
- Agrégats et données publiques uniquement ; pas de reproduction de visuels.
- CGU/RGPD, plafonds, délais comme partout (`garde-fous-scraping.md`).
- Rien d'inventé : un agrégat n'est produit que sur les fiches réellement scrapées.
