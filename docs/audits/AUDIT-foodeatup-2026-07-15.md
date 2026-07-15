# Audit MCP ↔ plugin — foodeatup — 2026-07-15

- Inventaire serveur : 164 outils (`docs/inventaires/foodeatup-tools.json`, source : 111 outils introspectés en direct (session) + 53 outils relevés dans la console d'autorisations MCP FoodEatUp (foodeatup.com/api/mcp, 2026-07-15) — absents du registre de session, schémas à introspecter quand le connecteur les exposera.).
- Couverture : **86/164 outils exploités (52 %)** par les skills du plugin.
- Orphelins : **78** · Références mortes suspectes : **11**.

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

78 outils, groupés par famille fonctionnelle :

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

### client (4)

| Outil | Description |
|---|---|
| `create_client` | Crée un client pour un établissement. |
| `delete_client` | Supprime un client d'un établissement. Action irréversible. |
| `list_clients` | Liste les clients d'un établissement. Filtres : recherche, statut. |
| `update_client` | Modifie un client d'un établissement. |

### daily (1)

| Outil | Description |
|---|---|
| `get_daily_brief` | Brief quotidien de l'établissement. |

### delivery (2)

| Outil | Description |
|---|---|
| `list_delivery_zones` | Liste les zones de livraison. |
| `upsert_delivery_zone` | Crée/met à jour une zone de livraison. |

### dish (3)

| Outil | Description |
|---|---|
| `create_dish` | Ajoute un plat à la carte d'un établissement. |
| `create_dish_category` | Crée une catégorie de PLAT (carte / vitrine), éventuellement en sous-catégorie. Apparaît … |
| `delete_dish` | Supprime un plat de la carte d'un établissement. Action irréversible. |

### domain (1)

| Outil | Description |
|---|---|
| `get_domain_status` | Statut du nom de domaine du site vitrine. |

### employee (3)

| Outil | Description |
|---|---|
| `delete_employee` | Supprime un employé et son planning. Action irréversible. |
| `get_employee` | Retourne les détails complets d'un employé (profil, rôle, planning, contrat). |
| `update_employee` | Modifie les informations d'un employé (prénom, nom, email, téléphone, rôle). |

### event (1)

| Outil | Description |
|---|---|
| `update_event_request_status` | Change le statut d'une demande d'événement privé. |

### gift (2)

| Outil | Description |
|---|---|
| `check_gift_card` | Vérifie une carte cadeau (solde/validité). |
| `list_gift_cards` | Liste les cartes cadeaux. |

### happy (2)

| Outil | Description |
|---|---|
| `list_happy_hours` | Liste les happy hours. |
| `upsert_happy_hour` | Crée/met à jour un happy hour. |

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

### job (3)

| Outil | Description |
|---|---|
| `create_job_offer` | Crée une offre d'emploi. |
| `list_job_applications` | Liste les candidatures reçues. |
| `update_job_offer` | Met à jour une offre d'emploi. |

### loyalty (5)

| Outil | Description |
|---|---|
| `get_loyalty_account` | Compte de fidélité d'un client. |
| `get_loyalty_program` | Programme de fidélité de l'établissement. |
| `list_loyalty_rewards` | Liste les récompenses de fidélité. |
| `update_loyalty_program` | Met à jour le programme de fidélité. |
| `upsert_loyalty_reward` | Crée/met à jour une récompense de fidélité. |

### page (1)

| Outil | Description |
|---|---|
| `get_page_content` | Contenu d'une page du site vitrine. |

### point (1)

| Outil | Description |
|---|---|
| `adjust_points` | Ajuste les points de fidélité d'un client. |

### pos (7)

| Outil | Description |
|---|---|
| `close_pos_session` | Clôture une session de caisse (rapport Z). |
| `get_pos_report` | Rapport de caisse (X/Z). |
| `get_pos_session` | Détail d'une session de caisse. |
| `list_pos_payments` | Liste les encaissements d'une session de caisse. |
| `list_pos_tabs` | Liste les additions/tabs de caisse ouvertes. |
| `open_pos_session` | Ouvre une session de caisse (POS). |
| `record_pos_payment` | Enregistre un encaissement en caisse. |

### private (1)

| Outil | Description |
|---|---|
| `list_private_event_requests` | Liste les demandes d'événements privés. |

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

### redemption (2)

| Outil | Description |
|---|---|
| `list_redemptions` | Liste les utilisations de récompenses de fidélité. |
| `validate_redemption` | Valide l'utilisation d'une récompense de fidélité. |

### review (3)

| Outil | Description |
|---|---|
| `list_reviews` | Liste les avis clients. |
| `moderate_review` | Modère un avis client. |
| `reply_review` | Répond à un avis client. |

### section (1)

| Outil | Description |
|---|---|
| `update_section` | Met à jour une section de page du site vitrine. |

### site (10)

| Outil | Description |
|---|---|
| `add_site_page` | Ajoute une page au site vitrine. |
| `apply_site_template` | Applique un modèle de site vitrine. |
| `get_site_pages` | Liste les pages du site vitrine. |
| `get_site_stats` | Statistiques de fréquentation du site vitrine. |
| `get_site_status` | Statut de publication du site vitrine. |
| `list_site_leads` | Leads capturés via le site vitrine. |
| `list_site_templates` | Modèles de site vitrine disponibles. |
| `publish_site` | Publie le site vitrine. |
| `set_site_theme` | Définit le thème (couleurs/typo) du site vitrine. |
| `toggle_site_page` | Active/désactive une page du site vitrine. |

### station (1)

| Outil | Description |
|---|---|
| `get_station_load` | Charge d'un poste (station) en cuisine. |

### supplier (1)

| Outil | Description |
|---|---|
| `create_supplier` | Crée un nouveau fournisseur pour un établissement. |

### survey (2)

| Outil | Description |
|---|---|
| `get_survey_results` | Résultats d'un sondage. |
| `list_surveys` | Liste les sondages. |

### tva (2)

| Outil | Description |
|---|---|
| `create_tva` | Crée un taux de TVA pour un établissement. |
| `list_tva` | Liste les taux de TVA configurés pour un établissement. |

### unit (1)

| Outil | Description |
|---|---|
| `list_units` | Liste les unités de mesure disponibles (référentiel global, lecture seule). |

### wheel (2)

| Outil | Description |
|---|---|
| `get_wheel_stats` | Statistiques des jeux de roue. |
| `list_wheel_games` | Liste les jeux de roue (wheel). |

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
| `production-stock` | `adjust_stock`, `create_production_plan`, `get_production_ingredients`, `list_low_stocks`, `list_production_alerts`, `list_production_plans`, `list_stocks`, `search_entities`, `validate_production` |
| `reappro-fournisseurs` | `adjust_stock`, `create_expense`, `create_haccp_reception`, `create_supplier_order`, `get_expense`, `get_supplier`, `list_deliveries`, `list_low_stocks`, `list_products`, `list_suppliers`, `search_entities` |
| `recette-cout-marge` | `create_recipe`, `get_recipe`, `list_recipes`, `search_entities` |
| `service-salle` | `add_waitlist`, `cancel_reservation`, `checkin_reservation`, `confirm_reservation`, `create_order`, `create_reservation`, `floor_plan_status`, `list_waitlist`, `no_show_reservation`, `reservation_availability`, `search_entities`, `seat_waitlist`, `update_table_status` |

## 4. Delta paramètres (vs inventaire précédent)

_Premier inventaire ou aucun précédent fourni_ — pas de comparaison possible. Les prochains runs compareront les `params_required`.
