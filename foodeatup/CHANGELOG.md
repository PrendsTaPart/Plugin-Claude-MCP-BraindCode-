# Changelog — plugin foodeatup

## 0.6.0 — 2026-07-06

- Couverture des outils orphelins — 3 nouveaux skills :
  - `carte-vitrine` : toute la carte en ligne en un appel
    (`import_storefront_menu`, idempotent sur les noms — reprendre les noms
    exacts de `list_dishes`), formules éditoriales, même source de vérité que
    le menu imprimable (rapido-canva) ;
  - `planning-equipe` : `create_shift`, `list_plannings` (coût estimé TOUJOURS
    affiché), `approve_leave`/`reject_leave`, `list_attendances` — règle dure :
    jamais de shift sur congé approuvé ;
  - `gestion-commandes` : `create_order` (canaux, table, facture+devis
    auto-générés), `update_order_status` (machine à états en_attente →
    confirmee → en_preparation → prete → livree, effets de bord
    facture/table), lien avec service-salle.

## 0.5.0 — 2026-07-06

- Utilisation de la base de connaissance `./rapido-kb/` : règle de chargement
  dans les directives (la KB PRIME sur les défauts, sans KB = défaut signalé) ;
  agent `chef-restaurateur` cite ses seuils maison (processus-internes.md) ;
  `analyse-rentabilite-carte` passe le seuil food cost maison à
  `menu_matrix.py` (2e argument, source du seuil dans la sortie).

## 0.4.0 — 2026-07-06

- Script de calcul `skills/analyse-rentabilite-carte/scripts/menu_matrix.py`
  (stdlib) : food cost %, marges, quadrants Kasavana-Smith, alertes > 30 % —
  le skill impose « utiliser le script pour tout calcul ; ne jamais calculer
  de tête ».
- `reference/pieges-outils.md` : tableau Outil | Paramètres pièges | Erreur
  fréquente | Parade (establishment_id, poids brut, TVA, item_id recipe_,
  adjust_stock, machine à états des tables…), référencé par les directives.

## 0.3.0 — 2026-07-06

- Hooks déterministes (`hooks/hooks.json` + `hooks/scripts/`) :
  - PreToolUse `garde-destructif` : confirmation forcée (ask) sur tous les
    `delete_*` du serveur foodeatup ;
  - PreToolUse `anti-donnee-inventee` : refus (deny) de toute température hors
    plage plausible (-30 °C à +90 °C) ou non numérique sur `add_temperature` ;
  - Stop `récap-actions` (hook prompt) : bloque la fin de tour si des écritures
    MCP ont eu lieu sans récapitulatif des IDs dans la réponse.

## 0.2.0 — 2026-07-06

- Ajout de la couche métier :
  - Agents : `chef-restaurateur` (ratios, priorités HACCP > client > rentabilité,
    diagnostic avant action) et `chef-cuisine` (fiches techniques, coefficients
    de cuisson, allergènes, anti-gaspillage).
  - Skills d'expertise : `analyse-rentabilite-carte` (ingénierie de menu,
    matrice popularité × marge) et `briefing-du-jour` (routine du matin,
    synthèse un écran + 3 priorités).
- Les agents connaissent et invoquent les skills du plugin au bon moment.

## 0.1.0 — 2026-07-06

- Version initiale : `.mcp.json` (serveur foodeatup), référence
  `directives-outils.md`, skills workflow `haccp-conformite-quotidienne`,
  `service-salle`, `recette-cout-marge`, `production-stock`,
  `reappro-fournisseurs`.
