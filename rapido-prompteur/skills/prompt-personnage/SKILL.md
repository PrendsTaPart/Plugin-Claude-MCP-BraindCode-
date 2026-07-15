---
name: prompt-personnage
description: >-
  Utiliser quand l'utilisateur veut des prompts de scène COHÉRENTS pour un
  personnage / une mascotte de marque récurrent(e) (« garde le même personnage »,
  « décline ma mascotte dans plusieurs scènes », « prompts cohérents pour [perso] »).
  S'appuie sur une banque de traits combinatoire (rapido-kb/traits-personnages.md)
  liée au registre personnages.json : traits de canon VERROUILLÉS + axes de scène
  VARIABLES → prompts cohérents, routés vers coherence-personnage (CMS) ou
  personnages-univers (Higgsfield) selon le média. Chaque combinaison validée
  enrichit la banque (boucle d'apprentissage).
---

# Prompt personnage — banque de traits combinatoire (cohérence de canon)

Réimplémentation **100 % maison** du concept « banque de traits combinatoire ».
> **Attribution** : le concept est inspiré du projet `huangserva` — **sans fichier
> de licence → « tous droits réservés »**, donc **zéro copie** de son texte ou de
> son code. Seule l'**idée** (non protégeable) est reprise, réécrite ici. Voir
> `NOTICE.md` et `docs/IMPORTS-PROMPTEUR.md` (politique contains-studio identique).

## Principe

Un personnage récurrent doit rester **reconnaissable** d'un rendu à l'autre. On
sépare deux familles de traits :

- **Traits VERROUILLÉS (canon)** — morphologie, tenue, style : **jamais variés**,
  toujours inclus tels quels dans chaque prompt.
- **Traits VARIABLES (axes de scène)** — pose, expression, éclairage, décor,
  cadrage : on **combine** une valeur par axe pour générer une scène nouvelle,
  **sans jamais casser le canon**.

Un prompt de scène cohérent = **tous les traits verrouillés** + **une combinaison**
des axes variables, assemblés selon la structure image 6 blocs
(`reference/regles-de-construction.md`).

## Étape 0 — Registre & banque (obligatoire)

1. Lire le registre **`personnages.json`** (canon : nom, marque, brand_id,
   description canonique, portraits de référence, version active). Le vrai registre
   vit dans `./rapido-kb/personnages.json` — jamais dans ce dépôt. brand_id manquant
   ou `0` → **résoudre via `get_brand`**, jamais inventé.
2. Lire la banque **`traits-personnages.md`** (axes par personnage). Le vrai
   fichier vit dans `./rapido-kb/traits-personnages.md` ; un **exemple** est fourni :
   `reference/traits-personnages.exemple.md` (mascotte BraindCode « Origami » +
   PronoClip « Pronoclip-kun »).

## Génération combinatoire

1. **Choisir le personnage** et sa version active.
2. **Injecter tous les traits verrouillés** (canon) — non négociables.
3. **Choisir une valeur par axe variable** (pose × expression × éclairage × décor
   × cadrage) selon la scène voulue (ou proposer 2-3 combinaisons).
4. **Assembler** le prompt (6 blocs), afficher le **prompt complet** en bloc.
5. Prévoir le **négatif** (délégué à `rapidocms:prompts-visuels-pro`) et l'espace
   texte si besoin.

> Nombre de scènes distinctes possibles = produit du nombre de valeurs par axe
> (p. ex. 4 poses × 3 expressions × 3 éclairages × 3 décors = 108 combinaisons),
> toutes **cohérentes** puisque le canon est verrouillé.

## Routage de sortie (selon le média)

| Besoin | Route | Pourquoi |
|---|---|---|
| Image **brandée courante** (visuel réseau, à partir d'un portrait canon) | `rapidocms:coherence-personnage` | rendu via `images_to_image` depuis le portrait de référence (1 à 3 URLs, < 5 Mo) — cohérence par l'image source |
| **Réaliste / vidéo / multi-sujets** (Elements, Soul, clip) | `rapido-higgsfield:personnages-univers` | identité entraînée (Soul) ou Element (Kling/Seedance) — voir `element_id` / `soul_id` du registre |

Le prompteur **prépare la combinaison** ; le rendu et la cohérence fine sont
exécutés par le skill de destination. `element_id`/`soul_id` absents = personnage
non encore câblé vidéo/réaliste → la voie CMS (`images_to_image`) fonctionne quand même.

## Boucle d'apprentissage

Une combinaison **validée** (rendu retenu par l'utilisateur) est **capitalisée** :

1. L'ajouter à la banque `./rapido-kb/traits-personnages.md` sous « Combinaisons
   éprouvées » (la combinaison + un lien vers le rendu).
2. Capitaliser le prompt gagnant (`add_prompt` / gestion `rapidocms:bibliotheque-prompts`),
   titre « [perso] — [scène] — vN ».

Au fil du temps, la banque encode ce qui marche pour chaque personnage.

## Interdits

- **Personnage 100 % original** : aucun trait repris d'un personnage sous licence
  (héros, mascotte tierce), même « inspiré de ». Garde-fou automatique : le hook
  PreToolUse anti-IP du plugin.
- Ne **jamais casser le canon** pour « faire joli » : un trait verrouillé modifié =
  personnage différent → rejet.
- Données réelles : portraits de référence = **assets réels** du registre, pas des
  visages inventés.

## Pièges

- Confondre trait de canon et axe de scène : verrouiller trop → scènes figées ;
  verrouiller trop peu → personnage qui dérive. La banque tranche par personnage.
- Générer sans portrait de référence quand la route CMS l'exige (cohérence par
  l'image) → dérive du personnage.
