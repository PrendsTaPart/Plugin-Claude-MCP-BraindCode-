# Audit — google-maps-scraper → rapido-gmaps (GMS0)

**Date** : 2026-07-15 · **Repo scraper** : `gosom/google-maps-scraper` (MIT),
inspecté par clonage direct (`--depth 1`, HEAD `develop`) et **compilé nativement**
en session (Go 1.24.7). **Portée** : audit uniquement — **aucune** création de skill,
**aucune** écriture CRM. Sondes CRM = **lecture seule**.

> **Résumé décision** : la chaîne technique est **prouvée fonctionnelle** en session
> jusqu'à la navigation Google Maps ; le seul point bloquant ici est **l'egress
> réseau du navigateur vers Google Maps** (limite du bac à sable, pas du scraper).
> Le mapping CRM et les modes d'exécution sont établis sur **source vérifiée**.
> **GO** pour construire le plugin (GMS1→GMS4) ; la **recette réelle** (GMS0 §mesures
> live + GMS5) doit tourner **là où Google Maps est joignable** : Docker local sur
> votre poste, ou l'API SaaS déployée sur votre VPS. **STOP** pour vos 3 décisions
> (fin de document).

---

## 1. Ce qui a été exécuté en session (faits réels)

| Étape | Résultat | Preuve |
|---|---|---|
| Clone du repo | OK | `git clone --depth 1` → 100+ fichiers, `go.mod` = `github.com/gosom/google-maps-scraper` |
| **Build natif Go** | **OK** | binaire de **79 Mo** produit (`go build .`, exit 0) — pas besoin de Docker pour compiler |
| Driver Playwright 1.60.0 | Contourné | Le CDN pinné `playwright.azureedge.net/…/driver/playwright-1.60.0-linux.zip` renvoie **404** (endpoint retiré). Résolu en réutilisant un driver npm `playwright@1.60.0` via `PLAYWRIGHT_DRIVER_PATH` |
| Téléchargement navigateur | OK | Chromium 148 (build v1223) tiré de `cdn.playwright.dev` (CDN vivant), lancé sans erreur |
| Moteur `scrapemate` | OK | démarre, crée le job `GET https://www.google.com/maps/search/restaurant+gastronomique+Lyon+France?hl=en` |
| **Navigation Google Maps** | **BLOQUÉ (réseau)** | sans proxy : `net::ERR_CONNECTION_RESET` ; via le proxy agent (`-proxies http://…`) : `net::ERR_CONNECTION_CLOSED`. `curl` vers la même URL passe (HTTP 200, page brute) mais la **session navigateur automatisée** n'est pas portée jusqu'à Google |

**Temps mesurés en session (indicatifs Linux, étiquetés — PAS des temps de scrape réels)** :
build ≈ (téléchargement deps + compilation) sous 8 min ; téléchargement navigateur ≈ 68 s
(première fois seulement) ; tentative de navigation avant échec ≈ 52 s (timeout DOM).
**Les temps de scrape réels, le taux de récupération d'emails et le test SaaS API
restent à mesurer** sur un environnement où Google Maps est joignable (voir §6).

**Pourquoi bloqué ici, pas en production** : le bac à sable route le trafic *outils/API*
via un proxy d'agent ; la navigation navigateur vers `google.com/maps` est réinitialisée
(RST/close). En **Docker local** (votre poste) ou en **SaaS sur votre VPS**, cette
contrainte n'existe pas — c'est précisément le mode d'exécution privilégié du plugin.

---

## 2. Struct `Entry` complète (vérifiée depuis `gmaps/entry.go`)

Tous les champs extraits par le scraper, avec type Go et clé JSON réelle.

| Champ Go | Clé JSON | Type | Exemple / note |
|---|---|---|---|
| `ID` | `input_id` | string | id de la requête d'entrée |
| `Link` | `link` | string | URL de la fiche Maps |
| `Cid` | `cid` | string | identifiant Google (customer id) |
| `Title` | `title` | string | « Le Neuvième Art » |
| `Categories` | `categories` | []string | ["Restaurant gastronomique", …] |
| `Category` | `category` | string | catégorie principale |
| `Address` | `address` | string | adresse en une ligne |
| `OpenHours` | `open_hours` | map[string][]string | { "Monday": ["12–14","19–22"], … } |
| `PopularTimes` | `popular_times` | map[string]map[int]int | jour → { heure → affluence } |
| `WebSite` | `web_site` | string | site officiel |
| `Phone` | `phone` | string | téléphone affiché |
| `PlusCode` | `plus_code` | string | code Plus Google |
| `ReviewCount` | `review_count` | int | 812 |
| `ReviewRating` | `review_rating` | float64 | 4.7 |
| `ReviewsPerRating` | `reviews_per_rating` | map[int]int | { 5: 600, 4: 150, … } |
| `Latitude` | `latitude` | float64 | 45.7640 |
| `Longtitude` | `longtitude` **+** `longitude` | float64 | ⚠️ champ mal orthographié (`longtitude`) conservé pour rétro-compat ; le JSON émet **aussi** `longitude` correct, et accepte les deux en entrée |
| `Status` | `status` | string | "Operational" / "Permanently closed" |
| `Description` | `description` | string | descriptif |
| `ReviewsLink` | `reviews_link` | string | lien vers les avis |
| `Thumbnail` | `thumbnail` | string | URL vignette |
| `Timezone` | `timezone` | string | "Europe/Paris" |
| `PriceRange` | `price_range` | string | "€€€" |
| `DataID` | `data_id` | string | identifiant interne |
| `StreetViewURL` | `street_view_url` | string | lien Street View |
| `PlaceID` | `place_id` | string | **clé de ré-scrape** d'une fiche |
| `Images` | `images` | []Image | { title, image } |
| `Reservations` | `reservations` | []LinkSource | { link, source } — **[] = pas de résa en ligne** |
| `OrderOnline` | `order_online` | []LinkSource | **[] = pas de commande en ligne** |
| `Menu` | `menu` | LinkSource | { link, source } |
| `Owner` | `owner` | Owner | { id, name, link } |
| `CompleteAddress` | `complete_address` | Address | { borough, street, city, postal_code, state, country } |
| `CreditCardsAccepted` | `credit_cards_accepted` | []string | ["Visa","Mastercard"] |
| `About` | `about` | []About | { id, name, options[] } — attributs (terrasse, accès PMR…) |
| `UserReviews` | `user_reviews` | []Review | avis (voir type Review) |
| `UserReviewsExtended` | `user_reviews_extended` | []Review | avis additionnels (`-extra-reviews`) |
| `Emails` | `emails` | []string | **peuplé seulement avec `-email`** (crawl du site) |

**Types imbriqués** (source) :
`Image{title,image}` · `LinkSource{link,source}` · `Owner{id,name,link}` ·
`Address{borough,street,city,postal_code,state,country}` ·
`About{id,name,Options[]}` avec `Option{name,enabled,values[]}` ·
`Review{Name,Rating,Description,When,review_id,rating_float,author_url,
posted_at_unix_micros,text_original,text_translated,language,reply_text,…}`.

**Champs souvent vides** (par conception) : `Emails` (nécessite `-email`) ;
`UserReviewsExtended` (nécessite `-extra-reviews`) ; `PopularTimes`, `About`,
`CreditCardsAccepted`, `Owner`, `PriceRange` (dépendent de ce que Google publie
pour la fiche — variables selon les établissements).

---

## 3. Contrat API REST (vérifié depuis `api/`)

**Endpoints** (`api/api.go`, préfixe `/api/v1`) :

| Méthode | Route | Rôle |
|---|---|---|
| GET | `/api/v1/health` | santé du service |
| POST | `/api/v1/scrape` | créer un job → renvoie un `id` |
| GET | `/api/v1/jobs` | lister les jobs (`?state=&limit=&cursor=`) |
| GET | `/api/v1/jobs/{job_id}` | statut + résultats d'un job |
| GET | `/api/v1/jobs/{job_id}/download` | télécharger les résultats en CSV (README) |
| DELETE | `/api/v1/jobs/{job_id}` | supprimer un job |

**Auth** (`api/middleware.go`) : header `Authorization` **ou** `X-API-Key`.

**Corps `POST /api/v1/scrape`** (`ScrapeRequest`, `api/responses.go`) :

| Champ JSON | Type | Défaut / borne | Rôle |
|---|---|---|---|
| `keyword` | string | **requis** | « restaurants in New York » (⚠️ **singulier** `keyword`) |
| `lang` | string | "en" | code langue des résultats |
| `max_depth` | int | 1 (max 100) | profondeur de pagination |
| `email` | bool | false | crawl des emails du site |
| `geo_coordinates` | string | — | "lat,lon" |
| `zoom` | int | 14 | niveau de zoom (1-21) |
| `radius` | float | — | rayon en km |
| `fast_mode` | bool | false | mode HTTP furtif (données réduites, ~21 résultats max/requête) |
| `extra_reviews` | bool | false | avis additionnels |
| `timeout` | int | 300 | timeout du job en s (1-300) |

**Serveur** : écoute sur `:8080` (`-addr`). Le SaaS (`docker-compose.saas.yaml`)
ajoute **PostgreSQL 15** + migrations (river queue). Le dev
(`docker-compose.dev.yaml`) = Postgres + `migrate`.

---

## 4. Modes d'exécution (prérequis de chacun)

| Mode | Commande / accès | Prérequis | Quand l'utiliser |
|---|---|---|---|
| **CLI Docker** | `docker run gosom/google-maps-scraper -input q.txt -results out.json -json -depth 1` | **Docker daemon actif** | scrapes **manuels ponctuels**, 0 coût, 0 clé |
| **CLI natif** | binaire Go compilé (`go build .`) + Playwright driver 1.60.0 + Chromium | Go **ou** binaire pré-buildé ; navigateur | idem, sans Docker (prouvé en session) |
| **API REST** | `POST /api/v1/scrape` + polling `GET /jobs/{id}` sur `:8080` | service lancé (dev ou SaaS) + `X-API-Key` | **routines n8n** automatisées |
| **SaaS auto-hébergé** | déploiement multi-users (script `PROVISION`, DigitalOcean/Hetzner) | **VPS** + Postgres | production, multi-zones, workers |

**Formats de sortie** : CSV (défaut), JSON (`-json`), PostgreSQL, S3, LeadsDB.
**⚠️ En session** : le **daemon Docker n'est pas actif** (`docker info` échoue) →
les modes Docker/SaaS n'ont **pas** pu être testés ici ; le mode **CLI natif** a été
bâti et lancé avec succès (bloqué seulement à l'egress Google, voir §1).

---

## 5. Mapping Entry → RapidoCRM (croisé avec les outils réels)

Statut : **MAPPÉ** (champ CRM confirmé) · **PARTIEL** (outil existe, clé de `payload`
exacte à confirmer au 1ᵉʳ usage réel — le `payload` CRM est un objet générique) ·
**MANQUANT** (aucun réceptacle structuré → candidat `OUTILS-MCP-MANQUANTS.md`).

Sonde lecture seule effectuée : `list_entreprises`/`get_entreprise` → l'entreprise
expose au minimum `id`, `nom`, `created_at`, `updated_at` ; `list_contacts` → `id`,
`nom`. Les enregistrements testés sont **peu remplis** → les clés `payload` complètes
(téléphone, site, email, adresse) sont à **valider au 1ᵉʳ usage** (à consigner dans
`reference/champs-crm.md`, GMS1).

| Champ Entry | Outil CRM cible | Champ / usage | Statut |
|---|---|---|---|
| `title` | `create_entreprise` | `payload.nom` (confirmé) | **MAPPÉ** |
| `complete_address.*` / `address` | `create_entreprise` | `payload` adresse (rue/ville/CP/pays) | **PARTIEL** |
| `phone` | `create_contact` / `create_entreprise` | `payload` téléphone | **PARTIEL** |
| `web_site` | `create_entreprise` | `payload` site web | **PARTIEL** |
| `emails[]` (avec `-email`) | `create_contact` | `payload` email → séquence outbound | **PARTIEL** |
| `latitude` + `longitude` | `prospecter_maps` (coordonnées) | croisement géo | **MAPPÉ** (outil dédié existe) |
| `review_rating`, `review_count` | `log_activity` + tag CRM | note de priorité prospect | **PARTIEL** (via note libre) |
| `open_hours` | `create_rdv` | fenêtre d'appel recommandée | **PARTIEL** |
| `popular_times` | `log_activity` (note) | moment de contact optimal | **PARTIEL** (pas de champ structuré) |
| `order_online[]`+`reservations[]` vides | tag « sans-systeme-numerique » | critère ICP FoodEatUp | **PARTIEL** (tag/note) |
| `thumbnail` / `images[]` | `rapidocms:upload_file_tool` | visuel pour CRM | **MAPPÉ** (autre serveur) |
| `place_id`, `cid`, `data_id` | — | **clé de ré-scrape/enrichissement** | **MANQUANT** (aucun champ CRM dédié — à stocker en note/tag ; candidat outil) |
| `reviews_per_rating`, `popular_times` (structuré) | — | analytics prospect structurés | **MANQUANT** |
| `about[]`, `credit_cards_accepted` | — | attributs structurés | **MANQUANT** (note libre) |

**Déduplication (obligatoire avant toute création)** : `rechercher_prospects(q=nom+ville)`
et, si SIRET connu, `rechercher_entreprise_siret` → exclure les doublons. Outils confirmés
présents dans le catalogue RapidoCRM.

**Pipeline** : `ajouter_prospect_pipeline` / `enregistrer_prospect` /
`enregistrer_tous_prospects` (lot) confirmés → alimentation directe du tunnel.

> **Entrées à porter dans `docs/OUTILS-MCP-MANQUANTS.md` (GMS1)** : (1) champ/relation
> pour stocker `place_id`/`cid` sur une fiche (clé de ré-scrape stable) ; (2) champ
> « score prospect » structuré ; (3) stockage structuré `popular_times`/`open_hours`.
> Tant qu'ils manquent : note `log_activity` + tags (dégradation propre, jamais de perte).

---

## 6. GO / NO-GO par prompt (GMS1 → GMS5)

| Prompt | Verdict | Raison |
|---|---|---|
| **GMS1** squelette (reference + hooks) | **GO** | modes + mapping + garde-fous établis sur source ; aucun prérequis réseau |
| **GMS2** `sourcing-gmaps` | **GO (build)** | pipeline requête→scoring→dedup→import spécifiable ; le **scoring** `score_leads_gmaps.py` (stdlib) est testable hors-ligne. ⚠️ la **démo live** de scrape nécessite Google joignable (Docker local / SaaS VPS) |
| **GMS3** enrichissement + détection | **GO (build)** | logique diff-CRM + filtre ICP FoodEatUp (`order_online=[]` ∧ `reservations=[]`) directe depuis les champs vérifiés |
| **GMS4** veille-concurrents + agent | **GO** | s'appuie sur les mêmes champs ; agent = orchestration |
| **GMS5** routine n8n + recette réelle + release | **CONDITIONNEL** | la **recette réelle** exige un environnement où Google Maps est joignable **et** l'API SaaS déployée → dépend de vos décisions §7 |

**Principe à encoder (GMS1)** — pattern « construire d'abord » (comme le squelette
ElevenLabs) : skills écrits d'après les grammaires vérifiées ci-dessus, dégradation
propre tant que le binaire/l'API n'est pas configuré côté client, **recette réelle
déférée** au poste/VPS du client. Aucun chiffre de scrape inventé.

---

## 7. STOP — 3 décisions requises avant GMS1

1. **Hébergement de l'exécution** : (a) **Docker CLI local** sur votre poste pour les
   scrapes ponctuels (0 coût, 0 clé) — recommandé pour démarrer ; et/ou (b) **API SaaS
   sur votre VPS** (à côté de n8n) pour les routines — dans ce cas, quelle **URL de
   base** et faut-il que je documente la structure `X-API-Key` dans `reference/` ?
2. **Confort CGU/RGPD** : validez le cadre encodé dans `garde-fous-scraping.md`
   (volumes plafonnés, délais entre requêtes, emails B2B = intérêt légitime + opt-out
   immédiat, dédup obligatoire, pas de revente). Un plafond par défaut vous convient-il
   (proposé : 500 résultats/requête, 3 requêtes/jour, 5 s entre jobs — éditables en KB) ?
3. **Complétude du mapping** : OK pour traiter `place_id`/`cid`, score structuré et
   `popular_times` comme **note/tag** en attendant les outils CRM dédiés (portés dans
   `OUTILS-MCP-MANQUANTS.md`) — ou préférez-vous attendre ces outils côté backend Tunis ?

---

*Sources : `gosom/google-maps-scraper` (`gmaps/entry.go`, `api/api.go`,
`api/responses.go`, `api/middleware.go`, `docker-compose.*.yaml`, `README.md`),
binaire compilé en session, et sondes lecture seule RapidoCRM. Aucune donnée de
scrape inventée — les mesures live manquantes sont explicitement étiquetées « à
mesurer » (§1, §4, §6).*
