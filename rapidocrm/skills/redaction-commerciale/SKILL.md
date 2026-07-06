---
name: redaction-commerciale
description: Utiliser quand l'utilisateur veut écrire un email de prospection, un message de relance ou une proposition commerciale. Frameworks AIDA/PAS, règles d'objet et de CTA, personnalisation obligatoire, ton selon l'étape du funnel.
---

# Rédaction commerciale

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (règles communes)
et `${CLAUDE_PLUGIN_ROOT}/reference/charte-graphique.md` — le ton de marque et
les do/don't s'appliquent à TOUT message produit.

## Règles non négociables (tout message)

- **Objet < 50 caractères**, sans majuscules criardes ni mots à spam.
- **UN seul CTA** par message (une question, un créneau, un lien — pas trois).
- **Personnalisation obligatoire** : nom du destinataire, secteur/activité, et
  un déclencheur concret (actualité, création récente, problème typique du
  secteur). Les données viennent de `get_entreprise` / `get_contact` /
  `get_historique_prospect` — jamais de personnalisation inventée. Sans ces
  éléments : demander ou aller les chercher, pas de message générique.
- **Arguments et objections depuis la KB** (`./rapido-kb/`, si elle existe) :
  les ARGUMENTS (promesse, différenciateurs, preuves, garanties) viennent de
  `propositions-valeur.md` ; les réponses aux OBJECTIONS et l'anti-concurrence
  de `concurrents.md` (nos parades) ; le ton et le vocabulaire maison de
  `ton-et-accroches.md` — citer la source utilisée. Sans KB : argumenter sur
  les données CRM réelles uniquement, et signaler que le message serait plus
  percutant après l'onboarding.
- Court : 80-120 mots pour un email de prospection, moins pour une relance.

## Frameworks — choisir selon le contexte

- **AIDA** (Attention → Intérêt → Désir → Action) : premier contact, annonce
  d'offre. Accroche personnalisée, bénéfice concret, preuve (cas client,
  chiffre), CTA unique.
- **PAS** (Problème → Agitation → Solution) : prospect avec un problème
  identifié. Nommer le problème précis du secteur, montrer ce qu'il coûte,
  proposer la solution + CTA.

## Ton selon l'étape du funnel

- **Froid (premier contact)** : sobre, service avant tout, zéro pression —
  l'objectif est la RÉPONSE, pas la vente.
- **Relance** (J+3 / J+7 / J+15) : chaque relance apporte un ANGLE NOUVEAU
  (valeur, cas client, question ouverte) — jamais « je me permets de revenir
  vers vous » seul. La dernière est une clôture franche (« je ferme le
  dossier ? »).
- **Closing (devis envoyé, négociation)** : précis, chiffré, échéance claire,
  lever la dernière objection, proposer un créneau ferme.

## Livraison

Produire le message PRÊT À ENVOYER (objet + corps), puis proposer le canal :
- envoi immédiat : `send_email` (`entreprise_id`, `sujet`, `contenu` ou
  `template_id`) — après validation explicite ;
- planification : `schedule_email` (`date_envoi` YYYY-MM-DD HH:MM:SS) ;
- réutilisable : `create_template_email` (ou `create_template_sms` pour un SMS)
  pour capitaliser sur les messages qui performent.

## Garde-fous

- Jamais d'envoi sans validation du texte ET du destinataire par l'utilisateur.
- Pas de promesse chiffrée invérifiable ni de fausse urgence ; respecter les
  don't de la charte.
- Consigner l'envoi via `log_activity` (traçabilité du deal).
