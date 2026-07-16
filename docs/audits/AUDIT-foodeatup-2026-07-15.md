# Audit MCP ↔ plugin — foodeatup — 2026-07-15

- Inventaire serveur : 164 outils (`docs/inventaires/foodeatup-tools.json`, source : 135 outils introspectés (111 initiaux + 24 familles prioritaires) + 8 outils parqués réintrospectés (site/caisse/avis, 2026-07-15, F3) = 143/164 ; 21 restants à réintrospecter (recrutement, offre, sondages/roue, divers).).
- Couverture : **143/164 outils exploités (87 %)** par les skills du plugin.
- Orphelins : **21** · Références mortes suspectes : **12**.

## 1. Références mortes (PRIORITÉ 1 — drift, bug silencieux)

Identifiants à **verbe d'action**, cités par le plugin mais absents de **tout** inventaire connu → drift probable à corriger. ⚠️ Serveurs secondaires déclarés sans inventaire encore construit : **rapidocrm** — un identifiant ci-dessous peut en venir ; confirmer en auditant ces serveurs.

| Identifiant cité | Fichiers |
|---|---|
| `enregistrer_prospect` | foodeatup/skills/site-vitrine-foodeatup/SKILL.md |
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

21 outils, groupés par famille fonctionnelle :

### application (1)

| Outil | Description |
|---|---|
| `update_application_status` | Change le statut d'une candidature. |

### beverage (3)

| Outil | Description |
|---|---|
| `list_beverages` | Liste les boissons (carte des boissons). |
| `remove_beverage_item` | Retire une boisson de la carte. |
| `upsert_beverage_item` | Crée/met à jour une boisson. |

### category (3)

| Outil | Description |
|---|---|
| `create_category` | Crée une catégorie d'ingrédient, de produit ou de recette (paramètre type). Les catégorie… |
| `delete_category` | Supprime une catégorie propre à un établissement (les catégories globales sont protégées). |
| `update_category` | Modifie une catégorie d'un établissement. |

### daily (1)

| Outil | Description |
|---|---|
| `get_daily_brief` | Brief quotidien de l'établissement. |

### delivery (2)

| Outil | Description |
|---|---|
| `list_delivery_zones` | Liste les zones de livraison. |
| `upsert_delivery_zone` | Crée/met à jour une zone de livraison. |

### event (1)

| Outil | Description |
|---|---|
| `update_event_request_status` | Change le statut d'une demande d'événement privé. |

### happy (2)

| Outil | Description |
|---|---|
| `list_happy_hours` | Liste les happy hours. |
| `upsert_happy_hour` | Crée/met à jour un happy hour. |

### job (3)

| Outil | Description |
|---|---|
| `create_job_offer` | Crée une offre d'emploi. |
| `list_job_applications` | Liste les candidatures reçues. |
| `update_job_offer` | Met à jour une offre d'emploi. |

### loyalty (1)

| Outil | Description |
|---|---|
| `get_loyalty_account` | Compte de fidélité d'un client. |

### private (1)

| Outil | Description |
|---|---|
| `list_private_event_requests` | Liste les demandes d'événements privés. |

### site (1)

| Outil | Description |
|---|---|
| `get_site_pages` | Liste les pages du site vitrine. |

### station (1)

| Outil | Description |
|---|---|
| `get_station_load` | Charge d'un poste (station) en cuisine. |

### unit (1)

| Outil | Description |
|---|---|
| `list_units` | Liste les unités de mesure disponibles (référentiel global, lecture seule). |

## 3. Couverture par skill

| Skill | Outils serveur cités |
|---|---|
| `analyse-rentabilite-carte` | `get_recipe`, `list_dishes`, `list_orders`, `list_recipes`, `list_top_productions`, `update_dish`, `update_recipe` |
| `briefing-du-jour` | `create_notification`, `floor_plan_status`, `list_haccp_reception`, `list_haccp_temperatures`, `list_low_stocks`, `list_notifications`, `list_plannings`, `list_production_alerts`, `list_production_plans`, `list_reservations`, `reservation_availability` |
| `caisse-du-jour` | `close_pos_session`, `finance_summary`, `get_pos_report`, `get_pos_session`, `list_employees`, `list_pos_payments`, `list_pos_tabs`, `open_pos_session`, `record_pos_payment` |
| `carte-vitrine` | `create_dish`, `create_dish_category`, `delete_dish`, `get_recipe`, `import_storefront_menu`, `list_categories`, `list_dishes`, `update_dish`, `update_recipe` |
| `coordination-cuisine` | `get_order`, `list_orders`, `search_entities`, `update_kds_item_status`, `update_order_status` |
| `fidelite-restaurant` | `adjust_points`, `check_gift_card`, `get_loyalty_program`, `get_survey_results`, `get_wheel_stats`, `list_dishes`, `list_gift_cards`, `list_loyalty_rewards`, `list_redemptions`, `list_surveys`, `list_wheel_games`, `search_entities`, `update_loyalty_program`, `upsert_loyalty_reward`, `validate_redemption` |
| `gestion-commandes` | `checkin_reservation`, `create_invoice`, `create_order`, `create_quote`, `floor_plan_status`, `get_invoice`, `get_order`, `get_quote`, `list_dishes`, `list_invoices`, `list_orders`, `list_products`, `list_quotes`, `search_entities`, `seat_waitlist`, `update_invoice_status`, `update_order_status`, `update_quote_status` |
| `haccp-conformite-quotidienne` | `add_temperature`, `create_haccp_label`, `create_haccp_reception`, `create_haccp_tracabilite`, `create_hygiene_checklist_validation`, `list_cleaning_actions`, `list_cleaning_zones`, `list_haccp_labels`, `list_haccp_temperatures`, `list_haccp_tracabilite`, `list_hygiene_checklists`, `record_cleaning_action`, `search_entities` |
| `handle-complaint` | `finance_summary`, `get_client`, `get_order`, `list_expenses`, `list_invoices`, `list_orders`, `list_reviews`, `moderate_review`, `reply_review` |
| `margin-analyzer` | `finance_summary`, `get_recipe`, `list_expenses`, `list_invoices`, `list_orders` |
| `onboarding-restaurateur` | `add_temperature`, `create_employee`, `create_employee_contract`, `create_hygiene_checklist_validation`, `create_table`, `create_tva`, `create_zone`, `floor_plan_status`, `import_storefront_menu`, `list_categories`, `list_dishes`, `list_employees`, `list_haccp_temperatures`, `list_hygiene_checklists`, `list_tables`, `list_tva`, `list_zones` |
| `planning-equipe` | `approve_leave`, `assign_task`, `create_employee`, `create_employee_contract`, `create_shift`, `delete_employee`, `get_employee`, `list_attendances`, `list_employee_contracts`, `list_employee_documents`, `list_employees`, `list_leaves`, `list_plannings`, `reject_leave`, `update_employee`, `update_employee_schedule` |
| `price-check` | `finance_summary`, `get_recipe`, `list_expenses`, `list_invoices`, `list_orders`, `search_entities`, `update_dish`, `update_product` |
| `production-stock` | `adjust_stock`, `create_production_plan`, `get_production_ingredients`, `list_low_stocks`, `list_production_alerts`, `list_production_plans`, `list_stocks`, `search_entities`, `validate_production` |
| `reappro-fournisseurs` | `adjust_stock`, `create_expense`, `create_haccp_reception`, `create_product`, `create_supplier`, `create_supplier_order`, `delete_product`, `get_expense`, `get_product`, `get_supplier`, `list_deliveries`, `list_low_stocks`, `list_products`, `list_suppliers`, `search_entities`, `update_product` |
| `recette-cout-marge` | `create_ingredient`, `create_recipe`, `delete_ingredient`, `delete_recipe`, `get_ingredient`, `get_recipe`, `list_recipes`, `search_entities`, `update_ingredient` |
| `service-salle` | `add_waitlist`, `cancel_reservation`, `checkin_reservation`, `confirm_reservation`, `create_client`, `create_order`, `create_reservation`, `delete_client`, `floor_plan_status`, `get_client`, `list_clients`, `list_waitlist`, `no_show_reservation`, `reservation_availability`, `search_entities`, `seat_waitlist`, `update_client`, `update_table_status` |
| `site-vitrine-foodeatup` | `add_site_page`, `apply_site_template`, `get_domain_status`, `get_page_content`, `get_site_stats`, `get_site_status`, `get_wheel_stats`, `list_site_leads`, `list_site_templates`, `publish_site`, `set_site_theme`, `toggle_site_page`, `update_section` |

## 4. Delta paramètres (vs inventaire précédent)

_Premier inventaire ou aucun précédent fourni_ — pas de comparaison possible. Les prochains runs compareront les `params_required`.
