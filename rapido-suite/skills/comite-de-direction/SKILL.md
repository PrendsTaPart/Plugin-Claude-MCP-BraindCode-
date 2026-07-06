---
name: comite-de-direction
description: Utiliser quand l'utilisateur demande un comité de direction, une vision globale ou « où en est l'entreprise ». Orchestre la revue business multi-domaines et la restitue en format CODIR — 1 page par domaine plus arbitrages inter-domaines.
---

# Comité de direction (CODIR)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
règles pendant toute l'exécution (IDs, données, formats, erreurs, récapitulatif).

## Workflow

1. **Cadrage** — période (défaut : `month` ; la MÊME sur tous les domaines) et
   périmètre (les 4 domaines, ou moins si un serveur ne concerne pas
   l'utilisateur — le mentionner).
2. **Collecte** — dérouler le skill `revue-hebdo-business` (lecture seule) :
   CRM (`get_dashboard_general_stats`, `get_revenue_summary`,
   `get_stats_pipeline_global`), CMS (`list_scheduled_posts` + `post_insights`,
   `ingishts_campagne`), RH (`get-projects-list-tool`, `get-dailies-tool`),
   FoodEatUp (`finance_summary`, `establishment_id` requis).
3. **Restitution CODIR — 1 page par domaine**, format identique pour les 4 :
   ```
   ── {DOMAINE} ─────────────────────────
   📌 Chiffre clé : LE chiffre qui résume la période
   📈 Tendance : vs période précédente (↗ ↘ →) — chiffrée si les données le permettent
   ⚠️ Alerte : le risque n° 1 du domaine (ou « RAS »)
   🎯 Décision proposée : UNE décision actionnable, avec son responsable naturel
   ```
   Domaines : Commercial (CRM) / Contenu & marque (CMS) / Équipe & projets (RH)
   / Restaurant (FoodEatUp) / Web & Produits (Lovable — si le plugin
   rapido-lovable est installé : `list_projects` publiés +
   `get_project_analytics` en RFC 3339 sur la même période, croisés avec
   `get_stats_campagne` ; sinon sauter cette page en le mentionnant).
4. **Arbitrages inter-domaines** — la section qui n'existe dans aucun domaine
   pris seul :
   - croiser les signaux (méthode de l'agent `directeur-general` : acquisition,
     organisation, delivery, conversion) et nommer les diagnostics croisés avec
     les deux chiffres qui les fondent ;
   - lister les tensions à arbitrer (ressources, priorités, séquencement) avec
     2 options chacune maximum et une recommandation ;
   - 3 DÉCISIONS maximum proposées au dirigeant pour la période suivante,
     priorisées.
5. **Suivi** — chaque décision actée pointe vers son exécutant : agent
   spécialiste du plugin concerné (`chef-restaurateur`,
   `directeur-commercial`, `responsable-marketing`, `chef-de-projet`/
   `responsable-rh`) ou skill transverse (`onboarding-client-360`). Aucune
   exécution depuis ce skill.

## Garde-fous

- Skill en LECTURE SEULE : le CODIR constate, propose et arbitre — il
  n'exécute rien ; l'exécution passe par les skills/agents dédiés après
  validation.
- Une tendance sans donnée de période précédente se marque « première mesure »
  — pas de tendance inventée.
- Si un domaine est indisponible (serveur, droits, pas d'établissement), sa
  page l'indique en une ligne au lieu de chiffres estimés.
- Maximum 3 décisions proposées : un CODIR qui décide de tout ne décide de
  rien.
