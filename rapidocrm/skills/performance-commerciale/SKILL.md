---
name: performance-commerciale
description: Utiliser quand l'utilisateur demande la performance de l'équipe, les objectifs, les KPIs ou un tableau de bord commercial. Agrège commerciaux, performances individuelles et indicateurs globaux en une synthèse structurée.
---

# Performance commerciale

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).

## Workflow

1. **Lister l'équipe** — `list_commerciaux` (`statut` = actif | inactif, `q`
   recherche par nom/fonction) : récupérer statuts et objectifs de chacun.
2. **Détailler les performances individuelles** — pour chaque commercial pertinent :
   `get_commercial` (`id`) pour objectifs + performance, et `get_user_performance`
   (`id`, `periode` ∈ today | week | month | quarter | year) pour l'activité.
3. **Indicateurs globaux** — `get_dashboard_general_stats` (KPIs CRM, marketing,
   commercial, facturation) et `get_dashboard_kpis`, avec la même `periode` que
   l'étape 2 pour rester comparable. Compléter si utile : `get_stats_pipeline_global`
   (conversion pipeline), `get_revenue_summary` (CA), `get_top_clients`.
4. **Synthèse structurée** à restituer :
   - vue équipe : effectif actif, objectifs atteints / en retard ;
   - top / flop par indicateur (CA, conversions, activité) — factuel, sans jugement ;
   - indicateurs globaux de la période vs objectifs ;
   - points d'attention et suggestions d'action (ex. redistribuer des prospects).

## Garde-fous

- Skill en LECTURE SEULE : ne jamais modifier objectifs (`update_commercial_objectifs`),
  statuts (`set_commercial_status`) ou profils depuis ce skill sans demande
  explicite et confirmation de l'utilisateur.
- Toujours préciser la période analysée dans la synthèse ; si l'utilisateur n'en
  donne pas, utiliser `month` et le dire.
- Ne comparer les commerciaux que sur des chiffres renvoyés par l'API — aucune
  extrapolation.
