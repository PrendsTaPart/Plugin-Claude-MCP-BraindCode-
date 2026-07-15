# Évals — plugin rapido-gmaps (0.5.0)

## Déclenchement (phrases → skill / agent)

| Phrase | Skill / agent |
|---|---|
| « Trouve-moi des restaurants à Lyon » / « prospecte les cafés de Tunis » | `sourcing-gmaps` |
| « Sourcing Google Maps » / « leads restauration Paris 11ème » | `sourcing-gmaps` |
| « Complète la fiche de [X] » / « numéro manquant » / « mets à jour les coordonnées CRM » | `enrichissement-fiches` |
| « Restaurants sans système numérique » / « prospects FoodEatUp » / « business sans réservation en ligne » | `detection-opportunites` |
| « Scrape les concurrents de [client] » / « veille concurrentielle zone » | `veille-concurrents-gmaps` |
| Brief autonome de sourcing (zone + volume + ICP) | agent `chasseur-leads` |

## Cas `veille-concurrents-gmaps` (3)

9. **Déclenchement** : « que proposent les concurrents restaurants du Vieux-Lyon »
   → scrape même catégorie/zone → rapport d'agrégat (notes, prix, affluence,
   canaux) dans `veille-concurrents.md`.
10. **Éthique avis** : la veille **n'extrait pas** les avis pour les republier /
    critiquer ; seulement des agrégats de positionnement (thumbnail only, aucune
    reproduction).
11. **Anti-collision** : « trouve-moi des restos à prospecter » → `sourcing-gmaps`,
    pas la veille ; « réponds à cet avis client » → `foodeatup` handle-complaint.

## Cas `enrichissement-fiches` (2)

5. **Non-écrasement** : fiche CRM avec un email déjà rempli, Maps renvoie un email
   **différent** → afficher **les deux**, laisser l'utilisateur choisir. Jamais
   d'écrasement automatique.
6. **Champ vide complété** : fiche sans téléphone, Maps trouve le numéro → proposé,
   `update_entreprise` / `create_contact` après confirmation champ par champ.

## Cas `detection-opportunites` (2)

7. **Filtre ICP + signal** : « restaurants sans système numérique à Paris 10ème »
   → scoring avec `--min-rating 3.5 --min-reviews 20 --categories restaurant,café,
   traiteur`, flag « SANS SYSTÈME NUMÉRIQUE » (`signal_opportunite` ×1.5) mis en
   avant, tag `opportunite-foodeatup`.
8. **Anti-collision** : « trouve-moi des restaurants à Lyon » (sans critère
   FoodEatUp) → `sourcing-gmaps` générique, pas `detection-opportunites`.

## Cas `sourcing-gmaps` (4)

1. **Déclenchement + chaîne** : « trouve-moi des restaurants gastronomiques à
   Lyon » → construction requête `"restaurant gastronomique in Lyon France"`,
   estimation volume/temps → **confirmation** → scrape → scoring par script →
   dédup → validation top 20 → import par lots de 10.
2. **Refus de volume** : requête à `-depth 40` (ou `radius 80`) → le hook
   `garde-scraping` force une **confirmation** (avertissement volumétrique) avant
   lancement.
3. **Déduplication** : un lead dont le nom+ville existe déjà (`rechercher_prospects`
   renvoie une fiche) → **écarté** de la création (ou routé vers
   `enrichissement-fiches`), jamais de doublon.
4. **Anti-collision** : « prospecte via le CRM » / « prospecte cette entreprise »
   → router vers **`rapidocrm` prospecter_maps / prospecter_entreprise** (workflows
   N8N), **pas** ce skill.

## Scoring (`scripts/score_leads_gmaps.py`)

- `score = review_rating × ln(review_count+1) × signal` ; `signal=1.5` si
  `order_online` **et** `reservations` vides, sinon `1.0`.
- Vérifié : note 4.7 / 800 avis / sans système → 47.135 ; mêmes note/avis **avec**
  système → 31.424 ; tri décroissant ; filtres ICP (min-rating/min-reviews/
  catégories) excluent sans planter.

## Anti-déclenchements

- « Prospecte via le CRM » → `rapidocrm` prospecter_maps (workflows N8N).
- « Enrichis depuis LinkedIn » → hors périmètre : ce plugin source depuis Google
  Maps, pas LinkedIn (router vers l'outbound CRM/marketing selon le besoin).
- « Analyse les avis clients FoodEatUp » → `foodeatup` handle-complaint.
- « Complète la fiche de… » → `enrichissement-fiches`.

## Routine `GMAPS-HEBDO`

- « Automatise le sourcing hebdo des restos de ma zone » → routine n8n
  `GMAPS-HEBDO` (recette `rapido-n8n/reference/recettes-gmaps.md`), **installée sur
  confirmation** ; ne s'installe pas sans mode d'exécution configuré.
- Mémoire `gmaps_jobs_journal` : n'importe que les **nouveaux** leads (anti-re-scraping).

## Recette réelle

- Runbook `docs/RECETTE-GMAPS.md` (3 scénarios) — **exécution côté client** (Google
  Maps non joignable depuis l'environnement de build, prouvé en GMS0). Aucun
  résultat simulé ; la grille de relevé se remplit au run réel.

## Garde-fous & principes

- Aucune donnée de scrape inventée ; dégradation propre si aucun mode configuré.
- Déduplication obligatoire ; import en lot confirmé (`garde-scraping`).
- Score **par script**, formule affichée.
