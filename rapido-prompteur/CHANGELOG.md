# Changelog — plugin rapido-prompteur

## 0.1.0 — 2026-07-15 — Squelette + patterns francisés

- Nouveau plugin **rapido-prompteur** (16e du marketplace) — **directeur de
  prompts** : orchestre la conception de prompts (image/vidéo/web/audio) pour
  Higgsfield, RapidoCMS, Lovable et Canva. **Il orchestre, il ne remplace pas**
  les skills prompts existants (cf. `docs/IMPORTS-PROMPTEUR.md`).
- `reference/grammaire-des-moteurs.md` : **RÈGLE D'OR** — la grammaire d'un moteur
  se **lit à chaque session** (`models_explore` par type, pièges plugins, doc
  Lovable, Canva), **jamais de mémoire** ; tableau moteur → où lire ses contraintes,
  lecture **à coût nul**.
- `reference/regles-de-construction.md` : anatomie d'un bon prompt par média
  (image 6 blocs ; vidéo plan/mouvement/rythme/durée ; web rôle/pages/design/data) ;
  **négatifs délégués** à `rapidocms:prompts-visuels-pro` (pas de doublon) ;
  **INTERDITS encodés** (aucune IP tierce, aucun « style de [artiste vivant] »,
  aucun personnage sous licence, texte incrusté → protocole zéro faute).
- `assets/patterns/` : **8 patterns francisés** classés par usage (packshot,
  portrait, food, ugc-ad, cinématique, personnage, hooks-viraux, web-apps) —
  chaque fiche : pattern à placeholders, moteurs compatibles, source + licence en
  pied. Patterns référençant des IP/artistes **exclus** (`NOTICE.md`).
- **Hooks** : `Stop` (récap des prompts produits — moteur, grammaire lue en live,
  prompt affiché, négatif, contrôle anti-IP) ; **`PreToolUse` `anti-ip.py`** (scan
  léger des prompts sortants vers les moteurs de génération contre la liste maison
  `reference/ip-a-risque.md` + formules « style de [artiste] » → **confirmation
  avec avertissement**, ne bloque pas).
- `NOTICE.md` : licences MIT des sources distillées (wshobson, Hao0321, rediumvex,
  ZeroLu, KingLeoJr) ; exclusions (`contains-studio` sans licence, `director-style-library`).
- Squelette : **reference + patterns + hooks**, skills à venir.
