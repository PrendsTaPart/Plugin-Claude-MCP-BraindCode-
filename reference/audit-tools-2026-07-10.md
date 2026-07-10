# Audit de vérité — serveurs foodeatup / rapidocrm / rapidocms (2026-07-10, v3)

**Méthode** : introspection des serveurs MCP réellement connectés à la
session du 2026-07-10 (catalogues live : **foodeatup 112 outils,
rapidocrm 103, rapidocms 43**), croisée avec les citations en backticks dans
TOUS les `.md` (`skills/`, `agents/`, `reference/`) de TOUS les plugins qui
déclarent le serveur dans leur `.mcp.json`. Un outil « orphelin » est un
outil live cité NULLE PART dans le dépôt. Chaque nouveau câblage a été fait
schéma en main (vérification live AVANT écriture).

Plugins déclarants par serveur :
- **foodeatup** : foodeatup, rapido-canva, rapido-direction, rapido-lovable,
  rapido-meta-ads, rapido-n8n, rapido-startup, rapido-suite ;
- **rapidocrm** : les mêmes + rapidocrm ;
- **rapidocms** : rapidocms, rapido-canva, rapido-lovable, rapido-meta-ads,
  rapido-n8n, rapido-startup, rapido-suite.

---

## (a) État final de la couverture

**Couverture : 87/112 foodeatup, 98/103 rapidocrm, 43/43 rapidocms.**
Plus AUCUN cluster fonctionnel non couvert (tableau section 4). Les
25 orphelins restants sont tous des CRUD unitaires ou de l'administration
sensible, **ignorés volontairement** — raison ci-dessous.

### foodeatup — 20 ignorés volontairement

| Outils | Raison (couverts par les workflows de plus haut niveau) |
|---|---|
| `create_dish`, `create_dish_category`, `create_category`, `update_category`, `create_ingredient`, `update_ingredient`, `create_product`, `update_product`, `get_product`, `get_ingredient` | Carte et catalogue : la mise en carte passe par `import_storefront_menu` (idempotent) et `update_dish`/`update_recipe` (cités) ; la création/édition unitaire reste accessible à la demande directe, sans skill dédié |
| `create_client`, `update_client`, `get_client` | Fiches clients créées au passage par les workflows réservation/commande ; consultation à la demande directe |
| `create_supplier` | Acte rare fait une fois — `list_suppliers` + `create_supplier_order` (cités) couvrent le flux récurrent |
| `create_tva`, `list_tva`, `list_units` | Paramétrage d'installation (une fois), pas un workflow récurrent |
| `get_employee`, `update_employee`, `get_invoice` | Lectures/CRUD unitaires atteignables à la demande directe ; les workflows passent par `list_employees`/`list_invoices` (cités) |

### rapidocrm — 5 ignorés volontairement

| Outils | Raison |
|---|---|
| `create_product`, `get_product`, `update_product` | Catalogue produits CRM géré dans l'app ; `list_products` (cité) suffit aux devis/factures |
| `create_user`, `get_user` | Administration des comptes utilisateurs : sensible, se fait dans l'interface d'admin |

### rapidocms — 0 orphelin

Les 43 outils du serveur sont tous cités par un skill.

---

## (b) Outils cités mais ABSENTS des serveurs

**AUCUN.** Zéro outil fantôme : chaque nom cité existe tel quel sur son
serveur (catalogues live du 2026-07-10).

---

## (c) Écarts de paramètres — tous CORRIGÉS le 2026-07-10

| Outil | Correction appliquée |
|---|---|
| `update_invoice_status` (FoodEatUp) | Enum élargi (brouillon, en_attente, envoyee, acceptee, refusee, litige, payee, annulee) + transitions DGFiP validées PAR LE SERVEUR — documenté (pieges foodeatup/suite/startup + devis-facture-relance) ET câblé (gestion-commandes § Devis et factures) : tenter l'appel, relayer l'erreur |
| `add_temperature` (FoodEatUp) | `equipment_id` REQUIS documenté (haccp + pièges) ; hooks anti-donnee-inventee (foodeatup + copie rapido-suite) refusent sans `equipment_id` ; résolution via `search_entities` |
| `create_draft_tool` (CMS) | Convention post texte VÉRIFIÉE PAR APPEL RÉEL (brouillon jetable créé puis supprimé) : `media_type: ""`, `media_url: ""`, `media_source: "biblio"`, `media_caption` = texte du post — documentée (pièges + pipeline-contenu-social) |
| `upload_file_tool` (CMS) | `type: "document"` → `"doc"` corrigé (dossier-startup-360) ; enum réel : image, video, doc |

---

## (4) Clusters fonctionnels — TOUS couverts

| Cluster | Couvert par |
|---|---|
| Dépenses CRM (lecture + saisie) | R4/R7 (`list_depenses`) + performance-commerciale (`create_depense`, confirmation) |
| Sondages / concours / fidélité | animation-client + R6 (SENSE) |
| Formulaires + CTA | R6 + journee-du-dirigeant |
| Cycle de vie commerciaux | performance-commerciale (create/update_profil/delete avec `confirm: true` serveur + hook ; `set_commercial_status` proposé d'abord) |
| Newsletters / templates éditeur / templates contrat | communication-client (`list_newsletters`), studio-templates (`list_editor_templates`), contrats-clients (`update_contrat_template`) |
| Bibliothèque de prompts CMS | bibliotheque-prompts |
| **Marques CMS (CRUD)** | **gestion-marques (nouveau skill)** — create/edit/delete_brand, delete sous hook |
| Assets de marque CMS | contenu-conforme-marque (+ `list_all_files` anti-doublon) |
| Éditions unitaires CMS | pipeline-contenu-social (`edit_draft_tool`), orchestration-campagne (`edit_campagne`), carte-digitale (`edit_digital_card`) |
| KDS FoodEatUp | coordination-cuisine |
| Nettoyage FoodEatUp | haccp-conformite-quotidienne |
| **Traçabilité HACCP** | **haccp-conformite-quotidienne étape 7** (create/list_haccp_tracabilite, list_haccp_labels) |
| Contrats employés | planning-equipe (+ `update_employee_schedule` sous hook — REMPLACE tout le planning —, `assign_task`) |
| **Devis restaurant** | **gestion-commandes § Devis et factures** (create/get/list_quotes, update_quote_status, update_invoice_status) |
| Stocks / livraisons / dépenses resto | production-stock (`list_stocks`), reappro-fournisseurs (`list_deliveries`, `create_expense`/`get_expense`) |
| Plan de salle / disponibilité / notifications | service-salle, briefing-du-jour, journee-du-dirigeant, routines R4/R7 |
| Recherche transverse | `search_entities` — règle § 1 ter des directives foodeatup, Étape 0 de 7 skills |

---

## (5) Les 7 outils apparus EN COURS de session — tous couverts ou gardés

| Outil | Couverture | Garde |
|---|---|---|
| `search_entities` (FoodEatUp) | règle § 1 ter + Étape 0 de 7 skills + coordination-cuisine | ambiguous=true → confirmation exigée |
| `update_kds_item_status` (FoodEatUp) | coordination-cuisine (machine à états 4 états) | item_id = ligne de commande (pièges) |
| `add_asset` (CMS) | contenu-conforme-marque | — |
| `remove_asset` (CMS) | contenu-conforme-marque | hook garde-destructif (matcher explicite, testé) |
| `create_brand` (CMS) | gestion-marques | confirmation avant écriture (référentiel global) |
| `edit_brand` (CMS) | gestion-marques | confirmation avant/après |
| `delete_brand` (CMS) | gestion-marques | hook garde-destructif (motif `delete_.*`) + confirmation |

---

## Historique des vagues

- **v1 (matin)** : constat — 52/36/12 jamais cités, clusters candidats.
- **v2 (après-midi)** : clusters candidats couverts (animation-client,
  bibliotheque-prompts, assets, KDS, nettoyage, contrats, notifications,
  formulaires, search_entities) ; 4 écarts documentaires corrigés ;
  54 orphelins avec propositions.
- **v3 (cette version)** : arbitrage appliqué — 29 « couvrir » câblés
  (traçabilité, devis resto, stocks/livraisons/dépenses, planning type,
  tâches, dépenses CRM, cycle commerciaux, newsletters, templates,
  gestion-marques, éditions CMS, bibliothèque média) ; 25 CRUD/admin
  « ignorés volontairement » avec raison. **Audit clos.**
