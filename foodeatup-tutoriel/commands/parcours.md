---
description: Programme de formation sur mesure (métier, module ou objectif)
argument-hint: "<métier, module ou objectif> [minutes/séance]"
---

Dérouler le skill `parcours-sur-mesure` :

- un métier (« serveur », « chef de cuisine ») → `parcours_apprentissage`
  avec `metierSlug` ;
- un module (« haccp », « caisse ») → `moduleSlug` ;
- un objectif libre → d'abord le cadrage du skill `demarrer-academie` si le
  secteur/niveau ne sont pas connus ;
- un nombre en fin d'argument = `minutesParSeance`.

Le `niveau` est obligatoire pour l'outil : le demander s'il n'est pas
déductible de la conversation.
