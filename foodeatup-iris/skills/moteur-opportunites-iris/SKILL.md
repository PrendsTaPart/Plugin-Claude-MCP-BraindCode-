---
name: moteur-opportunites-iris
description: Utiliser quand l'utilisateur veut savoir quoi publier et pourquoi — « qu'est-ce qu'Iris propose », « trouve-moi des raisons de publier », « détecte les opportunités de com », « pourquoi poster aujourd'hui ». Lit les données d'exploitation FoodEatUp, score les signaux (urgence × valeur × fraîcheur), déduplique, et sort des opportunités avec leur raison.
---

# Moteur d'opportunités (le cœur d'Iris)

C'est ce qu'aucun outil de social media ne peut copier : il faut les données
d'exploitation pour le faire tourner. Le stock parle au marketing.

## Capteurs (lecture seule, dans cet ordre)

| Signal | Source FoodEatUp | Contenu proposé | Urgence |
|---|---|---|---|
| Surstock avec DLC proche | `list_stocks` · `list_haccp_labels` | Plat du jour qui écoule | 🔴 |
| Créneau de réservation faible | `reservation_availability` | Offre flash sur le créneau | 🔴 |
| **Avis négatif** | `list_reviews` | **Alerte patron — AUCUN post** | 🔴 |
| Nouveau plat à la carte | `list_dishes` · `list_recipes` | Post de lancement + story | 🟠 |
| Avis 5 étoiles | `list_reviews` | Verbatim en visuel | 🟠 |
| Jour creux récurrent | `list_orders` (historique) | Campagne segment à risque | 🟠 |
| Segment endormi | `list_rfm_segments` | Réactivation | 🟠 |
| Plat star sous-exposé | `list_top_productions` | Mise en avant récurrente | 🟢 |
| Happy hour configurée | `list_happy_hours` | Rappel la veille | 🟢 |
| Production signature planifiée | `list_production_plans` | Contenu coulisses | 🟢 |
| Anniversaire client | `list_clients` | Message personnel — jamais un post | 🟢 |

## Scoring et déduplication

- `score = urgence × valeur_commerciale × fraîcheur`
- **Valeur commerciale** : la marge réelle du plat, lue via `get_recipe` —
  jamais estimée. Marge indisponible = le dire, scorer sur l'urgence seule.
- **Fraîcheur** : un sujet traité dans les 14 derniers jours est déclassé —
  vérifier dans `./rapido-kb/iris/journal-signaux.md` (l'historique local).
- **Déduplication obligatoire** : deux signaux qui pointent le même plat
  fusionnent en UNE opportunité (le score le plus élevé gagne).
- Seuils d'échantillon : un « jour creux » identifié sur moins de 3 commandes
  par jour observé = « données insuffisantes », pas une opportunité (même
  règle que le skill `croisement-service` du plugin foodeatup-boucles).

## Règles absolues

1. **Un avis négatif ne produit JAMAIS de proposition de contenu** : alerte au
   patron (`create_notification`), et c'est tout.
2. Chaque opportunité retenue porte **sa raison en une phrase** : « Parce
   que… », fondée sur la donnée qui l'a déclenchée (chiffre + source).
3. Tout ce qui est détecté — retenu ou non — est consigné avec son score dans
   `./rapido-kb/iris/journal-signaux.md` : c'est le journal qui crée la
   confiance (le restaurateur voit qu'Iris regarde tout).

## Sortie attendue

Un tableau `[opportunité | raison (« Parce que… ») | score | canal suggéré |
urgence]`, trié par score, dédupliqué, suivi du journal des signaux non
retenus. Aucune écriture à ce stade — la fabrication vient après, sur accord
(skill `fabrique-contenu-iris`).

## Ce que ce skill NE fait PAS

- Fabriquer le visuel/texte → skill `fabrique-contenu-iris`.
- Le diagnostic de la boucle communication → skill `boucle-6-communication`
  (plugin foodeatup-boucles).
- Lancer quoi que ce soit : le moteur propose, l'humain dispose.
