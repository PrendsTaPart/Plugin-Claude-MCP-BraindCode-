---
name: ideation-email-marketing-setup
description: "Utiliser quand l'utilisateur veut configurer son système d'email marketing complet avec automation (parcours idéation StartupsForge)."
tags: [marketing, contenu]
niveau: debutant
---

# Email Marketing Setup

**Catégorie** : Idéation  
**Durée** : 35-45 min

## Pourquoi

L'email marketing a le meilleur ROI de tous les canaux (42$ pour 1$ investi). Configurer correctement ton système dès le départ évite les problèmes de délivrabilité.

## Objectif

Configurer ton système d'email marketing complet avec automation.

## Livrable attendu

Compte email marketing configuré + premier workflow automation

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Choisir la plateforme** — Mailerlite (gratuit), ConvertKit, ou Resend pour les devs
2. **Configurer le domaine** — SPF, DKIM, DMARC pour la délivrabilité
3. **Créer les segments** — Prospects froids, leads chauds, clients
4. **Importer les contacts** — Nettoie ta liste avant import (pas de emails invalides)
5. **Créer le premier workflow** — Séquence de bienvenue automatique

## Pro tips

- Commence avec une plateforme gratuite comme Mailerlite
- Double opt-in pour une meilleure délivrabilité
- Segmente dès le début, même avec peu de contacts

## Erreurs fréquentes

- Ne pas configurer les enregistrements DNS (emails en spam)
- Acheter des listes email (illégal et inefficace)
- Envoyer sans avoir vérifié sur plusieurs clients email

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **RapidoCMS** (`rapidocms`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/ideation/ideation-email-marketing-setup.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapidocms:email-sequence` — séquences complètes
