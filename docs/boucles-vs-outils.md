# Cartographie : 8 boucles du livre blanc × 264 outils MCP FoodEatUp

> Source unique : `docs/inventaires/foodeatup-tools-live.txt` (liste réelle des
> outils exposés par le serveur MCP, session du 2026-10-19 — 264 outils, dont
> 87 ajoutés depuis le 2026-07-28, décrits d'après leur schéma live) croisée avec
> l'introspection `docs/inventaires/foodeatup-tools.json` (2026-07-15, 164/177 ;
> les 13 outils non introspectés sont marqués ⁽ⁿⁱ⁾). Chaque outil est affecté à
> **une et une seule** boucle — l'exhaustivité est vérifiée par script : toute
> régénération échoue si un outil manque ou est affecté deux fois.

Légende « confirm requis » : **serveur** = le serveur MCP exige `confirm:true` ;
**hook P2.1** = intercepté par le garde-fou PreToolUse du plugin
`foodeatup-boucles` (confirmation humaine forcée, non contournable par le
modèle) ; **garde native** = plafond/contrainte côté serveur.

## ① Configuration — 21 outils (8 lecture / 13 écriture)

Référentiels de l'établissement : catégories, TVA, unités, zones, tables, équipements. `create_equipment` crée les équipements froids dont les relevés vivent en boucle ④ — la création est un acte de paramétrage, il va donc ici.

| Outil | Lecture/Écriture | Confirm requis | Commentaire |
|---|---|---|---|
| `add_closure_period` | écriture | — | Déclare une fermeture exceptionnelle ; les réservations prises ne sont pas annulées. |
| `create_category` | écriture | — | Crée une catégorie d'ingrédient, de produit ou de recette (paramètre type). Les catégories de PLAT se gèrent d… |
| `create_dish_category` | écriture | — | Crée une catégorie de PLAT (carte / vitrine), éventuellement en sous-catégorie. Apparaît dans la carte et la v… |
| `create_equipment` ⁽ⁿⁱ⁾ | écriture | — | non introspecté — nom et présence relevés sur le serveur live |
| `create_table` | écriture | — | Crée une table dans le plan de salle. |
| `create_tva` | écriture | — | Crée un taux de TVA pour un établissement. |
| `create_zone` | écriture | — | Crée une zone du plan de salle. |
| `delete_category` | écriture | hook P2.1 | Supprime une catégorie propre à un établissement (les catégories globales sont protégées). |
| `delete_closure_period` | écriture | serveur, hook P2.1 | Supprime une fermeture exceptionnelle (le restaurant redevient réservable). |
| `delete_dish_category` | écriture | serveur, hook P2.1 | Supprime une catégorie de plat ; refusé s'il reste des plats actifs sauf reassign_to. |
| `get_opening_hours` | lecture | — | Horaires de la semaine (midi/soir) et fermetures à venir. |
| `list_categories` | lecture | — | Liste les catégories d'un établissement (y compris les catégories globales). |
| `list_closure_periods` | lecture | — | Fermetures exceptionnelles (à venir par défaut). |
| `list_dish_categories` | lecture | — | Catégories de PLATS (parent, visibilité vitrine, nb de plats) — à lire avant create_dish_category. |
| `list_tables` | lecture | — | Liste les tables avec leur statut temps réel. Filtre : statut. |
| `list_tva` | lecture | — | Liste les taux de TVA configurés pour un établissement. |
| `list_units` | lecture | — | Liste les unités de mesure disponibles (référentiel global, lecture seule). |
| `list_zones` | lecture | — | Liste les zones du plan de salle (Salle, Terrasse...). |
| `set_opening_hours` | écriture | hook P2.1 | REMPLACE les horaires de la semaine (jour absent = fermé) ; pilote réservations, site et agent vocal. |
| `update_category` | écriture | — | Modifie une catégorie d'un établissement. |
| `update_dish_category` | écriture | — | Modifie une catégorie de plat (nom, parent, description, visibilité vitrine), journalisée. |

## ② Équipe — 23 outils (10 lecture / 13 écriture)

Cycle RH complet : embauche, contrats, planning, pointages, congés, recrutement.

| Outil | Lecture/Écriture | Confirm requis | Commentaire |
|---|---|---|---|
| `approve_leave` | écriture | — | Approuve une demande de congé en attente. |
| `assign_task` | écriture | — | Assigne une tâche à un employé (date/heure/priorité optionnelles). |
| `create_employee` | écriture | — | Crée un nouvel employé pour un établissement avec son planning optionnel. |
| `create_employee_contract` | écriture | hook P2.1 | Crée un contrat de travail pour un employé. |
| `create_job_offer` | écriture | — | Crée une offre d'emploi. |
| `create_sales_target` | écriture | serveur | Crée un objectif de vente ou un challenge (CA, tickets, panier, couverts, quantité d'un plat). |
| `create_shift` | écriture | — | Crée un shift (créneau de travail) pour un employé un jour donné, et le publie. |
| `delete_employee` | écriture | hook P2.1 | Supprime un employé et son planning. Action irréversible. |
| `get_employee` | lecture | — | Retourne les détails complets d'un employé (profil, rôle, planning, contrat). |
| `list_attendances` | lecture | — | Liste les pointages (clock in/out) des employés sur une période. |
| `list_employee_contracts` | lecture | — | Liste les contrats des employés d'un établissement. Filtre : employé. |
| `list_employee_documents` | lecture | — | Liste les documents administratifs des employés. Filtre : employé. |
| `list_employees` | lecture | — | Liste tous les employés d'un établissement. |
| `list_job_applications` | lecture | — | Liste les candidatures reçues. |
| `list_leaves` | lecture | — | Liste les demandes de congés des employés. Filtre par statut. |
| `list_plannings` | lecture | — | Liste les shifts (planning des horaires) de l'équipe pour une semaine, avec heures et coût estimé. |
| `list_sales_targets` | lecture | — | Objectifs et challenges avec progression et classement des serveurs. |
| `list_tasks` | lecture | — | Tâches d'équipe (employé, date, priorité, état, shift) — repérer les doublons avant assign_task. |
| `reject_leave` | écriture | — | Refuse une demande de congé en attente. |
| `update_application_status` | écriture | — | Change le statut d'une candidature. |
| `update_employee` | écriture | — | Modifie les informations d'un employé (prénom, nom, email, téléphone, rôle). |
| `update_employee_schedule` | écriture | hook P2.1 | Remplace entièrement le planning hebdomadaire d'un employé. |
| `update_job_offer` | écriture | — | Met à jour une offre d'emploi. |

## ③ Stock / Production — 48 outils (22 lecture / 26 écriture)

Chaîne amont : ingrédients, produits, recettes, plats, production, cuisine (KDS/stations) et achats fournisseurs. Les plats pourraient aller en ① (paramétrage de carte) : ils vont ici car leur coût/marge dépend des recettes et du stock. `list_deliveries` = livraisons **fournisseurs** (introspection), donc ici et pas en ⑤.

| Outil | Lecture/Écriture | Confirm requis | Commentaire |
|---|---|---|---|
| `adjust_stock` | écriture | — | Ajuste la quantité en stock d'un produit du catalogue (définir ou incrémenter). |
| `bulk_update_ingredients` | écriture | serveur | Modifie des ingrédients en masse (prix, unité, seuil, coefficient, allergènes) — tout ou rien, aperçu. |
| `create_dish` | écriture | — | Ajoute un plat à la carte d'un établissement. |
| `create_ingredient` | écriture | — | Crée un nouvel ingrédient pour un établissement. |
| `create_orders_from_shopping_list` | écriture | serveur | Transforme la liste de courses en commandes fournisseurs réelles (une par fournisseur). |
| `create_product` | écriture | — | Crée un nouveau produit dans le menu d'un établissement. |
| `create_production_plan` | écriture | — | Planifie une production (plat ou recette) pour un établissement. |
| `create_recipe` | écriture | — | Crée une recette COMPLÈTE (ingrédients + étapes + catégories) pour un établissement. |
| `create_supplier` | écriture | — | Crée un nouveau fournisseur pour un établissement. |
| `create_supplier_order` | écriture | — | Crée une commande fournisseur. |
| `delete_dish` | écriture | hook P2.1 | Supprime un plat de la carte d'un établissement. Action irréversible. |
| `delete_ingredient` | écriture | hook P2.1 | Supprime un ingrédient d'un établissement. Action irréversible. |
| `delete_product` | écriture | hook P2.1 | Supprime un produit du catalogue d'un établissement. Action irréversible. |
| `delete_production_plan` | écriture | serveur, hook P2.1 | Supprime un plan de production non réalisé (et ses courses/livraisons en attente). |
| `delete_recipe` | écriture | hook P2.1 | Supprime une recette d'un établissement (corbeille / soft delete). |
| `fill_ingredient_from_ean` | écriture | — | Complète un ingrédient depuis OpenFoodFacts, champs vides uniquement. |
| `get_cadencier` | lecture | — | Cadencier d'un fournisseur : colis habituels / proposés par jour de livraison. |
| `get_dish_portions` | lecture | — | Portions d'un plat suivi : solde, vendables aujourd'hui, mouvements. |
| `get_ingredient` | lecture | — | Retourne le détail d'un ingrédient d'un établissement. |
| `get_product` | lecture | — | Retourne le détail d'un produit du catalogue d'un établissement. |
| `get_production_ingredients` | lecture | — | Retourne les ingrédients nécessaires pour un plan de production (statut suffisant/manquant). |
| `get_recipe` | lecture | — | Retourne le détail d'une recette d'un établissement. |
| `get_shopping_list` | lecture | — | Liste de courses depuis une prévision de couverts ou de plats, groupée par fournisseur. |
| `get_station_load` | lecture | — | Charge d'un poste (station) en cuisine. |
| `get_supplier` | lecture | — | Retourne les détails d'un fournisseur spécifique. |
| `list_beverages` | lecture | — | Liste les boissons (carte des boissons). |
| `list_deliveries` | lecture | — | Liste les livraisons fournisseurs d'un établissement. |
| `list_dishes` | lecture | — | Liste les plats de la carte d'un établissement. |
| `list_ingredients` | lecture | — | Liste les ingrédients d'un établissement. Filtres : recherche par nom, type. |
| `list_low_stocks` | lecture | — | Liste les articles en stock dont le niveau est bas (is_low = true). |
| `list_production_alerts` | lecture | — | Liste les ingrédients manquants pour les productions planifiées dans les prochains jours. |
| `list_production_plans` | lecture | — | Liste les plans de production sur une période donnée. |
| `list_products` | lecture | — | Liste tous les produits d'un établissement. |
| `list_recipes` | lecture | — | Liste toutes les recettes d'un établissement. |
| `list_stocks` | lecture | — | Liste tous les articles en stock d'un établissement. |
| `list_suppliers` | lecture | — | Liste tous les fournisseurs d'un établissement. |
| `list_top_productions` | lecture | — | Liste les plats/recettes les plus produits sur une période. |
| `lookup_ean` | lecture | — | Recherche un code-barres : catalogue du restaurant puis OpenFoodFacts. |
| `remove_beverage_item` | écriture | — | Retire une boisson de la carte. |
| `send_cadencier` | écriture | serveur | Envoie des cases du cadencier à la liste de courses. |
| `set_dish_portions` | écriture | — | Suivi des portions : activation, inventaire compté, perte motivée, seuil. |
| `update_dish` | écriture | — | Modifie un plat de la carte d'un établissement. |
| `update_ingredient` | écriture | — | Modifie un ingrédient (nom, unité, prix, stock, seuil, valeurs nutritionnelles). |
| `update_kds_item_status` | écriture | — | Change le statut cuisine d'un plat d'une commande (pending → in_progress → ready → served). Écrans KDS. |
| `update_product` | écriture | — | Modifie un produit du catalogue (prix, unité, stock, description, nom, promotion). |
| `update_recipe` | écriture | — | Modifie une recette (ingredients/steps/catégories resynchronisés uniquement si fournis). |
| `upsert_beverage_item` | écriture | — | Crée/met à jour une boisson. |
| `validate_production` | écriture | — | Valide une production planifiée. |

## ④ HACCP — 26 outils (10 lecture / 16 écriture)

Conformité sanitaire : températures, étiquettes DLC, réceptions, traçabilité, checklists hygiène, plan de nettoyage.

| Outil | Lecture/Écriture | Confirm requis | Commentaire |
|---|---|---|---|
| `add_oil_change` | écriture | — | Changement d'huile (volume et type requis). |
| `add_oil_filtration` | écriture | — | Filtration d'huile, sans effacer une non-conformité. |
| `add_oil_test` | écriture | — | Test d'huile (testeur, bandelette, visuel) ; action corrective obligatoire au seuil critique. |
| `add_temperature` | écriture | — | Enregistre une mesure de température d'équipement (HACCP). |
| `add_thermal_reading` | écriture | — | Ajoute un relevé à un cycle thermique en cours. |
| `close_thermal_cycle` | écriture | — | Clôt un cycle ; conformité calculée par le serveur, correctif imposé en cas d'écart. |
| `complete_haccp_tracabilite` ⁽ⁿⁱ⁾ | écriture | — | non introspecté — nom et présence relevés sur le serveur live |
| `create_cleaning_zone` ⁽ⁿⁱ⁾ | écriture | — | non introspecté — nom et présence relevés sur le serveur live |
| `create_haccp_label` | écriture | — | Crée une étiquette HACCP (DLC). Le numéro de lot est généré automatiquement si absent. |
| `create_haccp_reception` | écriture | — | Crée un contrôle de réception HACCP manuel (arrivée fournisseur). |
| `create_haccp_tracabilite` | écriture | — | Crée un enregistrement de traçabilité HACCP. |
| `create_hygiene_checklist` ⁽ⁿⁱ⁾ | écriture | — | non introspecté — nom et présence relevés sur le serveur live |
| `create_hygiene_checklist_validation` | écriture | — | Enregistre une validation de checklist hygiène pour un modèle donné. |
| `list_cleaning_actions` | lecture | — | Liste les actions de nettoyage réalisées. Filtres : période. |
| `list_cleaning_zones` | lecture | — | Liste les zones de nettoyage (avec leurs postes) d'un établissement. |
| `list_fryers` | lecture | — | Friteuses actives et état de leur huile. |
| `list_haccp_labels` | lecture | — | Liste les étiquettes HACCP (DLC) d'un établissement. Filtre : statut. |
| `list_haccp_reception` | lecture | — | Liste les fiches de réception HACCP d'un établissement. |
| `list_haccp_temperatures` | lecture | — | Liste les relevés de températures HACCP. Filtres : période, équipement, type. |
| `list_haccp_tracabilite` | lecture | — | Liste les enregistrements de traçabilité HACCP d'un établissement. |
| `list_hygiene_checklists` | lecture | — | Liste les modèles de checklist hygiène HACCP d'un établissement. |
| `list_oil_logs` | lecture | — | Carnet d'huile (100 opérations par page). |
| `list_thermal_cycles` | lecture | — | Cycles thermiques et courbes de relevés. |
| `record_cleaning_action` | écriture | — | Enregistre une action de nettoyage réalisée sur un poste. |
| `start_thermal_cycle` | écriture | — | Démarre un refroidissement ou une remise en température (lot unique, température à cœur). |
| `update_hygiene_checklist` | écriture | — | Modifie un modèle de checklist (les validations passées ne changent pas). |

## ⑤ E-commerce / Vente & service — 72 outils (35 lecture / 37 écriture)

Tout ce qui vend et encaisse : commandes, réservations, salle, caisse (POS), zones de livraison, happy hours, site vitrine (canal de vente) et privatisations. `import_storefront_menu` écrit la carte **vitrine** : il va ici, la carte interne (plats/recettes) restant en ③.

| Outil | Lecture/Écriture | Confirm requis | Commentaire |
|---|---|---|---|
| `add_call_note` | écriture | — | Note de suivi signée sur un appel. |
| `add_site_page` | écriture | — | Ajoute une page au site vitrine. |
| `add_site_section` | écriture | — | Ajoute une section à une page du site. |
| `add_waitlist` | écriture | — | Ajoute un client à la file d'attente. |
| `apply_site_template` | écriture | serveur, hook P2.1 | Applique un modèle de site vitrine. |
| `bulk_update_dish_images` | écriture | serveur | Pose les photos de plats en lot (remplacement d'une photo = confirm). |
| `bulk_update_dishes` | écriture | serveur | Modifie des plats en masse (prix, TVA, catégorie, actif) — tout ou rien, aperçu. |
| `cancel_reservation` | écriture | — | Annule une réservation (libère la table). |
| `checkin_reservation` | écriture | — | Check-in : installe le client (table occupée) et crée la commande sur place. |
| `close_pos_session` | écriture | serveur, hook P2.1 | Clôture une session de caisse (rapport Z). |
| `confirm_reservation` | écriture | — | Confirme une réservation (assigne une table si besoin → table réservée). |
| `create_order` | écriture | — | Crée une commande (génère automatiquement facture + devis). Peut être liée à une table (sur place). |
| `create_payment_link` | écriture | hook P2.1 | Crée un lien de paiement Smile&Pay et peut l'envoyer au client par SMS/WhatsApp. |
| `create_reservation` | écriture | — | Crée une réservation de table (assigne la meilleure table libre, ou celle choisie / dans la zone demandée). |
| `create_site_page` | écriture | — | Crée une page libre du site, en brouillon. |
| `etat_borne` | lecture | — | État d'une borne et chiffres du jour (payées, panier moyen, abandons). |
| `floor_plan_status` | lecture | — | Vue d'ensemble temps réel du plan de salle : compteurs par statut + chaque table avec sa commande active. |
| `generate_callback_pitch` | lecture | — | Pitch de rappel préparé depuis la transcription (rien n'est envoyé). |
| `generer_qr_table` | lecture | — | Adresse, QR et lien d'impression des chevalets de table (n'invalide rien). |
| `get_call` | lecture | — | Détail d'un appel : transcription, notes de suivi. |
| `get_consolidated_pos_report` | lecture | — | Z consolidé de la maison (toutes caisses, écarts par poste). |
| `get_domain_status` | lecture | — | Statut du nom de domaine du site vitrine. |
| `get_hubrise_status` | lecture | — | Connecteur HubRise : connexion, plats sans sku_ref, commandes en attente. |
| `get_order` | lecture | — | Détail d'une commande (articles, totaux, facture/devis liés, table). |
| `get_page_content` | lecture | — | Contenu d'une page du site vitrine. |
| `get_payment_link_status` | lecture | — | Statut d'un lien de paiement. |
| `get_pos_report` | lecture | — | Rapport de caisse (X/Z). |
| `get_pos_session` | lecture | — | Détail d'une session de caisse. |
| `get_site_pages` | lecture | — | Liste les pages du site vitrine. |
| `get_site_stats` | lecture | — | Statistiques de fréquentation du site vitrine. |
| `get_site_status` | lecture | — | Statut de publication du site vitrine. |
| `get_smilepay_reconciliation` | lecture | — | Rapprochement Smile&Pay du jour (non rapprochés à vérifier). |
| `get_table_status` | lecture | — | État réel d'une table vu par la caisse, avec conflits détectés. |
| `import_storefront_menu` | écriture | hook P2.1 | Construit TOUTE la carte vitrine en un appel : catégories + sous-catégories + plats + formules éditoriales. Id… |
| `link_option_group` | écriture | — | Rattache / détache un groupe d'options à des catégories ou des plats. |
| `list_calls` | lecture | — | Appels reçus par Caroline (assistante vocale) : intention, résumé, suivi. |
| `list_delivery_zones` | lecture | — | Liste les zones de livraison. |
| `list_formules` | lecture | — | Formules telles que la caisse les vend, avec « vendable » ou la raison sinon. |
| `list_happy_hours` | lecture | — | Liste les happy hours. |
| `list_option_groups` | lecture | — | Groupes d'options (cuissons, suppléments, retraits) et rattachements. |
| `list_orders` | lecture | — | Liste les commandes (tous canaux). Filtres : statut, canal, date. |
| `list_payment_terminals` | lecture | — | Terminaux de paiement Smile&Pay. |
| `list_pos_payments` | lecture | — | Liste les encaissements d'une session de caisse. |
| `list_pos_tabs` | lecture | — | Liste les additions/tabs de caisse ouvertes. |
| `list_private_event_requests` | lecture | — | Liste les demandes d'événements privés. |
| `list_reservations` | lecture | — | Liste les réservations de table. Filtres : statut, date. |
| `list_site_templates` | lecture | — | Modèles de site vitrine disponibles. |
| `list_terminal_payments` | lecture | — | Encaissements TPE (statut, montant, pourboire, rapprochement). |
| `list_waitlist` | lecture | — | Liste la file d'attente active (walk-ins en attente / prévenus). |
| `lister_bornes` | lecture | — | Bornes de commande et tablettes de table (en ligne, commandes du jour, quota). |
| `lister_commandes_borne` | lecture | — | Commandes passées sur les bornes (50 dernières). |
| `mark_call_handled` | écriture | — | Marque un appel traité (ou le rouvre). |
| `no_show_reservation` | écriture | — | Marque une réservation en no-show (client absent → libère la table). |
| `open_pos_session` | écriture | — | Ouvre une session de caisse (POS). |
| `publish_site` | écriture | serveur, hook P2.1 | Publie le site vitrine. |
| `record_pos_payment` | écriture | hook P2.1, garde native | Enregistre un encaissement en caisse. |
| `regenerer_qr_table` | écriture | serveur | Change l'adresse QR d'une table — le chevalet imprimé ne fonctionne plus. |
| `remove_site_section` | écriture | serveur | Retire une section d'une page du site. |
| `reservation_availability` | lecture | — | Vérifie la disponibilité d'un créneau : restaurant ouvert + tables libres (anti-double-booking). |
| `save_formule` | écriture | — | Crée ou remplace une formule vendable (étapes de plats, TVA ventilée par composant). |
| `save_option_group` | écriture | — | Crée ou modifie un groupe d'options (choix absents désactivés, jamais supprimés). |
| `seat_waitlist` | écriture | — | Installe un client de la file d'attente sur une table (crée la commande sur place). |
| `set_dish_sold_out` | écriture | — | Plat épuisé / de retour pour la journée, partout (caisse, QR, borne, boutique, menu boards). |
| `set_site_theme` | écriture | — | Définit le thème (couleurs/typo) du site vitrine. |
| `toggle_site_page` | écriture | — | Active/désactive une page du site vitrine. |
| `update_event_request_status` | écriture | — | Change le statut d'une demande d'événement privé. |
| `update_order_status` | écriture | — | Change le statut d'une commande (répercute sur facture/devis et table). |
| `update_section` | écriture | — | Met à jour une section de page du site vitrine. |
| `update_site_page` | écriture | — | Modifie titre, adresse, place dans le menu et ordre d'une page. |
| `update_table_status` | écriture | — | Change le statut d'une table (free|reserved|occupied|cleaning|blocked). |
| `upsert_delivery_zone` | écriture | — | Crée/met à jour une zone de livraison. |
| `upsert_happy_hour` | écriture | — | Crée/met à jour un happy hour. |

## ⑥ Communication — 37 outils (18 lecture / 19 écriture)

Campagnes, templates WhatsApp, e-réputation (avis), segments RFM et capture de leads. La fiche client va ici (base de contacts des campagnes) plutôt qu'en ⑦ : la fidélité consomme les clients, la communication les constitue.

| Outil | Lecture/Écriture | Confirm requis | Commentaire |
|---|---|---|---|
| `add_marketing_event` | écriture | — | Ajoute un événement local à l'agenda marketing. |
| `arreter_diffusion` | écriture | serveur | Arrête une diffusion immédiate en cours. |
| `create_campaign` ⁽ⁿⁱ⁾ | écriture | — | non introspecté — nom et présence relevés sur le serveur live |
| `create_client` | écriture | — | Crée un client pour un établissement. |
| `create_whatsapp_template` ⁽ⁿⁱ⁾ | écriture | — | non introspecté — nom et présence relevés sur le serveur live |
| `creer_code_appairage` | écriture | — | Déclare un nouvel écran et renvoie son code d'appairage (compte dans le quota). |
| `creer_playlist` | écriture | — | Crée une playlist d'affiches (ne diffuse rien). |
| `delete_client` | écriture | hook P2.1 | Supprime un client d'un établissement. Action irréversible. |
| `diffuser_maintenant` | écriture | serveur | Diffuse immédiatement des affiches sur des écrans, au-dessus du programme. |
| `etat_parc` | lecture | — | État du parc d'écrans, diffusions en cours, quota, crédits d'affiches. |
| `generer_affiche` | écriture | garde native | Affiche IA depuis des plats de la carte ; coûte des crédits d'affiches. |
| `get_campaign_stats` ⁽ⁿⁱ⁾ | lecture | — | non introspecté — nom et présence relevés sur le serveur live |
| `get_client` | lecture | — | Retourne le détail d'un client d'un établissement. |
| `get_credit_balance` | lecture | — | Crédits de communication SMS / WhatsApp / vocal. |
| `get_marketing_calendar` | lecture | — | Agenda marketing du mois : marronniers, événements, jours creux, campagnes. |
| `get_qr_code` | lecture | — | QR code d'une destination ou d'une adresse du restaurant (SVG/PNG). |
| `get_qr_destinations` | lecture | — | Adresses publiques du restaurant et leur QR (actives ou non, module requis). |
| `importer_media` | écriture | — | Ajoute une affiche depuis une URL d'image publique (sans diffuser). |
| `launch_campaign` ⁽ⁿⁱ⁾ | écriture | hook P2.1 | non introspecté — nom et présence relevés sur le serveur live |
| `list_campaigns` ⁽ⁿⁱ⁾ | lecture | — | non introspecté — nom et présence relevés sur le serveur live |
| `list_clients` | lecture | — | Liste les clients d'un établissement. Filtres : recherche, statut. |
| `list_reviews` | lecture | — | Liste les avis clients. |
| `list_rfm_segments` ⁽ⁿⁱ⁾ | lecture | — | non introspecté — nom et présence relevés sur le serveur live |
| `list_site_leads` | lecture | — | Leads capturés via le site vitrine. |
| `list_whatsapp_templates` ⁽ⁿⁱ⁾ | lecture | — | non introspecté — nom et présence relevés sur le serveur live |
| `lister_ecrans` | lecture | — | Écrans d'affichage et ce qu'ils jouent maintenant. |
| `lister_medias` | lecture | — | Bibliothèque d'affiches et affiches IA en cours ; termine une fabrication en attente. |
| `lister_playlists` | lecture | — | Playlists et créneaux programmés. |
| `moderate_review` | écriture | hook P2.1 | Modère un avis client. |
| `obtenir_ecran` | lecture | — | Détail d'un écran : programme, créneaux, derniers événements. |
| `planifier_diffusion` | écriture | — | Programme une playlist sur un écran ou un groupe (chevauchement refusé). |
| `propose_campaigns` ⁽ⁿⁱ⁾ | écriture | — | non introspecté — nom et présence relevés sur le serveur live |
| `rapport_diffusion` | lecture | — | Ce que diffuse chaque écran et passages réellement joués. |
| `reply_review` | écriture | hook P2.1 | Répond à un avis client. |
| `submit_whatsapp_template` ⁽ⁿⁱ⁾ | écriture | hook P2.1 | non introspecté — nom et présence relevés sur le serveur live |
| `synchroniser_carte` | écriture | — | Menu board : pose / retire / rafraîchit la carte en direct sur les écrans. |
| `update_client` | écriture | — | Modifie un client d'un établissement. |

## ⑦ Fidélité — 17 outils (11 lecture / 6 écriture)

Programme de fidélité, récompenses, bons, cartes cadeaux, et moteur d'engagement (roues cadeaux, sondages — création possible depuis le 2026-10 avec `create_wheel_game` / `create_survey`, toujours INACTIFS à la création ; voir docs/couverture-fidelite-jeux.md).

| Outil | Lecture/Écriture | Confirm requis | Commentaire |
|---|---|---|---|
| `adjust_points` | écriture | hook P2.1, garde native | Ajuste les points de fidélité d'un client. |
| `check_gift_card` | lecture | — | Vérifie une carte cadeau (solde/validité). |
| `create_survey` | écriture | — | Crée un sondage (inactif par défaut). |
| `create_wheel_game` | écriture | — | Crée une roue cadeaux (inactive par défaut, probabilités = 100 %). |
| `get_loyalty_account` | lecture | — | Compte de fidélité d'un client. |
| `get_loyalty_capture` | lecture | — | Taux de capture client : tickets rattachés à une fiche, CA identifié. |
| `get_loyalty_program` | lecture | — | Programme de fidélité de l'établissement. |
| `get_survey_results` | lecture | — | Résultats d'un sondage. |
| `get_wheel_stats` | lecture | — | Statistiques des jeux de roue. |
| `list_gift_cards` | lecture | — | Liste les cartes cadeaux. |
| `list_loyalty_rewards` | lecture | — | Liste les récompenses de fidélité. |
| `list_redemptions` | lecture | — | Liste les utilisations de récompenses de fidélité. |
| `list_surveys` | lecture | — | Liste les sondages. |
| `list_wheel_games` | lecture | — | Liste les jeux de roue (wheel). |
| `update_loyalty_program` | écriture | hook P2.1 | Met à jour le programme de fidélité. |
| `upsert_loyalty_reward` | écriture | — | Crée/met à jour une récompense de fidélité. |
| `validate_redemption` | écriture | garde native | Valide l'utilisation d'une récompense de fidélité. |

## ⑧ Comptabilité — 15 outils (10 lecture / 5 écriture)

Factures, devis, dépenses, synthèse financière.

| Outil | Lecture/Écriture | Confirm requis | Commentaire |
|---|---|---|---|
| `create_expense` | écriture | — | Enregistre une dépense (achat) avec ses lignes. Totaux calculés automatiquement. |
| `create_invoice` | écriture | — | Crée une facture (brouillon) avec ses lignes. Totaux calculés automatiquement. |
| `create_quote` | écriture | — | Crée un devis (brouillon) avec ses lignes. Totaux et acompte calculés automatiquement. |
| `finance_summary` | lecture | — | Synthèse financière : CA facturé, encaissé, impayés, dépenses, marge sur une période. |
| `get_expense` | lecture | — | Retourne le détail complet d'une dépense (lignes incluses). |
| `get_invoice` | lecture | — | Retourne le détail complet d'une facture (lignes incluses). |
| `get_pos_analytics` | lecture | — | Statistiques de caisse : CA, tickets, panier, couverts, marge estimée, ventilations. |
| `get_quote` | lecture | — | Retourne le détail complet d'un devis (lignes incluses). |
| `get_table_turnover` | lecture | — | Temps de table et rotations sur une période. |
| `get_top_flop_products` | lecture | — | Meilleures ventes et flops de la carte (zéro vente inclus). |
| `list_expenses` | lecture | — | Liste les dépenses (achats fournisseurs) d'un établissement. Filtres : statut, recherche. |
| `list_invoices` | lecture | — | Liste les factures d'un établissement. Filtres : statut, recherche. |
| `list_quotes` | lecture | — | Liste les devis d'un établissement. Filtre : statut. |
| `update_invoice_status` | écriture | — | Change le statut d'une facture en respectant les transitions légales autorisées (DGFiP). |
| `update_quote_status` | écriture | — | Change le statut d'un devis (brouillon, envoye, accepte, refuse, expire). |

## ⑨ Transverse (hors boucles) — 5 outils (4 lecture / 1 écriture)

N'entrent dans aucune boucle du livre blanc : résolution de noms vers IDs (`search_entities`), brief quotidien multi-boucles (`get_daily_brief`), notifications génériques. Candidats officiels à la 9e catégorie « transverse ».

| Outil | Lecture/Écriture | Confirm requis | Commentaire |
|---|---|---|---|
| `create_notification` | écriture | — | Crée une nouvelle notification pour un établissement. |
| `get_daily_brief` | lecture | — | Brief quotidien de l'établissement. |
| `get_subscription_overview` | lecture | — | Abonnement : plan, add-ons, statut, échéances. |
| `list_notifications` | lecture | — | Liste les notifications d'un établissement. |
| `search_entities` | lecture | — | Résout un nom parlé/écrit vers un ID (produits, ingrédients, plats, équipements, tables, recettes). Fuzzy FR ;… |

## Synthèse

| Boucle | Outils | Lecture | Écriture |
|---|---|---|---|
| ① Configuration | 21 | 8 | 13 |
| ② Équipe | 23 | 10 | 13 |
| ③ Stock / Production | 48 | 22 | 26 |
| ④ HACCP | 26 | 10 | 16 |
| ⑤ E-commerce / Vente & service | 72 | 35 | 37 |
| ⑥ Communication | 37 | 18 | 19 |
| ⑦ Fidélité | 17 | 11 | 6 |
| ⑧ Comptabilité | 15 | 10 | 5 |
| ⑨ Transverse (hors boucles) | 5 | 4 | 1 |
| **Total** | **264** | **128** | **136** |

### Boucles sous-outillées (moins de 5 outils)

Aucune boucle du livre blanc n'est couverte par moins de 5 outils. La
catégorie ⑨ transverse (4 outils) est hors boucles par construction.

### Outils hors boucles (9e catégorie « transverse »)

`search_entities`, `get_daily_brief`, `create_notification`,
`list_notifications` — voir boucle ⑨ ci-dessus.

