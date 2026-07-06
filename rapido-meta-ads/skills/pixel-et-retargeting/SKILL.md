---
name: pixel-et-retargeting
description: Utiliser quand l'utilisateur veut poser le pixel, tracker les conversions ou faire du retargeting. Installe et active les événements pixel sur les landings Lovable, vérifie en Test Events, construit l'audience WEBSITE et propose la campagne de retargeting.
---

# Pixel et retargeting (Lovable × Meta)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`,
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-meta-ads.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/CONFORMITE.md`.

## Workflow

1. **Identifier la landing** — `list_projects` (Lovable, `publish_status:
   "published"`) : le projet et son URL déployée.
2. **Pixel du compte** — `ads_get_datasets` : le pixel (dataset) existant du
   compte ; `ads_get_dataset_details` si besoin. Pas de pixel = le signaler
   (création côté Business Manager).
3. **Injecter le snippet si absent** — demander à Lovable d'ajouter le pixel
   dans la page : `send_message` (projet concerné) avec l'ID du pixel — base
   code dans le head + événement standard sur l'action clé (soumission du
   formulaire → Lead). Consentement cookies : bannière si pas déjà en place.
4. **Créer les événements** — `ads_pixel_event_create` selon la page :
   `Lead` (capture de formulaire) ou `Purchase` (vente — paramètres `value` +
   `currency` OBLIGATOIRES). Les événements naissent INACTIVE.
5. **Activer et VÉRIFIER** — `ads_pixel_event_update` (activation) puis
   vérification GUIDÉE avec l'utilisateur dans Test Events (Events Manager) :
   visiter la page, déclencher l'action, confirmer la réception. Pas de
   campagne de conversion sur un événement non vérifié.
6. **Audience WEBSITE** — `ads_create_custom_audience` type WEBSITE
   (VISITORS_BY_URL sur l'URL de la landing, fenêtre 30 jours par défaut) :
   retargeting sans PII.
7. **Proposer la campagne de retargeting** — skill `lancement-campagne-meta`
   avec l'audience WEBSITE (objectif OUTCOME_SALES ou OUTCOME_LEADS selon la
   page) — création PAUSED, activation confirmée comme toujours.

## Garde-fous

- `Purchase` sans `value`/`currency` = données de conversion inutilisables :
  refuser de créer l'événement incomplet.
- Vérification Test Events AVANT toute campagne d'optimisation sur
  l'événement.
- Le pixel collecte des données de navigation : bannière de consentement sur
  la landing (RGPD) — le vérifier avec Lovable, pas d'exception.
