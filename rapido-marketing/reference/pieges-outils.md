# Pièges des outils marketing (3 serveurs Rapido)

Repris de l'audit `docs/MATRICE-COUVERTURE.md` (M0) et des schémas MCP live.
À charger avant tout appel d'écriture marketing.

## RapidoCRM

- **`create_editor_template`** : `type` ∈ `newsletter | site_web |
  landing_page | carte_visite | email_marketing | brochure`. **`landing_page`
  existe** (tunnel Rapido-first). `html` requis ; **appeler l'outil directement**
  avec le HTML (ne pas fabriquer de widget/artefact JS). Retourne l'URL d'édition.
- **`schedule_email`** : requis `entreprise_id`, `date_envoi`
  (`YYYY-MM-DD HH:MM:SS`), `sujet`. `target` ∈ Contacts | Employes | Entreprises.
  = **envoi** → confirmation (hook `garde-envois`).
- **`send_newsletter`** : requis `entreprise_id` ; `cible` ∈ Entreprises |
  Employes | Contacts ; sans `date_envoi` = **envoi immédiat**. → confirmation.
- **`create_segment`** : filtres `domaine_contient` / `ville_contient` ;
  `recalculer` pour rafraîchir. Vérifier le **consentement** avant d'exploiter le
  segment en séquence/audience (RGPD).
- **`get_formulaire_soumissions`** : renvoie vues, clics, **taux de conversion**,
  entreprise/segment liés, champs ; `{error, disponibles[]}` si introuvable.
- **`list_formulaires`** / **`list_cta`** : `{count, …[]}` — vide si aucun
  formulaire/CTA (ne pas conclure à une erreur).
- **`get_conversion_par_canal`** / **`get_stats_campagne`** :
  `{success, total, par_statut[]}` — conversion **single-touch par canal**
  (pas d'attribution multi-touch — cf. manques M0).
- **`prospecter_maps`/`prospecter_entreprise`/`prospecter_prospect`** : seuls
  workflows de sourcing **autorisés** (pas de scraping hors CRM — RGPD/garde-fous).

## RapidoCMS

- **`create_draft_tool`** : champs `media_*` requis **même pour un post texte**
  (`media_type: ""`, `media_url: ""`, `media_source: "biblio"`,
  `media_caption` = le texte). Un appel **par réseau**.
- **`schedule_draft_tool`** : `post_date` `Y-m-d`, `post_heure` **STRICT
  `H-i-s`** (tirets). = **publication programmée** → confirmation.
- **`ingishts_campagne`** : orthographe serveur (« ingishts »), pas « insights ».
- **`post_insights`** : `post_ids` **≤ 10** par appel.
- **`images_to_image`** : URLs publiques **< 5 Mo**, **≤ 3** références ;
  couleurs **non validées** côté serveur (valider l'hex avant).
- Marque : `get_brand(nom)` renvoie un **tableau** ; `upload_file_tool` ne
  renvoie **pas** d'id (résoudre via `list_all_files`) ; `remove_asset` prend
  l'id du **lien** (voir `rapidocms/reference/outils-marque.md`).

## RapidoRH

- Outils orientés **projet/équipe** (`create-project-tool`, `create-task-tool`,
  `get-dailies-tool`, `get-users-list-tool`) — pas d'outil marketing direct ;
  usage marketing = **capacité de delivery** et **marque employeur**.
- Suppressions (`delete-user-tool`, `delete-project-link-tool`) = destructif
  (hook `garde-destructif` du plugin rapidorh).

## Renvois
- Priorité des serveurs : `reference/priorite-mcp.md`.
- Garde-fous : `reference/garde-fous-marketing.md`.
