---
name: enrichissement-fiches
description: Utiliser quand l'utilisateur veut compléter/rafraîchir une fiche CRM existante depuis Google Maps — « complète la fiche de [entreprise] », « mets à jour les coordonnées CRM », « fiche incomplète », « numéro manquant », « site absent ». Scrape ciblé d'un établissement déjà en base → diff → mise à jour confirmée champ par champ, jamais d'écrasement silencieux. À NE PAS utiliser pour créer de nouveaux leads (sourcing-gmaps).
---

# Enrichissement de fiches CRM depuis Google Maps

Compléter une fiche **déjà en base** dont il manque des coordonnées (téléphone,
site, email…) en la re-scrapant sur Google Maps — **sans jamais écraser
silencieusement** un champ déjà rempli.

## Étape 0 — contexte

Lire `reference/modes-execution.md`, `reference/champs-crm.md`,
`reference/garde-fous-scraping.md`, `rapido-kb/scraping-config.md` si présent.
Sans mode d'exécution configuré : le dire et s'arrêter.

## 1. Désigner la ou les fiches

- Une entreprise nommée par l'utilisateur → `get_entreprise` (ou
  `search_entreprises` / `list_entreprises` avec un filtre) ;
- ou une liste ciblée (« toutes mes fiches sans téléphone ») → `list_entreprises`
  puis repérer les champs vides (téléphone absent ? site absent ? email absent ?).

## 2. Requête Maps ciblée

Pour chaque fiche : construire `"{nom} {ville}"` et lancer un scrape **ciblé**
(`depth 1`, `fast_mode` si des `geo_coordinates` sont connues en KB). Objectif :
retrouver LA fiche, pas une liste. Utiliser le `place_id` s'il a été mémorisé
(note/tag) pour lever l'ambiguïté.

## 3. Comparer (diff), ne jamais écraser en silence

Comparer les champs Google Maps aux champs CRM actuels et **afficher le diff** :

- champ CRM **vide** + valeur Maps trouvée → proposé au remplissage ;
- champ CRM **déjà rempli** et **différent** de Maps (ex. un email divergent) →
  **afficher les deux** et laisser l'utilisateur choisir. **Jamais d'écrasement
  automatique** d'un champ rempli.

## 4. Mettre à jour, champ par champ, après confirmation

`update_entreprise` (coordonnées) et/ou `create_contact` (téléphone, email
manquants) — **confirmation champ par champ**. Consigner via `log_activity`
(« Enrichi depuis Google Maps le {date} : {champs} »). Mémoriser `place_id`
(note/tag) s'il n'y était pas encore, pour les ré-enrichissements futurs.

## Passerelles

Fiche introuvable sur Maps / nouveau lead à créer → `sourcing-gmaps`. Fiche
enrichie prête à travailler → `rapidocrm:prospection-pipeline`.

## Règles

- **Jamais d'écrasement silencieux** d'un champ rempli — diff + choix explicite.
- Rien d'inventé : un champ absent sur Maps reste vide, pas deviné.
- Déduplication déjà acquise (on part d'une fiche existante) ; ne pas recréer
  d'entreprise.
- CGU/RGPD comme partout (`garde-fous-scraping.md`).
