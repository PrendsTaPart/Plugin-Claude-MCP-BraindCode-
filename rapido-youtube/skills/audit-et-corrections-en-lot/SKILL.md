---
name: audit-et-corrections-en-lot
description: Utiliser quand l'utilisateur corrige son catalogue YouTube en masse — « audite la chaîne », « corrige les descriptions des 200 vidéos », « remplace l'ancien lien partout ». Audit, puis aperçu obligatoire, puis le vrai job sur accord, suivi jusqu'au bout.
---

# Audit et corrections en lot

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (loi n° 9).

## Démarche
1. **Auditer** : `yt_audit_channel` — ce qui cloche, par familles
   (titres, descriptions, miniatures, métadonnées).
2. **Aperçu OBLIGATOIRE** : `yt_create_bulk_job` avec preview_only à
   true (jusqu'à 500 vidéos) — l'aperçu est MONTRÉ à l'humain. Le hook
   garde-lot refuse tout job réel sans aperçu identique dans la session.
3. **Lancer SUR ACCORD** : le même job en réel, puis
   `yt_get_bulk_job_status` jusqu'au terme, `yt_retry_failed_items` pour
   les éléments en échec, `yt_cancel_bulk_job` si ça tourne mal.
4. **Chercher-remplacer** : `yt_find_replace_descriptions` TOUJOURS en
   dry_run d'abord (résultats montrés), puis en réel sur accord — même
   recherche exactement (le hook compare).
5. **Journal** : ce qui a été modifié en masse se consigne (nombre,
   type, date) dans la restitution.

## Pièges
- Un lot sur 500 vidéos consomme du quota : l'estimer AVANT
  (scripts/quota.py) et vérifier le risque.
- Un chercher-remplacer trop large casse des descriptions valides : le
  dry_run se LIT, pas seulement se lance.

## Dégradation propre
Job bloqué : yt_cancel_bulk_job sur accord et constat honnête de ce qui
est passé / resté — jamais de relance aveugle.
