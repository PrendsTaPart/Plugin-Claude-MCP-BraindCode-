---
name: agenda-rdv
description: Utiliser quand l'utilisateur veut prendre un rendez-vous client, voir son agenda du jour ou de la semaine, ou créer un événement commercial. Gère les RDV (visio, téléphone, présentiel), l'agenda et les événements.
---

# Agenda et rendez-vous

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).

## Workflow

1. **Consulter l'agenda d'abord** — `get_today_schedule` (`periode` ∈ today |
   tomorrow | week) : rendez-vous et événements existants. TOUJOURS vérifier
   les conflits de créneau avant de créer un RDV.
2. **Prendre un RDV** — `create_rdv` (`entreprise_id`, `titre`,
   `date_debut`/`date_fin` au format `YYYY-MM-DD HH:MM:SS`, `type` ∈
   Visioconférence | Téléphonique | Présentiel) :
   - champs conditionnels selon le type : `adresse` OBLIGATOIRE si
     Présentiel ; `telephone` si Téléphonique ;
   - participants : `emails` (contacts externes) et/ou `user_ids` (internes,
     via `list_users`) ;
   - `mode_envoi` ∈ SMS | Email | SMS et Email : c'est la convocation
     envoyée au client — confirmer le mode et le destinataire avant l'appel ;
   - `commentaire` pour le contexte (objectif du RDV, deal lié).
3. **Créer un événement** (salon, porte ouverte, webinaire) —
   `create_evenement` (`payload` avec les données de l'événement). Retrouver
   les événements via `list_evenements`.
4. **Boucler avec le commercial** — tracer la prise de RDV sur le deal
   (`log_activity`), et rappeler le RDV dans la revue de pipeline
   (`coaching-pipeline` : un deal avec RDV posé a une « prochaine action »).

## Garde-fous

- Pas de RDV sans vérification de conflit (`get_today_schedule` sur la
  période) ni sans les champs du type (adresse pour le présentiel, téléphone
  pour l'appel).
- `mode_envoi` déclenche une notification au client : récapituler
  (destinataire + date/heure + type) et confirmer avant `create_rdv`.
- Fuseau : confirmer l'heure locale avec l'utilisateur ; format strict
  `YYYY-MM-DD HH:MM:SS`.
- Un RDV annulé/déplacé : prévenir le client (send_email/send_sms avec
  confirmation) — jamais de suppression silencieuse.
