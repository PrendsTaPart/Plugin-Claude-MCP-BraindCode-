---
name: tunnel-de-vente-360
description: Utiliser quand l'utilisateur veut construire son tunnel de vente, un funnel complet pour un produit, un tunnel parfait pour [produit], ou aller de la pub au client. Conçoit ET construit le tunnel Rapido-first en 5 actes avec validation entre chaque acte, en déléguant chaque brique et en confirmant tout envoi ou dépense.
---

# Tunnel de vente 360° — concevoir ET construire (5 actes)

Skill **orchestrateur flagship** : il conçoit puis construit un tunnel complet
pour un produit donné, **Rapido-first**, en **5 actes avec validation
OBLIGATOIRE entre chaque acte** (pattern du skill `lancement-projet-360`). Il ne
réexécute rien — il enchaîne les skills et pose garde-fous, KPI et IDs.

## Étape 0 — Charger (obligatoire)
- `${CLAUDE_PLUGIN_ROOT}/reference/priorite-mcp.md` et `garde-fous-marketing.md`.
- `./rapido-kb/marketing/` (`icp.md`, `tunnels.md`, et **`apprentissages.md` +
  `benchmarks.md` à lire AVANT de proposer le schéma** — les leçons priment sur
  les défauts). Fichiers absents → créés depuis
  `${CLAUDE_PLUGIN_ROOT}/reference/kb-templates/` (voir `reference/memoire.md`).
- **Transversal** : créer le **projet Kanban RapidoRH** dès l'Acte 1 (le tunnel
  EST un projet) → skills `setup-projet` puis `flux-kanban` ; **chaque acte = une
  colonne**. Récap des IDs à chaque fin d'acte (hook Stop).

## ACTE 1 — Stratégie
- **Offre & value ladder** → skills méthodo (`lead-magnet-machine`,
  `core-four-strategie`) + skill `hundred-million-offers`.
- **ICP** → skill `icp-generator` (si `icp.md` absent).
- **Messages par étape TOFU/MOFU/BOFU** → skills `funnel-tofu-mofu-bofu` +
  `storybrand-messaging`.
- **Livrable** : schéma du tunnel (étapes, messages, **KPI cibles**) écrit dans
  `./rapido-kb/marketing/tunnels.md` (via `mise-a-jour-kb`).
- ⏸️ **VALIDATION** avant l'Acte 2.

## ACTE 2 — Construction des pages
- **Landing(s)** : **voie 1** `create_editor_template` type `landing_page`
  (rapidocrm) ; **voie 2** skill `usine-a-landing` (Lovable) si disponible.
- **Formulaire de capture CRM** + **CTA trackés** (`list_cta`).
- **Visuels brandés** → skill `studio-visuel-marque` (logo + charte **réels**).
- ⏸️ **VALIDATION** avant l'Acte 3.

## ACTE 3 — Séquences & automatisations
- **Emails de conversion** → skill `email-sequence` + templates CRM
  (`create_template_email`).
- **Relances devis** → skill `devis-facture-relance`.
- **Automatisation des passages d'étape** → skills `usine-automatisations` +
  `memoire-operationnelle` (n8n).
- **Rien n'est activé sans confirmation** (hook `garde-envois`).
- ⏸️ **VALIDATION** avant l'Acte 4.

## ACTE 4 — Acquisition
- **Entrant** → skill `machine-inbound` ; **sortant** → skill `machine-outbound` ;
  **paid** → skills `lancement-campagne-meta` + `pixel-et-retargeting`
  (**budget plafonné confirmé**, entités PAUSED).
- ⏸️ **VALIDATION avant toute activation** (dépense = argent réel).

## ACTE 5 — Mesure & optimisation
- **Funnel report étape par étape** :
  `python3 "${CLAUDE_PLUGIN_ROOT}/skills/tunnel-de-vente-360/scripts/funnel_metrics.py"`
  (stdlib) sur données réelles (soumissions, `list_cta`, pipeline, ventes,
  `get_conversion_par_canal`) — taux par passage, **goulot** identifié, jamais
  de calcul de tête.
- **Plan d'A/B tests** sur le goulot → skill `ideation-growth-experiments`.
- **Leçons (automatique)** → 1 à 3 leçons datées et **sourcées** (chiffres de `funnel_metrics.py`) dans `./rapido-kb/marketing/apprentissages.md` + **màj `benchmarks.md`** si un taux change (via `mise-a-jour-kb`).
- **Registre** `tunnels.md` mis à jour avec les **IDs réels** : campagne CMS,
  templates, segments, séquences, workflows n8n, projet RH.

## Livrable type
Un **tunnel opérationnel** de bout en bout + son schéma, ses pages, ses séquences,
son acquisition et son rapport funnel — chaque brique déléguée, chaque acte
validé, chaque envoi/dépense confirmé.

## Frontières
- **Lancer une entreprise entière** (pas seulement un tunnel) → skill
  `lancement-projet-360` (rapido-suite).
- Une **brique unitaire** (juste une landing, juste une séquence) → le skill
  d'exécution correspondant, pas cet orchestrateur.

## Garde-fous
Validation entre **chaque acte** ; aucun envoi ni publication sans confirmation
(`garde-envois`) ; **budget pub plafonné confirmé**, entités PAUSED ; KPI par
script ; voie Rapido d'abord ; récap des IDs à chaque fin d'acte ; RGPD respecté.
