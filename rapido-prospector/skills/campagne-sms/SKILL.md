---
name: campagne-sms
description: Utiliser quand l'utilisateur veut une campagne SMS Prospector Hub — « SMS aux mobiles de la base », « envoie ce SMS aux boulangers de Lille ». mobileOnly, segments GSM-7 calculés, mention STOP, fenêtre horaire, accord explicite, puis statuts list_sms.
---

# Campagne SMS

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/conformite-prospection.md` ;
- `./rapido-kb/prospection.md` : mention STOP, quotas, fenêtre.

## Démarche
1. **Cibles** : `list_clients` avec `mobileOnly: true` (mobiles français
   seulement) + filtres de segment. Normaliser et vérifier :
   `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/normaliser_telephone.py --json
   tels.json` — un numéro invalide ne part jamais.
2. **Texte** : modèle `kind: sms` (`list_message_templates`) ou rédaction
   courte. Mention STOP OBLIGATOIRE dans le texte.
3. **Segments et coût relatif** :
   `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/segments_sms.py "texte"` —
   GSM-7 160 puis 153/segment, UCS-2 70 puis 67 ; un emoji fait tout
   basculer. Montrer segments × destinataires.
4. **Quota + fenêtre** : `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/quotas.py` ;
   plafonds serveur : 200 cibles, 1 600 caractères — ceux de la KB sont
   plus bas et priment.
5. **Accord explicite** sur la liste E.164 finale et le texte final
   (widget apercu-sms : texte, segments, STOP, nb destinataires).
6. **Envoyer** : `send_sms` (targets E.164, content — Twilio).
7. **Statuts** : `list_sms` (délivrés / échoués), puis `add_log`.

## Pièges
- `mobileOnly` est le SEUL filtre fiable pour les SMS : un fixe en E.164
  passe la forme mais ne reçoit rien — Twilio facture quand même.
- Réponse STOP reçue = liste d'opposition de la KB le jour même, tous
  canaux.

## Dégradation propre
Texte non conforme ou quota atteint : montrer le verdict du script et du
hook, proposer la correction ou le créneau suivant.
