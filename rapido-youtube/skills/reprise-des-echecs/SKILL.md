---
name: reprise-des-echecs
description: Utiliser quand des envois YouTube ont échoué — « pourquoi cette vidéo est en erreur ? », « relance les envois échoués », « c'est quoi uploadLimitExceeded ? ». Chaque erreur expliquée, reprise dans le quota, heure de réarmement respectée.
---

# Reprise des échecs

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (loi n° 10).

## Démarche
1. **Lister** : `yt_list_videos` filtré sur les erreurs — chaque erreur
   est EXPLIQUÉE en clair (quota, fichier, droits, limite d'upload)
   avant toute action.
2. **Reprendre** : `yt_retry_video` (une), `yt_retry_videos` (plusieurs,
   avec délai entre reprises) — chaque reprise coûte UN ENVOI COMPLET :
   quota lu avant (hook garde-quota), estimation scripts/quota.py.
3. **uploadLimitExceeded** : le serveur REFUSE une reprise à moins de
   24 h du blocage et donne l'HEURE DE RÉARMEMENT — on la respecte, on
   la transmet, on planifie la reprise après.
4. **Côté jobs** : les éléments en échec d'un lot passent par
   `yt_retry_failed_items` (skill `audit-et-corrections-en-lot`).

## Pièges
- Relancer en boucle une erreur non comprise gaspille le quota : une
  explication d'abord, une reprise ensuite.
- Après la reprise : `yt_get_video_status` pour CONSTATER, pas supposer.

## Dégradation propre
Erreur inconnue du serveur : restituer le message brut et proposer le
support de l'application — pas de diagnostic inventé.
