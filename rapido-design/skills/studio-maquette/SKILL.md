---
name: studio-maquette
description: Utiliser quand l'utilisateur veut les maquettes hi-fi et le design system — « maquette », « design du site », « écrans hi-fi », « design system », « maquette Figma de [projet] ». Design system Figma d'abord (variables des tokens), écrans hi-fi qui consomment les variables, gates critique + accessibilité, puis handoff Lovable. À NE PAS utiliser sans DA + wireframes validés (direction-artistique, architecture-info).
---

# Studio maquette (design system Figma ↔ Lovable)

Le **design system d'abord**, puis les écrans hi-fi qui **consomment les variables** (zéro
valeur en dur). Fil rouge des tokens : charte → Figma → Lovable.

## Étape 0 — prérequis

Lire `reference/pipeline-design.md`, `reference/passerelles.md`, `reference/jugement-design.md`.
**Prérequis** : **DA validée** (`direction-artistique`) + **wireframes validés**
(`architecture-info`). Si absents → **renvoyer** (pas de hi-fi sur structure non validée).
Charger la charte (`get_brand` + KB).

## 1. Design system d'abord

Créer le **design system Figma** (`figma-generate-library`) : **variables** depuis les
tokens de la DA (couleurs hex de la charte, **modes clair/sombre**, échelle d'espacement),
**composants** de base. Enrichi des **audits** de design system (WCAG, scoring de
composants — patterns de work-with-design-systems, cf. `NOTICE.md`).

## 2. Écrans hi-fi (consomment les variables)

Écrans par lot (`figma-generate-design`) **qui référencent les variables**, **JAMAIS** de
valeur en dur. Une idée par écran, hiérarchie claire (`jugement-design.md`).

## 3. Gates (bloquants avant livraison)

- **Gate critique** : passer `reference/jugement-design.md` (anti-goût-IA, hiérarchie,
  respiration) → corriger tant que ça sent le template.
- **Gate accessibilité (WCAG)** : contrastes AA, tailles de cibles tactiles (≥ 44 px),
  focus visibles, ordre de lecture. Un rouge bloque.
- **Détection valeur en dur** : toute couleur/typo écrite en dur (hors variable) → **corriger**.

## 4. Publication & handoff

- **(a)** Fichier Figma **organisé** : pages Fondations / Composants / Écrans.
- **(b)** Design system maison **poussé en projet design system Lovable** : créer/mettre à
  jour le projet DS du workspace (utilisable ensuite via `create_project(design_systems)`).
  **Confirmation avant** (touche les projets futurs), **versionné**. Aujourd'hui le
  workspace n'a **aucun DS** (D0) → c'est ici qu'on le crée.
- **(c)** Handoff : `figma-design-to-code` **ou** brief `rapido-lovable:mvp-lovable`
  **enrichi des tokens** (le MVP démarre du DS).

## Passerelles

Structure absente → `architecture-info`. DA absente → `direction-artistique`. Build du MVP
→ `rapido-lovable:mvp-lovable` / `architecte-lovable`. Animations → `animations-web`.

## Règles

- **DS d'abord**, écrans qui **consomment les variables** (zéro valeur en dur).
- **Gates critique + a11y** bloquants ; push DS Lovable **confirmé** et versionné.
- Fil rouge des tokens sans divergence ; pas de copie de maquettes de designers réels.
