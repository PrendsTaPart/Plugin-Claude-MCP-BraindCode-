---
name: autopilote
description: Utiliser quand l'utilisateur met la chaîne en pilotage automatique — « active l'autopilote », « mets la file en automatique », « pause l'autopilote pendant les vacances ». Réglages Europe/Paris, exclusions, espacement - sur accord, coût quota des envois rappelé.
---

# Autopilote

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/quota-et-credits.md` ;
  `./rapido-kb/youtube.md` (fenêtre de publication par défaut).

## Démarche
1. **Régler SUR ACCORD** : `yt_set_autopilot` — fuseau Europe/Paris,
   jours et heures EXCLUS (nuit, dimanche…), espacement minimal entre
   publications, horizon de planification, pause avec MOTIF explicite.
   Les créneaux choisis viennent de l'historique réel (loi n° 4).
2. **Alimenter la file** : `yt_queue_autopilot` — chaque vidéo mise en
   file coûtera UN ENVOI COMPLET au moment de partir : le rappeler et
   estimer (scripts/quota.py) AVANT l'accord.
3. **Surveiller** : la file se voit dans `yt_list_schedule` ; le
   tableau de bord signale ce que l'autopilote a avancé
   (published_early).

## Pièges
- L'autopilote n'est pas un oubli : le quota du jour reste la limite —
  une file trop pleine finira en will_fail.
- La pause se motive (yt_set_autopilot) : une pause sans motif rend la
  reprise illisible.

## Dégradation propre
Historique insuffisant pour l'espacement : réglage manuel proposé à
l'humain, pas d'autopilote « au hasard ».
