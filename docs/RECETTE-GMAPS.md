# Recette réelle — rapido-gmaps (runbook client)

> **Statut : à exécuter côté client.** La chaîne technique du scraper a été
> **prouvée fonctionnelle en session** (build natif, driver Playwright, Chromium,
> moteur scrapemate — voir `docs/AUDIT-GMAPS.md`), mais l'**egress navigateur vers
> Google Maps est bloqué par le réseau du bac à sable** (ERR_CONNECTION_RESET /
> CLOSED). Les trois scénarios ci-dessous se lancent donc **là où Google Maps est
> joignable** : votre poste (Docker local) ou votre VPS (API SaaS). Aucun résultat
> n'est simulé ici — ce document est le **mode opératoire** + la grille de relevé.

## Prérequis

- Un mode d'exécution configuré (`reference/modes-execution.md`) :
  - **Docker local** : `docker info` OK ; ou binaire natif (`go build .`).
  - **API SaaS** : `GMAPS_API_URL` + `GMAPS_API_KEY` dans `rapido-kb/scraping-config.md`.
- MCP RapidoCRM (+ FoodEatUp, RapidoCMS) connectés.
- Seuils/villes ICP dans `rapido-kb/` (défauts sinon).

## Scénario (a) — Sourcing

- **Commande** : « trouve-moi des restaurants gastronomiques à Lyon » →
  `sourcing-gmaps`. Requête `"restaurant gastronomique in Lyon France"`, `lang=fr`,
  `depth 1`, `email:true`.
- **Attendu** : scrape → `score_leads_gmaps.py` → top 20 validés → import CRM (tags
  `gmaps`, priorité) dans le pipeline.
- **À relever** : durée du scrape · nb de résultats · **taux de récupération
  d'email** · score moyen · nb de doublons écartés · IDs entreprises/contacts créés.

## Scénario (b) — Détection FoodEatUp

- **Commande** : « restaurants sans système numérique Paris 10ème » →
  `detection-opportunites`. Filtre ICP `--min-rating 3.5 --min-reviews 20
  --categories restaurant,café,traiteur`.
- **Attendu** : liste triée, flag « SANS SYSTÈME NUMÉRIQUE » ; fiche CRM créée pour
  les 5 premiers (tag `opportunite-foodeatup`).
- **À relever** : nb de leads avec signal / total (taux) · IDs créés.

## Scénario (c) — Enrichissement

- **Commande** : « complète 3 fiches CRM sans téléphone » → `enrichissement-fiches`.
- **Attendu** : scrape ciblé `"{nom} {ville}"` → diff → `update_entreprise` /
  `create_contact` **confirmé champ par champ** (jamais d'écrasement silencieux).
- **À relever** : champs complétés · conflits rencontrés (email divergent) · IDs
  mis à jour.

## Grille de relevé (à remplir à l'exécution)

| Scénario | Volume traité | Durée | Taux email | Taux signal | Doublons écartés | Crédits (attendu : 0) | Frictions | IDs |
|---|---|---|---|---|---|---|---|---|
| (a) Sourcing Lyon | | | | | | 0 | | |
| (b) Détection Paris 10 | | | | | | 0 | | |
| (c) Enrichissement ×3 | | | — | — | — | 0 | | |

> **Coût attendu : 0 €** (scraper MIT, Docker local ou VPS ; aucun service tiers
> payant). Une fois cette grille remplie sur un run réel, le passage **1.0.0** du
> plugin est justifié — jusque-là, les scénarios restent des **procédures
> vérifiées** (grammaire/outils confirmés sur source), non des résultats mesurés.
