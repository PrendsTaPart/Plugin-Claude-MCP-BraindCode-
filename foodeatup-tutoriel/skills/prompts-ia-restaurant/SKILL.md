---
name: prompts-ia-restaurant
description: Utiliser quand on cherche quoi demander à l'IA, que l'utilisateur dit « quels prompts utiliser avec FoodEatUp », « comment te parler pour la caisse », « donne-moi des exemples de demandes », « le prompt de cette fiche ». Sert la bibliothèque de prompts de formation par niveau et les prompts prêts à l'emploi d'un tutoriel précis.
---

# Prompts IA du restaurant (la bibliothèque et les prompts de fiche)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.

## Workflow

1. **Demande générale** (« comment te parler ? ») : `prompts_formation` —
   filtrer par `niveau` si le profil est connu (`Découverte`,
   `Prise en main`, `Métier`, `Pilotage`). Présenter 3 à 5 prompts
   pertinents pour la situation, pas la bibliothèque entière.
2. **Demande liée à une fiche** : `obtenir_prompts_tutoriel` (slug) —
   prompts de la fiche, astuce du chef et conseils. Slug inconnu → skill
   `trouver-un-tuto` d'abord.
3. **Expliquer l'usage** : ces prompts s'adressent à un assistant branché
   sur le connecteur produit (compte réel). Tant que le connecteur n'est pas
   installé, les prompts se lisent comme des exemples — l'installation,
   c'est le skill `passer-a-l-action`.
4. Les placeholders type `[ID établissement]` dans un prompt se remplacent
   par les valeurs RÉELLES de l'utilisateur — jamais par une valeur
   inventée ; s'il ne la connaît pas, lui montrer où la trouver (fiche du
   tutoriel concerné).

## Garde-fous

- Les prompts se citent tels que renvoyés (reformulation possible UNIQUEMENT
  si l'utilisateur la demande, en gardant les placeholders intacts).
- Ne jamais exécuter soi-même un prompt destiné au connecteur produit : ce
  plugin enseigne, il n'agit pas.
