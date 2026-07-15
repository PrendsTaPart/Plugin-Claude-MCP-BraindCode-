---
name: clips-et-shorts
description: Utiliser quand l'utilisateur veut « transformer en short », « des clips depuis cette vidéo YouTube », « décliner en 9:16 », ou « restyler cette vidéo ». Trois chaînes de post-production Higgsfield — Personal Clipper (YouTube → clips sous-titrés), Shorts Studio (restyle → set de shorts), reframe/upscale à l'unité — avec rapatriement CMS et brouillons confirmés.
---

# Clips & shorts — post-production sans logiciel

Décliner et restyler des vidéos existantes. **Chiffré avant** (un short = ~90 cr, H0),
**jamais publié directement**.

## Étape 0 — Charger & router
- `${CLAUDE_PLUGIN_ROOT}/reference/routage-media.md` + `garde-fous-media.md`.
- `gouvernance-credits` : préflight (shorts coûteux ; `reframe` a un get_cost).

## Routage en tête
- **Si les rushes existent déjà** (couper/assembler/sous-titrer/reframe des médias
  réels) → **`rapido-video:montage-express` (0 crédit)**, pas Shorts Studio.
- **Shorts Studio** (ci-dessous) est réservé au **restyle génératif** (changer le
  look d'une vidéo via un preset IA) — payant.

## Trois chaînes
### (a) Personal Clipper — YouTube → clips
- `personal_clipper_create` : **URLs YouTube** → N clips sous-titrés. **Demander
  avant** : nombre de clips, `clip_aspect` (défaut 9:16), `subtitle_font`.
  **Long-running (30 min+)** → **prévenir** l'utilisateur, ne pas poller en boucle.

### (b) Shorts Studio — restyle → set de shorts
- Source : une **vidéo uploadée** ; style : `shorts_studio_list_presets` (ou en
  créer un depuis les références de la marque). Préflight coût
  (`shorts_studio_create` avec le paramètre get_cost + `duration_seconds`) → verdict
  `gouvernance-credits` (**BLOQUÉ = on ne lance pas**) → `shorts_studio_create`
  (poll `shorts_studio_status`).

### (c) À l'unité
- `reframe` (9:16 ↔ 16:9, get_cost dispo) ; `upscale_video` (netteté/résolution).

## Sortie (systématique)
- Rapatriement **CMS** (`upload_file_tool`) → **brouillons planifiés confirmés**
  (`rapidocms:pipeline-contenu-social`), **rattachés à une campagne**. Jamais de
  publication automatique.
- Boost éventuel : **seulement après** `analyse-video-virale` (gate).

## Routine récurrente (proposée, installée sur confirmation)
Déléguer à `rapido-n8n:usine-automatisations` : **lundi 9h** — top post vidéo de la
semaine (`rapidocms:analyse-performance-contenu`) → short → brouillon planifié.
(Table mémoire dédiée ; aucun envoi sans confirmation.)

## Garde-fous
Coût **préflighté** (BLOQUÉ = pas de génération) ; Personal Clipper **long → prévenu** ;
**aucune publication directe** (brouillons confirmés) ; boost **après gate viral** ;
rendus rapatriés et nommés côté CMS.
