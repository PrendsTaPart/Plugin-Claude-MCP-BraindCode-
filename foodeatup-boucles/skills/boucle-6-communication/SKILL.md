---
name: boucle-6-communication
description: Utiliser quand l'utilisateur veut l'état de la boucle ⑥ Communication — « où en est ma boucle communication », « bilan campagnes et avis », « ma base clients est-elle exploitable pour une campagne », « état de mon e-réputation ». Diagnostic campagnes/segments/avis avec seuil de taille de segment, pas la rédaction de contenu.
---

# Boucle ⑥ — Communication (campagnes, segments, e-réputation)

## Quand l'utiliser

Pour l'**état du système de communication** : campagnes en cours et passées,
base de contacts, segments exploitables, avis clients à traiter. La question de
la boucle : « ai-je de quoi parler, et à qui ? »

## Enchaînement d'outils MCP (l'ordre compte)

1. **Toujours commencer par la volumétrie** : `list_clients` (taille de la base),
   `list_rfm_segments` (taille de chaque segment). C'est le prérequis de toute
   proposition.
2. `list_campaigns` + `get_campaign_stats` : campagnes actives, performances
   réelles (jamais estimées).
3. `propose_campaigns` pour les suggestions serveur, à filtrer par la règle des
   10 contacts ci-dessous.
4. E-réputation : `list_reviews` — avis sans réponse, avis négatifs récents.
   Réponse via `reply_review` (publique → confirmation).
5. Templates : `list_whatsapp_templates`, `create_whatsapp_template` (brouillon).
6. Capture : `list_site_leads` (leads du site non convertis en clients →
   proposer `create_client` un par un).

## Règles métier

- **Règle des 10 contacts** : si le segment cible compte moins de 10 contacts,
  REFUSER de proposer une campagne segmentée. Dire pourquoi (base trop petite
  pour un signal exploitable) et renvoyer vers la capture de leads :
  `list_site_leads`, jeux et roue cadeaux (boucle ⑦), collecte en salle.
- Une campagne mettant en avant un plat exige la vérification du stock de son
  ingrédient principal (boucle ③) et de sa marge (skill `recette-cout-marge`) —
  détections portées par le skill `croisement-service`.
- Les statistiques d'une campagne encore active se lisent, ne se projettent pas.

## Garde-fous (opérations exigeant confirmation)

Interceptés par le hook du plugin (confirmation humaine obligatoire) :
- `launch_campaign` — envoi réel aux destinataires ;
- `submit_whatsapp_template` — soumission Meta ;
- `reply_review`, `moderate_review` — actes publics ;
- côté CRM : `send_email`, `send_sms`, `send_newsletter`, `lancer_campagne`.
Créer une campagne (`create_campaign`) est libre : c'est un brouillon.
La lancer ne l'est jamais.

## Sortie attendue

Un tableau `[sujet | volumétrie | état | action proposée]` pour : base clients,
segments, campagnes actives, avis, leads. Chaque proposition de campagne indique
la taille réelle du segment visé.

## Ce que ce skill NE fait PAS

- Rédiger les contenus et visuels → plugins rapidocms / rapido-copywriter.
- Le marketing multi-canal complet → plugin rapido-marketing.
- Piloter la fidélité qui alimente les segments → skill `boucle-7-fidelite`.
