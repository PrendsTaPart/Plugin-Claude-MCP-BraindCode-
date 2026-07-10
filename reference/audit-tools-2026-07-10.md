# Audit de vérité — serveurs foodeatup / rapidocrm / rapidocms (2026-07-10, v2)

**Méthode (v2 — élargie)** : introspection des serveurs MCP réellement
connectés à la session du 2026-07-10 (catalogues live : **foodeatup 112
outils, rapidocrm 103, rapidocms 43**), croisée avec les citations en
backticks dans TOUS les `.md` (`skills/`, `agents/`, `reference/`) de TOUS
les plugins qui déclarent le serveur dans leur `.mcp.json` — et plus
seulement les 3 plugins homonymes comme dans la v1. Un outil « orphelin »
est un outil live cité NULLE PART dans le dépôt.

Plugins déclarants par serveur :
- **foodeatup** : foodeatup, rapido-canva, rapido-direction, rapido-lovable,
  rapido-meta-ads, rapido-n8n, rapido-startup, rapido-suite ;
- **rapidocrm** : les mêmes + rapidocrm ;
- **rapidocms** : rapidocms, rapido-canva, rapido-lovable, rapido-meta-ads,
  rapido-n8n, rapido-startup, rapido-suite.

---

## (a) Orphelins restants — 54 au total (34 + 13 + 7)

Depuis la v1, TOUS les clusters fonctionnels identifiés ont été couverts :
KDS (`update_kds_item_status`), nettoyage (3 outils), contrats employés (3),
`search_entities`, notifications (`list_notifications` dans briefing-du-jour
et journee-du-dirigeant, `create_notification` dans les routines R4/R7),
dépenses (`list_depenses` dans R4/R7), sondages/concours/fidélité
(animation-client + R6), formulaires + CTA (R6 + journee-du-dirigeant),
bibliothèque de prompts, assets de marque (`add_asset`/`remove_asset`).
Restent des orphelins majoritairement CRUD — chacun ci-dessous avec une
proposition (couvrir / ignorer volontairement + raison), à arbitrer.

### foodeatup — 34 orphelins

**Proposition COUVRIR (valeur métier réelle) :**

| Outils | Où | Raison |
|---|---|---|
| `create_haccp_tracabilite`, `list_haccp_tracabilite`, `list_haccp_labels` | extension `haccp-conformite-quotidienne` | La traçabilité est un pilier HACCP ; `create_haccp_label` est cité mais ni la lecture des étiquettes ni la traçabilité |
| `create_quote`, `get_quote`, `list_quotes`, `update_quote_status` | extension `gestion-commandes` (ou skill devis-traiteur) | Cycle devis restaurant (groupes, traiteur) entièrement non couvert |
| `update_invoice_status` | extension `gestion-commandes` | Statut de facture post-commande — enum élargi + validation DGFiP serveur (voir (c)) ; hook ask déjà en filet possible |
| `list_stocks` | une ligne dans `production-stock` | L'inventaire complet à côté de `list_low_stocks` déjà cité |
| `list_deliveries` | une ligne dans `reappro-fournisseurs` | Suivi des livraisons à côté des réceptions HACCP |
| `create_expense`, `get_expense` | une ligne dans `analyse-rentabilite-carte` ou directives | Saisie d'une dépense dictée — `list_expenses` est déjà lu par R4 |
| `update_employee_schedule`, `assign_task` | extension `planning-equipe` | Modifier un horaire / affecter une tâche : fonctionnels, pas CRUD |

**Proposition IGNORER VOLONTAIREMENT (raison) :**

| Outils | Raison |
|---|---|
| `create_dish`, `create_dish_category`, `create_category`, `update_category`, `create_ingredient`, `update_ingredient`, `create_product`, `update_product`, `get_product`, `get_ingredient` | Carte et catalogue : la mise en carte passe par `import_storefront_menu` (idempotent) et les `update_dish`/`update_recipe` cités ; la création unitaire reste possible à la demande directe sans skill dédié |
| `create_client`, `update_client`, `get_client` | Fiches clients gérées par les workflows réservation/commande qui les créent au passage (`create_client` serveur appelé par l'app) |
| `create_supplier` | `list_suppliers` + `create_supplier_order` cités ; la création d'un fournisseur est un acte rare fait une fois (onboarding possible à la demande) |
| `create_tva`, `list_tva`, `list_units` | Paramétrage d'installation (une fois), pas un workflow récurrent |
| `get_employee`, `update_employee`, `get_invoice`, `assign_task`* | Lectures/CRUD unitaires atteignables à la demande directe (*assign_task listé aussi en « couvrir » — arbitrage) |

### rapidocrm — 13 orphelins

**Proposition COUVRIR :**

| Outils | Où | Raison |
|---|---|---|
| `create_depense` | extension du skill dépenses/pilotage CRM | Complète le cluster : la lecture (`list_depenses`) est câblée dans R4/R7, la saisie dictée manque |
| `create_commercial`, `delete_commercial`, `update_commercial_profil` | extension du skill pilotage commerciaux | Cycle de vie (entrée/sortie/profil) — le pilotage (objectifs, statut, performance) est déjà cité ; `delete_commercial` sous garde-destructif |
| `list_newsletters` | une ligne à côté de `send_newsletter` (cité) | Lire avant d'envoyer |
| `update_contrat_template` | une ligne à côté de `create_contrat_template`/`list_contrat_templates` (cités) | Compléter le CRUD des modèles de contrat |
| `list_editor_templates` | une ligne à côté de `create_editor_template` (cité) | Idem |
| `get_interaction_stats` | une ligne dans le skill stats/pilotage | Un indicateur de plus, coût nul |

**Proposition IGNORER VOLONTAIREMENT :**

| Outils | Raison |
|---|---|
| `create_user`, `get_user` | Administration des comptes utilisateurs : sensible, se fait dans l'interface d'admin |
| `create_product`, `get_product`, `update_product` | Catalogue produits CRM géré dans l'app ; `list_products` (cité) suffit aux devis/factures |

### rapidocms — 7 orphelins

**Proposition COUVRIR (tous — petites extensions) :**

| Outils | Où | Raison |
|---|---|---|
| `create_brand`, `edit_brand`, `delete_brand` | extension `contenu-conforme-marque` (multi-marques) | Schéma vérifié live : requis `nom`/`langue`/`slogan`, `couleurs` hex CSV, `font_family` enum web-safe, `logo` URL publique ; `delete_brand` déjà attrapé par le matcher `delete_.*` du hook |
| `edit_draft_tool` | une ligne dans `pipeline-contenu-social` | Corriger un brouillon avant planification — vraie valeur, coût une phrase |
| `edit_campagne` | une ligne dans `orchestration-campagne` | create/delete campagne cités, l'édition manque |
| `edit_digital_card` | une ligne dans `carte-digitale` | `edit_card_page` cité, l'édition de la carte elle-même manque |
| `list_all_files` | une ligne dans `contenu-conforme-marque` ou `prompt-engineering-visuel` | Consulter la bibliothèque média avant de re-uploader |

---

## (b) Outils cités mais ABSENTS des serveurs — à corriger

**AUCUN.** Zéro outil fantôme : chaque nom d'outil cité dans le dépôt existe
tel quel sur son serveur (vérifié contre les catalogues live du 2026-07-10).
Les câblages du jour (`floor_plan_status`, `reservation_availability`,
`list_notifications`, `create_notification`, `list_depenses`,
`list_formulaires`, `get_formulaire_soumissions`, `list_cta`,
`list_sondages`, `get_sondage_resultats`) ont tous été vérifiés schéma en
main AVANT écriture.

---

## (c) Écarts de paramètres — schémas live vs ce que documentent les skills

| Outil | Schéma LIVE (2026-07-10) | Ce que dit le dépôt | Verdict |
|---|---|---|---|
| `update_invoice_status` (FoodEatUp) | **CHANGÉ** — `status` ENUM élargi : `brouillon, en_attente, envoyee, acceptee, refusee, litige, payee, annulee` ; le serveur valide lui-même les transitions (DGFiP) | pieges-outils (foodeatup, rapido-suite, rapido-startup) + devis-facture-relance à jour : ne pas pré-filtrer, tenter et relayer l'erreur serveur ; hook en confirmation | ✅ **CORRIGÉ le 2026-07-10** |
| `add_temperature` (FoodEatUp) | `equipment_id` REQUIS | haccp-conformite-quotidienne + pieges-outils : equipment_id REQUIS, résolu via `search_entities` (jamais deviné) ; hook anti-donnee-inventee refuse sans equipment_id (testé) | ✅ **CORRIGÉ le 2026-07-10** |
| `create_draft_tool` (CMS) | `media_type/media_source/media_url/media_caption` requis MÊME en `post_type: text` | pieges-outils rapidocms : convention post texte VÉRIFIÉE PAR APPEL RÉEL (brouillon jetable créé puis supprimé) — `media_type: ""`, `media_url: ""`, `media_source: "biblio"`, `media_caption` = texte du post | ✅ **CORRIGÉ le 2026-07-10** |
| `upload_file_tool` (CMS) | `type` ∈ `image, video, doc` | dossier-startup-360 corrigé : `type: "doc"` (aucune autre occurrence de `document` comme valeur de type dans le dépôt) | ✅ **CORRIGÉ le 2026-07-10** (était ouvert depuis le 06/07) |
| `reservation_availability` (FoodEatUp) | teste UN créneau (`date`, `time` HH:MM, `party_size` requis) — pas de liste des résas du jour | briefing-du-jour v1.2.0 le documente ainsi ✓ (sondage créneau par créneau, `list_reservations` conservé pour les couverts/notes) | ✅ conforme |
| `list_notifications` (FoodEatUp) | `establishment_id` seul — PAS de filtre « non lues » serveur | briefing-du-jour v1.2.0 : filtrage côté réponse, documenté ✓ | ✅ conforme |
| `create_notification` (FoodEatUp) | `title` + `message` requis, `type` ∈ info/warning/danger/success (défaut info) | R4/R7 + autonomie.md (canal d'alerte, danger/warning) ✓ | ✅ conforme |
| `list_depenses` (CRM) | aucun requis ; `statut` ∈ en_attente/payee, `periode` ∈ today/week/month/quarter/year | R4 (semaine) / R7 (`periode: "month"`) ✓ | ✅ conforme |
| `get_formulaire_soumissions` (CRM) | `formulaire_id` OU `formulaire_nom` (recherche partielle) — vues, clics, taux de conversion | R6 / journee-du-dirigeant ✓ | ✅ conforme |
| `get_sondage_resultats` (CRM) | `sondage_id` OU `sondage_nom` ; `type` ∈ companie/client (défaut companie) | R6 / animation-client ✓ | ✅ conforme |
| `generate_image`, `post_insights`, `schedule_draft_tool` (CMS) | inchangés | ✓ | ✅ conforme |
| `search_entities`, `update_kds_item_status` (FoodEatUp) | inchangés depuis v1 | câblés (coordination-cuisine, 1.1.0) ✓ | ✅ conforme |

---

## (4) Clusters — état final

| Cluster | État |
|---|---|
| Dépenses CRM | ✅ lecture câblée (R4, R7) ; `create_depense` → proposition couvrir |
| Sondages / concours / fidélité CRM | ✅ couvert (animation-client + R6) |
| Formulaires + CTA CRM | ✅ couvert (R6 + journee-du-dirigeant) |
| Gestion commerciaux CRM | pilotage couvert ; cycle de vie (3 outils) → proposition couvrir |
| Bibliothèque de prompts CMS | ✅ couvert (bibliotheque-prompts) |
| Assets de marque CMS | ✅ add/remove_asset couverts ; CRUD marque (3 outils) → proposition couvrir |
| KDS FoodEatUp | ✅ couvert (coordination-cuisine) |
| Nettoyage FoodEatUp | ✅ couvert (haccp-conformite-quotidienne) |
| Contrats employés FoodEatUp | ✅ couvert (planning-equipe) |
| Plan de salle / disponibilité | ✅ couvert (service-salle, briefing-du-jour) |
| Recherche transverse (`search_entities`) | ✅ câblé (coordination-cuisine) ; généralisation Étape 0 → recommandation |
| Notifications FoodEatUp | ✅ couvert (briefing-du-jour, journee-du-dirigeant, routines R4/R7) |

---

## Recommandations (à arbitrer)

1. **Corrections documentaires : les 4 sont FAITES (2026-07-10)** — enum
   élargi + validation DGFiP d'`update_invoice_status` ; `equipment_id`
   requis d'`add_temperature` (hook étendu) ; piège `media_*` de
   `create_draft_tool` (convention vérifiée par appel réel) ;
   `type: "document"` → `doc` dans dossier-startup-360. Bonus :
   `delete_prompt` explicitement couvert par le hook garde-destructif
   rapidocms (attrapé par le motif `delete_.*`, test figé dans
   tester-skills.py).
2. **Arbitrage des 54 orphelins** selon les tableaux (a) : ~23 « couvrir »
   (petites extensions, souvent une ligne) et ~31 « ignorer volontairement »
   (CRUD unitaires atteignables à la demande directe, paramétrage
   d'installation, administration sensible).
3. **Généraliser `search_entities`** en Étape 0 des skills FoodEatUp
   (résolution nom parlé → ID, confirmation si `ambiguous=true`).
