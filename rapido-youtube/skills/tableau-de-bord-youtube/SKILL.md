---
name: tableau-de-bord-youtube
description: Utiliser quand l'utilisateur demande « où en sont mes chaînes YouTube ? », « fais le point YouTube », « quota et planning du jour ». Un écran - chaîne ciblée, quota et risque, crédits, planning 7 jours, échecs, santé, momentum, commentaires sans réponse - et trois priorités.
---

# Tableau de bord YouTube

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (les lois du
  serveur) et `${CLAUDE_PLUGIN_ROOT}/reference/chaines.md`.

## Démarche (lectures seules, gratuites sauf mention)
1. **La cible** : `yt_get_channel_status` (active vs favorite, divergence
   signalée) + `yt_list_channels`.
2. **Les moyens** : `yt_get_quota_status` (quota du jour, réservations
   sous 24 h, DISPONIBLE RÉEL, risque) + `yt_get_credit_balance`.
3. **Le planning** : `yt_list_schedule` sur 7 jours, avec
   published_early — ce qui est parti en avance se voit.
4. **Ce qui coince** : `yt_list_videos` filtré erreurs / en attente.
5. **La santé** : `yt_get_channel_health_score`, `yt_get_video_momentum`
   SANS refresh (le refresh coûte du quota et se fait sur accord).
6. **Le public** : `yt_list_comments` filtré sans réponse, SANS sync.
7. **La distribution** : `yt_list_connected_accounts` (au relevé du
   2026-10-25 : aucun compte connecté — le dire tel quel).
8. **Restitution en UN écran** (widget tableau-de-bord-chaine sur
   demande) + TROIS priorités argumentées, proposées, jamais exécutées
   d'office. Si le risque est will_fail : la priorité n° 1 est TOUJOURS
   la revue du planning sous 24 h.

## Pièges
- Le disponible réel peut être à zéro avec un quota brut non nul (part
  réservée aux publications planifiées) : afficher les trois nombres.
- Momentum : une erreur « Analytics coupée » = reconnecter la chaîne,
  pas réessayer.

## Dégradation propre
Serveur non connecté (OAuth au premier appel) : le dire, ne rien estimer.
