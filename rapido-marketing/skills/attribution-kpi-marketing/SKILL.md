---
name: attribution-kpi-marketing
description: Utiliser quand l'utilisateur demande d'où viennent ses clients, une attribution, le ROI par canal, ou ses CAC/LTV. Collecte les métriques multi-sources (CRM, CMS, Meta), applique un modèle d'attribution simple et honnête (premier/dernier point), calcule CAC/LTV/ROI par script et recommande une allocation.
---

# Attribution & KPI marketing — d'où viennent les clients

> **Honnêteté du modèle.** Le serveur n'expose **pas** d'attribution multi-touch
> (matrice M0). Ce skill fait une attribution **single-touch** (premier OU
> dernier point de contact), **limites documentées** — jamais de multi-touch
> probabiliste inventé.

## Étape 0 — Charger (obligatoire)
- `${CLAUDE_PLUGIN_ROOT}/reference/priorite-mcp.md` et `garde-fous-marketing.md`.
- **Lire `./rapido-kb/marketing/apprentissages.md` et `benchmarks.md` AVANT de
  conclure** — les taux de référence maison **priment** sur tout repère par
  défaut. `icp.md` (segments). Fichiers absents → créés depuis
  `${CLAUDE_PLUGIN_ROOT}/reference/kb-templates/` (voir `reference/memoire.md`).

## Méthode

### 1. Collecte multi-sources (données réelles)
- **CRM** : `get_conversion_par_canal`, `get_dashboard_general_stats`,
  `get_revenue_summary`, `list_depenses` (rapidocrm).
- **CMS** : `ingishts_campagne`, `post_insights` (rapidocms).
- **Meta** : skill `pilotage-performance-ads` (dépense, coût par résultat).
- Un signal absent = « pas de visibilité sur X », jamais inventé.

### 2. Modèle d'attribution (simple et assumé)
Choisir **premier** ou **dernier** point de contact avec l'utilisateur ;
**documenter la limite** (single-touch). C'est la part d'attribution par canal.

### 3. Calculs (jamais de tête)
- **Voie 1** : skill `catalogue-kpi` (rapido-startup) pour CAC/LTV/ROI si installé.
- **Voie 2 (repli)** :
  `python3 "${CLAUDE_PLUGIN_ROOT}/skills/attribution-kpi-marketing/scripts/kpi_marketing.py"`
  avec `{modele, canaux:[{canal, depense, clients, revenu_brut, cout_livraison,
  contacts_premier, contacts_dernier}]}` → CAC, LTGP, ROI, part d'attribution.

### 4. Sortie
**Tableau par canal** (CAC / LTGP / ROI / part) + **3 recommandations
d'allocation** (renforcer le canal au meilleur ROI, corriger/couper le pire,
tester le sous-exploité). **Capitalisation automatique** : à chaque run, mettre à
jour `./rapido-kb/marketing/benchmarks.md` ET ajouter 1-3 leçons datées et
sourcées (chiffres de `kpi_marketing.py`) dans `apprentissages.md` — via
`mise-a-jour-kb`. Pas de leçon sans preuve chiffrée.

## Livrable type
Tableau d'attribution + KPI par canal + 3 recommandations d'allocation budgétaire,
avec la limite du modèle rappelée.

## Cas d'usage croisés
- Formules détaillées (MRR, churn, runway…) → skill `catalogue-kpi`.
- Performance pub détaillée → skill `pilotage-performance-ads`.
- Money math d'acquisition (LTGP:CAC, seuils) → skill `money-math-acquisition`.

## Sources d'attribution (multi-canal étendu)
Quand les plugins sont installés, croiser les sources (serveur absent = sauté en le disant) :
- **GA4** (`run_report`) — trafic et conversions par **source/medium**.
- **GSC** (`rapido-seo:performance-organique`) — canal **organique** (positions, clics).
- **Google Ads** (`rapido-google-ads`) — **SEA** (dépense, conversions par campagne).
- **TikTok Ads** (`rapido-tiktok-ads`) et **Meta** (`rapido-meta-ads`) — **payant social**.
- KPI **« part organique vs payante du CA »** : CA attribué organique ÷ CA total (et
  la part payante) — formule au **Registre des KPIs** (`reference/registre-routines.md`),
  calcul `rapido-startup:catalogue-kpi`.

## Frontière KPI (source unique des formules)
- **`rapido-startup:catalogue-kpi` = source de vérité des FORMULES** (CAC, LTV,
  ratio, runway, DSO…). Le CAC calculé ici (`dépense / clients`) est **la même
  formule** que `catalogue-kpi.cac`, simplement **scopée par canal** — pas une
  formule concurrente.
- **Ce skill = ce qui lui est PROPRE** : la **répartition par canal** et le **modèle
  d'attribution** (single-touch premier/dernier point) — que `catalogue-kpi` ne fait
  pas. `LTGP` (marge brute/client) et `ROI` par canal sont **propres au marketing**
  (≠ LTV). Voir le **Registre des KPIs** de `reference/registre-routines.md`.
- **`money-math-acquisition`** = cadrage décisionnel (combien dépenser, LTGP:CAC) —
  calculs **délégués** au script KPI, jamais recalculés de tête.

## Garde-fous
Attribution **single-touch assumée** (limites dites) ; KPI **par script**, **formules
de `catalogue-kpi` (source unique)** ; données live > KB ; aucune donnée inventée ;
benchmarks datés.
