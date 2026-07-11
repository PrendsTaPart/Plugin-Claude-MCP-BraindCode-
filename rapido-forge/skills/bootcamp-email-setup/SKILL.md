---
name: bootcamp-email-setup
description: "Utiliser quand l'utilisateur veut configure ses séquences email (bootcamp 5 jours StartupsForge — Jour 4)."
---

# Email Marketing Setup

**Bootcamp 5 jours — Jour 4**  
**Catégorie** : Marketing  
**Framework** : Email Marketing Automation  
**Durée** : 35 min

## Objectif

Configure tes séquences email

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Choisir l'outil et le domaine d'envoi** — sous-domaine dédié (ex. mail.domaine.com) pour protéger le domaine principal
2. **Configurer SPF, DKIM, DMARC** — non négociable : sans ça, direction spam
3. **Créer les listes et le consentement** — opt-in propre, RGPD, lien de désinscription
4. **Séquence de bienvenue** — 3 emails : livrer la promesse, prouver, proposer l'étape suivante
5. **Warmup** — monter le volume progressivement, surveiller bounces et plaintes

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **RapidoCMS** (`rapidocms`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/bootcamp/bootcamp-email-setup.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-forge:ideation-email-marketing-setup` — setup email marketing
