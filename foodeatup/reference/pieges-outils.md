# Pièges des outils MCP (foodeatup) — référence rapide

Consulter ce tableau au moindre doute avant d'appeler un outil.

| Outil | Paramètres pièges | Erreur fréquente | Parade |
|---|---|---|---|
| (quasi tous) | `establishment_id` requis presque partout | Appel sans ID → erreur, ou ID deviné | Étape 0 de chaque skill : obtenir l'ID avant tout appel, le demander s'il est inconnu |
| `create_recipe` | `ingredients[].quantity` en poids **BRUT** ; `desc` ≠ étapes/ingrédients ; `tax_rate` en % | Quantités en poids net → food cost et stock faux ; étapes collées dans `desc` | Convertir avec le coefficient de cuisson (rendement) ou demander le brut ; utiliser les tableaux `ingredients` et `steps` |
| `create_recipe` (TVA) | `tax_rate` selon la NATURE du plat | 20 % appliqué partout, ou 10 % sur l'alcool | immediate = 10 % ; conservable = 10 % sur place / 5,5 % emporté (demander le canal) ; alcohol = 20 % |
| `create_haccp_label` | `lot_number` optionnel | Numéro de lot inventé | Ne pas le fournir : il est auto-généré |
| `create_haccp_reception` | `etat_livraison` enum ; `non_conformites` | `non_conforme` sans liste de non-conformités | Toujours renseigner `non_conformites` si l'état est `non_conforme` |
| `add_temperature` | `temperature` en °C ; **`equipment_id` REQUIS** (vérifié serveur 2026-07-10) ; `measured_at` optionnel ISO 8601 | Valeur estimée/inventée ; `equipment_id` deviné ou omis | Uniquement le relevé réel fourni par l'utilisateur (hook deny hors -30/+90 °C et sans equipment_id) ; résoudre l'équipement via `search_entities` (`types: ["equipment"]`), confirmation si `ambiguous=true` |
| `adjust_stock` | `establishment_product_id` ; `mode` | ID d'ingrédient passé à la place du produit ; `set` qui écrase le stock | Prendre le champ `id` de `list_products` ; `increment` à réception, `set` réservé aux inventaires (confirmer) |
| `create_production_plan` | `item_id` en chaîne | ID de recette passé sans préfixe | Plat = ID entier en chaîne (`"42"`) ; recette = préfixe `recipe_` (`"recipe_12"`) |
| `validate_production` | met à jour le stock automatiquement | `adjust_stock` appelé en plus → double comptage | Ne jamais ajuster le stock manuellement pour une production validée |
| `checkin_reservation` / `seat_waitlist` | créent la commande sur place | `create_order` appelé en plus → commande en double | Laisser ces outils créer la commande |
| `update_table_status` | `status` machine à états | Saut d'état (`occupied` → `free`) | Respecter free → reserved → occupied → cleaning → free (+ `blocked`) |
| `create_reservation` | risque de double-booking | Créer sans vérifier le créneau | `reservation_availability` TOUJOURS avant |
| tout outil à paramètres de dates | dates `YYYY-MM-DD`, heures `HH:MM` | Formats libres (« demain 19h ») | Convertir en ISO avant l'appel |
| `update_kds_item_status` | `item_id` = ligne de commande ; `status` 4 états | ID du plat au menu passé à la place de l'item ; oubli de `served` | Prendre l'ID de l'item dans la commande (`list_orders`/`get_order`) ; machine à états pending → in_progress → ready → served |
| `record_cleaning_action` | `poste_nettoyage_id` | ID de la ZONE passé à la place du POSTE | Les postes sont dans `list_cleaning_zones` (chaque zone contient ses postes) ; `statut` défaut `complete` |
| `create_employee_contract` | `type` enum ; `end_date` ; données sensibles | CDD sans date de fin ; salaire/heures devinés | `type` ∈ CDI, CDD, Extra, Apprentissage, Stage ; `end_date` pour un CDD ; confirmation niveau 2 avant l'appel (hook) |
| `update_invoice_status` | `status` ENUM élargi (vérifié serveur 2026-07-10) : brouillon, en_attente, envoyee, acceptee, refusee, litige, payee, annulee ; transitions DGFiP validées PAR LE SERVEUR | Pré-filtrer les transitions côté skill | Tenter l'appel et relayer l'erreur serveur si transition illégale — le serveur fait foi ; hook garde-destructif en confirmation |
| `list_categories` vs `list_dish_categories` | deux référentiels distincts | Chercher une catégorie de PLAT dans `list_categories` (ingrédients/produits) → doublon créé | Catégories de plats = `list_dish_categories` / `update_dish_category` / `delete_dish_category` |
| `set_dish_sold_out` | rupture du JOUR seulement | L'utiliser pour retirer un plat de la carte | Retombe seule à la bascule de journée ; retrait durable = `update_dish` `active: false` |
| `bulk_update_dishes` / `bulk_update_ingredients` | tout ou rien ; `confirm` | Écrire sans relire l'aperçu ; `allergens` qui REMPLACE la liste | Appeler sans `confirm` → aperçu avant/après validé → `confirm: true` |
| `set_opening_hours` | REMPLACE toute la semaine | Envoyer seulement le jour modifié → les autres jours deviennent fermés | Relire `get_opening_hours`, renvoyer la semaine complète ; garder `previous_hours` |
| `regenerer_qr_table` | invalide le chevalet imprimé | L'utiliser pour « obtenir le QR » d'une table | QR existant = `generer_qr_table` / `get_qr_code` ; régénérer seulement si QR compromis |
| `add_oil_test` | `method` visuel ≠ mesure | `polar_pct` renseigné sur un contrôle visuel | `visuel` → `visual_result` seulement ; `polar_pct` uniquement mesuré au testeur ou à la bandelette |
| `start_thermal_cycle` / `close_thermal_cycle` | `lot_ref` unique ; conformité calculée serveur | Températures estimées ; conformité annoncée avant clôture | Températures à cœur MESURÉES ; relayer la conformité rendue par le serveur |
| `diffuser_maintenant` / `arreter_diffusion` | `confirm` exigé | `confirm: true` au premier appel | Premier appel sans `confirm` = liste des écrans visés, à relire |
| `generer_affiche` | crédits d'affiches ; `modele` selon le nombre de plats | Modèle incompatible (hero avec 3 plats) ; diffusion sans relecture | hero 1 / vitrine 2–4 / menu_board 5–20 ; `lister_medias` puis relecture |
| `create_payment_link` | envoie un SMS/WhatsApp au client | Lien créé et envoyé sans accord | Récapituler montant, libellé, destinataire, canal → confirmation |
| `create_orders_from_shopping_list` | commandes RÉELLES | `confirm: true` sans aperçu | Aperçu par fournisseur validé, ingrédients sans produit signalés |
