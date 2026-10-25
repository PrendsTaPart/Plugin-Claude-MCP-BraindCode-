---
name: journal-d-activite
description: Utiliser quand l'utilisateur veut tracer ou auditer l'activité Prospector Hub — « consigne cette campagne au journal », « qu'est-ce qui a été fait cette semaine ? », « audit des actions Prospect ». add_log après chaque série, list_logs pour l'audit.
---

# Journal d'activité

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Démarche
1. **Consigner** : `add_log` (action, message, count) après CHAQUE
   prospection, campagne ou série d'envois — l'action est un verbe court
   réutilisable (« prospection », « campagne-email », « relances »), le
   count est le volume réel.
2. **Auditer** : `list_logs` (action, search) — restituer la période
   demandée, grouper par action, totaux calculés et montrés.
3. **Croiser** : un journal qui ne colle pas aux historiques
   (`list_emails`, `list_sms`, `list_calls`) se signale tel quel — le
   journal dit ce qu'on a DÉCLARÉ, les historiques ce qui est PARTI.
4. **Local** : le hook journal-prospect tient en plus un journal technique
   masqué (.claude/logs/, e-mails et téléphones masqués) — il complète,
   il ne remplace pas `add_log`.

## Pièges
- Un journal sans count ne permet aucun suivi de quota a posteriori :
  toujours chiffrer.
- Ne JAMAIS consigner de données personnelles en clair dans le message du
  log (nom de zone et volumes suffisent).

## Dégradation propre
Rien à consigner : ne pas créer de log vide « pour faire propre ».
