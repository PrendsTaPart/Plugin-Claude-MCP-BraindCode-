---
name: sourcing-gmaps
description: Utiliser quand l'utilisateur veut trouver/prospecter des établissements d'une zone depuis Google Maps — « trouve-moi des restaurants à [ville] », « prospecte les [type] de [zone] », « sourcing Google Maps », « leads [secteur] [géo] ». Sourcing DIRECT Google Maps → scoring ICP par script → déduplication → pipeline RapidoCRM confirmé. À NE PAS utiliser pour la prospection via les workflows CRM (prospecter_maps) ni l'enrichissement d'une fiche existante (enrichissement-fiches).
---

# Sourcing Google Maps → pipeline RapidoCRM

**Positionnement (à lire d'abord).** `prospecter_maps` / `prospecter_entreprise` /
`prospecter_prospect` (RapidoCRM) sont des **workflows N8N** avec leurs propres
sources : on les **laisse en place**. Ce skill fait du **sourcing DIRECT Google
Maps** quand le CRM ne couvre pas assez bien une zone ou un secteur précis (marché
FoodEatUp : restaurants/cafés en France, Tunisie…). Les deux coexistent —
déclencheurs distincts. Si l'utilisateur dit « prospecte via le CRM », router vers
`prospecter_maps`, pas ce skill.

## Étape 0 — charger le contexte

Lire `reference/modes-execution.md`, `reference/champs-crm.md`,
`reference/garde-fous-scraping.md`, et `rapido-kb/scraping-config.md` +
`rapido-kb/marketing/icp.md` s'ils existent (seuils volume, ICP, villes cibles,
`GMAPS_API_URL`/`GMAPS_API_KEY`). Sans mode d'exécution configuré (ni Docker actif,
ni API SaaS) : **le dire et s'arrêter** — aucun résultat inventé.

## 1. Construire la requête

Reformuler le besoin en requête Google Maps optimale : `"{type de business} in
{ville} {pays}"`. Choisir les paramètres (voir `reference/modes-execution.md`) :
`lang` (fr par défaut sur marché FR), `depth`/`max_depth` selon le volume attendu,
`email:true` si des emails sont nécessaires, `geo_coordinates`+`radius` pour une
zone précise, `fast_mode` pour un aperçu rapide. **Annoncer le volume et le temps
estimés → CONFIRMATION avant lancement.** Un `depth`/`radius` au-delà des seuils
déclenche de toute façon le garde-fou `garde-scraping` (confirmation forcée).

## 2. Lancer le scrape

- **Docker CLI local** (ponctuel) ou **API SaaS** (si `GMAPS_API_URL` configurée)
  selon `reference/modes-execution.md`. Une requête par ligne dans un fichier
  d'entrée ; sortie **JSON** dans `docs/scrapes/{date}-{slug-requete}/results.json`.
- Toujours un critère d'arrêt (`-exit-on-inactivity`). Respecter le délai minimum
  entre jobs et le plafond de requêtes/jour (garde-fous).

## 3. Parser et scorer — par script

Passer le JSON du scrape à `scripts/score_leads_gmaps.py` (stdlib, **jamais de
calcul de tête**) :

```
python3 "${CLAUDE_PLUGIN_ROOT}/skills/sourcing-gmaps/scripts/score_leads_gmaps.py" \
  --input docs/scrapes/{date}-{slug}/results.json
```

Formule appliquée par le script :
`score = review_rating × ln(review_count + 1) × signal_opportunite`, avec
`signal_opportunite = 1.5` si `order_online` **et** `reservations` sont vides
(« sans système numérique »), sinon `1.0`. Sortie triée par score décroissant,
enrichie de `score`, `signal_opportunite`, `sans_systeme_numerique`. **Afficher la
formule** avec les résultats.

## 4. Dédupliquer (obligatoire, avant toute création)

Pour chaque lead scoré : `rechercher_prospects` (nom + ville) et, si SIRET connu,
`rechercher_entreprise_siret` → **exclure** les doublons (ou les router vers
`enrichissement-fiches`). Jamais deux fiches pour le même établissement.

## 5. Valider avec l'utilisateur

Afficher le **top 20** : nom, téléphone, email, note, nombre d'avis, score,
`signal_opportunite`. L'utilisateur **valide / retire** des entrées avant toute
écriture CRM.

## 6. Importer dans le CRM (par lots de 10, confirmés)

Mapper selon `reference/champs-crm.md` :

- `create_entreprise` (nom + adresse + site) puis `create_contact` (téléphone,
  email) ;
- `log_activity` : « Sourcé Google Maps le {date}, score={x}, signal={…} » ;
- **Tags** : `gmaps`, `sans-systeme-numerique` si détecté, tag de priorité selon
  le score ; puis `enregistrer_prospect` (ou `enregistrer_tous_prospects` pour le
  lot — **confirmation forcée** par `garde-scraping`).

Importer **par lots de 10 avec confirmation par lot**. Les champs sans réceptacle
CRM structuré (`place_id`, `popular_times`…) vont en note/tag (voir
`champs-crm.md` et `docs/OUTILS-MCP-MANQUANTS.md`).

## 7. Capitaliser

Consigner dans `rapido-kb/marketing/benchmarks.md` : taux de récupération d'email
par secteur/zone, score moyen des leads importés, taux de doublons. Si des motifs
ICP se dégagent (quel profil score le plus), les noter dans
`rapido-kb/marketing/apprentissages.md` — matière d'entraînement pour
`rapido-marketing:icp-generator`.

## Passerelles

Leads importés → `rapido-marketing:machine-outbound` (séquence outbound) ou
`rapidocrm:prospection-pipeline`. Détection ICP FoodEatUp poussée →
`detection-opportunites`. Fiche à compléter → `enrichissement-fiches`.

## Règles

- **Rien d'inventé** : aucun résultat de scrape présenté comme certain si le
  scrape n'a pas réellement tourné ; valeur manquante = champ vide, pas deviné.
- **Déduplication non négociable** avant création.
- **Calcul par script**, formule affichée.
- **CGU/RGPD** : plafonds, opt-out B2B, pas de revente (`garde-fous-scraping.md`).
