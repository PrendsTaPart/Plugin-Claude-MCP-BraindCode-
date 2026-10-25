---
name: routines-sur-evenement
description: Utiliser quand une routine doit réagir à un événement, que l'utilisateur dit « quand je reçois un e-mail de… », « dès qu'un message arrive », « à chaque nouvel événement d'agenda, lance… ». Liste les événements des connecteurs réellement connectés, branche la routine en gouvernance validation par défaut, débranche sur confirmation.
---

# Routines sur événement (déclenchées, pas planifiées)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.

## Workflow

1. **`list_event_sources`** — les événements disponibles (nouvel e-mail
   Gmail, message, événement d'agenda…) parmi les connecteurs Composio
   RÉELLEMENT connectés, avec le slug et la configuration attendue. Un
   connecteur absent de la liste n'est pas connecté → proposer de le
   connecter (app), ne pas promettre l'événement.
2. **La routine cible** : elle doit appartenir à l'utilisateur et exister
   (sinon, la concevoir d'abord — skill `creer-une-routine`).
3. **`subscribe_event`** — gouvernance **`validation` par défaut** (la
   routine est PROPOSÉE à chaque événement) ; `alerte` si l'utilisateur veut
   seulement être prévenu ; **`auto` seulement sur sa décision explicite, et
   REFUSÉ si la routine contient un outil destructif** (règle du serveur ;
   le hook garde-autonomie bloque en filet).
4. **`unsubscribe_event`** — sur confirmation (le trigger Composio est
   révoqué, plus aucune alerte ni lancement) ; l'ID vient du subscribe ou de
   la liste des abonnements.
5. Les routines événementielles se retrouvent À PART dans le calendrier
   (`event_routines` — skill `agenda-des-routines`).

## Garde-fous

- Jamais un abonnement auto par défaut ; jamais un événement promis sur un
  connecteur non connecté.
- Un événement bavard (boîte mail très active) se signale : la gouvernance
  validation peut générer beaucoup de propositions — en parler avant.
