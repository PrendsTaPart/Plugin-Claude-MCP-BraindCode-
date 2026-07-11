---
name: scale-nps-survey
description: "Utiliser quand l'utilisateur veut mettre en place une mesure régulière du NPS avec actions correctives (parcours scale StartupsForge)."
tags: [data]
niveau: intermediaire
---

# Nps Survey

**Catégorie** : Scale  
**Durée** : 30 min

## Pourquoi

Le NPS (Net Promoter Score) mesure la satisfaction et la propension à recommander. Un NPS > 50 est excellent. C'est LE KPI qui prédit le growth par referral.

## Objectif

Mettre en place une mesure régulière du NPS avec actions correctives.

## Livrable attendu

Survey NPS automatisé + tableau de suivi + process de follow-up

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Choisir l'outil** — Delighted, Typeform, Wootric, in-app custom
2. **Définir le timing** — Après quel événement envoyer ? (X jours après signup, post-usage)
   > Prompt: Quel est le meilleur moment pour envoyer un NPS pour un SaaS [TYPE] ?
3. **Configurer les questions** — Score 0-10 + question ouverte 'Pourquoi ?'
4. **Définir les segments** — Détracteurs (0-6), Passifs (7-8), Promoteurs (9-10)
5. **Créer le follow-up** — Actions par segment, closing the loop

## Pro tips

- La question ouverte est plus précieuse que le score lui-même
- Contacte personnellement les détracteurs pour comprendre
- Les promoteurs sont tes meilleurs candidats referral

## Erreurs fréquentes

- Envoyer trop tôt (avant que le user ait expérimenté la valeur)
- Ne pas lire les réponses ouvertes
- Ignorer les détracteurs au lieu de les reconvertir

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-nps-survey.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapidocrm:animation-client` — sondage NPS réel dans le CRM
