---
name: ideation-automation-workflow
description: "Utiliser quand l'utilisateur veut créer un workflow complet de traitement des nouveaux leads (parcours idéation StartupsForge)."
---

# Automation Workflow

**Catégorie** : Idéation  
**Durée** : 40-60 min

## Pourquoi

L'automation peut économiser 10+ heures par semaine. Un workflow bien configuré traite tes leads 24/7 sans intervention humaine.

## Objectif

Créer un workflow complet de traitement des nouveaux leads.

## Livrable attendu

Workflow automatisé : capture → enrichissement → notification → séquence email

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Mapper le parcours lead** — Formulaire → CRM → Email → Notification
2. **Configurer le trigger** — Webhook ou app native (Tally, Typeform)
3. **Ajouter les actions** — Créer contact CRM, envoyer email, notifier Slack
4. **Ajouter les conditions** — Si email pro → tag 'B2B', etc.
5. **Activer et monitorer** — Logs, alertes d'erreur

## Pro tips

- Commence simple, complexifie ensuite
- Teste chaque étape individuellement
- Documente ton workflow pour les futurs membres

## Erreurs fréquentes

- Workflow trop complexe dès le début
- Pas de monitoring des erreurs
- Données dupliquées sans déduplication

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **n8n** (`n8n`, via le plugin `rapido-n8n`) — workflow testé puis publié après confirmation

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/ideation/ideation-automation-workflow.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-n8n:usine-automatisations` — workflow n8n réel, testé et publié
