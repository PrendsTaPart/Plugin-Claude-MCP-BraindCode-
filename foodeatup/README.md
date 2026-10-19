# foodeatup — Gestion restaurant FoodEatUp

Gestion restaurant FoodEatUp : HACCP (températures, huiles, refroidissement), service en salle, caisse et TPE, coordination cuisine (KDS), carte, formules et options, recettes & marges, production, réapprovisionnement, écrans et bornes, appels de l'assistante vocale — avec agents chef-restaurateur et chef-cuisine.

## Skills (27)

| Skill | Quand l'utiliser |
|---|---|
| `analyse-rentabilite-carte` | Analyser sa carte, savoir quels plats garder ou parle d'ingénierie de menu |
| `appels-assistante-vocale` | Appels téléphoniques reçus par Caroline (l'assistante vocale du restaurant), d'appels manqués,… |
| `boissons-offres-livraison` | Sa carte des boissons, d'un happy hour ou de ses zones de livraison — « ajoute ce cocktail à l… |
| `briefing-du-jour` | Le briefing du jour, « ma journée » ou un point du matin |
| `caisse-du-jour` | Caisse, de POS, d'ouvrir la caisse, d'encaisser une note, de rendu monnaie, de clôture Z, de r… |
| `campagnes-restaurant` | Créer, lancer ou suivre une campagne marketing FoodEatUp ou un template WhatsApp pour son rest… |
| `carte-caisse-options` | Modifier sa carte telle que la caisse, la borne et le QR de table la vendent — catégories de p… |
| `carte-vitrine` | Construire ou mettre à jour sa carte en ligne (vitrine web), ses catégories de carte ou ses fo… |
| `coordination-cuisine` | Pendant le service : passe (comptoir d'envoi), écran cuisine (KDS), plats prêts ou à lancer |
| `ecrans-affichage-borne` | Écrans du restaurant (télé, affichage dynamique, menu board), d'affiches à diffuser, de playli… |
| `evenements-prives` | Privatisation ou d'événement privé — « une demande de privatisation est arrivée », « réponds à… |
| `fidelite-restaurant` | Fidélité, de points, de récompenses, de cartes cadeaux, de bons à valider ou d'un geste commer… |
| `gestion-commandes` | Créer une commande, suivre les commandes en cours ou changer le statut d'une commande (confirm… |
| `haccp-conformite-quotidienne` | Relevé de température, HACCP, contrôle réception, étiquette DLC, checklist hygiène, plan de ne… |
| `haccp-huiles-cycles-thermiques` | Huile de friture, de friteuse, de test de polaires, de filtration ou de changement d'huile, ou… |
| `handle-complaint` | Client se plaint (email, avis, ticket) et qu'il faut traiter la réclamation de bout en bout :… |
| `margin-analyzer` | Augmenter ses prix, de marges, de coûts qui grignotent le profit, ou demande « est-ce que je g… |
| `onboarding-restaurateur` | Nouveau client restaurateur démarre sur FoodEatUp, ou quand l'utilisateur dit « installe mon r… |
| `planning-equipe` | Planning, de shifts, d'horaires d'équipe, de demandes de congé, de pointages, de contrat de tr… |
| `price-check` | Vérifier ses prix ou voir ses marges par produit avant une décision tarifaire |
| `production-stock` | Planifier une production, consulter les alertes de production ou valider une production réalis… |
| `qr-codes-supports` | Un QR code (menu de table, réservation, avis Google, fidélité, roue cadeaux, sondage, carte ca… |
| `reappro-fournisseurs` | Stock bas, de commande fournisseur ou de réapprovisionnement |
| `recette-cout-marge` | Créer une recette, calculer le coût d'une recette, une marge, ou fixer un prix de vente |
| `recrutement-restaurant` | Recruter pour son restaurant — offres d'emploi, candidatures, statuts |
| `service-salle` | Réservation, d'installer un client, de plan de salle, de file d'attente ou de table libre |
| `site-vitrine-foodeatup` | Gérer son site vitrine FoodEatUp — « mon site », « publie ma page », « change le thème du site… |

## Agents (5)

- **`chef-cuisine`** — Chef de cuisine, expert fiches techniques et production.
- **`chef-de-passe`** — Chef de passe (comptoir d'envoi des plats) pendant le service.
- **`chef-restaurateur`** — Directeur de restaurant expérimenté.
- **`gerant-digital`** — Gérant de la présence en ligne du restaurant — orchestre le site vitrine, la fidélité, les avis et les leads captés.
- **`responsable-evenements`** — Responsable événementiel du restaurant.

## Installation

```
/plugin install foodeatup --marketplace PrendsTaPart/Plugin-Claude-MCP-BraindCode-
```

Au premier appel d'un outil, Claude Code ouvre la connexion OAuth au serveur
MCP FoodEatUp (`https://foodeatup.com/api/mcp`) avec votre compte FoodEatUp.
Dans Claude Code, les outils s'appellent
`mcp__plugin_foodeatup_foodeatup__<outil>`.

## Confidentialité & données

- Le plugin ne lit aucun fichier d'identification ni aucune variable
  d'environnement de la machine : l'accès au compte passe uniquement par la
  connexion OAuth du serveur MCP FoodEatUp.
- Les données envoyées au serveur sont celles des outils appelés (relevés
  HACCP, réservations, commandes, carte…), pour le compte connecté.
  Politique de confidentialité : https://site.foodeatup.com/confidentialite
- Les deux hooks (`hooks/scripts/*.sh`) sont des scripts shell locaux : ils lisent
  l'appel d'outil sur l'entrée standard pour demander une confirmation ou
  refuser une température invalide, et ne font aucun appel réseau.
- Les écritures sensibles (paiement, envois, suppressions, diffusion sur les
  écrans, modifications en masse) demandent toujours la confirmation de
  l'utilisateur.

## Serveurs MCP requis

`foodeatup` (seul serveur requis — plugin découplé de RapidoCRM) — connexion et clés : voir « Prérequis & connecteurs » du [README racine](../README.md). Aucune clé n'est stockée dans le dépôt.

## Déclencheurs (exemples réels)

- « ma journée »
- « est-ce que je gagne assez ? »
- « je devrais facturer plus ? »
- « installe mon restaurant »
- « mets le tartare en épuisé »
- « diffuse l'affiche happy hour sur la télé du bar »
- « qui faut-il rappeler aujourd'hui ? »
- « fais-moi la liste de courses pour 80 couverts samedi »

## Version & conventions

v1.11.1 — historique dans [CHANGELOG.md](CHANGELOG.md). Skills en français (« Utiliser quand… »), calculs par script stdlib, garde-fous déterministes, rien d'inventé (KB `./rapido-kb/` prioritaire).
