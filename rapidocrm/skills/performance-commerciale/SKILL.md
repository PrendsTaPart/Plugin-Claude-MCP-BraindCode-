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
   (conversion pipeline), `get_revenue_summary` (CA), `get_top_clients`,
   `get_interaction_stats` (`periode`) pour le volume d'interactions.
   Côté coûts : `list_depenses` (`statut` ∈ en_attente, payee ; `periode`) —
   et pour SAISIR une dépense dictée : `create_depense` (`entreprise_id`,
   `total_ht` requis ; `taux_tva` en %, TTC/TVA auto-calculés sinon ;
   `mode_paiement` ∈ Espèce, Carte bleu, Virement, Chèque ; `statut`) après
   confirmation — une dépense enregistre de l'argent sorti.
4. **Synthèse structurée** à restituer :
   - vue équipe : effectif actif, objectifs atteints / en retard ;
   - top / flop par indicateur (CA, conversions, activité) — factuel, sans jugement ;
   - indicateurs globaux de la période vs objectifs ;
   - points d'attention et suggestions d'action (ex. redistribuer des prospects).

## Garde-fous

- Skill en LECTURE SEULE par défaut : ne jamais modifier objectifs
  (`update_commercial_objectifs`), statuts (`set_commercial_status`) ou
  profils depuis ce skill sans demande explicite et confirmation.

## Cycle de vie d'un commercial (sur demande explicite uniquement)

- **Entrée** — `create_commercial` (`nom`, `prenom`, `email` requis ;
  objectifs mensuels `nombre_appel`/`nombre_RDV`/`nombre_contrat`/
  `nombre_email`/`nombre_sms`/`nombre_prospection`, `disponible`) — après
  récapitulatif confirmé.
- **Profil** — `update_commercial_profil` (`id` requis ; ne passer que les
  champs qui changent).
- **Sortie** — `delete_commercial` (`id`, **`confirm: true` exigé par le
  serveur**) : supprime aussi ses objectifs — irréversible, hook
  garde-destructif + confirmation explicite ; proposer d'abord
  `set_commercial_status` (inactif), qui préserve l'historique.
- Toujours préciser la période analysée dans la synthèse ; si l'utilisateur n'en
  donne pas, utiliser `month` et le dire.
- Ne comparer les commerciaux que sur des chiffres renvoyés par l'API — aucune
  extrapolation.
