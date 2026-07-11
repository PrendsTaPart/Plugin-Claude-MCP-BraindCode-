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

1. **Notifications non lues** — `list_notifications` (`establishment_id`
   seul ; pas de filtre serveur : filtrer les non lues dans la réponse) —
   elles ouvrent le briefing : ce sont les alertes déposées par le système
   et les routines (dont Loop Engine).
2. **Conformité HACCP** — `list_haccp_temperatures` (date du jour) : relevés
   faits ? valeurs hors seuil ? `list_haccp_reception` : réceptions à contrôler ?
   Toute non-conformité passe EN TÊTE du briefing.
3. **Salle & réservations — UN appel temps réel** — `floor_plan_status`
   (compteurs par statut + commande active par table) remplace tout appel
   séparé aux tables/zones. `list_reservations` (date du jour) reste la
   source des couverts, gros groupes et notes (allergies, VIP) —
   l'outil de disponibilité ne renvoie pas les réservations du jour.
   Puis **créneaux chauds du midi** : `reservation_availability` teste UN
   créneau à la fois (`date`, `time` HH:MM, `party_size`) — sonder 12:00 /
   12:30 / 13:00 avec la taille de groupe typique et annoncer la capacité
   restante (« complet à 12:30, reste 2 tables à 13:00 »).
4. **Staffing** — `list_plannings` (jour) : qui est présent par service ;
   croiser avec la charge (couverts attendus) et signaler un sous/sur-staffing.
5. **Productions planifiées** — `list_production_plans` (date du jour) : quoi
   produire, en quelle quantité, à quelle heure.
6. **Alertes ingrédients** — `list_production_alerts` : ingrédients manquants
   pour les productions à venir.
7. **Stocks bas** — `list_low_stocks` : articles sous le seuil.
8. **Publier les alertes (seule écriture, sur confirmation)** — pour chaque
   alerte retenue du briefing (non-conformité HACCP, relevé manquant, stock
   critique, surbooking), PROPOSER `create_notification`
   (`establishment_id`, `title` court, `message` factuel, `type` ∈
   `warning` | `danger`) pour qu'elle atteigne toute l'équipe dans
   FoodEatUp. Une confirmation PAR notification ; IDs récapitulés.

## Format de sortie — UN écran, pas plus

```
📋 BRIEFING — {date} — {établissement}

🔔 NOTIFICATIONS NON LUES : n — les warning/danger citées une par une

🎯 3 PRIORITÉS DU JOUR
1. … (toujours la conformité s'il y a une non-conformité HACCP)
2. …
3. …

🌡 HACCP : relevés OK/KO, non-conformités, réceptions attendues
🍽 SERVICE : X couverts midi / Y soir, groupes & notes, état salle
   (floor_plan_status), créneaux midi restants (12:00/12:30/13:00)
👥 ÉQUIPE : présents par service, alerte staffing éventuelle
🔥 PRODUCTION : plans du jour, ingrédients manquants
📦 STOCK : articles bas → commande à prévoir ?
```

Les 3 priorités sont ARBITRÉES, pas listées : une seule phrase chacune,
actionnable, choisie selon l'ordre HACCP > expérience client > rentabilité.

## Garde-fous

- Briefing en LECTURE SEULE — une seule exception : la PUBLICATION des
  alertes (`create_notification`), toujours après confirmation, une par
  une. Chaque priorité
  pointe vers le skill qui permet d'agir (`haccp-conformite-quotidienne`,
  `service-salle`, `production-stock`, `reappro-fournisseurs`) — l'action ne se
  lance que si l'utilisateur le demande.
- Si une source ne renvoie rien (pas de planning, pas de production), l'indiquer
  d'un mot — ne pas inventer.
- Proposer en fin de briefing : « on traite la priorité 1 ? ».
