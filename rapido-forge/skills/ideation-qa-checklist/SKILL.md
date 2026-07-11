---
name: ideation-qa-checklist
description: "Utiliser quand l'utilisateur veut tester exhaustivement son site avant le lancement (parcours idéation StartupsForge)."
---

# Qa Checklist

**Catégorie** : Idéation  
**Durée** : 45-60 min

## Pourquoi

Un bug le jour du lancement peut ruiner des semaines de travail. Le QA final garantit une expérience impeccable pour tes premiers visiteurs.

## Objectif

Tester exhaustivement ton site avant le lancement.

## Livrable attendu

Checklist QA complétée avec tous les tests passés

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Tester tous les liens** — Liens internes, externes, boutons
2. **Vérifier les formulaires** — Soumission, validation, réception
3. **Tester sur mobile** — iOS et Android, différentes tailles
4. **Vérifier la performance** — Temps de chargement < 3s, Core Web Vitals
5. **Tester les edge cases** — Erreurs 404, champs vides, navigation

## Pro tips

- Teste dans différents navigateurs (Chrome, Safari, Firefox)
- Demande à quelqu'un d'extérieur de tester
- Vérifie les redirections et le sitemap

## Erreurs fréquentes

- Tester seulement sur son propre appareil
- Ignorer les performances mobile
- Oublier les pages légales (CGV, mentions)

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/ideation/ideation-qa-checklist.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).
