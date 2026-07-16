# NOTICE — rapido-gmaps

Ce plugin **réimplémente des patterns** d'un scraper open source **sous licence MIT** —
il **ne redistribue aucun code source** : la structure de requête/réponse de l'API et le
pattern « construire d'abord » sont **ré-encodés maison**. Détail : `docs/AUDIT-GMAPS.md`.

## Source MIT (patterns réimplémentés, code non redistribué)

| Dépôt | Licence | Ce qui est repris |
|---|---|---|
| [gosom/google-maps-scraper](https://github.com/gosom/google-maps-scraper) | MIT (© gosom) | **Structure des champs extraits** (clés JSON réelles), **forme de l'API** (`POST /api/v1/scrape`, `GET /api/v1/jobs`), mode **CLI Docker** — ré-encodés dans le plugin ; **aucun fichier Go copié** |

## Exclusions (règle maison)

- **Aucun code source du scraper fusionné** : le dépôt a été cloné en audit
  (`git clone --depth 1`), lu, puis les patterns distillés — rien n'est redistribué.
- Le scraping réel passe par le **Docker/API du client** (variables d'environnement) ;
  aucune clé ni donnée client dans le dépôt.
