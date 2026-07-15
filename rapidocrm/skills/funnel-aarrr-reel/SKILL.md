---
name: funnel-aarrr-reel
description: Utiliser quand l'utilisateur veut son funnel AARRR, ses métriques pirates, ou savoir où fuit son funnel. Calcule Acquisition/Activation/Rétention/Referral/Revenue sur les données MCP réelles (leads CRM, actions clés, clients actifs, parrainage/loyalty, factures) ; toutes les formules via catalogue-kpi ; sortie = funnel chiffré, étape la plus fuyante, 3 actions routées.
---

# Funnel AARRR réel — les métriques pirates sur données MCP

Le funnel pirate **chiffré sur le vrai business**, pas un exercice théorique.

## Étape 0 — Pont forge
- **Livrable `scale-funnel-aarrr`** (`./rapido-kb/startup/forge/`) comme **définition
  des étapes** (quelle « action clé » = activation par produit) ; absent → défauts en
  le disant. Voir `reference/pont-forge-operations.md`.

## Sense (données MCP réelles)
- **Acquisition** : leads CRM par canal (`get_stats_pipeline_global`, `list_campagnes`).
- **Activation** : première action clé par produit (définie par le livrable forge).
- **Rétention** : clients actifs mois M vs M-1.
- **Referral** : leads source parrainage + `get_loyalty_points`.
- **Revenue** : factures encaissées (`list_factures` statut payé).
Serveur absent = volet sauté en le disant.

## Plan (calculs via catalogue-kpi UNIQUEMENT)
- Chaque taux via `rapido-startup:catalogue-kpi` : `taux_activation`, `taux_retention`,
  `taux_referral` (ajoutés au catalogue), conversions d'étape, revenue. **Jamais de
  calcul local** — si un taux manque au catalogue, l'y **ajouter** (fait : AARRR).
- **Étape la plus fuyante** = le plus faible taux de passage (chiffre à l'appui).

## Report
- Le **funnel pirate chiffré** (A/A/R/R/R avec formules), **l'étape qui fuit**, et **3
  actions** routées vers les skills concernés (acquisition → `rapido-marketing` /
  `rapido-seo` ; activation → produit ; rétention → `rapido-relation-client:sante-client` ;
  referral → `programme-ambassadeurs`).

## Garde-fous
Formules **catalogue-kpi** (jamais de tête ni en local) ; définition d'étapes du
livrable forge ; données réelles ; étape fuyante **sourcée** ; serveur absent = dit.
