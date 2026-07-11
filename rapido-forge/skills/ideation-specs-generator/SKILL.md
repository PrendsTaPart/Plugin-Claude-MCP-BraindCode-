---
name: ideation-specs-generator
description: "Utiliser quand l'utilisateur veut créer un cahier des charges technique complet avec wireframes pour faire développer son MVP (parcours idéation StartupsForge)."
---

# Specs Generator

**Catégorie** : Idéation  
**Durée** : 45-60 min

## Pourquoi

Un cahier des charges professionnel est indispensable pour faire développer ton projet par une agence ou un freelance. Sans spécifications claires, tu risques des malentendus coûteux, des délais explosés et un produit qui ne correspond pas à ta vision. 70% des projets échouent à cause d'un mauvais cadrage initial.

## Objectif

Créer un cahier des charges technique complet avec wireframes pour faire développer ton MVP.

## Livrable attendu

Cahier des charges PDF de 20-40 pages incluant : contexte, MCD/MLD, user stories, wireframes et planning

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Renseigner la page de garde** — Nom du projet, contacts, identification du commanditaire
2. **Définir le contexte et objectifs** — Pourquoi ce projet ? Quels résultats attendus ?
   > Prompt: Génère une introduction pour un projet de [TYPE] qui vise à [OBJECTIF PRINCIPAL]
3. **Lister les problématiques** — Besoins fonctionnels, acteurs du système, périmètre
4. **Créer le MCD/MLD** — Entités, attributs, relations entre les données
   > Prompt: Génère un MCD pour une application de [TYPE] avec les entités : [LISTE]
5. **Rédiger les user stories** — En tant que [ROLE], je veux [ACTION] afin de [BÉNÉFICE]
6. **Définir l'architecture technique** — Technologies frontend, backend, base de données, APIs
7. **Générer les wireframes IA** — Maquettes des écrans principaux générées par l'IA
8. **Exporter le PDF** — Document professionnel prêt à envoyer aux développeurs

## Pro tips

- Complète ton DNA projet avant de commencer pour de meilleures générations IA
- Sélectionne les APIs recommandées depuis le Marketplace pour enrichir ton stack technique
- Génère les wireframes APRÈS avoir décrit les fonctionnalités pour plus de précision
- Fais relire ton CDC par un profil technique avant de l'envoyer à une agence
- Utilise le CTA BraindCode pour obtenir un devis gratuit sous 48h

## Erreurs fréquentes

- Cahier des charges trop vague sans user stories précises
- Oublier de spécifier les contraintes techniques (performance, sécurité)
- Ne pas inclure de wireframes - les développeurs ont besoin de visuels
- Sous-estimer le temps de développement dans le planning

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/ideation/ideation-specs-generator.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).
