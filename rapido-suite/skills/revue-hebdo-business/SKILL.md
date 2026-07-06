---
name: revue-hebdo-business
description: Utiliser quand l'utilisateur demande une revue hebdo, un point business ou un tableau de bord global. Agrège en LECTURE SEULE les indicateurs des 4 serveurs (CRM, CMS, RH, FoodEatUp) en une synthèse exécutive unifiée.
---

# Revue hebdo business

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

## Synthèse exécutive unifiée (format de sortie)

Produire UNE synthèse structurée, avec la période en en-tête :
1. **Chiffres clés** : CA (CRM + FoodEatUp séparés), pipeline (taux de
   conversion), impayés ;
2. **Commercial** : évolution du pipeline, deals gagnés/perdus ;
3. **Contenu** : posts publiés, portée/engagement, meilleur post ;
4. **Projets** : en cours / en retard / terminés ;
5. **Points d'attention** : impayés, projets à risque, baisses d'indicateurs —
   avec suggestion d'action (sans l'exécuter).

## Garde-fous

- Ne JAMAIS modifier une donnée depuis ce skill (pas de create/update/delete),
  quel que soit le constat.
- Utiliser la MÊME période sur tous les systèmes pour que la synthèse soit
  cohérente ; l'indiquer explicitement.
- Ne comparer que des chiffres renvoyés par les API — aucune extrapolation ; si
  une source est indisponible, le dire plutôt que d'estimer.
