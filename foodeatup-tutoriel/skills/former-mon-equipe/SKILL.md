---
name: former-mon-equipe
description: Utiliser quand on forme d'autres personnes que soi, que l'utilisateur dit « je dois former mes serveurs », « on intègre un nouveau commis lundi », « forme l'équipe cuisine au HACCP », « prépare le plan de formation du personnel ». Construit le plan d'équipe par postes — qui, sur quoi, dans quel ordre, avec les vidéos à remettre — sans jamais rien envoyer.
---

# Former mon équipe (le plan par postes)

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
   `${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.
2. KB : `./rapido-kb/entreprise.md` donne souvent les postes réels de
   l'équipe — partir de là.

## Workflow

1. **Cadrer** : secteur (`secteurSlug`) si doute, postes présents
   (`metierSlugs`, max 6 — ex. `["commis", "serveur"]`), niveau d'ensemble,
   temps par séance (`minutesParSeance`).
2. **`former_son_equipe`** — le plan renvoyé dit qui on forme, sur quoi,
   dans quel ordre, avec les vidéos à remettre. Le restituer par poste puis
   par séance, durées telles que renvoyées.
3. **Mettre en page** : proposer le widget `plan-formation-equipe`
   (`${CLAUDE_PLUGIN_ROOT}/scripts/render_widget.py`) — un plan imprimable à
   afficher en cuisine ou à remettre en main propre.
4. **Individualiser** : pour un membre précis qui sort du cadre, un
   programme personnel via `parcours_apprentissage` (skill
   `parcours-sur-mesure`).
5. **Suivre** : chaque personne tient SON code de reprise
   (skill `carnet-de-reprise`) ; le responsable garde la liste des codes.
6. Au moment de pratiquer sur le compte réel (créer les employés, les
   plannings) : skill `passer-a-l-action` — ce plugin n'agit pas.

## Garde-fous

- **Aucun message n'est « envoyé »** : ce plugin n'a aucun outil d'envoi
  (ni mail, ni WhatsApp). Les vidéos et plans se REMETTENT (lien, papier,
  oral) — ne jamais dire « j'ai envoyé ».
- Un poste absent des slugs du secteur ne s'invente pas ; faire choisir
  parmi les postes proposés.
- Les vidéos listées dans le plan existent (elles viennent du serveur) ; un
  sujet non filmé pour un poste se signale, il ne se remplace pas par une
  improvisation.
