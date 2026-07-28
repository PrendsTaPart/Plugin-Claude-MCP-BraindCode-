---
name: campagnes-restaurant
description: Utiliser quand l'utilisateur veut créer, lancer ou suivre une campagne marketing FoodEatUp ou un template WhatsApp pour son restaurant — « envoie une offre à mes clients fidèles », « lance la campagne de la Saint-Valentin », « crée un template WhatsApp », « comment a marché ma dernière campagne ». Exécution de bout en bout côté restaurant, pas les campagnes B2B du CRM.
---

# Campagnes restaurant (FoodEatUp) & templates WhatsApp

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et l'appliquer.
2. S'assurer d'avoir l'`establishment_id` (le demander si absent).
3. Charger les seuils marketing maison de `./rapido-kb/` s'ils existent (ils priment).

## 1. Qualifier la cible AVANT de proposer (lecture)

- `list_rfm_segments` : segments disponibles et leur taille ; `list_clients`
  pour la volumétrie totale.
- **Règle des 10 contacts** : un segment de moins de 10 contacts → REFUSER la
  campagne segmentée, expliquer pourquoi (aucun signal exploitable) et renvoyer
  vers la capture (leads du site, fidélité, collecte en salle).
- `list_campaigns` : ne pas doubler une campagne active sur la même cible.
- `propose_campaigns` : suggestions du serveur, à filtrer par la règle ci-dessus.

## 2. Construire (écriture libre : un brouillon n'envoie rien)

- `create_campaign` : nom, segment cible (avec sa taille réelle citée), message,
  offre, période. Si la campagne met un plat en avant : vérifier le stock de son
  ingrédient principal (`list_low_stocks`) et sa marge (`get_recipe`) — un plat
  épuisé ou à marge négative ne se met pas en avant.
- WhatsApp : `create_whatsapp_template` (brouillon), `list_whatsapp_templates`
  pour l'existant et les statuts de validation Meta.

## 3. Lancer (acte humain, jamais automatique)

- **`launch_campaign` = envoi réel aux destinataires** → garde-fou du plugin :
  confirmation utilisateur obligatoire, avec récapitulatif « segment X,
  N destinataires, message, offre ». Ne jamais présenter le lancement comme
  réversible.
- **`submit_whatsapp_template`** soumet le template à la validation Meta →
  même garde-fou (acte externe, file d'attente Meta).

## 4. Mesurer (lecture, chiffres réels)

- `get_campaign_stats` après envoi : ouvertures/usages réels, jamais estimés.
  Une campagne de moins de 7 jours d'activité se lit, ne se juge pas.

## Ce que ce skill NE fait PAS

- Le diagnostic d'ensemble de la communication → skill `boucle-6-communication`
  (plugin foodeatup-boucles).
- Les campagnes emailing/SMS B2B du CRM → plugin rapidocrm (outils CRM
  volontairement non connectés à ce plugin).
- Les visuels et posts sociaux → plugin rapidocms.
