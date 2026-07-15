# rapido-gmaps — Google Maps → pipeline RapidoCRM

Le **chaînon manquant de la prospection** : sourcer des leads directement depuis
Google Maps (nom, téléphone, email, note, horaires, signaux d'opportunité),
les **scorer**, les **dédupliquer** et les verser dans le pipeline RapidoCRM —
puis enrichir des fiches existantes et faire de la veille concurrentielle.

Bâti sur `gosom/google-maps-scraper` (MIT). Le scraper n'est **pas** un serveur
MCP : il tourne en **Docker/CLI local** (scrapes ponctuels, 0 coût, 0 clé) ou en
**API REST auto-hébergée** (routines n8n). Le pontage vers le CRM passe par les
outils MCP RapidoCRM / FoodEatUp / RapidoCMS.

## État : squelette (0.1.0)

Fondations posées ; les skills arrivent (sourcing, enrichissement, détection
d'opportunités FoodEatUp, veille concurrents) + l'agent chasseur-leads et la
routine `R-GMAPS-HEBDO`. Voir `CHANGELOG.md` et l'audit `docs/AUDIT-GMAPS.md`.

## Prérequis

- **Un** des deux modes d'exécution (voir `reference/modes-execution.md`) :
  - **Docker** installé et actif (`docker info`) — pour le CLI local ; **ou**
  - **API SaaS** déployée sur votre VPS + `GMAPS_API_URL` / `GMAPS_API_KEY`
    dans `rapido-kb/scraping-config.md`.
- Serveurs MCP RapidoCRM (obligatoire), FoodEatUp et RapidoCMS (croisements)
  connectés — voir le README racine, section « Connecter ou héberger les MCP ».
- Sans mode d'exécution configuré : **dégradation propre** — les skills
  l'annoncent et s'arrêtent, aucun résultat inventé.

## Garde-fous (déterministes)

- **`garde-scraping`** (PreToolUse) — confirmation forcée quand une commande de
  scraping dépasse les seuils de volume (`-depth` / `-radius`), et sur tout
  import CRM en lot (`enregistrer_tous_prospects`).
- **CGU / RGPD / volumétrie** — plafonds, délais, opt-out B2B, déduplication
  obligatoire, pas de revente : `reference/garde-fous-scraping.md` (éditable en
  `rapido-kb/scraping-config.md`).
- **Stop** — récapitulatif exigé (requête, volume, IDs CRM créés, doublons
  écartés, formule de score) ; aucune donnée présentée comme certaine si le
  scrape n'a pas réellement tourné.

## Portabilité

Aucune donnée client dans le dépôt : URL d'API, clé, villes cibles et seuils
vivent dans `rapido-kb/scraping-config.md` (gitignoré). Slug **immuable**.
