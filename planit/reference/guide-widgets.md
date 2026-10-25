# Guide des widgets — Plan'It

## Côté Plan'It : les widgets KPI de l'accueil (`add_kpi_widget`)

Le type se choisit d'après la nature du KPI (catalogue : `list_kpi_catalog`,
qui donne l'unité, le sens de lecture et le coût de collecte — à annoncer
AVANT la pose). Périodes : today, 7d, 30d, mtd.

| Type | Quand | Exemples |
|---|---|---|
| `metric` | une valeur instantanée qui se lit seule | solde de crédits, tâches en retard |
| `trend` | la même valeur dans le temps (le sens compte plus que le niveau) | demandes entrantes/semaine |
| `gauge` | une valeur contre un objectif ou un plafond | budget consommé, quota d'envois |
| `bar` | comparer quelques catégories | exécutions par routine, posts par réseau |
| `line` | série continue à lecture fine | MRR, visiteurs |
| `list` | les N éléments qui demandent l'œil | routines en échec, alertes ouvertes |
| `donut` | répartition d'un tout | crédits par routine |
| `status` | un état binaire/ternaire | connecteurs OK/erreur |

Règles : un KPI dont le connecteur n'est pas connecté se pose mais ne se
collecte pas — le dire ; `remove_kpi_widget` n'efface pas l'historique ;
`refresh_kpi` rapproché renvoie `throttled` (valeur « pas fraîche », âge en
minutes).

## Côté plugin : les gabarits HTML (`widgets/` + `scripts/render_widget.py`)

Pages autonomes rendues UNIQUEMENT depuis le JSON des outils (un champ
absent = « — », jamais estimé). Charte : aucune charte Plan'It n'est
versionnée dans ce dépôt (vérifié le 2026-10-25) → **thème neutre signalé**,
jetons CSS surchargables (`:root`), sombre/clair.

| Gabarit | Source JSON | Montre |
|---|---|---|
| `accueil-pilotage` | get_kpi_home (+ pending) | crédits, jours d'autonomie, widgets, alertes, décisions |
| `calendrier-des-routines` | get_calendar | semaine/mois, états done/failed/missed/scheduled, chevauchements |
| `rapport-de-routine` | get_routine_report | exécutions, taux de réussite, crédits, outils appelés, signaux |
| `boucles-kpi` | list_active_loops / evaluate_loops | référence figée, valeur courante, écart orienté, verdict (« pas assez de données » explicite) |
| `diff-amelioration` | propose_routine_improvement | avant/après de LA proposition en attente |
| `credits-par-routine` | scripts/credits_autonomie.py | consommation par routine, classement, jours d'autonomie, formule affichée |
