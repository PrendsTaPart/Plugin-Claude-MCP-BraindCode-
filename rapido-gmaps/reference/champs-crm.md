# Mapping Entry (Google Maps) → RapidoCRM

Source vérifiée : `gmaps/entry.go` du scraper + sondes lecture seule RapidoCRM
(voir `docs/AUDIT-GMAPS.md`). Statut de chaque champ :

- **MAPPÉ** — outil + champ CRM confirmés.
- **PARTIEL** — l'outil existe mais la clé exacte du `payload` (objet générique)
  est à **confirmer au 1ᵉʳ usage réel** ; le skill lit la réponse du serveur
  pour se caler (« le serveur fait foi »).
- **MANQUANT** — aucun réceptacle CRM structuré → stocké en **note
  (`log_activity`) + tags** en attendant, et porté dans
  `docs/OUTILS-MCP-MANQUANTS.md` (backend Tunis). Aucune perte de donnée.

## Fiche prospect

| Champ Entry | Outil CRM | Cible | Statut |
|---|---|---|---|
| `title` | `create_entreprise` | `payload.nom` | **MAPPÉ** |
| `complete_address` (street/city/postal_code/country) · `address` | `create_entreprise` | `payload` adresse | **PARTIEL** |
| `phone` | `create_contact` / `create_entreprise` | `payload` téléphone | **PARTIEL** |
| `web_site` | `create_entreprise` | `payload` site web | **PARTIEL** |
| `emails[]` (avec `-email`) | `create_contact` | `payload` email → séquence outbound | **PARTIEL** |
| `latitude` + `longitude` | `prospecter_maps` | coordonnées (croisement géo) | **MAPPÉ** (outil dédié) |
| `thumbnail` / `images[]` | `rapidocms:upload_file_tool` | visuel pour le CRM | **MAPPÉ** (autre serveur) |

## Signaux & scoring (note + tag)

| Champ Entry | Traitement | Statut |
|---|---|---|
| `review_rating`, `review_count` | note `log_activity` + tag priorité ; entrent dans le score | **PARTIEL** (note libre) |
| `reviews_per_rating` | note (répartition des avis) | **MANQUANT** (pas de champ structuré) |
| `open_hours` | `create_rdv` (fenêtre d'appel recommandée) + note | **PARTIEL** |
| `popular_times` | note (moment de contact optimal) | **MANQUANT** (pas de champ structuré) |
| `order_online[]` ∧ `reservations[]` **vides** | tag `sans-systeme-numerique` (critère ICP FoodEatUp) | **PARTIEL** (tag) |
| `price_range`, `about[]`, `credit_cards_accepted` | note d'attributs | **MANQUANT** (note libre) |
| `place_id`, `cid`, `data_id` | note + tag (**clé de ré-scrape stable**) | **MANQUANT** (pas de champ dédié) |

## Pipeline & déduplication (outils confirmés)

- **Dédup obligatoire avant toute création** : `rechercher_prospects` (nom + ville)
  et, si SIRET connu, `rechercher_entreprise_siret` → exclure les doublons.
- **Entrée pipeline** : `enregistrer_prospect` (unitaire) ou
  `enregistrer_tous_prospects` (lot — **confirmation forcée** par le hook
  `garde-scraping`). `ajouter_prospect_pipeline` / `deplacer_prospect_etape`
  pour le placement dans le tunnel.
- **Traçabilité** : `log_activity("Sourcé Google Maps le {date}, score={x}, "
  "signal={…}")` sur chaque fiche importée.

## Tags posés à l'import

`gmaps` (source) · `sans-systeme-numerique` (si signal) · `opportunite-foodeatup`
(détection ICP) · tag de priorité selon le score. Les tags remplacent
provisoirement les champs structurés MANQUANTS.

> Les 3 items **MANQUANT** structurés (`place_id`/`cid`, score prospect,
> `popular_times`/`reviews_per_rating`) sont listés dans
> `docs/OUTILS-MCP-MANQUANTS.md` pour le backend Tunis. Décision produit :
> note + tag en attendant (aucun blocage).
