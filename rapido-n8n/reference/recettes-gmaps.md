# Recettes de sourcing Google Maps — n8n

> Le **sourcing récurrent multi-zones DOIT vivre en n8n** (mémoire des jobs,
> anti-re-scraping, volume gouverné), **jamais en conversationnel**. Format maison :
> déclencheur, pseudo-nœuds, table mémoire, garde-fous. Identifiant au registre
> unifié (`GMAPS-*`). Installation **sur confirmation** via `usine-automatisations`
> — **aucun workflow créé d'office**. Prérequis : un mode d'exécution du scraper
> configuré (Docker local **ou** API SaaS `GMAPS_API_URL`/`GMAPS_API_KEY` en KB).

## GMAPS-HEBDO — sourcing ICP par zone (lundi 8h)

- **Déclencheur** : Schedule cron `0 8 * * 1`.
- **Workflow (pseudo-nœuds)** :
  Schedule → lire les **villes cibles** de `rapido-kb/scraping-config.md` →
  pour chaque ville : **HTTP POST** `${GMAPS_API_URL}/api/v1/scrape`
  (`{keyword:"restaurant in {ville}", lang, max_depth, email:true}`, header
  `X-API-Key`) → **polling** `GET /api/v1/jobs/{id}` jusqu'à complétion →
  **scoring ICP** (règle `score_leads_gmaps.py` : rating × ln(avis+1) × signal) →
  **déduplication** (`rechercher_prospects` par nom+ville) → **filtrer les
  nouveaux** (absents de `gmaps_jobs_journal`) → **import CRM** des nouveaux
  uniquement (`create_entreprise`/`create_contact` + tags `gmaps`,
  `opportunite-foodeatup` si signal) → **email interne** : N nouveaux, score moyen,
  taux de signal.
- **Table mémoire** : `gmaps_jobs_journal` (`date`, `ville`, `place_id`,
  `nom`, `score`, `signal`, `importe`) — **anti-re-scraping** d'une même zone dans
  la semaine et anti-doublon d'import.
- **Garde-fous** : plafonds volume (résultats/requête, requêtes/jour, délai entre
  jobs) **lus en KB** ; import en lot **confirmé** (hook `garde-scraping`) ;
  respect CGU/RGPD (emails B2B, opt-out, pas de revente) ; **aucun résultat
  inventé** — si un job échoue, il est journalisé et signalé, pas simulé.

> Réglages réels (villes, seuils, cadence) → `rapido-kb/scraping-config.md`,
> jamais en dur. La routine ne s'installe pas si aucun mode d'exécution n'est
> configuré (dégradation propre annoncée).
