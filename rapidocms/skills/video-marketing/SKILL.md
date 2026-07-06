---
name: video-marketing
description: Utiliser quand l'utilisateur veut une vidéo, un teaser, une vidéo de campagne ou une vidéo du menu. Compose une vidéo HyperFrames (HeyGen) alignée sur la marque, la fait valider, la rend en MP4 (action payante) puis l'enchaîne dans le pipeline RapidoCMS.
---

# Vidéo marketing (HyperFrames × RapidoCMS)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (règles communes)
et `${CLAUDE_PLUGIN_ROOT}/reference/charte-graphique.md` ; KB :
`ton-et-accroches.md` + `charte-graphique.md` si `./rapido-kb/` existe.

## Workflow

1. **Brief** — objectif, message clé, durée cible, registre (pop/promo vs
   corporate). Refuser de composer sur un brief vague : clarifier d'abord
   (l'outil rejette les demandes floues).
2. **Composer** — `compose` (`prompt` requis) :
   - prompt DÉTAILLÉ : sujet, narration, textes à l'écran, ton (KB), couleurs
     de la charte, rythme ;
   - `designSource` selon le registre : `blockframe` pour du pop/promo,
     `signal` pour du corporate ; l'omettre = style maison par défaut ;
   - premier appel SANS `projectId` (nouveau projet) ; les itérations
     repassent le `projectId` retourné (et n'ajoutent `designSource` que pour
     changer volontairement de style).
   - La composition rend automatiquement un aperçu MP4 : pas de rendu à ce
     stade.
3. **Suivre** — `get_project_status` (`projectId`) : respecter STRICTEMENT
   `retry_after_seconds` (15 s) entre les appels, jamais plus vite. Statuts :
   `processing`/`pending` = en cours ; `waiting` = l'agent pose une question
   (`latest_agent_message`) → transmettre à l'utilisateur et répondre via un
   nouveau `compose` ; `draft`/`completed` = prêt ; `error`/`failed` = relayer
   le message et proposer de reformuler. Après ~5 min sans changement :
   demander à l'utilisateur s'il veut continuer d'attendre.
4. **Montrer la preview** — l'aperçu arrive dans `widget_data` (ou via
   `get_project`). Itérer avec `compose` (+ `projectId`) tant que l'utilisateur
   n'est pas satisfait.
5. **Rendu final — NIVEAU 3 DE CONFIRMATION** : `render_video` est PAYANT.
   Avant l'appel, annoncer explicitement « le rendu final est une action
   payante » et obtenir un OUI clair de l'utilisateur (pas de rendu implicite,
   pas pendant qu'une composition est en cours — statut `waiting`/`processing`
   = rendu rejeté).
6. **Livrer** — `get_render_status` (`projectId` + `videoId` retourné par
   `render_video` ; `retry_after_seconds` = 30 s) → transmettre l'URL MP4
   (`video_url`, URL signée à utiliser telle quelle) directement dans la
   réponse.
7. **Post CMS d'accompagnement (proposer)** — `upload_file_tool`
   (`type: "video"`, `file_url` = URL MP4) puis `create_draft_tool`
   (`post_type: "media"`, `media_type: "video"`, caption au ton de la marque)
   et `schedule_draft_tool` après confirmation.

## Garde-fous

- `render_video` : JAMAIS sans confirmation explicite du coût (niveau 3).
- Respecter les cadences de polling (`retry_after_seconds`) — pas de boucle
  rapide.
- Limite connue : sur certains clients (CLI/IDE), le serveur peut refuser
  `compose`/`render_video` et renvoyer vers les skills locaux HyperFrames
  (`npx skills add heygen-com/hyperframes`) — relayer ce message tel quel.
- Contenu : ton et accroches de la KB, pas de données personnelles clients
  dans une vidéo publique, chiffres avec source uniquement.
