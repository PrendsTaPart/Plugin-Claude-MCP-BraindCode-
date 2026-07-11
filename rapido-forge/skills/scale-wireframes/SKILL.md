---
name: scale-wireframes
description: "Utiliser quand l'utilisateur veut esquisser les 5 écrans clés de son application (parcours scale StartupsForge)."
---

# Wireframes

**Catégorie** : Scale  
**Durée** : 45 min

## Pourquoi

Les wireframes permettent d'itérer rapidement sur l'UX avant d'investir en design ou code. Corriger une erreur UX en wireframe coûte 100x moins cher qu'après développement.

## Objectif

Esquisser les 5 écrans clés de ton application.

## Livrable attendu

5 wireframes low-fidelity validés avec flow annotés

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Identifier les 5 écrans clés** — Home, Sign-up, Dashboard, Core feature, Settings
2. **Sketcher le layout** — Zones de contenu, navigation, CTA principaux
   > Prompt: Quel layout pour une page [TYPE] d'une app [DESCRIPTION] ?
3. **Annoter les interactions** — Où clique-t-on ? Que se passe-t-il ?
4. **Créer le flow** — Liens entre les écrans, parcours principal
5. **Valider avec des users** — Test 'paper prototype' avec 3 personnes

## Pro tips

- Low-fidelity = boîtes grises, pas de couleurs ni d'images
- Focus sur la hiérarchie d'information et le flow
- Teste avec de vrais utilisateurs, même au stade wireframe

## Erreurs fréquentes

- Trop de détails visuels (c'est du wireframe, pas du design)
- Oublier les états vides et les erreurs
- Ne pas tester avant de passer au high-fidelity

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **Lovable** (`lovable`, via le plugin `rapido-lovable`) pour la construction réelle

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-wireframes.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-lovable:frontend-design` — construction réelle
