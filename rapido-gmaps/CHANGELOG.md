# Changelog — plugin rapido-gmaps

## 0.2.0 — 2026-07-15 — sourcing-gmaps (Google Maps → pipeline CRM)

- Skill **`sourcing-gmaps`** — de la requête Google Maps au pipeline CRM en
  chaîne confirmée : construction de requête + estimation de volume (confirmation),
  scrape (Docker local / API SaaS), scoring **par script**, déduplication
  obligatoire, validation top 20, import par lots de 10 confirmés, capitalisation
  KB. Positionnement explicite vs `prospecter_maps` (workflows N8N) — coexistence,
  déclencheurs distincts.
- `scripts/score_leads_gmaps.py` (stdlib) — score =
  `review_rating × ln(review_count+1) × signal_opportunite` (1.5 si sans système
  numérique : `order_online` ∧ `reservations` vides), tri décroissant, filtres ICP
  optionnels (min-rating / min-reviews / catégories). Formule affichée, jamais de
  calcul de tête.
- Évals : 4 cas (déclenchement, refus de volume, déduplication, anti-collision
  `prospecter_maps`).

## 0.1.0 — 2026-07-15 — Squelette (mapping CRM, garde-fous)

- Nouveau plugin **rapido-gmaps** (22e du marketplace) — sourcing de leads
  Google Maps → pipeline RapidoCRM, bâti sur `gosom/google-maps-scraper` (MIT).
  Le scraper est un binaire/API, **pas** un serveur MCP : Docker CLI local
  (ponctuel, 0 coût, 0 clé) **ou** API SaaS auto-hébergée (routines n8n) — les
  **deux** modes documentés (choix client). Aucune clé/URL client dans le dépôt.
- `.mcp.json` : rapidocrm (create/dedup/pipeline/log), foodeatup (contexte ICP),
  rapidocms (upload de vignettes).
- `reference/modes-execution.md` : CLI Docker / CLI natif / API REST / SaaS +
  règle de choix. `reference/champs-crm.md` : mapping Entry → CRM
  (MAPPÉ / PARTIEL / MANQUANT), items MANQUANT portés dans
  `docs/OUTILS-MCP-MANQUANTS.md`. `reference/garde-fous-scraping.md` : plafonds
  (500 résultats/requête, 3 requêtes/jour, 5 s entre jobs), RGPD (emails B2B =
  intérêt légitime + opt-out immédiat), CGU, déduplication obligatoire.
- **Hooks** : `garde-scraping` (ask sur volume `-depth`/`-radius` au-delà des
  seuils **et** sur import en lot `enregistrer_tous_prospects`) + `Stop` (récap
  requête/volume/IDs/dedup/score). Tests fonctionnels au testeur.
- Fondé sur l'audit **GMS0** (`docs/AUDIT-GMAPS.md`) : struct Entry, contrat API
  et mapping vérifiés sur source + binaire compilé en session. Skills, agent et
  routine `R-GMAPS-HEBDO` à venir (GMS2→GMS5).
