---
name: linkedin-du-jour
description: Utiliser quand l'utilisateur traite sa file LinkedIn quotidienne — « fais le LinkedIn du matin », « qu'est-ce qui part aujourd'hui sur LinkedIn ? », « envoie les messages du jour ». File du jour, anti-répétition par l'historique, envois un par un sur accord, dans le quota.
---

# LinkedIn du jour (rituel du matin)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` ;
- `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/quotas.py` — invitations et
  messages restants aujourd'hui.

## Démarche
1. **La file** : `list_linkedin_scheduled_day` (date du jour, heure de
   Paris) — destinataires, textes, modèles prévus.
2. **Anti-répétition** : pour CHAQUE destinataire,
   `list_linkedin_message_history` (connectionId) — jamais deux fois le
   même message à la même personne ; un doublon se reformule ou s'annule
   (`update_linkedin_scheduled_message`, statut).
3. **Prérequis** : connexion enrichie (provider_id) et `account_id` réel
   (`list_linkedin_accounts`) — sinon passer par le skill
   `reseau-linkedin` d'abord.
4. **Envoyer UN PAR UN, sur accord** : `send_linkedin_invite` (invitation,
   message court) ou `send_linkedin_message` (message ou templateId) —
   chaque envoi montré, confirmé, compté dans le quota du jour (hook).
5. **Clore** : marquer les messages traités
   (`update_linkedin_scheduled_message`), `add_log` du rituel.

## Origine (routines Academy, en renvoi)
Ce rituel exécute les routines « Liste LinkedIn du matin » et « Du
LinkedIn au CRM » du registre reference/registre-routines.md — la
déclinaison CRM (créer l'entreprise, l'étape de pipeline) passe par le
skill `synchroniser-vers-rapidocrm`.

## Pièges
- Le calendrier n'envoie RIEN tout seul : ignorer la file du jour, c'est
  ne rien envoyer du tout.
- Quota atteint en cours de file : s'arrêter, dire ce qui reste, reporter
  au lendemain (`update_linkedin_scheduled_message`).

## Dégradation propre
File vide : le dire et proposer le skill `sequences-linkedin` pour
alimenter les jours suivants.
