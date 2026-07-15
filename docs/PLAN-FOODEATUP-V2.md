# PLAN FoodEatUp V2 — audit MCP + intégration (série SYNC S1) — 2026-07-15

> **État d'avancement (2026-07-15).**
> - ✅ **Fait** : correctifs des 3 skills half-adaptés (1.5.2) ; inventaire 164 ;
>   **3 nouveaux skills** `fidelite-restaurant`, `caisse-du-jour`, `site-vitrine-foodeatup`
>   + agent `gerant-digital` + hook étendu (1.6.0), sur **schémas réels** (24 outils).
> - ⏳ **Buildable maintenant** (schémas connus, dans les 111) : extensions CRUD
>   (client, produit, ingrédient, plat, employé, tva, fournisseur, facture, recette).
> - ⛔ **Bloqué sur schémas** (29 outils à réintrospecter, **ne pas inventer**) :
>   `recrutement-resto` (job_offer/applications), offre (happy hours/livraison/boissons),
>   avis complet (`list_reviews`/`reply_review`), + POS `list_pos_tabs`/`close_pos_session`
>   (params exacts), site `add_site_page`/`update_section`/`publish_site`/`get_domain_status`.


Analyse des outils du MCP FoodEatUp croisée avec le plugin `foodeatup`.
Audit : `docs/audits/AUDIT-foodeatup-2026-07-15.md` · inventaire :
`docs/inventaires/foodeatup-tools.json`.

> **Correction importante (registre de session tronqué).** Un premier passage n'a vu
> que **111 outils** (ce que le registre de la session Claude Code exposait) et avait
> conclu à tort que les familles POS/fidélité/avis/recrutement/site vitrine n'existaient
> pas. La **console d'autorisations MCP FoodEatUp** (`foodeatup.com/api/mcp`) fait foi :
> le serveur expose **164 outils**. Les 53 manquants sont réintégrés à l'inventaire
> (noms exacts de la console ; **schémas — paramètres — à introspecter** quand le
> connecteur les exposera à une session, cf. `schema_introspected:false`).
> **Leçon méthode** : ne jamais prendre le registre de session (`ToolSearch`) pour la
> vérité du serveur — **recroiser avec la console/doc du serveur** (ajouté à `METHODE.md`).

## 1. Couverture

- **164 outils** exposés · **86 exploités (52 %)** · **78 orphelins** · **0 référence
  morte réelle**.
- Les **11 « suspects »** (`get_pipeline`, `list_factures`, `send_email`, `get_contact`,
  `get_loyalty_points`…) sont des outils **RapidoCRM** légitimement appelés (cross-serveur ;
  le harnais les reclassera quand l'inventaire CRM existera, S2).

## 2. Correctifs immédiats — FAITS

Le harnais a révélé une **adaptation d'import incomplète** sur 3 skills venus de
`knowledge-work-plugins` : table de correspondance QuickBooks/PayPal→Rapido en tête,
**mais le corps des étapes appelait toujours les outils d'origine, inexistants** (bug
silencieux).

| Skill | Cassé | Corrigé |
|---|---|---|
| `margin-analyzer` | `profit-loss-quickbooks-account`, `company-info`, PayPal `list_transactions` | recettes (`get_recipe`) + `list_expenses` ; revenus FoodEatUp/CRM ; `gotchas.md` réécrit |
| `price-check` | « Pull QuickBooks/PayPal » | outils réels FoodEatUp/CRM |
| `handle-complaint` | « Search HubSpot/PayPal » + skills fantômes `ticket-deflector`, `customer-pulse-check` | historique CRM + commandes FoodEatUp ; renvoi `rapidocrm:draft-response` |

→ Commits `fix(foodeatup): sync outils MCP — {skill}`, bump **1.5.2**, `tester` 0/0/0.

## 3. Outils orphelins (78) — deux classes

### A) Nouvelles familles = vraie valeur dormante → **nouveaux skills** (les « pistes » confirmées)

| Famille | Outils (extraits) | Proposition |
|---|---|---|
| **Site vitrine** (13) | `get_site_pages`, `add_site_page`, `toggle_site_page`, `update_section`, `apply_site_template`, `list_site_templates`, `set_site_theme`, `publish_site`, `get_site_stats`, `get_site_status`, `list_site_leads`, `get_domain_status`, `get_page_content` | **NOUVEAU skill `site-vitrine-foodeatup`** : construire/éditer/publier la vitrine (pont `rapido-lovable`/`rapido-design` pour la charte et les tokens ; `list_site_leads` → CRM). `publish_site` = **confirmation** (visible public). |
| **Caisse / POS** (7) | `open_pos_session`, `close_pos_session`, `get_pos_session`, `get_pos_report`, `record_pos_payment`, `list_pos_payments`, `list_pos_tabs` | **NOUVEAU skill `caisse-du-jour`** : ouverture, encaissements, **clôture Z**. `record_pos_payment` et `close_pos_session` = **confirmation systématique** (argent réel). |
| **Fidélité + cartes cadeaux** (10) | `get_loyalty_program`, `update_loyalty_program`, `get_loyalty_account`, `adjust_points`, `list_loyalty_rewards`, `upsert_loyalty_reward`, `list_redemptions`, `validate_redemption`, `check_gift_card`, `list_gift_cards` | **NOUVEAU skill `fidelite-restaurant`** (pont `rapidocrm:animation-client` + `get_loyalty_points` CRM). `adjust_points`, `validate_redemption`, `update_loyalty_program` = **confirmation**. |
| **Avis clients** (3) | `list_reviews`, `reply_review`, `moderate_review` | **Volet dans `handle-complaint`** OU skill dédié `avis-clients`. `reply_review`/`moderate_review` = **brouillon puis confirmation** (public). |
| **Recrutement** (4) | `create_job_offer`, `update_job_offer`, `list_job_applications`, `update_application_status` | **NOUVEAU skill `recrutement-resto`** (pont `rapidorh`). Publication d'offre + suivi candidatures = confirmation. |
| **Animation** (sondages+roue, 4) | `list_surveys`, `get_survey_results`, `list_wheel_games`, `get_wheel_stats` | **Volet du skill `fidelite-restaurant`** (animation client : jeux, sondages) — lecture surtout. |
| **Offre commerciale** (7) | `list_happy_hours`, `upsert_happy_hour`, `list_delivery_zones`, `upsert_delivery_zone`, `list_beverages`, `upsert_beverage_item`, `remove_beverage_item` | **Extension `carte-vitrine`** : happy hours, zones de livraison, carte des boissons. Écritures = confirmation. |
| **Événements privés** (2) | `list_private_event_requests`, `update_event_request_status` | **Volet `service-salle` / devis** : traiter les demandes d'événements privés → devis (`create_quote`). |
| **Pilotage** (3) | `get_daily_brief`, `get_station_load`, `validate_production` | **Extensions** : `briefing-du-jour` (brief), `coordination-cuisine` (charge poste), `production-stock` (valider prod). |

> **Prérequis avant d'écrire ces skills** : **introspecter les paramètres réels** des 53
> outils (aujourd'hui `schema_introspected:false`) — le connecteur doit les exposer à la
> session, ou lire la doc FoodEatUp. **Ne pas inventer les paramètres.**

### B) Primitives CRUD → **extensions** de skills existants (pas de nouveau skill)

| Famille | Orphelins | Extension |
|---|---|---|
| **client** (4) | `create_client`, `list_clients`, `update_client`, `delete_client` | `service-salle` (fichier resto ; CRM reste référence B2B). `delete_client` = confirmation. |
| **product** (3) | `create_product`, `get_product`, `delete_product` | `reappro-fournisseurs` (catalogue). |
| **ingredient** (4) | `create_ingredient`, `get_ingredient`, `update_ingredient`, `delete_ingredient` | `recette-cout-marge` / `reappro-fournisseurs`. |
| **dish** (3) | `create_dish`, `create_dish_category`, `delete_dish` | `carte-vitrine`. |
| **employee** (3) | `get_employee`, `update_employee`, `delete_employee` | `planning-equipe` / `onboarding-restaurateur`. |
| **tva** (2) · **category** (3) · **supplier** (1) · **invoice** (1) · **recipe** (1) · **unit** (1) | — | Extensions (`onboarding`, réappro, gestion-commandes) ; `category`/`unit` = primitives internes, pas de skill dédié. |

## 4. Constat corrigé — les pistes SONT exposées → un agent se justifie

Contrairement au premier passage : **POS, fidélité, avis, recrutement, site vitrine,
cartes cadeaux, jeux, sondages, happy hours, zones de livraison, boissons, événements
privés existent tous** côté serveur. La **présence en ligne du restaurateur** (site
vitrine + avis + fidélité + jeux) forme un ensemble cohérent → **agent complémentaire
`gerant-digital`** qui orchestre ces skills. Les **ponts** du brief sont réalisables :
site ↔ `rapido-lovable`/`rapido-design`, fidélité ↔ `animation-client` CRM, recrutement
↔ `rapidorh`, avis ↔ `handle-complaint`.

## 5. Exécution (après validation)

- **D'abord** : introspecter les paramètres des 53 outils (mise à jour de l'inventaire,
  `schema_introspected:true`) — bloquant pour écrire des appels corrects.
- Un commit par skill créé/étendu (Étape 0, tests de déclenchement + anti-déclenchement,
  scripts stdlib, bump + CHANGELOG). Agent `gerant-digital` ensuite.
- Recette réelle sur l'**établissement démo `establishment_id = 2`** (jamais `26` sans
  accord) : une action par famille, confirmations tracées.
- Écritures sensibles (**encaissement POS, clôture Z, points fidélité, publication du
  site, réponse à un avis, offre d'emploi**) = **confirmation systématique**, à couvrir
  par le hook `garde-destructif`/un nouveau garde-fou selon les cas.

> **STOP** — validation attendue : (a) quels nouveaux skills lancer en premier
> (site-vitrine, caisse, fidélité, recrutement, avis) et dans quel ordre ; (b) OK pour
> introspecter d'abord les 53 schémas ; (c) périmètre de l'agent `gerant-digital`.
