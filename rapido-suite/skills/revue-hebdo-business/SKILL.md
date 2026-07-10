---
name: revue-hebdo-business
description: Utiliser quand l'utilisateur demande une revue hebdo, un point business ou un tableau de bord global. Agrège en LECTURE SEULE les indicateurs des 4 serveurs (CRM, CMS, RH, FoodEatUp) en une synthèse exécutive unifiée.
---

# Revue hebdo business

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
règles pendant toute l'exécution (IDs, données, formats, erreurs, récapitulatif).

Skill STRICTEMENT EN LECTURE SEULE : aucun outil de création, modification ou
suppression ne doit être appelé, même si un problème est détecté — le signaler
dans la synthèse et laisser l'utilisateur décider.

## Workflow (période par défaut : semaine — `periode: "week"`)

1. **CRM — commercial et finances** :
   - `get_dashboard_general_stats` (`periode`) : KPIs CRM, marketing, commercial,
     facturation ;
   - `get_revenue_summary` (`periode`) : CA d'après factures et devis ;
   - `get_stats_pipeline_global` (`periode`) : conversion du pipeline.
2. **CMS — contenu social** :
   - `list_scheduled_posts` (`start_date`/`end_date` de la semaine, format Y-m-d)
     pour identifier les posts récents ;
   - `post_insights` (`post_ids`, MAX 10 par appel — découper au-delà) sur les
     posts publiés de la période.
3. **RH — projets** :
   - `get-projects-list-tool` (`statuses: [0]` en cours ; ajouter `[1]` terminés
     si comparaison utile) : état d'avancement des projets ;
   - optionnel si l'utilisateur veut le détail équipe : `get-dailies-tool` sur la
     période.
4. **FoodEatUp — restaurant** (si un établissement est géré) :
   - `finance_summary` (`establishment_id` requis — le demander si inconnu ;
     `date_from`/`date_to` = la semaine, sinon défaut = mois en cours) : CA
     facturé, encaissé, impayés, dépenses, marge.
   - Si l'utilisateur ne gère pas d'établissement FoodEatUp, sauter cette section
     en le mentionnant.
5. **Web / Produits** (si le serveur Lovable est disponible — plugin
   rapido-lovable installé ; sinon sauter en le mentionnant) :
   - `list_projects` (`publish_status: "published"`) : les apps publiées ;
   - `get_project_analytics` par projet (`start_date`/`end_date` en RFC 3339,
     MÊMES dates que la période analysée) : visiteurs, conversion, sources,
     appareils ;
   - croiser avec `get_stats_campagne` (CRM) : le trafic vient-il des
     campagnes ? Les pics correspondent-ils aux envois/publications ?
6. **Acquisition payante** (si le serveur facebook-ads est disponible —
   plugin rapido-meta-ads installé ; sinon sauter en le mentionnant) :
   - `ads_get_ad_entities` (période explicite, mêmes dates) : dépense,
     résultats, coût par résultat ;
   - `ads_insights_anomaly_signal` : décrochages à signaler ;
   - croiser avec les leads CRM réellement entrés en pipeline (coût par
     client, pas par clic).
7. **Automatisations** (serveur n8n optionnel du plugin — si `N8N_MCP_URL`
   est définie ; sinon sauter en le mentionnant) :
   - `search_workflows` : nombre de workflows actifs (vs registre
     `rapido-kb/processus-internes.md`) ;
   - `search_executions` (`status: ["error","crashed"]`, `startedAfter` = la
     période) + total des succès : taux de succès ;
   - échecs à traiter → renvoyer vers `surveillance-automatisations`.

## Synthèse exécutive unifiée (format de sortie)

Produire UNE synthèse structurée, avec la période en en-tête :
1. **Chiffres clés** : CA (CRM + FoodEatUp séparés) COMPARÉ à la période
   précédente (↗ ↘ → chiffré), top ventes de la période
   (`list_top_productions` FoodEatUp / meilleurs devis signés CRM), pipeline
   (taux de conversion), impayés ;
2. **Commercial** : évolution du pipeline, deals gagnés/perdus ;
3. **Contenu** : posts publiés, portée/engagement, meilleur post ;
4. **Projets** : en cours / en retard / terminés ;
5. **Web / Produits** (si disponible) : visiteurs, conversion, sources — et le
   lien trafic ↔ campagnes ;
6. **Acquisition payante** (si disponible) : dépense de la période, coût par
   résultat, anomalies ;
7. **Automatisations** (si disponible) : workflows actifs, taux de succès,
   échecs à traiter ;
8. **Wins & watches** : les victoires de la période (à célébrer, factuel) puis
   les points d'attention — impayés, projets à risque, baisses d'indicateurs —
   avec suggestion d'action (sans l'exécuter).

(Le format « comparaison vs période précédente, top ventes, wins & watches »
est hérité de « friday-brief », pack small-business
d'anthropics/knowledge-work-plugins, Apache 2.0, fusionné dans ce skill —
voir ATTRIBUTIONS.md du plugin.)

## Garde-fous

- Ne JAMAIS modifier une donnée depuis ce skill (pas de create/update/delete),
  quel que soit le constat.
- Utiliser la MÊME période sur tous les systèmes pour que la synthèse soit
  cohérente ; l'indiquer explicitement.
- Ne comparer que des chiffres renvoyés par les API — aucune extrapolation ; si
  une source est indisponible, le dire plutôt que d'estimer.
