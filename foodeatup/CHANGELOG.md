# Changelog — plugin foodeatup

## 1.2.1 — 2026-07-10

- Corrections documentaires (audit) : `update_invoice_status` — enum élargi
  vérifié serveur (brouillon, en_attente, envoyee, acceptee, refusee,
  litige, payee, annulee), transitions DGFiP validées PAR LE SERVEUR : ne
  plus pré-filtrer côté skill, tenter l'appel et relayer l'erreur (ligne
  pieges-outils ajoutée).
- `add_temperature` : `equipment_id` REQUIS documenté (haccp +
  pieges-outils) — jamais deviné, résolu via `search_entities`
  (`types: ["equipment"]`), confirmation si `ambiguous=true` ; le hook
  anti-donnee-inventee refuse désormais tout relevé sans `equipment_id`
  (testé stdin : deny sans, allow avec).

## 1.2.0 — 2026-07-10

- `briefing-du-jour` exploite les utilitaires (schémas vérifiés serveur) :
  - notifications non lues EN TÊTE du briefing (`list_notifications` —
    pas de filtre serveur, filtrage côté réponse ; y arrivent les alertes
    des routines Loop Engine) ;
  - salle & réservations : `floor_plan_status` = l'appel temps réel unique
    (compteurs + commande active par table) ; `reservation_availability`
    sonde les créneaux chauds du midi (UN créneau par appel : `date`,
    `time` HH:MM, `party_size`) ; `list_reservations` conservé — c'est la
    seule source des couverts/groupes/notes du jour.
- tests/evals.md : scénarios briefing 1.2.0 + non-régression (2 scénarios
  existants rejoués).

## 1.1.0 — 2026-07-10

- Nouveau skill `coordination-cuisine` (pass / KDS) : `list_orders` (en
  cours) → `update_kds_item_status` plat par plat (machine à états vérifiée
  serveur : pending → in_progress → ready → **served** — 4 états, `item_id` =
  ligne de commande, jamais l'ID du plat au menu) → quand tous les plats
  d'une commande sont `ready`, PROPOSER `update_order_status` (`prete`).
  Noms de plats dictés à l'oral résolus via `search_entities`
  (si `ambiguous=true` → confirmation demandée).
- `haccp-conformite-quotidienne` — volet nettoyage : `list_cleaning_zones`
  (zones et postes = référentiel attendu), `record_cleaning_action` après
  confirmation (`poste_nettoyage_id` = le POSTE, statut défaut `complete`),
  `list_cleaning_actions` pour le registre. Le contrôle du jour couvre
  désormais températures + réceptions + DLC + checklist hygiène + plan de
  nettoyage ; KPI conformité étendu : actions faites / attendues.
- `planning-equipe` — volet administratif : `create_employee_contract`
  (confirmation niveau 2, données sensibles — type ∈ CDI, CDD, Extra,
  Apprentissage, Stage ; `end_date` obligatoire pour un CDD),
  `list_employee_contracts`, `list_employee_documents`. Croisement
  `detection-surcharge` (rapidorh) : heures contractuelles désormais lues
  depuis les contrats réels (`weekly_hours`), plus supposées ; salaires
  jamais affichés dans une vue d'équipe.
- Hook `garde-destructif` : matcher étendu à `create_employee_contract`
  (testé fonctionnellement — décision `ask`) ; libellé élargi aux actions
  sensibles.
- `reference/pieges-outils.md` : 3 lignes (item_id KDS, poste vs zone de
  nettoyage, CDD sans end_date).
- `tests/evals.md` : 8 scénarios de déclenchement et de comportement.

## 1.0.0 — 2026-07-06

- Première version publique.

## 0.9.0 — 2026-07-06

- Nouveau skill maison `onboarding-restaurateur` (créé avec la méthodologie
  skill-creator) : mise en place complète d'un nouveau client — carte via
  `import_storefront_menu` (idempotence sur les noms), zones et tables
  (`create_zone`/`create_table` + contrôle `floor_plan_status`), équipe
  (`create_employee`), premier relevé HACCP (`add_temperature`, garde-fou
  anti-donnée-inventée rappelé, equipment_id jamais deviné). Une confirmation
  par chantier ; pas d'outil MCP de création d'établissement (naît à
  l'inscription FoodEatUp) — documenté honnêtement en Étape 0.

## 0.8.0 — 2026-07-06

- Intégration de 3 skills Apache 2.0 du pack small-business
  d'anthropics/knowledge-work-plugins (LICENSE dans chaque dossier,
  provenance dans ATTRIBUTIONS.md à la racine du plugin) :
  `margin-analyzer` (unit economics par produit, benchmarks sectoriels),
  `handle-complaint` (réclamation client de bout en bout) et `price-check`
  (marge par produit + 3 scénarios de prix) — complètent
  analyse-rentabilite-carte et service-salle.
- Chaque skill : mention MCP/KB en fin de description + section « Adaptation
  Rapido » (QuickBooks/PayPal/HubSpot/Slack… → équivalents FoodEatUp/CRM ;
  seuils maison de la KB prioritaires sur les défauts US).

## 0.7.0 — 2026-07-06

- Passe de portabilité : devise lue depuis la KB (défaut euros signalé), règles TVA marquées France/défaut produit (la KB prime pour une autre juridiction).

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
