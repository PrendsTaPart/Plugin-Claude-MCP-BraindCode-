# Routines — rapido-gmaps

Le récurrent et le volume vivent en **n8n**, pas en conversationnel. Identifiant au
**registre unifié** (`reference/registre-routines.md`, préfixe `GMAPS-*`).

## GMAPS-HEBDO

- **Cadence** : hebdomadaire, lundi 8h (cron n8n).
- **Propriétaire** : `sourcing-gmaps` (+ `detection-opportunites` si ICP FoodEatUp).
- **Recette n8n** : `rapido-n8n/reference/recettes-gmaps.md`.
- **Mémoire** : table n8n `gmaps_jobs_journal` — évite le re-scraping d'une même
  zone dans la semaine, n'importe que les **nouveaux** leads.
- **Contenu** : pour chaque ville de `rapido-kb/scraping-config.md` → scrape ICP →
  déduplication → import des nouveaux leads → résumé (N nouveaux, score moyen).
- **Prérequis** : un mode d'exécution configuré (Docker local ou API SaaS). Sans
  lui, la routine **ne s'installe pas** (dégradation propre annoncée).
- **Garde-fous** : plafonds volume KB, import en lot confirmé (`garde-scraping`),
  CGU/RGPD, aucun résultat inventé.

Installation **sur confirmation** via `rapido-n8n:usine-automatisations` — jamais
d'office.
