# Audit de vérité — serveurs foodeatup / rapidocrm / rapidocms (2026-07-10)

**Méthode** : introspection des serveurs MCP réellement connectés à la session
du 2026-07-10 (catalogues live : **foodeatup 112 outils, rapidocrm 103,
rapidocms 43** — dont 7 outils apparus EN COURS de session), croisée avec les
outils cités en backticks dans les `SKILL.md` des plugins `foodeatup/`,
`rapidocrm/`, `rapidocms/` (les agents et `reference/` ne sont pas comptés
dans le croisement). **Aucun skill n'a été modifié** — cet audit constate.

Outils apparus en session (serveurs en évolution) :
`search_entities`, `update_kds_item_status` (FoodEatUp) ; `add_asset`,
`create_brand`, `edit_brand`, `delete_brand`, `remove_asset` (RapidoCMS).

---

## (a) Outils JAMAIS cités par les SKILL.md des 3 plugins — « les nouveaux »

Lecture : beaucoup de CRUD unitaires sont volontairement non cités (les
workflows passent par les `list_*`/outils de plus haut niveau) — les vrais
« nouveaux » sont les clusters fonctionnels de la section 4.

### foodeatup — 52/112 jamais cités

CRUD unitaires probablement volontaires (couverts par les workflows) :
`assign_task`, `create_category`, `create_client`, `create_dish`,
`create_dish_category`, `create_expense`, `create_ingredient`,
`create_product`, `create_quote`, `create_supplier`, `create_tva`,
`delete_category`, `delete_client`, `delete_dish`, `delete_employee`,
`delete_ingredient`, `delete_product`, `delete_recipe`, `get_client`,
`get_employee`, `get_expense`, `get_ingredient`, `get_invoice`,
`get_product`, `get_quote`, `list_clients` *(cité ailleurs : rapido-meta-ads,
rapido-startup)*, `list_deliveries`, `list_ingredients`, `list_quotes`,
`list_stocks`, `list_tva`, `list_units`, `update_category`, `update_client`,
`update_employee`, `update_employee_schedule`, `update_ingredient`,
`update_product`, `update_quote_status`.

Fonctionnels non couverts (→ section 4) : `list_cleaning_actions`,
`list_cleaning_zones`, `record_cleaning_action` (nettoyage),
`list_employee_contracts`, `list_employee_documents` (contrats employés),
`create_haccp_tracabilite`, `list_haccp_tracabilite`, `list_haccp_labels`
(traçabilité — create_haccp_label est cité, la lecture non),
`create_notification`, `list_notifications` (notifications),
`update_invoice_status` (statut de facture restaurant — voir aussi (c)),
`search_entities` **[NOUVEAU]**, `update_kds_item_status` **[NOUVEAU]**.

### rapidocrm — 36/103 jamais cités

CRUD unitaires probablement volontaires : `create_contact`,
`create_entreprise`, `create_task`, `get_contacts_segment`, `list_rdvs`,
`list_segments` *(tous cités ailleurs dans le dépôt)*, `create_product`,
`create_user`, `delete_contact`, `delete_entreprise`, `delete_product`,
`delete_template_email`, `delete_template_sms`, `get_product`, `get_user`,
`list_editor_templates`, `list_entreprises`, `list_newsletters`,
`update_contact`, `update_contrat_template`, `update_entreprise`,
`update_product`, `get_interaction_stats`.

Fonctionnels non couverts (→ section 4) : `create_depense` (dépenses —
list_depenses est cité, la création non), `lancer_sondage_entreprise`,
`get_sondage_resultats`, `list_sondages`, `lancer_jeu_concours_entreprise`,
`list_jeux_concours`, `get_loyalty_points` (sondages/concours/fidélité),
`list_formulaires`, `get_formulaire_soumissions`, `list_cta`
(formulaires + CTA), `create_commercial`, `delete_commercial`,
`update_commercial_profil` (cycle de vie commerciaux — le pilotage
get/list/objectifs/statut/performance est déjà cité).

### rapidocms — 12/43 jamais cités

`delete_draft_tool`, `delete_prompt`, `edit_campagne`, `edit_digital_card`,
`edit_draft_tool`, `list_all_files`, `list_digital_card` *(cité ailleurs :
rapido-canva)* — éditions/suppressions unitaires, faible enjeu (le hook
garde-destructif couvre les delete_*).

**Assets de marque — cluster entier NOUVEAU** : `create_brand`, `edit_brand`,
`delete_brand`, `add_asset`, `remove_asset` (voir (c) pour le schéma).

---

## (b) Outils cités mais ABSENTS des serveurs — à corriger

**AUCUN.** Zéro outil fantôme dans les 3 plugins : chaque nom d'outil cité
existe tel quel sur son serveur. (L'extraction remonte 16 tokens qui sont en
réalité des noms de PARAMÈTRES cités en backticks — `post_date`,
`post_heure`, `post_id`, `post_ids`, `post_name`, `post_type`,
`reservation_id`, `search`, `set` — pas des outils. Faux positifs assumés.)

---

## (c) Écarts de paramètres — schémas live vs ce que documentent les skills

| Outil | Schéma LIVE (2026-07-10) | Ce que dit le dépôt | Verdict |
|---|---|---|---|
| `update_invoice_status` (FoodEatUp) | **CHANGÉ** — `status` est un ENUM élargi : `brouillon, en_attente, envoyee, acceptee, refusee, litige, payee, annulee` ; description : « en respectant les transitions légales autorisées (DGFiP) » → **le serveur valide lui-même les transitions** | pieges-outils (suite/startup) : « la vérification DGFiP ne s'applique qu'aux factures CRM, statuts FoodEatUp non vérifiés (schéma différent) » ; devis-facture-relance (CRM) le dit « FoodEatUp-only » ✓ | ⚠️ ÉCART DOC : 5 statuts nouveaux (envoyee/acceptee/refusee/litige/annulee) et validation DGFiP native côté serveur — nos références FoodEatUp sont en retard d'une version. Le hook ask (garde-destructif) reste pertinent en confirmation |
| `add_temperature` (FoodEatUp) | `establishment_id` + **`equipment_id` REQUIS** + `temperature` + `measured_at` optionnel (ISO 8601) | Les skills HACCP et le hook anti-donnee-inventee ne nomment que `temperature` (+ establishment_id) | ⚠️ ÉCART : `equipment_id` obligatoire non documenté — le nouveau `search_entities` (« frigo 3 » → ID) est justement fait pour le résoudre |
| `create_draft_tool` (CMS) | `required` inclut `media_type`, `media_source`, `media_url`, `media_caption` **même quand `post_type` = `text`** ; `media_source` default `biblio` ✓ ; `post_type` ∈ media/text/mediatext ; `social_type` ∈ linkedin/facebook/instagram/tiktok | media_source « biblio » documenté ✓ ; l'exigence des champs media_* en post TEXTE n'est nulle part | ⚠️ PIÈGE NON DOCUMENTÉ à ajouter aux pieges-outils |
| `upload_file_tool` (CMS) | `type` ∈ `image, video, doc` | dossier-startup-360 (rapido-suite) écrit `type: "document"` | ❌ ÉCART CONNU toujours ouvert (signalé le 2026-07-06, en attente d'arbitrage) : `document` → `doc` |
| `generate_image` (CMS) | `prompt` + `size` (`hd`/`standard`), RIEN d'autre | prompt-engineering-visuel / prompts-visuels-pro : pas de paramètre négatif dédié, négatif en fin de prompt ✓ ; size hd/standard ✓ | ✅ conforme |
| `post_insights` (CMS) | `post_ids` array, **max 10** | « découper en lots de 10 » ✓ | ✅ conforme |
| `schedule_draft_tool` (CMS) | `post_date` `Y-m-d`, `post_heure` **strict `H-i-s`** | pieges-outils ✓ (revérifié ce jour) | ✅ conforme |
| `search_entities` (FoodEatUp) **[NOUVEAU]** | `establishment_id` + `query` ; `types` ∈ product/ingredient/dish/equipment/table/recipe ; fuzzy FR (accents, pluriels) ; **si `ambiguous=true` → DEMANDER confirmation avant d'agir** | inexistant dans le dépôt | 🆕 à câbler (résout le piège « establishment_id/IDs devinés ») |
| `create_brand` (CMS) **[NOUVEAU]** | requis `nom`, `langue`, `slogan` ; `couleurs` = hex séparés par virgules ; `font_family` = ENUM de piles web-safe ; `logo` = URL publique | inexistant dans le dépôt | 🆕 à câbler (écriture de marque = confirmation, delete_brand sous garde-destructif) |

---

## (4) Clusters attendus — état

| Cluster | Outils (serveur) | État |
|---|---|---|
| Dépenses CRM | create_depense, list_depenses | ½ couvert : lecture citée, création jamais |
| Sondages / concours / fidélité CRM | lancer_sondage_entreprise, get_sondage_resultats, list_sondages, lancer_jeu_concours_entreprise, list_jeux_concours, get_loyalty_points | **6/6 jamais cités → candidat skill** (animation client) |
| Formulaires + CTA CRM | list_formulaires, get_formulaire_soumissions, list_cta | **3/3 jamais cités → candidat skill** (capture de leads) |
| Gestion commerciaux CRM | 8 outils | Pilotage déjà couvert (5/8 cités) ; cycle de vie create/delete/update_profil jamais cité |
| Bibliothèque de prompts CMS | add/list/edit/delete_prompt | Couvert (3/4) ; delete_prompt jamais cité (garde-destructif le couvre) |
| **Assets de marque CMS** | create/edit/delete_brand, add/remove_asset | **5/5 NOUVEAUX, jamais cités → candidat skill** (gestion de marques multiples) |
| **KDS FoodEatUp** | update_kds_item_status | **NOUVEAU, jamais cité → candidat skill** (écran cuisine) |
| Nettoyage FoodEatUp | list_cleaning_zones/actions, record_cleaning_action | **3/3 jamais cités → candidat extension** du skill haccp-conformite-quotidienne |
| Contrats employés FoodEatUp | create/list_employee_contracts, list_employee_documents | Création citée, lecture jamais → extension planning-equipe |
| Plan de salle | floor_plan_status | ✅ couvert (service-salle) |
| **Recherche transverse** | search_entities | **NOUVEAU, jamais cité → à câbler PARTOUT** (Étape 0 des skills FoodEatUp : nom parlé → ID) |
| Notifications FoodEatUp | create_notification, list_notifications | 2/2 jamais cités → candidat extension (briefing-du-jour, alertes) |

---

## Recommandations (rien n'est modifié — à arbitrer)

1. **Corrections documentaires prioritaires** : statuts update_invoice_status
   FoodEatUp (enum élargi + validation serveur), `equipment_id` requis
   d'add_temperature, piège media_* de create_draft_tool, et l'écart
   `type: "document"` → `doc` de dossier-startup-360 (ouvert depuis le 06/07).
2. **Câbler `search_entities`** dans les directives foodeatup (résolution
   nom → ID, confirmation si ambiguous) — supprime une classe entière
   d'erreurs d'ID.
3. **3 candidats skills** : assets de marque CMS, animation client CRM
   (sondages/concours/fidélité), KDS cuisine FoodEatUp.
4. **3 candidats extensions** : nettoyage (haccp-conformite-quotidienne),
   formulaires/CTA (prospection-pipeline ou campagne-marketing),
   notifications (briefing-du-jour).
