---
name: prompts-academie
description: Utiliser quand l'utilisateur cherche un prompt prêt à l'emploi de l'Académie FoodEatUp — « y a-t-il un prompt pour ça », « montre le marketplace de prompts », « donne-moi le prompt du briefing », « partage ce cours en lien public ». Marketplace de prompts et liens publics de l'Académie.
---

# Prompts de l'Académie & liens publics

## Enchaînement d'outils MCP (lecture seule)

1. `marketplace_list_prompts` : le catalogue des prompts publiés par
   l'Académie — filtrer par le besoin exprimé, présenter 3 candidats maximum
   avec leur usage en une ligne.
2. `marketplace_get_prompt` : le texte complet du prompt choisi. Le restituer
   TEL QUEL (c'est un contenu d'auteur), puis proposer de l'adapter au
   contexte de l'utilisateur — l'adaptation est une copie de travail, pas une
   modification du marketplace.
3. Partage : `academy_get_public_link` pour le lien public d'un contenu,
   `academy_list_public_links` pour l'inventaire des liens déjà créés.

## Règles

- Un prompt du marketplace s'exécute avec les outils des plugins concernés
  (foodeatup, rapidocms…) — vérifier que les serveurs cités sont connectés
  avant de promettre le résultat.
- Créer un nouveau prompt au marketplace → `admin_prompt_create` (skill
  `fabriquer-des-cours`, brouillon + validation humaine).
- Les prompts personnels Braindcode (serveur Braindcode_Plugin) sont un autre
  catalogue : ne pas confondre les deux sources, citer laquelle on utilise.

## Ce que ce skill NE fait PAS

- Dérouler la formation → skill `se-former-foodeatup`.
- Gérer la bibliothèque de prompts VISUELS RapidoCMS → plugin rapidocms
  (skill `bibliotheque-prompts`).
