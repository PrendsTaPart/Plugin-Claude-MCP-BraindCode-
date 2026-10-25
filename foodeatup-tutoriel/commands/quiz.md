---
description: Quiz de l'Académie sur un tutoriel ou un module
argument-hint: "<slug de tutoriel ou slug de module>"
---

Lancer `quiz_tutoriel` selon l'argument :

- slug de tutoriel → quiz ciblé (`slug`) ;
- slug de module (ex. « haccp ») → quiz de révision (`moduleSlug`) ;
- sans argument : quiz sur la dernière leçon vue dans la conversation,
  sinon demander le sujet.

Toujours appliquer la consigne du serveur (skill `lecon-guidee`, étape
quiz) : une question à la fois, réponse cachée, correction en une phrase,
renvoi vers la vidéo `revoir` en cas d'erreur, note finale. Passer une
`graine` (date du jour ou prénom) pour varier les propositions d'un passage
à l'autre.
