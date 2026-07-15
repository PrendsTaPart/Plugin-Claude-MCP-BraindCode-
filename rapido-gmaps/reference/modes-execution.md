# Modes d'exécution — rapido-gmaps

Le scraper `gosom/google-maps-scraper` (MIT) n'est **pas un serveur MCP** : il
s'exécute en **binaire** (CLI/Docker) ou s'expose en **API REST**. Le plugin
l'orchestre via des commandes shell (Bash) et le pontage vers RapidoCRM se fait
par les outils MCP. **Aucune clé, aucune URL client n'est stockée dans le dépôt** —
l'URL de l'API et les seuils vivent dans `rapido-kb/scraping-config.md` (hors dépôt).

Le marketplace privilégie **deux modes** (choix client) :

## 1. Docker CLI local — scrapes manuels ponctuels (0 coût, 0 clé)

À utiliser quand vous demandez un sourcing à la volée depuis votre poste.

```
docker run -v "$PWD/out":/out gosom/google-maps-scraper \
  -input /out/query.txt -results /out/results.json -json \
  -depth 1 -c 1 -exit-on-inactivity 3m
```

- **Prérequis** : Docker installé et **daemon actif** (`docker info`).
- `-input` = fichier de requêtes (une par ligne) ; `-json` = sortie JSON
  (sinon CSV) ; `-depth` = profondeur de défilement ; `-email` = crawl des
  emails du site (plus lent) ; `-extra-reviews` = avis additionnels ;
  `-fast-mode` = extraction rapide HTTP (≈ 21 résultats max/requête, données
  réduites) ; `-geo "lat,lon"` + `-radius km` = zone précise ; `-proxies` =
  proxys (format `protocole://user:pass@hote:port`).
- **Variante sans Docker** : le binaire se compile en natif (`go build .`,
  Go ≥ 1.24) et fonctionne à l'identique (driver Playwright + Chromium requis).
  Vérifié en session ; voir `docs/AUDIT-GMAPS.md`.

## 2. API REST SaaS auto-hébergée — routines automatisées (n8n)

À utiliser pour les routines récurrentes (R-GMAPS-HEBDO). Le service tourne sur
**votre VPS** (à côté de n8n) ; le plugin l'appelle en HTTP.

- **Prérequis** : service déployé (`docker-compose.saas.yaml` : app + PostgreSQL,
  ou script `PROVISION` pour un VPS), **URL de base** et **clé API** consignées
  dans `rapido-kb/scraping-config.md` (`GMAPS_API_URL`, `GMAPS_API_KEY`).
- **Créer un job** :

  ```
  curl -s -X POST "$GMAPS_API_URL/api/v1/scrape" \
    -H "X-API-Key: $GMAPS_API_KEY" -H "Content-Type: application/json" \
    -d '{"keyword":"restaurant gastronomique Lyon France","lang":"fr","max_depth":1,"email":true}'
  ```

- **Suivre puis récupérer** : `GET /api/v1/jobs/{id}` (statut + résultats) ;
  `GET /api/v1/jobs/{id}/download` (CSV). Auth : header `X-API-Key` **ou**
  `Authorization`. Champs du corps : `keyword` (**singulier**, requis), `lang`,
  `max_depth` (défaut 1, max 100), `email`, `geo_coordinates` ("lat,lon"),
  `zoom` (1-21), `radius` (km), `fast_mode`, `extra_reviews`, `timeout`
  (1-300 s, défaut 300).

## Règle de choix

| Besoin | Mode |
|---|---|
| « Trouve-moi des restaurants à Lyon » (ponctuel, interactif) | **Docker CLI local** |
| Sourcing hebdo automatique multi-villes (R-GMAPS-HEBDO) | **API SaaS** (via n8n) |
| Aucun des deux configuré | Dégradation propre : le skill l'annonce et s'arrête (jamais d'invention de résultats) |

> **Portabilité** : ni l'URL de l'API, ni la clé, ni les villes cibles ne sont
> écrites dans le dépôt. Tout ce qui est propre au client va dans
> `rapido-kb/scraping-config.md` (gitignoré).
