---
name: detection-opportunites
description: Utiliser quand l'utilisateur cherche des prospects FoodEatUp — « restaurants sans système numérique », « prospects FoodEatUp », « trouve des leads pour FoodEatUp », « business sans réservation en ligne ». Sourcing Google Maps filtré sur l'ICP FoodEatUp (restauration, bien notée, sans commande ni réservation en ligne) → priorité aux « sans système numérique ». À NE PAS utiliser pour un sourcing générique (sourcing-gmaps) ni l'enrichissement (enrichissement-fiches).
---

# Détection d'opportunités FoodEatUp

Le cas d'usage phare : un établissement **actif et bien noté** mais **sans système
numérique** (ni commande ni réservation en ligne) = prospect idéal FoodEatUp.
Ce skill spécialise `sourcing-gmaps` avec l'ICP FoodEatUp et met en avant ce signal.

## Étape 0 — contexte + ICP

Lire `reference/champs-crm.md`, `reference/garde-fous-scraping.md`,
`reference/modes-execution.md`, et **`rapido-kb/marketing/icp.md`** pour l'ICP
FoodEatUp. Défauts si absent : catégories restaurant / café / traiteur, note
≥ 3.5, nombre d'avis ≥ 20. Sans mode d'exécution configuré : le dire et s'arrêter.

## 1. Sourcer sur la zone cible

Déléguer à `sourcing-gmaps` (même chaîne : requête → scrape → dédup) sur la zone
demandée, en passant l'ICP au scoring :

```
python3 "${CLAUDE_PLUGIN_ROOT}/skills/sourcing-gmaps/scripts/score_leads_gmaps.py" \
  --input docs/scrapes/{date}-{slug}/results.json \
  --min-rating 3.5 --min-reviews 20 --categories "restaurant,café,traiteur"
```

Le script applique déjà le **bonus `signal_opportunite` ×1.5** aux fiches dont
`order_online` **et** `reservations` sont vides, et filtre selon l'ICP. Seuils
surchargés par `rapido-kb/marketing/icp.md`.

## 2. Mettre en avant le signal

Afficher la liste triée par score avec le flag **« SANS SYSTÈME NUMÉRIQUE »**
(`sans_systeme_numerique = true`) mis en évidence — ce sont les cibles
prioritaires FoodEatUp.

## 3. Importer (validation puis lots confirmés)

Comme `sourcing-gmaps` (dédup → validation → import par lots de 10 confirmés),
avec le tag **`opportunite-foodeatup`** en plus des tags standards. `log_activity`
mentionne le signal.

## 4. Handoff + statistique de session

- Handoff : `rapido-marketing:machine-outbound` (séquence) ou
  `rapidocrm:prospection-pipeline`.
- Statistique : combien de leads sur combien portent le signal (taux) →
  `rapido-kb/marketing/benchmarks.md`. Ce taux nourrit `rapido-marketing:icp-generator`.

## Règles

- L'ICP FoodEatUp prime depuis `rapido-kb/marketing/icp.md` (défauts sinon).
- Signal `sans_systeme_numerique` calculé **par script**, jamais à l'œil.
- Déduplication, CGU/RGPD, rien d'inventé — comme `sourcing-gmaps`.
