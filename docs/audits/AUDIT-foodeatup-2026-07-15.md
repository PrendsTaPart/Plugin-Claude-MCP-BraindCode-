# Audit MCP ↔ plugin — foodeatup — 2026-07-15

- Inventaire serveur : 111 outils (`docs/inventaires/foodeatup-tools.json`, source : introspection du MCP FoodEatUp connecté (session Claude Code, 2026-07-15)).
- Couverture : **85/111 outils exploités (77 %)** par les skills du plugin.
- Orphelins : **26** · Références mortes suspectes : **11**.

## 1. Références mortes (PRIORITÉ 1 — drift, bug silencieux)

Identifiants à **verbe d'action**, cités par le plugin mais absents de **tout** inventaire connu → drift probable à corriger. ⚠️ Serveurs secondaires déclarés sans inventaire encore construit : **rapidocrm** — un identifiant ci-dessous peut en venir ; confirmer en auditant ces serveurs.

| Identifiant cité | Fichiers |
|---|---|
| `get_contact` | foodeatup/skills/handle-complaint/SKILL.md |
| `get_entreprise` | foodeatup/skills/handle-complaint/SKILL.md, foodeatup/skills/margin-analyzer/SKILL.md, foodeatup/skills/price-check/SKILL.md |
| `get_historique_prospect` | foodeatup/skills/handle-complaint/SKILL.md, foodeatup/skills/margin-analyzer/SKILL.md, foodeatup/skills/price-check/SKILL.md |
| `get_loyalty_points` | foodeatup/skills/handle-complaint/SKILL.md |
| `get_pipeline` | foodeatup/skills/handle-complaint/SKILL.md, foodeatup/skills/margin-analyzer/SKILL.md, foodeatup/skills/price-check/SKILL.md |
| `get_revenue_summary` | foodeatup/skills/handle-complaint/SKILL.md, foodeatup/skills/margin-analyzer/SKILL.md, foodeatup/skills/margin-analyzer/reference/gotchas.md, foodeatup/skills/price-check/SKILL.md |
| `list_depenses` | foodeatup/skills/handle-complaint/SKILL.md, foodeatup/skills/margin-analyzer/SKILL.md, foodeatup/skills/margin-analyzer/reference/gotchas.md, foodeatup/skills/price-check/SKILL.md |
| `list_devis` | foodeatup/skills/handle-complaint/SKILL.md, foodeatup/skills/margin-analyzer/SKILL.md, foodeatup/skills/price-check/SKILL.md |
| `list_factures` | foodeatup/skills/handle-complaint/SKILL.md, foodeatup/skills/margin-analyzer/SKILL.md, foodeatup/skills/margin-analyzer/reference/gotchas.md, foodeatup/skills/price-check/SKILL.md |
| `schedule_email` | foodeatup/skills/handle-complaint/SKILL.md, foodeatup/skills/margin-analyzer/SKILL.md, foodeatup/skills/price-check/SKILL.md |
| `send_email` | foodeatup/skills/handle-complaint/SKILL.md, foodeatup/skills/margin-analyzer/SKILL.md, foodeatup/skills/price-check/SKILL.md |

## 2. Outils orphelins (valeur dormante — exposés, cités par aucun skill)

26 outils, groupés par famille fonctionnelle :

### category (3)

| Outil | Description |
|---|---|
| `create_category` | Crée une catégorie d'ingrédient, de produit ou de recette (paramètre type). Les catégorie… |
| `delete_category` | Supprime une catégorie propre à un établissement (les catégories globales sont protégées). |
| `update_category` | Modifie une catégorie d'un établissement. |

### client (4)

| Outil | Description |
|---|---|
| `create_client` | Crée un client pour un établissement. |
| `delete_client` | Supprime un client d'un établissement. Action irréversible. |
| `list_clients` | Liste les clients d'un établissement. Filtres : recherche, statut. |
| `update_client` | Modifie un client d'un établissement. |

### dish (3)

| Outil | Description |
|---|---|
| `create_dish` | Ajoute un plat à la carte d'un établissement. |
| `create_dish_category` | Crée une catégorie de PLAT (carte / vitrine), éventuellement en sous-catégorie. Apparaît … |
| `delete_dish` | Supprime un plat de la carte d'un établissement. Action irréversible. |

### employee (3)

| Outil | Description |
|---|---|
| `delete_employee` | Supprime un employé et son planning. Action irréversible. |
| `get_employee` | Retourne les détails complets d'un employé (profil, rôle, planning, contrat). |
| `update_employee` | Modifie les informations d'un employé (prénom, nom, email, téléphone, rôle). |

### ingredient (4)

| Outil | Description |
|---|---|
| `create_ingredient` | Crée un nouvel ingrédient pour un établissement. |
| `delete_ingredient` | Supprime un ingrédient d'un établissement. Action irréversible. |
| `get_ingredient` | Retourne le détail d'un ingrédient d'un établissement. |
| `update_ingredient` | Modifie un ingrédient (nom, unité, prix, stock, seuil, valeurs nutritionnelles). |

### invoice (1)

| Outil | Description |
|---|---|
| `get_invoice` | Retourne le détail complet d'une facture (lignes incluses). |

### product (3)

| Outil | Description |
|---|---|
| `create_product` | Crée un nouveau produit dans le menu d'un établissement. |
| `delete_product` | Supprime un produit du catalogue d'un établissement. Action irréversible. |
| `get_product` | Retourne le détail d'un produit du catalogue d'un établissement. |

### recipe (1)

| Outil | Description |
|---|---|
| `delete_recipe` | Supprime une recette d'un établissement (corbeille / soft delete). |

### supplier (1)

| Outil | Description |
|---|---|
| `create_supplier` | Crée un nouveau fournisseur pour un établissement. |

### tva (2)

| Outil | Description |
|---|---|
| `create_tva` | Crée un taux de TVA pour un établissement. |
| `list_tva` | Liste les taux de TVA configurés pour un établissement. |

### unit (1)

| Outil | Description |
|---|---|
| `list_units` | Liste les unités de mesure disponibles (référentiel global, lecture seule). |

## 3. Couverture par skill

| Skill | Outils serveur cités |
|---|---|
| `analyse-rentabilite-carte` | `get_recipe`, `list_dishes`, `list_orders`, `list_recipes`, `list_top_productions`, `update_dish`, `update_recipe` |
| `briefing-du-jour` | `create_notification`, `floor_plan_status`, `list_haccp_reception`, `list_haccp_temperatures`, `list_low_stocks`, `list_notifications`, `list_plannings`, `list_production_alerts`, `list_production_plans`, `list_reservations`, `reservation_availability` |
| `carte-vitrine` | `get_recipe`, `import_storefront_menu`, `list_categories`, `list_dishes`, `update_dish`, `update_recipe` |
| `coordination-cuisine` | `get_order`, `list_orders`, `search_entities`, `update_kds_item_status`, `update_order_status` |
| `gestion-commandes` | `checkin_reservation`, `create_invoice`, `create_order`, `create_quote`, `floor_plan_status`, `get_order`, `get_quote`, `list_dishes`, `list_orders`, `list_products`, `list_quotes`, `search_entities`, `seat_waitlist`, `update_invoice_status`, `update_order_status`, `update_quote_status` |
| `haccp-conformite-quotidienne` | `add_temperature`, `create_haccp_label`, `create_haccp_reception`, `create_haccp_tracabilite`, `create_hygiene_checklist_validation`, `list_cleaning_actions`, `list_cleaning_zones`, `list_haccp_labels`, `list_haccp_temperatures`, `list_haccp_tracabilite`, `list_hygiene_checklists`, `record_cleaning_action`, `search_entities` |
| `handle-complaint` | `finance_summary`, `get_client`, `get_order`, `list_expenses`, `list_invoices`, `list_orders` |
| `margin-analyzer` | `finance_summary`, `get_recipe`, `list_expenses`, `list_invoices`, `list_orders` |
| `onboarding-restaurateur` | `add_temperature`, `create_employee`, `create_employee_contract`, `create_hygiene_checklist_validation`, `create_table`, `create_zone`, `floor_plan_status`, `import_storefront_menu`, `list_categories`, `list_dishes`, `list_employees`, `list_haccp_temperatures`, `list_hygiene_checklists`, `list_tables`, `list_zones` |
| `planning-equipe` | `approve_leave`, `assign_task`, `create_employee_contract`, `create_shift`, `list_attendances`, `list_employee_contracts`, `list_employee_documents`, `list_employees`, `list_leaves`, `list_plannings`, `reject_leave`, `update_employee_schedule` |
| `price-check` | `finance_summary`, `get_recipe`, `list_expenses`, `list_invoices`, `list_orders`, `search_entities`, `update_dish`, `update_product` |
| `production-stock` | `adjust_stock`, `create_production_plan`, `get_production_ingredients`, `list_low_stocks`, `list_production_alerts`, `list_production_plans`, `list_stocks`, `search_entities` |
| `reappro-fournisseurs` | `adjust_stock`, `create_expense`, `create_haccp_reception`, `create_supplier_order`, `get_expense`, `get_supplier`, `list_deliveries`, `list_low_stocks`, `list_products`, `list_suppliers`, `search_entities` |
| `recette-cout-marge` | `create_recipe`, `get_recipe`, `list_recipes`, `search_entities` |
| `service-salle` | `add_waitlist`, `cancel_reservation`, `checkin_reservation`, `confirm_reservation`, `create_order`, `create_reservation`, `floor_plan_status`, `list_waitlist`, `no_show_reservation`, `reservation_availability`, `search_entities`, `seat_waitlist`, `update_table_status` |

## 4. Delta paramètres (vs inventaire précédent)

_Premier inventaire ou aucun précédent fourni_ — pas de comparaison possible. Les prochains runs compareront les `params_required`.
