---
name: webinaire-du-mois
description: Utiliser quand le webinaire se prépare ou se suit, que l'utilisateur dit « monte le webinaire du mois », « où en sont les inscrits », « invite les prospects de la zone au webinaire », « transforme les présents en rendez-vous ». Crée la session, prépare les invitations sur modèle validé, suit les inscrits et pose les rendez-vous des présents.
---

# Webinaire du mois (créer, inviter, convertir)

Familles engagées : **configurer** (création de la session) +
**prospecter** (invitations, Aperçu) + **preparer** (rendez-vous).

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.
2. Prospector Hub requis pour ce volet : absent → skill sauté en le disant
   (le webinaire peut vivre hors outil, mais rien ne s'y automatise).

## Workflow

1. **`add_webinar`** — la session du mois : sujet (depuis les questions
   récurrentes des prospects), date dans les disponibilités déclarées,
   page d'inscription. Les rappels automatiques (SMS 1 h avant, appel 5 min
   avant) sont une mécanique du hub : les annoncer aux inscrits.
2. **Inviter** : `send_email` sur le MODÈLE VALIDÉ, liste issue du pipeline
   de la zone — famille prospecter : destinataires, objet et texte se
   montrent AVANT, l'accord déclenche. Quota `envoisJour` respecté (le
   garde-envois compte).
3. **Suivre** : `list_webinars` — inscrits, présence ; restituer sans
   embellir.
4. **Convertir** : pour chaque PRÉSENT intéressé, `create_rdv` (RapidoCRM)
   et `deplacer_prospect_etape` — le webinaire n'a servi que s'il produit
   des rendez-vous tenus.
5. **Mesurer au vendredi** : inscrits → présents → rendez-vous → signatures,
   dans la boucle (skill `boucle-du-vendredi`).

KPI : `webinaire-inscrits`, `webinaire-presence`, `webinaire-rdv`.
Formations : `webinaire`, `communication-claude`.

## Garde-fous

- Invitations UNIQUEMENT sur modèle validé, avec expéditeur et moyen de
  refuser ; un « non » arrête les invitations pour ce contact.
- Pas de sur-promesse dans le sujet du webinaire (anti-donnee-inventee en
  filet sur les promesses chiffrées).
