---
name: widgets-accueil
description: Utiliser quand l'accueil Plan'It s'aménage, que l'utilisateur dit « pose le MRR sur mon accueil », « ajoute un widget tendance des demandes », « retire ce widget », « rafraîchis ce KPI ». Pose, retire et rafraîchit les widgets KPI — coût de collecte annoncé avant la pose, règle throttled respectée.
---

# Widgets de l'accueil (poser, retirer, rafraîchir)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/guide-widgets.md` (quel type pour quel KPI).

## Workflow

1. **`list_kpi_catalog`** — TOUJOURS avant la pose : formule, unité, sens de
   lecture, connecteur (connecté ?), et **coût de collecte annoncé** à
   l'utilisateur. (Le hook garde-cout-annonce refuse un add sans catalogue
   lu dans la session.)
2. **`add_kpi_widget`** — type choisi d'après le guide (`metric`, `trend`,
   `gauge`, `bar`, `line`, list, `donut`, `status`), taille, période
   (`today`, `7d`, `30d`, `mtd`). Échoue si le KPI est déjà posé : le dire,
   ne pas forcer. KPI dont le connecteur n'est pas connecté : il se pose
   mais ne se collectera pas — le dire aussi.
3. **`remove_kpi_widget`** — sur confirmation seulement ; rappeler que le
   KPI et son historique SONT CONSERVÉS, seul l'affichage disparaît.
4. **`refresh_kpi`** — collecte forcée (facturée pour un KPI métier). Si la
   réponse porte `throttled: true` : la valeur n'est PAS fraîche — la donner
   avec son âge (`age_minutes`), jamais comme un relevé du moment.

## Garde-fous

- Le coût de collecte vient du catalogue — jamais estimé de tête.
- Pas de « tableau de bord complet » posé d'un coup sans l'accord ligne par
  ligne : chaque widget a son coût.
