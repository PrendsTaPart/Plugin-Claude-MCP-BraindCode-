---
name: ideation-legal-docs
description: "Utiliser quand l'utilisateur veut générer des CGV et mentions légales conformes (parcours idéation StartupsForge)."
tags: [juridique]
niveau: debutant
---

# Legal Docs

**Catégorie** : Idéation  
**Durée** : 30-40 min

## Pourquoi

Les CGV et mentions légales sont obligatoires et te protègent juridiquement. C'est aussi un signal de professionnalisme pour tes clients.

## Objectif

Générer des CGV et mentions légales conformes.

## Livrable attendu

Pages légales prêtes à publier

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Collecter les infos requises** — Raison sociale, SIRET, adresse, etc.
2. **Générer avec l'IA** — Template adapté à ton activité
   > Prompt: Génère des CGV pour une [ACTIVITÉ] en France. Inclus : responsabilité, paiement, livraison, rétractation.
3. **Ajouter les mentions légales** — Hébergeur, cookies, RGPD
4. **Faire relire par un juriste** — Pour validation finale
5. **Publier sur le site** — Footer accessible partout

## Pro tips

- Les générateurs gratuits sont un bon départ
- Fais toujours valider par un professionnel
- Mets à jour lors de changements d'activité

## Erreurs fréquentes

- Copier-coller sans adapter
- Oublier les cookies/RGPD
- Pas de date de mise à jour

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/ideation/ideation-legal-docs.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).
