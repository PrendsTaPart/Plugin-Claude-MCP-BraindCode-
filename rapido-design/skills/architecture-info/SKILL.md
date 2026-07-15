---
name: architecture-info
description: Utiliser quand l'utilisateur veut structurer un site avant le design — « sitemap », « user flow », « parcours utilisateur », « arborescence du site », « wireframes ». Produit sitemap + flows (FigJam) + wireframes basse-fi, validés AVANT toute maquette hi-fi. À NE PAS utiliser pour les maquettes hi-fi/design system (studio-maquette) ni la direction artistique (direction-artistique).
---

# Architecture de l'information

La **structure d'abord** : sitemap, parcours, wireframes gris — validés **avant** tout
pixel joli. Règle : jamais de hi-fi sur une structure non validée.

## Étape 0 — contexte

Lire `reference/pipeline-design.md`, `reference/jugement-design.md`. Brief : pages, cible,
**personas** (croiser `rapido-forge` si un travail d'idéation existe). La théorie sitemap
pédagogique renvoie à `rapido-forge:ideation-sitemap-generator` (ici on **exécute**).

## 1. Sitemap

Générer le **sitemap** en FigJam (`figma-generate-diagram`) : arborescence des pages,
regroupements, profondeur. Valider la couverture (aucune page orpheline).

## 2. User flows (parcours critiques)

Diagrammes de décision des **2-3 parcours critiques** (ex. inscription, achat, réservation)
en FigJam (`figma-generate-diagram`) : entrées, décisions, états d'erreur, sortie.

## 3. Wireframes basse-fi

Wireframes **gris, sans style** des écrans clés (`figma-generate-design`) — la **structure**
(blocs, hiérarchie, placement), pas l'esthétique. Une idée par écran (`jugement-design.md`).

## 4. Validation AVANT la hi-fi (bloquant)

Faire **valider sitemap + flows + wireframes** par l'utilisateur. **Tant que la structure
n'est pas validée, on ne passe pas en hi-fi** — renvoyer à cette étape si `studio-maquette`
est appelé sans wireframes validés.

## Passerelles

Maquettes hi-fi + design system → `studio-maquette`. La spec `rapido-lovable:mvp-lovable`
référence les diagrammes FigJam produits ici.

## Règles

- **Structure validée avant tout pixel joli** (règle bloquante).
- Wireframes **gris** (pas de couleur/typo à ce stade) ; une idée par écran.
- Rien d'inventé (pages/parcours reflètent le brief réel).
