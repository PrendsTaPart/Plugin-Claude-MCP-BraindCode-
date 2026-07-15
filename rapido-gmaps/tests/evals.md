# Évals — plugin rapido-gmaps (0.1.0, squelette)

Le plugin est au stade squelette : garde-fous + fondations. Les évals de
déclenchement des skills seront ajoutées avec eux (GMS2→GMS4).

## Garde-fous (hook `garde-scraping`, testés au testeur)

| Entrée | Décision attendue |
|---|---|
| Bash `... google-maps-scraper ... -depth 40` | **ask** (profondeur > seuil 10) |
| Bash `... /api/v1/scrape ... "max_depth": 50` | **ask** (profondeur > seuil) |
| Bash `... gms-bin ... -radius 80` | **ask** (rayon > seuil 20 km) |
| Bash `... google-maps-scraper ... -depth 1` | **allow** (sous les seuils) |
| Bash `ls -la` (non-scraper) | **allow** |
| `mcp__rapidocrm__enregistrer_tous_prospects` | **ask** (import en lot) |
| `mcp__rapidocrm__list_contacts` | **allow** |

## Anti-déclenchements (à respecter dans les skills)

- « Prospecte via le CRM » / « prospecte cette entreprise » →
  **`rapidocrm` `prospecter_maps` / `prospecter_entreprise`** (workflows N8N
  officiels), pas le scraping direct.
- « Enrichis depuis LinkedIn » → **`rapido-marketing` draft-outreach /
  account-research**, pas Google Maps.
- « Analyse les avis clients FoodEatUp » → **`foodeatup` handle-complaint**,
  pas la veille concurrents.

## Principes vérifiés

- Aucune donnée de scrape inventée : si aucun mode d'exécution n'est configuré,
  le skill l'annonce et s'arrête.
- Déduplication obligatoire avant toute création CRM.
- Score de priorité **par script** (formule affichée), jamais de tête.
