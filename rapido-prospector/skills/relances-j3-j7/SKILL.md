---
name: relances-j3-j7
description: Utiliser quand l'utilisateur veut relancer ses prospects Prospector Hub — « qui dois-je relancer ? », « relances J+3 », « ce prospect n'a pas répondu depuis une semaine ». Chronologie croisée des quatre canaux, relances dues détectées, envoi sur accord seulement.
---

# Relances J+3 / J+7

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` ;
- `./rapido-kb/prospection.md` : liste d'opposition (un opposé ne se
  relance JAMAIS, sur aucun canal).

## Démarche
1. **Chronologie par prospect** : croiser `list_emails`, `list_sms`,
   `list_calls` (clientId / e-mail / téléphone) et
   `list_linkedin_message_history` (connectionId) — reconstituer qui a été
   touché, quand, par quel canal (widget chronologie-prospect sur
   demande).
2. **Relances dues** : dernier contact ≥ 3 jours ouvrés (1re relance) ou
   ≥ 7 jours (2e) SANS trace de réponse. Le serveur Prospect ne mesure pas
   les réponses : croiser avec le CRM si branché, sinon demander à
   l'humain qui a répondu — ne jamais le supposer.
3. **Rédiger** : relance courte qui fait référence au message précédent
   (jamais le même texte — l'historique fait foi). Modèles via le skill
   `modeles-de-messages`.
4. **Envoyer sur accord** : canal par canal, dans les quotas et la
   fenêtre, un prospect à la fois ou petit lot homogène — `send_email` /
   `send_sms` / `send_linkedin_message` (hooks : ask + conformité).
5. **Journal** : `add_log` (« relances », count) ; statut de la fiche mis
   à jour (`update_client`).

## Pièges
- Rien n'est envoyé à qui a demandé à ne plus être contacté : la liste
  d'opposition bloque l'envoi ENTIER (hook garde-conformite) — l'écarter
  AVANT de composer le lot.
- Après 2 relances sans réponse : statut « sans réponse » et on passe —
  la cadence outbound longue (J+14, rupture) se conçoit côté
  rapido-marketing (skill `machine-outbound`).

## Dégradation propre
Historique vide (base jamais contactée) : le dire, proposer
`campagne-email` plutôt que des « relances » qui n'en sont pas.
