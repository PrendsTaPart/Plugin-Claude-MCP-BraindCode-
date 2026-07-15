# PLAN FoodEatUp V2 — audit MCP + intégration (série SYNC S1) — 2026-07-15

Analyse **exhaustive** des **111 outils** du MCP FoodEatUp connecté
(`docs/inventaires/foodeatup-tools.json`, introspecté) croisée avec le plugin
`foodeatup`. L'audit fait foi : `docs/audits/AUDIT-foodeatup-2026-07-15.md`.

## 1. Couverture

- **111 outils** exposés · **85 exploités (77 %)** · **26 orphelins** · **0 référence
  morte réelle** (après correctif, cf. §2 — la couverture a gagné 2 outils, `get_client`
  et `update_product`, désormais cités par les skills corrigés).
- Les **11 « suspects »** (`get_pipeline`, `list_factures`, `send_email`, `get_contact`,
  `get_loyalty_points`…) sont
  des outils **RapidoCRM** légitimement appelés (le plugin déclare `rapidocrm` dans son
  `.mcp.json`, avec table de correspondance explicite dans les skills). Le harnais les
  reclassera automatiquement en **cross-serveur** dès que l'inventaire CRM existera (S2).

## 2. Correctifs immédiats — FAITS (le vrai bug trouvé)

Le harnais a mis en évidence une **adaptation d'import incomplète** sur **3 skills**
venus de `anthropics/knowledge-work-plugins` : une table de correspondance
QuickBooks/PayPal/HubSpot → Rapido avait été ajoutée en tête, **mais le corps des
étapes appelait toujours les outils d'origine, inexistants ici** (bug silencieux).

| Skill | Ce qui était cassé | Corrigé en |
|---|---|---|
| `margin-analyzer` | Étapes 1/3/6 : `company-info`, `quickbooks-profile-info-update`, `profit-loss-quickbooks-account`, PayPal ; `gotchas.md` : `list_transactions` (PayPal) | recettes (`get_recipe`, `recette-cout-marge`) + `list_expenses` pour les coûts ; `finance_summary`/`list_orders`/`list_invoices` + CRM pour les revenus ; `gotchas.md` réécrit Rapido-natif |
| `price-check` | Step 1 « Pull QuickBooks/PayPal », connector failures, approval gates | mêmes outils réels FoodEatUp/CRM |
| `handle-complaint` | Step 2 « Search HubSpot/PayPal » ; skills fantômes `ticket-deflector`, `customer-pulse-check` | historique client CRM (`get_contact`, `get_historique_prospect`, `get_loyalty_points`) + statut commande FoodEatUp ; renvoi `rapidocrm:draft-response` |

→ Commits `fix(foodeatup): sync outils MCP — {skill}`, bump **1.5.2**. `tester` 0/0/0.

> **Limite du harnais révélée** : la détection de références mortes ne retient que les
> tokens à **verbe d'action** (pour écarter les paramètres), donc les faux outils à
> préfixe **nom** (`profit-loss-quickbooks-account`, `company-info`) passaient au travers ;
> et le regex ne capte que le **snake_case** (les outils RapidoRh sont en **kebab-case**).
> **À améliorer avant S4** (rapidorh) : capter aussi le kebab-case + une section
> informative « citations non reconnues » (tout token *tool-like* absent de tout
> inventaire, à revoir humainement).

## 3. Outils orphelins (26) — décision par famille

**Règle** : ne créer un skill que s'il y a une vraie **valeur d'usage**. La plupart des
orphelins sont des **primitives CRUD** qui complètent des skills existants → **extension**,
pas nouveau skill. Écritures sensibles (suppressions) = confirmation (hook `garde-destructif`).

| Famille | Outils orphelins | Décision |
|---|---|---|
| **client** (4) | `create_client`, `list_clients`, `update_client`, `delete_client` | **Extension `service-salle`** : créer/retrouver un client au moment de la réservation (fidéliser le fichier resto). Le CRM (`rapidocrm`) reste le système de référence B2B — pont, pas doublon. `delete_client` = confirmation. (`get_client` déjà mobilisé par `handle-complaint`.) |
| **product** (3) | `create_product`, `get_product`, `delete_product` | **Extension `reappro-fournisseurs`** (catalogue produits/épicerie, distinct des plats). CRUD au sein du réappro. |
| **ingredient** (4) | `create_ingredient`, `get_ingredient`, `update_ingredient`, `delete_ingredient` | **Extension `recette-cout-marge` / `reappro-fournisseurs`** : gérer la fiche ingrédient (prix, seuil) qui alimente le coût de revient. |
| **dish** (3) | `create_dish`, `create_dish_category`, `delete_dish` | **Extension `carte-vitrine`** : créer/supprimer un plat unitaire + sa catégorie (aujourd'hui seul `import_storefront_menu` en masse + `update_dish` sont utilisés). |
| **employee** (3) | `get_employee`, `update_employee`, `delete_employee` | **Extension `planning-equipe` / `onboarding-restaurateur`** : édition de fiche + offboarding. `delete_employee` = confirmation. |
| **tva** (2) | `create_tva`, `list_tva` | **Extension `onboarding-restaurateur`** : configurer les taux de TVA à l'installation. |
| **category** (3) | `create_category`, `update_category`, `delete_category` | **Non couvert en propre** : primitive utilisée implicitement (catégories d'ingrédient/produit/recette) — à mobiliser dans les extensions ci-dessus, pas de skill dédié. |
| **supplier** (1) | `create_supplier` | **Extension `reappro-fournisseurs`** : créer un fournisseur (aujourd'hui `get`/`list_suppliers` seulement). |
| **invoice** (1) | `get_invoice` | **Extension `gestion-commandes`** : détail d'une facture (déjà `create_invoice`/`list_invoices`/`update_invoice_status`). |
| **recipe** (1) | `delete_recipe` | **Extension `recette-cout-marge`** : supprimer une recette (confirmation). |
| **unit** (1) | `list_units` | **Non couvert** : référentiel global lecture seule, mobilisé à la volée — aucun skill dédié. |

**Bilan** : **0 nouveau skill** clairement justifié — la valeur dormante est une
**complétude CRUD** à ajouter aux skills existants (surtout `carte-vitrine`,
`reappro-fournisseurs`, `recette-cout-marge`, `planning-equipe`, `service-salle`,
`onboarding-restaurateur`). Pas d'agent complémentaire nécessaire.

## 4. Constat majeur — les « pistes » ne sont PAS exposées

Les familles espérées dans le brief SYNC (**site vitrine** complet, **caisse/POS**,
**fidélité/cartes cadeaux/jeux**, **avis clients**, **recrutement resto**, **happy hours /
zones de livraison**) **n'existent pas** dans les 111 outils du serveur connecté. Seuls
`import_storefront_menu` + `show_on_storefront` (construction de carte vitrine) s'en
approchent — aucun `publish_site`, `open_pos_session`, `loyalty_*`, `list_reviews`,
`create_job_offer`, etc.

**Conséquence** : impossible de construire des skills « présence en ligne » (agent
`gerant-digital`), fidélité, avis ou recrutement resto **contre ce serveur**. Deux cas :
1. ces familles vivent sur une **version du MCP non connectée** à cette session → à
   **confirmer avec Tunis** (entrée `docs/OUTILS-MCP-MANQUANTS.md`, consolidée en S5) ;
2. réintrospecter dès qu'elles sont disponibles, puis rejouer ce plan.

Les **ponts inter-plugins** du brief en dépendent donc : carte vitrine ↔
`rapido-lovable`/`rapido-design` **reste faisable** (via `import_storefront_menu`) ;
fidélité ↔ `animation-client` CRM, recrutement ↔ `rapidorh`, avis ↔ `handle-complaint`
**sont en attente d'outils serveur**.

## 5. Exécution (après validation)

- Un commit par skill étendu (conventions : Étape 0, tests de déclenchement +
  anti-déclenchement, scripts stdlib pour tout calcul, bump + CHANGELOG).
- Recette réelle sur l'**établissement démo `establishment_id = 2`** (jamais le `26` sans
  accord) : une action par famille étendue, confirmations tracées.
- Écritures sensibles (suppressions, statuts de facture, encaissements) = **confirmation
  systématique**.

> **STOP** — validation attendue sur : (a) la liste des extensions §3 (lesquelles retenir),
> (b) le traitement des familles absentes §4 (spec `OUTILS-MCP-MANQUANTS` pour Tunis).
