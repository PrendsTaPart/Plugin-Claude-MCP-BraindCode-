# Audit de vérité — serveurs MCP de la marketplace (2026-07-10, v4)

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

---

# (6) v4 — Audit complet ÉTENDU À TOUS LES SERVEURS (soir)

**Nouveauté v4** : les catalogues des 6 serveurs restants (gmail,
google-calendar, google-drive, n8n, facebook-ads, stripe) ont été relevés
LIVE dans la session du 2026-07-10 et EMBARQUÉS dans
`scripts/tester-skills.py`. Conséquence : **plus aucun outil « à vérifier en
ligne »** — le testeur est passé de 78 INFO à **0 FAIL / 0 WARN / 0 INFO**,
chaque outil cité dans le dépôt est vérifié contre un catalogue serveur.
Seul canva reste sur son relevé du 2026-07-06 (OAuth non connecté ce jour —
invérifiable).

## Ce que l'embarquement a immédiatement révélé (corrigé)

1. Le catalogue rapidocms du testeur n'avait jamais reçu les 5 outils
   marques apparus en session (add_asset, remove_asset, create/edit/
   delete_brand) → ajoutés.
2. **rapido-suite citait `search_workflows`/`search_executions` (n8n) sans
   déclarer le serveur** — corrigé : n8n déclaré dans son `.mcp.json`
   (`${N8N_MCP_URL}`, optionnel, dégradation propre — pattern
   rapido-direction) ; le README omettait aussi lovable et facebook-ads
   pourtant déclarés par rapido-suite → ligne corrigée.

## Couverture par serveur (cités / live, dans les plugins déclarants)

| Serveur | Couverture | Lecture |
|---|---|---|
| rapidocms | **43/43** | complet |
| rapidocrm | 98/103 | 5 ignorés volontairement (§a) |
| foodeatup | 92/112 | 20 ignorés volontairement (§a) |
| n8n | 24/26 | orphelins : search_folders, search_projects (navigation d'instance — inutiles aux workflows du plugin) |
| rapidorh | 18/22 | orphelins : documents/liens de projet + update-user (candidats : une ligne dans revue-projet-hebdo) |
| hyperframes | 5/6 | orphelin : list_projects (candidat : une ligne dans video-marketing pour retrouver un projet) |
| gmail | 8/13 | orphelins : labels sensibles/unlabel/list_drafts — le plugin est volontairement « brouillons + tri » |
| google-drive | 5/8 | orphelins : métadonnées/téléchargement — coffre-documents privilégie recherche + lecture |
| google-calendar | 4/8 | orphelins : get/update/respond_to_event, list_calendars (candidats : gestion d'un RDV existant dans journee-du-dirigeant) |
| stripe | 4/9 | outils d'aide au DÉVELOPPEUR (documentation, planner, feedback) volontairement hors périmètre — le plugin utilise l'API read/write/search |
| lovable | 22/44 | la moitié = skills workspace/connecteurs/analytics avancés — candidats si besoin client |
| facebook-ads | 31/82 | 51 orphelins = catalogue produits (28 outils), pixel (8) et expérimentations (7) — 3 clusters entiers volontairement hors périmètre v1 de rapido-meta-ads |
| canva | 17/38 | relevé du 06/07 (OAuth requis pour re-vérifier) — éditions transactionnelles et commentaires hors périmètre v1 |

## Améliorations recommandées (par priorité)

1. **FAIT (cette vague)** : catalogues live embarqués (0 INFO), agents
   manquants créés (chef-produit-web, architecte-automatisations),
   déclaration n8n de rapido-suite, évals rapido-lovable + rapido-n8n.
2. **Évals manquantes** : rapidorh, rapido-suite, rapido-canva,
   rapido-meta-ads n'ont pas encore de `tests/evals.md` (les scénarios
   existent en partie dans tests/test-routage.md racine) — à créer sur le
   modèle des autres plugins.
3. **Clusters candidats** (si besoin métier) : catalogue produits + pixel
   Meta (e-commerce), gestion d'un RDV existant (google-calendar),
   `list_projects` HyperFrames, documents/liens de projet RapidoRH.
4. **Ré-audit périodique** : les serveurs évoluent EN COURS de session
   (7 outils apparus le 10/07) — rejouer l'introspection live à chaque
   vague et comparer aux catalogues embarqués (écart = mise à jour).
5. **Côté utilisateur** : tag v1.0.0 + Release GitHub (le proxy de session
   bloque les tags), test réel `/plugin install rapido-suite@rapido`,
   OAuth Canva pour re-vérifier son catalogue, parties 3-4 du master plan
   à réconcilier (formules-kpi, routines, gouvernance, R9).
