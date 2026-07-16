# foodeatup — Gestion restaurant FoodEatUp

Gestion restaurant FoodEatUp : HACCP, service en salle, coordination cuisine (KDS), recettes & marges, production, réapprovisionnement — avec agents chef-restaurateur et chef-cuisine.

## Skills (15)

| Skill | Quand l'utiliser |
|---|---|
| `analyse-rentabilite-carte` | Analyser sa carte, savoir quels plats garder ou parle d'ingénierie de menu |
| `briefing-du-jour` | Le briefing du jour, « ma journée » ou un point du matin. Routine du directeur de restaurant |
| `carte-vitrine` | Construire ou mettre à jour sa carte en ligne (vitrine web), ses catégories de carte ou ses fo… |
| `coordination-cuisine` | Pass, de l'écran cuisine (KDS), d'un plat prêt, en préparation ou à lancer, ou de coordonner c… |
| `gestion-commandes` | Créer une commande, suivre les commandes en cours ou changer le statut d'une commande (confirm… |
| `haccp-conformite-quotidienne` | Relevé de température, HACCP, contrôle réception, étiquette DLC, checklist hygiène, plan de ne… |
| `handle-complaint` | Client se plaint (email, avis, ticket) et qu'il faut traiter la réclamation de bout en bout :… |
| `margin-analyzer` | Augmenter ses prix, de marges, de coûts qui grignotent le profit, ou demande « est-ce que je g… |
| `onboarding-restaurateur` | Nouveau client restaurateur démarre sur FoodEatUp, ou quand l'utilisateur dit « installe mon r… |
| `planning-equipe` | Planning, de shifts, d'horaires d'équipe, de demandes de congé, de pointages, de contrat de tr… |
| `price-check` | Vérifier ses prix ou voir ses marges par produit avant une décision tarifaire |
| `production-stock` | Planifier une production, consulter les alertes de production ou valider une production réalis… |
| `reappro-fournisseurs` | Stock bas, de commande fournisseur ou de réapprovisionnement |
| `recette-cout-marge` | Créer une recette, calculer le coût d'une recette, une marge, ou fixer un prix de vente |
| `service-salle` | Réservation, d'installer un client, de plan de salle, de file d'attente ou de table libre |

## Agents (3)

- **`chef-cuisine`** — Chef de cuisine, expert fiches techniques et production.
- **`chef-de-pass`** — Chef de pass pendant le service.
- **`chef-restaurateur`** — Directeur de restaurant expérimenté.

## Serveurs MCP requis

`foodeatup`, `rapidocrm` — connexion et clés : voir « Prérequis & connecteurs » du [README racine](../README.md). Aucune clé n'est stockée dans le dépôt.

## Déclencheurs (exemples réels)

- « ma journée »
- « est-ce que je gagne assez ? »
- « je devrais facturer plus ? »
- « installe mon restaurant »

## Version & conventions

v1.7.0 — historique dans [CHANGELOG.md](CHANGELOG.md). Skills en français (« Utiliser quand… »), calculs par script stdlib, garde-fous déterministes, rien d'inventé (KB `./rapido-kb/` prioritaire).
