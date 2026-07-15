# Garde-fous scraping — CGU, RGPD, volumétrie

Le scraping de données **publiques** de Google Maps pour de la prospection B2B
entre dans une zone à cadrer. Ces règles sont **encodées** (hook déterministe
`garde-scraping` + règles de skill) et **éditables** dans
`rapido-kb/scraping-config.md` (hors dépôt). Défauts prudents ci-dessous.

## 1. Volumétrie (plafonds par défaut)

| Plafond | Défaut | Variable d'env / KB |
|---|---|---|
| Résultats par requête | **500** | `GMAPS_RESULTATS_MAX` |
| Requêtes par jour | **3** | `GMAPS_REQUETES_JOUR` |
| Délai minimum entre deux jobs | **5 s** | `GMAPS_DELAI_MIN_S` |
| Profondeur (`-depth`/`max_depth`) au-delà de laquelle on **confirme** | **10** | `GMAPS_DEPTH_MAX` |
| Rayon (`-radius`, km) au-delà duquel on **confirme** | **20** | `GMAPS_RADIUS_MAX` |

Le hook `garde-scraping` force une **confirmation** (ask, jamais deny) dès qu'une
commande de scraping dépasse `GMAPS_DEPTH_MAX` ou `GMAPS_RADIUS_MAX`. Les autres
plafonds (résultats/jour, délai) sont appliqués par la logique de skill et par la
routine n8n (table mémoire anti-re-scrape). **Jamais de flood, jamais de boucle
infinie** : toujours un critère d'arrêt explicite (`-exit-on-inactivity`).

## 2. RGPD (démarchage B2B)

- Les **emails professionnels** crawlés depuis des sites web d'entreprises sont
  licites en démarchage **B2B** au titre de l'**intérêt légitime**, à condition :
  - d'un **opt-out honoré immédiatement** — le retrait d'une séquence
    `machine-outbound` est la règle n°1 déjà en place ; un contact qui se
    désinscrit n'est jamais re-sourcé ;
  - de ne cibler que des **personnes morales / adresses génériques** (contact@,
    info@) — pas de données personnelles sensibles.
- **Pas de revente ni de redistribution** des données : usage interne
  BraindCode / clients uniquement.

## 3. CGU Google

- Usage **raisonnable** : volumes limités (plafonds ci-dessus), données
  **publiques** affichées sur les fiches, pas de contournement de mesures
  techniques au-delà de ce que fait le scraper open source.
- **Pas de scraping des avis pour les republier/critiquer** publiquement — les
  avis servent à qualifier un prospect (santé du business), pas à alimenter du
  contenu.

## 4. Déduplication (non négociable)

Avant **toute** création CRM : `rechercher_prospects` (+ `rechercher_entreprise_siret`
si SIRET) → un doublon détecté est **écarté** (ou routé vers `enrichissement-fiches`).
Jamais deux fiches pour le même établissement.

## 5. Confirmation des imports en lot

Toute création groupée (`enregistrer_tous_prospects`, ou import > 10 fiches) passe
par une **confirmation** (hook `garde-scraping` + affichage des leads à valider
avant écriture). L'utilisateur retire/valide les entrées avant l'import CRM.

> Ces garde-fous sont **indépendants du modèle** : le hook s'exécute même si le
> paramètre de volume est implicite. Les seuils client priment via
> `rapido-kb/scraping-config.md`.
