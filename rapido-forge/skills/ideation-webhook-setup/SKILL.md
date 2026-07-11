---
name: ideation-webhook-setup
description: "Utiliser quand l'utilisateur veut configurer un webhook pour capturer les leads de son formulaire (parcours idéation StartupsForge)."
tags: [organisation, data]
niveau: intermediaire
---

# Webhook Setup

**Catégorie** : Idéation  
**Durée** : 25-35 min

## Pourquoi

Les webhooks connectent tes outils entre eux automatiquement. Sans automation, tu passeras des heures à copier-coller des données manuellement.

## Objectif

Configurer un webhook pour capturer les leads de ton formulaire.

## Livrable attendu

Webhook fonctionnel envoyant les données vers ton CRM/outil

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Créer le workflow n8n/Make** — Nouveau workflow avec trigger Webhook
2. **Copier l'URL du webhook** — URL unique générée par l'outil
3. **Configurer dans le formulaire** — Tally/Typeform → Settings → Webhooks
4. **Mapper les données** — email → email, name → name...
5. **Tester le flux** — Soumets un formulaire test

## Pro tips

- Toujours tester avec des données fictives d'abord
- Log les erreurs pour débugger
- Ajoute un email de confirmation

## Erreurs fréquentes

- Mauvais mapping des champs
- Pas de gestion des erreurs
- URL webhook non sécurisée

## Données & serveurs MCP

- **RapidoCMS** (`rapidocms`) — données réelles, lecture d'abord
- **n8n** (`n8n`, via le plugin `rapido-n8n`) — workflow testé puis publié après confirmation

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/ideation/ideation-webhook-setup.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-n8n:usine-automatisations` — webhooks dans un workflow n8n
