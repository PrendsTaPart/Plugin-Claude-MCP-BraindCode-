---
name: ideation-email-sequence
description: "Utiliser quand l'utilisateur veut rédiger un email de bienvenue engageant (parcours idéation StartupsForge)."
---

# Email Sequence

**Catégorie** : Idéation  
**Durée** : 25-35 min

## Pourquoi

L'email de bienvenue a un taux d'ouverture de 50-60% - le plus élevé de toute séquence. C'est ton meilleur moment pour créer une connexion.

## Objectif

Rédiger un email de bienvenue engageant.

## Livrable attendu

Email de bienvenue formaté avec objet, corps et CTA

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Écrire l'objet** — Court, personnalisé, promesse de valeur
2. **Rédiger l'intro** — Remerciement + rappel de ce qu'ils vont recevoir
   > Prompt: Écris un email de bienvenue chaleureux pour les nouveaux abonnés de [STARTUP]. Ton: [STYLE]. Inclure: remerciement, ce qu'ils vont apprendre, premier conseil actionable, CTA
3. **Délivrer de la valeur immédiate** — Premier conseil, ressource, ou accès
4. **Ajouter le CTA** — Une seule action claire
5. **Configurer l'envoi auto** — Trigger sur inscription

## Pro tips

- L'objet personnalisé (prénom) augmente les ouvertures de 26%
- Donne de la valeur AVANT de demander quoi que ce soit
- Un seul CTA par email

## Erreurs fréquentes

- Email trop long
- Pas de valeur immédiate
- Plusieurs CTAs qui confusent

## Données & serveurs MCP

- **RapidoCMS** (`rapidocms`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/ideation/ideation-email-sequence.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapidocms:email-sequence` — séquence complète : copy, timing, embranchements, benchmarks
