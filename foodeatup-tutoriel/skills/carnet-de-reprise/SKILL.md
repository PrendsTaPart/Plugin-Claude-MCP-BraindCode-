---
name: carnet-de-reprise
description: Utiliser quand une séance de formation se clôt ou reprend, que l'utilisateur dit « on reprendra demain », « garde ma progression », « voici mon code de reprise », « où j'en étais ? ». Encode un code court qui mémorise l'avancement, et le décode à la séance suivante pour repartir exactement là où on s'était arrêté.
---

# Carnet de reprise (encoder en partant, décoder en revenant)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.

## Workflow — fin de séance (encoder)

1. Rassembler l'état réel de la séance : `slugsVus` (dans l'ordre vu),
   `secteurSlug`, `metierSlug`, `niveau` (défaut `debutant`).
2. **`carnet_de_formation`** avec `mode: "encoder"` — remettre le code
   renvoyé à l'utilisateur, en expliquant : « notez-le, il me redonnera
   votre progression à la prochaine séance ». Le `mode` est obligatoire
   (piège vérifié).
3. Rappeler ce que le code contient (et ne contient pas) : il ne vaut que ce
   que `slugsVus` portait — rien d'autre n'est mémorisé.

## Workflow — début de séance (décoder)

1. **`carnet_de_formation`** avec `mode: "decoder"` et le `code` fourni.
2. Confirmer à voix haute ce qui est relu (secteur, métier, niveau, leçons
   vues) — si l'utilisateur corrige, c'est sa parole qui prime.
3. Enchaîner sur la suite : `lecon_suivante` avec les `dejaVus` du carnet
   (skill `parcours-sur-mesure`).

## Garde-fous

- Proposer l'encodage SYSTÉMATIQUEMENT en fin de séance — une progression
  non encodée est perdue.
- Un code illisible ou refusé par le serveur : le dire et recadrer via le
  skill `demarrer-academie`, ne jamais « reconstituer » une progression de
  mémoire.
- Chaque personne a son code (une formation d'équipe = un code par membre,
  skill `former-mon-equipe`).
