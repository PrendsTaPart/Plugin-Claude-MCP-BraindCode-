#!/usr/bin/env bash
# Hook SessionStart — chaîne ciblée et quota : les deux réflexes YouTube.
set -u
cat <<'FIN'
[rapido-youtube] Les deux réflexes de chaque session :
1. LA CHAÎNE : yt_get_channel_status d'abord — sans channel_id, les envois
   partent vers la chaîne active (sinon la favorite). Règle du plugin :
   channel_id EXPLICITE et nom de la chaîne annoncé avant toute écriture.
   4 chaînes : FoodEatUp, RapidoCMS, RapidoCRM, Formation Braindcode
   (pas de chaîne RapidoRH) — reference/chaines.md.
2. LE QUOTA : yt_get_quota_status avant toute campagne — quota du jour,
   part réservée aux publications sous 24 h, DISPONIBLE RÉEL, risque
   (ok/tight/will_fail). Le hook garde-quota refuse tout envoi sans
   lecture < 30 min ou sur will_fail.
Rappels : noms d'outils en yt_ UNIQUEMENT (alias dépréciés refusés) ;
privacy private par défaut, public sur accord ; preview_only/dry_run avant
tout lot ; les champs confirm/dry_run posés par le modèle ne valent jamais
confirmation humaine. Référence : reference/directives-outils.md.
FIN
exit 0
