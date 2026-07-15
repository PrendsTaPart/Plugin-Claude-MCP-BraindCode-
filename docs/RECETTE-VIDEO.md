# Recette rapido-video — preuves & écarts

> Clôture V5. **Environnement de test : conteneur Linux** (proxy bloquant github) —
> chronos étiquetés **« conteneur Linux (mesuré) »** ; les mesures Windows sont
> **« à mesurer en session locale (~5 min) »** (jamais transposées). Licence
> Remotine : **[B] différée → mode aperçu** (gabarits Remotion exclus du livrable
> publié ; habillage via `montage-express`).

## (d) DELTA V5 — clean-install VIERGE → montage sans action manuelle : **RÉUSSI**
Environnement vierge → `scripts/bootstrap_video.py --install ffmpeg --yes` (annonce +
confirmation) → `ffmpeg-static` (npm) **bloqué github-403** → **repli `imageio-ffmpeg`
(PyPI) OK** → chemins écrits dans `rapido-kb/outils-locaux.md` → `montage-express`
enchaîne le montage. **Zéro installation utilisateur, zéro action manuelle.**

## (a) PronoClip — épisode 9:16 monté : **chaîne PROUVÉE** (sur médias synthétiques)
Chaîne réelle exécutée (conteneur Linux, mesuré) : carton titre (`title-card`, libass)
→ `normalize`+`concat` (titre + 3 clips) → `overlay-logo` (coin, zone protégée) →
`burn-srt` (sous-titres FR) → `preset tiktok` (9:16). Sortie 1080×1920, 8,6 s.
**Montage total ≈ 10,7 s (conteneur Linux, mesuré) · 0 crédit.**
- **Écart** : les **3 clips Kling réels n'existent pas encore** (leur génération =
  crédits, hors périmètre « 0 crédit ») → test fait sur clips synthétiques.
- **Écart** : **gate viral H6** (`analyse-video-virale`) et **brouillon campagne #20**
  non exécutés ici (nécessitent le MCP Higgsfield + la vidéo réelle) — à faire en
  session avec les vrais clips.

## (b) FoodEatUp — sous-titres FR + doublage EN : **partiellement prouvé**
- **Sous-titres FR (Whisper local)** : chaîne validée (faster-whisper `transcribe`
  → SRT → `burn`). **0 crédit.** Écart : l'**extrait V1 réel** doit être fourni
  (source CMS/foodeatup) — non présent dans ce conteneur.
- **Doublage EN** : **Higgsfield `dubbing`** = **payant (crédits)** → non exécuté sans
  ta confirmation. À lancer en session avec l'extrait réel + accord budget.

## (c) Recap 60 s depuis un transcript Fireflies réel : **écart**
Nécessite un **transcript Fireflies réel** (MCP Fireflies, connecteur optionnel) →
script → montage. Non exécuté ici (pas de réunion réelle rattachée). Procédure prête
(`fireflies_get_summary` → script → `montage-express`).

## Bilan
| Étape | Statut | Coût | Chrono |
|---|---|---|---|
| (d) clean-install → montage | ✅ **RÉUSSI** | 0 | conteneur Linux (mesuré) ; Windows à mesurer (~5 min) |
| (a) chaîne épisode 9:16 | ✅ **PROUVÉE** (synthétique) | 0 | ≈ 10,7 s (Linux, mesuré) |
| (a) clips Kling réels + gate viral + #20 | ⛔ **écart** | crédits (clips) | session locale |
| (b) sous-titres FR | ✅ chaîne OK | 0 | Linux (mesuré) |
| (b) doublage EN | ⛔ **écart** | crédits | session locale + accord |
| (c) recap Fireflies | ⛔ **écart** | 0 (Fireflies requis) | session locale |

**Le socle (zéro-install + chaîne de montage) est prouvé.** Les recettes de contenu
réel (a/b/c) attendent leurs **sources réelles** (et crédits pour le doublage) — à
exécuter en session locale ; aucune donnée fabriquée ici.
