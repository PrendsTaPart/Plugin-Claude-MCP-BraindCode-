---
name: lecon-guidee
description: Utiliser quand on suit une leçon précise, que l'utilisateur dit « montre-moi comment faire un relevé de température », « lance la vidéo », « je ne peux pas regarder, donne-moi le texte », ou après chaque leçon d'un parcours. Déroule le rituel complet d'une leçon — vignette, vidéo, étapes, quiz, exercice — une leçon à la fois.
---

# Leçon guidée (le rituel vidéo → quiz → exercice)

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
   `${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.
2. Pas de slug en main → le trouver avec le skill `trouver-un-tuto` (jamais
   de slug deviné).

## Workflow

1. **Annoncer la leçon** : `lecteur_video_tutoriel` (slug) — lire
   `aDireAvantDeLancer` à voix haute, joindre la vignette en bloc image
   (`vignetteUrl`), donner le lecteur (`markdown` ou `lecteurHtml`) et la
   durée. Pour un simple aperçu sans lancer la vidéo : `apercu_video`.
2. **Pendant la vidéo** : afficher les `etapes` renvoyées (à suivre en
   parallèle). Vidéos longues : s'il y a des chapitres, les proposer via le
   widget `lecteur-chapitres` ; sinon les `etapes` tiennent ce rôle (piège
   vérifié).
3. **L'utilisateur ne peut pas regarder** → `transcription_tutoriel`
   (texte intégral, ou `recherche` pour retrouver un passage précis).
4. **Quiz après la leçon** : `quiz_tutoriel` (slug ; `graine` = date ou
   prénom pour varier les propositions). Suivre la `consigne` du serveur :
   une question à la fois, réponse cachée, correction en une phrase, renvoi
   vers la vidéo du champ `revoir` en cas d'erreur, note sur le total à la
   fin. Option widget `quiz-interactif`.
5. **Exercice après le quiz** : `exercice_pratique` (slug) — énoncer
   l'exercice et ses critères de réussite. L'exercice se fait DANS
   FoodEatUp : s'il faut agir par l'IA, passer le relais au skill
   `passer-a-l-action`.
6. **Prompts associés** : `obtenir_prompts_tutoriel` pour donner les
   demandes prêtes à l'emploi et l'astuce du chef de la fiche.
7. Clore : proposer `lecon_suivante` (skill `parcours-sur-mesure`) ou le
   code de reprise (skill `carnet-de-reprise`).

## Garde-fous

- Une leçon à la fois ; vignette toujours jointe en bloc image — un lien nu
  ne suffit pas.
- Ne jamais « corriger » un quiz en inventant : la `bonneReponse` du serveur
  fait foi ; en cas d'erreur, c'est la vidéo `revoir` qu'on rejoue.
- Jamais de réponse du quiz montrée avant que l'utilisateur ait répondu.
- Aucun lien ni slug de mémoire : tout vient de la réponse en cours.
