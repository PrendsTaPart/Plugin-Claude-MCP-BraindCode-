---
name: webinaires
description: Utiliser quand l'utilisateur organise un webinaire Prospector Hub — « crée le webinaire du mois prochain », « combien d'inscrits ? », « active la page du webinaire ». Création inactive d'abord, activation sur accord, suivi des inscrits, suppression avec cascade annoncée.
---

# Webinaires

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
  `${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md` (lien visible des
  seuls inscrits).

## Démarche
1. **Créer INACTIF** : `add_webinar` avec `is_active: false` — titre,
   sujet, description, script, image, lien de session, places, date,
   heures, durée, document support.
2. **Aperçu** : restituer la fiche complète (ce que verra la page
   publique) AVANT toute activation.
3. **Activer sur accord** : `update_webinar` avec `is_active: true` — le
   hook garde-publication demande (page publique). La promotion du
   webinaire renvoie vers la page d'INSCRIPTION, jamais vers le lien de
   connexion (visible des seuls inscrits).
4. **Suivre** : `list_webinars` (inscrits inclus) — restituer les chiffres
   tels quels, sans embellir.
5. **Supprimer** : `delete_webinar` sur confirmation, en annonçant la
   CASCADE (inscriptions + rappels effacés) — préférer `is_active: false`
   pour dépublier sans perdre les inscrits.

## Pièges
- Modifier la date d'un webinaire actif : prévenir que les inscrits
  existants ont peut-être déjà reçu l'ancienne — proposer une
  communication de report (campagne-email sur les inscrits si la liste
  est accessible, sinon le dire).
- Le suivi post-webinaire (conversion des présents) passe par le skill
  `synchroniser-vers-rapidocrm` et le CRM.

## Dégradation propre
Les inscriptions vivent côté serveur : si la liste nominative n'est pas
servie par un outil, dire qu'on n'a que le COMPTE d'inscrits.
