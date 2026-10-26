---
name: planifier-et-grille
description: Utiliser quand l'utilisateur planifie ses publications YouTube — « planifie la vidéo mardi 18 h », « propose mes créneaux », « refais la grille de la chaîne ». Créneaux depuis l'historique réel, grille lue avant d'être remplacée, lots de 10 maximum.
---

# Planifier et tenir la grille

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (lois n° 3 et 4).

## Démarche
1. **Les créneaux** : `yt_suggest_publishing_slots`, `yt_get_slot_scores`
   (recompute = quota, sur accord), `yt_get_publishing_slots`,
   `yt_suggest_slots` — tout vient de l'HISTORIQUE réel : sans
   historique, l'outil le dit et on ne brode pas.
2. **La grille** : `yt_list_schedule_slots` D'ABORD, puis
   `yt_set_schedule_slots` en montrant la NOUVELLE grille complète — il
   REMPLACE tout, et une liste vide EFFACE (hook garde-grille) ;
   chevauchements entre chaînes vérifiés par
   `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/grille.py grilles.json`.
3. **Planifier** : `yt_schedule_video` en mode upload_now_publish_at (le
   plus fiable), client_request_id posé ; en lot : `yt_bulk_schedule`,
   10 vidéos AU PLUS par appel — quota estimé AVANT (scripts/quota.py).
4. **Suivre et ajuster** : `yt_list_schedule` (published_early inclus),
   `yt_reschedule_video`, `yt_cancel_scheduled_video` (sur confirmation).

## Pièges
- Les publications planifiées sous 24 h RÉSERVENT du quota : les voir
  dans yt_get_quota_status avant d'en ajouter — au relevé du 2026-10-25,
  cette réserve dépassait le plafond (will_fail).
- Deux chaînes de la maison sur le même créneau se cannibalisent :
  scripts/grille.py le détecte.

## Dégradation propre
Pas d'historique pour suggérer : grille proposée par l'HUMAIN, scores
absents affichés « — ».
