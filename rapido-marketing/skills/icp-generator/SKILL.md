---
name: icp-generator
description: Utiliser quand l'utilisateur veut définir son ICP, son client idéal, ou savoir quelles entreprises cibler. Construit le profil d'ENTREPRISE cible (secteur, taille, signaux, techno, région) à partir des clients réellement gagnés dans RapidoCRM, l'écrit dans la KB, et le traduit en critères de prospection et segments CRM.
---

# ICP Generator — profil d'entreprise cible, fondé sur les données

> **ICP ≠ persona.** L'**ICP** décrit une **ENTREPRISE** cible (firmographie :
> secteur, taille, région, techno, signaux d'achat). Le **persona** décrit un
> **individu** (rôle, douleurs, déclencheurs) → déléguer aux skills
> `bootcamp-persona-deep` ou `ideation-persona-maker` (rapido-forge). Ce skill ne
> fait **que** l'ICP entreprise.

## Étape 0 — Charger (obligatoire)
- `${CLAUDE_PLUGIN_ROOT}/reference/priorite-mcp.md` et `garde-fous-marketing.md`.
- `./rapido-kb/marketing/` si présent, sinon `produits-services.md`,
  `cibles-personas.md`, `propositions-valeur.md`.

## Méthode

### (a) Analyser les clients GAGNÉS (données, pas intuition)
Collecter les clients réels : `list_entreprises` + `get_top_clients` (rapidocrm)
et, si dispo, `get_conversion_par_canal`. Passer au **script** (jamais de calcul
de tête) :
`python3 "${CLAUDE_PLUGIN_ROOT}/skills/icp-generator/scripts/analyse_clients.py"`
avec `{"clients": [{secteur, taille, canal, region, techno}...],
"conversion_par_canal": [...]}` → distributions par dimension + **top segments**
(secteur × taille) + parts en %.

### (b) Croiser avec la KB
Confronter les segments dominants aux **offres** et **personas** de la KB : un
segment fréquent mais non rentable/non stratégique n'est pas l'ICP. Signaler tout
écart données ↔ KB, demander l'arbitrage.

### (c) Produire `./rapido-kb/marketing/icp.md`
Écrire (via `mise-a-jour-kb`, après validation) : **segments priorisés**,
**signaux d'achat** (déclencheurs firmographiques : levée, recrutement, ouverture
d'établissement…), **critères de disqualification** (qui NE PAS cibler). Daté.

### (d) Traduction opérationnelle
- **Prospection** : critères pour `prospecter_maps` / `prospecter_entreprise`
  (secteur, zone, taille) — délégués au skill `prospection-pipeline`.
- **Segments CRM** : `create_segment` (filtres `domaine_contient`/`ville_contient`)
  — **création APRÈS confirmation** explicite ; consentement RGPD avant tout
  usage en séquence/audience.

## Livrable type
`icp.md` (segments priorisés + signaux + disqualification) + un **jeu de critères
de prospection** prêt à passer à `prospection-pipeline`.

## Cas d'usage croisés
- Choisir le canal pour atteindre cet ICP → skill `core-four-strategie`.
- Machine outbound B2B sur l'ICP → skill `predictable-revenue`.
- Persona (l'individu dans l'entreprise cible) → skills `bootcamp-persona-deep`,
  `ideation-persona-maker`.
- Signaux chiffrés terrain (note Google, volume d'avis, affluence, « sans système
  numérique ») pour valider/affiner l'ICP → `rapido-gmaps:detection-opportunites`
  (taux consignés dans `rapido-kb/marketing/benchmarks.md`).

## Garde-fous
Segments **mesurés par script**, jamais estimés ; données CRM live > KB ;
`create_segment` et toute prospection **confirmés** ; RGPD respecté.
