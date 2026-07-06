---
name: tri-boite-mail
description: Utiliser quand l'utilisateur veut trier ses mails, viser l'inbox zero ou répondre à un mail. Classe la boîte du compte connecté par étiquettes, reconnaît les clients CRM et prépare des brouillons de réponse contextualisés — l'envoi reste humain.
---

# Tri de boîte mail

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/regles-direction.md`. Outils Gmail
absents → expliquer + renvoyer vers `README-installation.md`.

## Workflow

1. **Collecter** — `search_threads` (périmètre convenu : non lus, ou une
   requête ciblée type `from:… / is:important`) ; `get_thread` pour le
   contenu des fils à traiter.
2. **Classer chaque fil** — croiser avec le CRM (`search_entreprises` /
   `list_contacts` sur l'expéditeur) :
   - CLIENT reconnu (existe au CRM) ;
   - PROSPECT (inconnu mais métier — cf. `cibles-personas.md`) ;
   - ADMIN (factures, banque, administratif) ;
   - BRUIT (newsletters, spam mou).
3. **Étiqueter** — `list_labels` puis `create_label` si manquants :
   `Clients`, `Prospects`, `Factures`, `À-traiter` — appliquer via
   `label_thread`/`label_message`. Le BRUIT est étiqueté, jamais supprimé
   (règle : on classe, on ne supprime pas).
4. **Brouillons pour l'actionnable** — pour chaque fil qui attend une
   réponse : `create_draft` CONTEXTUALISÉ —
   - client/prospect CRM reconnu : historique (`get_historique_prospect`),
     devis en cours (`list_devis`) intégrés à la réponse ;
   - ton de `rapido-kb/ton-et-accroches.md` ;
   - un prospect entrant chaud → proposer d'enchaîner sur le skill
     `secretariat-commercial` (RDV).
5. **Récap** — `N fils classés (par étiquette), N brouillons prêts (liste
   destinataire + objet)` — RAPPELER que les brouillons attendent dans Gmail
   et que l'ENVOI appartient à l'utilisateur.

## Garde-fous

- JAMAIS d'envoi (l'outil ne le permet pas — ne pas le contourner par un
  autre canal) ; corbeille/spam = confirmation (hook).
- Un fil ambigu (litige, ton juridique, RH) = escalade : le signaler dans le
  récap SANS brouillon automatique (règle « sensible » de
  regles-direction.md).
- Ne pas étiqueter à tort un email personnel : en cas de doute, demander.
