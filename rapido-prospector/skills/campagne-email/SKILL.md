---
name: campagne-email
description: Utiliser quand l'utilisateur veut envoyer une campagne e-mail Prospector Hub — « envoie la campagne de démo aux pizzerias de Lyon », « campagne e-mail sur le segment X ». Segment → modèle → aperçu → conformité → quota → accord explicite → send_email → journal.
---

# Campagne e-mail

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
  `${CLAUDE_PLUGIN_ROOT}/reference/conformite-prospection.md` ;
- `./rapido-kb/prospection.md` : quotas, fenêtre, identité, désinscription.

## Démarche
1. **Segment** : `list_clients` (city, speciality, search, statut) —
   montrer le volume et un échantillon. Écarter les fiches sans e-mail et
   celles de la liste d'opposition.
2. **Modèle** : `list_email_templates`, ou rédaction via le plugin
   rapido-copywriter s'il est installé, puis skill `modeles-de-messages`
   pour l'enregistrer. Variables remplies avec les champs RÉELS des fiches.
3. **Aperçu** : widget apercu-email (`${CLAUDE_PLUGIN_ROOT}/scripts/render_widget.py`)
   — objet, expéditeur, corps rendu, mention de désinscription visible.
4. **Conformité + quota** :
   `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/conformite.py --canal email …`
   puis `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/quotas.py` — le lot se
   découpe sous le plafond, le reste attend demain (jamais de
   fractionnement pour contourner un quota).
5. **Accord explicite sur CET envoi** : liste finale des destinataires +
   contenu final montrés. Le hook garde-envois-prospect demandera de toute
   façon ; un champ posé par le modèle ne vaut pas confirmation.
6. **Envoyer** : `send_email` (recipients, subject, content — webhook n8n).
7. **Vérifier et journaliser** : `list_emails` (les envois y apparaissent),
   puis `add_log` (campagne, volume).

## Pièges
- La séquence froide multi-étapes (J0/J3/J7) se CONÇOIT avec le plugin
  rapido-marketing (skill `machine-outbound`) ; ce skill-ci EXÉCUTE un
  envoi Prospect.
- La délivrabilité se dégrade avec les gros lots : petits volumes réguliers
  (voir `delivrabilite-email` côté rapido-marketing).

## Dégradation propre
Hook en deny (quota, fenêtre, conformité) : expliquer la raison exacte,
proposer le créneau ou la correction — jamais de contournement.
