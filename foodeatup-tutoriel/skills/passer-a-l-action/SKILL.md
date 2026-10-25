---
name: passer-a-l-action
description: Utiliser quand la formation doit déboucher sur un geste réel, que l'utilisateur dit « ok, fais-le sur mon compte », « crée-le pour de vrai », « comment je branche Claude à mon restaurant », « passe à la pratique ». Explique le pont entre l'Académie (qui enseigne) et le connecteur produit (qui agit), guide son installation et passe le relais aux bons skills produit.
---

# Passer à l'action (le pont vers le compte réel)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.

## Le principe (à dire tel quel)

Ce serveur de formation est public et en lecture seule : **il n'agit sur
aucun compte**. Agir pour de vrai (créer un shift, saisir un relevé HACCP,
modifier la carte) demande le **connecteur produit FoodEatUp** :
https://foodeatup.com/api/mcp — personnel, protégé par jeton, à installer
par l'utilisateur dans ses réglages de connecteurs. **Ce plugin ne
l'appellera jamais lui-même.**

## Workflow

1. **Vérifier l'équipement** : le connecteur produit est-il déjà branché
   (des outils FoodEatUp produit apparaissent dans la session) ? Si oui,
   sauter à l'étape 4.
2. **Guider l'installation par la leçon officielle** : dérouler le tutoriel
   `brancher-son-mcp-sur-claude` avec le skill `lecon-guidee` (vidéo 0:36,
   étapes à l'écran). L'URL se copie depuis la Marketplace de prompts de
   FoodEatUp — l'utilisateur colle, nomme, valide, puis choisit précisément
   les outils autorisés (et peut révoquer à tout moment).
3. **Côté développeur/automatisation** (n8n, scripts, clé API) : skill
   `developpeur-api` — jamais d'endpoint improvisé.
4. **Passer le relais au bon plugin produit** : une fois le connecteur en
   place, les gestes réels se mènent avec le plugin `foodeatup`
   (ex. skill `haccp-conformite-quotidienne`, skill `onboarding-restaurateur`)
   et le diagnostic par boucle avec `foodeatup-boucles`. L'exercice en cours
   (`exercice_pratique`) se rejoue alors en vrai, avec ses critères de
   réussite comme checklist.
5. **Boucler la boucle pédagogique** : après le geste réel, revenir à la
   formation (quiz de validation, leçon suivante) — skill `lecon-guidee`.

## Garde-fous

- Jamais d'action simulée « comme si » le connecteur était là : sans
  connecteur produit, on guide l'humain clic par clic, on n'invente pas de
  résultat.
- Le jeton du connecteur produit est un secret personnel : il ne se colle ni
  dans la conversation ni dans un fichier du dépôt.
- Les exercices gardent leurs critères de réussite du serveur — la réussite
  se constate (par l'utilisateur ou par le plugin produit), elle ne se
  déclare pas.
