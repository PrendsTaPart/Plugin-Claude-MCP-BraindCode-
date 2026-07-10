---
name: bibliotheque-prompts
description: Utiliser quand l'utilisateur veut sauvegarder un prompt qui a bien fonctionné, réutiliser un prompt gagnant, ou gérer sa bibliothèque de prompts (visuels, copy, vidéo).
---

# Bibliothèque de prompts — capitaliser les prompts gagnants

La bibliothèque RapidoCMS est la mémoire des prompts qui MARCHENT : chaque
génération réussie l'enrichit, chaque nouvelle génération commence par la
consulter. Économie d'itérations = économie réelle.

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.
**Piège de schéma (vérifié serveur)** : `type` n'accepte QUE `text` ou
`visuel` — pas de type « vidéo » : les prompts vidéo se rangent en `visuel`
avec un titre préfixé « vidéo — ».

## Consulter AVANT de générer

`list_prompts` (`type: "visuel"` pour l'image/vidéo, `"text"` pour le copy ;
`search` par mot-clé du sujet) **AVANT toute génération d'image** :
- un prompt proche existe → le PROPOSER comme base, placeholders
  `[entre crochets]` remplacés par les valeurs du brief — on itère depuis un
  gagnant, on ne repart pas de zéro ;
- rien d'adapté → générer normalement (et capitaliser à la fin).
C'est l'Étape 0 des skills `prompt-engineering-visuel` et
`prompts-visuels-pro`, qui délèguent ici la gestion de la bibliothèque.

## Sauvegarder — à chaque visuel VALIDÉ (proposer, pas imposer)

Quand l'utilisateur VALIDE un visuel (ou un copy/une vidéo), **proposer** la
sauvegarde — jamais l'imposer ni sauvegarder en silence :

- `add_prompt` avec :
  - **`title` normalisé : « type — sujet — style »** (ex. « visuel — plat
    signature — photo chaude », « vidéo — teaser menu — pop », « copy —
    relance devis — AIDA ») ;
  - **`content` = le prompt COMPLET, négatifs inclus** (bloc positif +
    `Négatif : …`), valeurs spécifiques généralisées en placeholders
    `[entre crochets]` (`[nom du plat]`, `[couleur primaire]`…) ;
  - `type` = `visuel` (image ET vidéo) ou `text` (copy).
- Vérifier d'abord via `list_prompts` qu'un équivalent n'existe pas déjà —
  sinon proposer l'amélioration plutôt que le doublon.

## Versionner et nettoyer

- **`edit_prompt`** (`prompt_id`) pour versionner une amélioration d'un
  prompt existant : conserver le même `title` (ajouter « v2 » seulement si
  les deux versions doivent coexister), mettre à jour le `content`.
- **`delete_prompt`** (`prompt_id`) UNIQUEMENT sur confirmation explicite
  (hook garde-destructif en filet) — proposer d'abord l'archivage par
  édition du titre (« [obsolète] … ») si l'historique a de la valeur.

## Garde-fous

- Jamais de sauvegarde silencieuse : l'utilisateur valide le visuel PUIS la
  capitalisation.
- Un prompt sauvegardé sans ses négatifs est incomplet (voir
  `prompts-visuels-pro`) : les inclure dans le `content`.
- Les données métier du prompt (prix, noms) se généralisent en placeholders
  — la bibliothèque est réutilisable, pas un journal.
