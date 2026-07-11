---
name: scale-cold-email-prospection
description: "Utiliser quand l'utilisateur veut rédiger une séquence de cold emails avec personnalisation et follow-ups (parcours scale StartupsForge)."
---

# Cold Email Prospection

**Catégorie** : Scale  
**Durée** : 30 min

## Pourquoi

Un cold email bien rédigé atteint 40%+ de taux d'ouverture vs 15% en moyenne. C'est le canal le plus scalable pour la prospection B2B avec un coût quasi nul.

## Objectif

Rédiger une séquence de cold emails avec personnalisation et follow-ups.

## Livrable attendu

3 templates de cold emails + séquence de 4-5 follow-ups + ligne de sujet testées

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Définir l'ICP précis** — À qui écris-tu ? Titre, entreprise, taille, douleur
2. **Écrire la ligne de sujet** — Court, curieux, personnalisé - pas de 'Opportunité pour vous'
   > Prompt: Génère 10 lignes de sujet pour un cold email à [PERSONA] concernant [PROBLÈME]
3. **Structurer le corps** — Hook personnalisé → Problème → Solution (1 phrase) → CTA clair
4. **Créer la séquence de follow-up** — 4-5 emails espacés de 3-4 jours avec angles différents
5. **Préparer l'A/B testing** — 2 versions de sujet et hook à tester

## Pro tips

- L'email doit faire moins de 100 mots - mobile first
- Une seule question/CTA par email
- Personnalise les 2 premières phrases avec une vraie recherche

## Erreurs fréquentes

- Parler de soi au lieu de parler du client
- Email trop long (plus de 100 mots)
- CTA vague ('si vous êtes intéressé...')

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **RapidoCMS** (`rapidocms`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/scale/scale-cold-email-prospection.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapidocrm:predictable-revenue` — machine outbound complète
- `rapidocrm:draft-outreach` — premier message personnalisé
