---
name: briefing-du-jour
description: Utiliser quand l'utilisateur demande le briefing du jour, « ma journée » ou un point du matin. Routine du directeur de restaurant — HACCP, réservations, salle, staffing, productions, stocks — synthétisée en un écran avec les 3 priorités de la journée.
---

# Briefing du jour

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
   règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).
2. S'assurer d'avoir l'`establishment_id` (le demander si absent) avant tout appel.

## Workflow — collecte (lecture seule, date du jour)

Dérouler dans l'ordre des priorités maison (HACCP > client > rentabilité) :

1. **Conformité HACCP** — `list_haccp_temperatures` (date du jour) : relevés
   faits ? valeurs hors seuil ? `list_haccp_reception` : réceptions à contrôler ?
   Toute non-conformité passe EN TÊTE du briefing.
2. **Réservations du jour** — `list_reservations` (date du jour) : couverts par
   service, gros groupes, notes particulières (allergies, VIP).
3. **Plan de salle** — `floor_plan_status` : état des tables, commandes actives.
4. **Staffing** — `list_plannings` (jour) : qui est présent par service ;
   croiser avec la charge (couverts attendus) et signaler un sous/sur-staffing.
5. **Productions planifiées** — `list_production_plans` (date du jour) : quoi
   produire, en quelle quantité, à quelle heure.
6. **Alertes ingrédients** — `list_production_alerts` : ingrédients manquants
   pour les productions à venir.
7. **Stocks bas** — `list_low_stocks` : articles sous le seuil.

## Format de sortie — UN écran, pas plus

```
📋 BRIEFING — {date} — {établissement}

🎯 3 PRIORITÉS DU JOUR
1. … (toujours la conformité s'il y a une non-conformité HACCP)
2. …
3. …

🌡 HACCP : relevés OK/KO, non-conformités, réceptions attendues
🍽 SERVICE : X couverts midi / Y soir, groupes & notes, état salle
👥 ÉQUIPE : présents par service, alerte staffing éventuelle
🔥 PRODUCTION : plans du jour, ingrédients manquants
📦 STOCK : articles bas → commande à prévoir ?
```

Les 3 priorités sont ARBITRÉES, pas listées : une seule phrase chacune,
actionnable, choisie selon l'ordre HACCP > expérience client > rentabilité.

## Garde-fous

- Briefing en LECTURE SEULE : aucune création/modification. Chaque priorité
  pointe vers le skill qui permet d'agir (`haccp-conformite-quotidienne`,
  `service-salle`, `production-stock`, `reappro-fournisseurs`) — l'action ne se
  lance que si l'utilisateur le demande.
- Si une source ne renvoie rien (pas de planning, pas de production), l'indiquer
  d'un mot — ne pas inventer.
- Proposer en fin de briefing : « on traite la priorité 1 ? ».
