---
name: analytics-et-rapports
description: Utiliser quand l'utilisateur mesure ses chaînes YouTube — « les stats de la chaîne », « compare ces deux vidéos », « le momentum des dernières 72 h », « génère le rapport du mois ». Lectures gratuites d'abord, refresh sur accord, rapport partageable sur accord.
---

# Analytics et rapports

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (loi n° 8).

## Démarche
1. **Mesurer** : `yt_get_channel_analytics`, `yt_get_video_analytics`,
   `yt_compare_videos`, `yt_get_slot_scores` — chiffres restitués tels
   quels, périodes dites.
2. **Momentum** : `yt_get_video_momentum` SANS refresh d'abord ; refresh
   (quota) sur accord — widget momentum : vues/heure face à la
   trajectoire habituelle de la chaîne.
3. **Analytics coupée** : `yt_compare_videos` et `yt_get_video_momentum`
   renvoient une erreur EXPLICITE si l'API est coupée — la réponse est
   « reconnecter la chaîne », transmise telle quelle.
4. **Rapport** : `yt_generate_report` SUR ACCORD (hook garde-public) —
   kit de marque de la chaîne appliqué, DURÉE DE VIE du lien de partage
   annoncée ; widget rapport-de-chaine pour la version locale.
5. **Santé** : `yt_get_channel_health_score` en synthèse.

## Pièges
- Un lien de rapport public expire : jamais collé dans un contenu
  durable sans date.
- Comparer deux vidéos d'âges très différents sans le dire fausse tout :
  afficher les fenêtres.

## Dégradation propre
Donnée absente : « — », jamais zéro ; API coupée : reconnexion demandée,
pas de boucle d'essais.
