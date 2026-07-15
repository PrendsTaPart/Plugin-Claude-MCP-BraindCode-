# Changelog — plugin rapido-prompteur

## 0.3.0 — 2026-07-15 — Agent directeur-prompts + boucle d'apprentissage

- Agent **`directeur-prompts`** — du besoin au **prompt exécutable** : étape 0
  (grammaire-des-moteurs + regles-de-construction + patterns + **prompts gagnants
  d'abord** via `list_prompts`), 3 variantes (prompt complet affiché + paramètres
  lus en direct + coût + références), **délégation aux skills exécutants**,
  **capitalisation systématique** (`add_prompt`). Frontmatter `tools` **sans aucun
  outil de génération payante** (`get_brand`/`list_prompts`/`add_prompt`/`edit_prompt`
  CMS + `models_explore` Higgsfield + lecture des références) — **il prompte, il ne
  produit pas**. Squelette inspiré du `prompt-engineer` de `wshobson/agents` (MIT,
  structure PR0 réécrite — cf. `docs/IMPORTS-PROMPTEUR.md`).
- **Boucle d'apprentissage** (`reference/boucle-apprentissage.md` +
  `scripts/score_prompts.py`, stdlib) : après production/publication, les skills
  exécutants rapportent les **métriques réelles** (`post_insights`, virality,
  réutilisations) → le script classe **GAGNANT / NEUTRE** (formule transparente,
  seuils surchargeables) et émet un plan `edit_prompt` + journal daté
  `rapido-kb/marketing/apprentissages.md`. **Aucun score inventé** : sans métrique
  réelle → **INSUFFISANT** (non taggé). L'agent **pioche les GAGNANT d'abord**.
- **2 évals** ajoutées (DP1 agent, BA1 boucle). Bump 0.2.0 → 0.3.0.

## 0.2.0 — 2026-07-15 — Skills prompt-lovable + prompt-personnage

- Skill **`prompt-lovable`** — produit un **brief Lovable structuré** (6 sections :
  rôle & objectif → pages & sections → design system imposé par la charte
  (`get_brand`/KB, hex/police/logo) → données & **mode B** (formulaire → CRM
  `enregistrer_prospect`, contraintes `rapido-lovable:usine-a-landing` /
  `site-restaurant`) → **interdits** (pas de `localStorage` métier, clé côté serveur,
  parse par nom, données réelles) → **critères d'acceptation testables**). Doc
  Lovable **lue en ligne** (aucun system prompt divulgué). Articulation avec
  `rapido-forge:ideation-lovable-prompt` (idéation) et les builders `rapido-lovable`
  (construction) — déclencheurs distincts, renvois croisés. Source pattern
  `web-apps` (KingLeoJr **MIT** francisé).
- Skill **`prompt-personnage`** — réimplémentation **maison** de la « banque de
  traits combinatoire » (concept inspiré de `huangserva`, **sans licence → zéro
  copie**) : banque `rapido-kb/traits-personnages.md` (traits de canon VERROUILLÉS
  + axes de scène VARIABLES), liée au registre `personnages.json` → **génération
  combinatoire** de prompts de scène cohérents avec le canon → **routage média**
  (`rapidocms:coherence-personnage` image brandée / `rapido-higgsfield:personnages-univers`
  réaliste-vidéo) → **boucle d'apprentissage** (chaque combinaison validée enrichit
  la banque + `add_prompt`).
- **Banque de traits d'exemple** `reference/traits-personnages.exemple.md` : mascotte
  BraindCode « Origami » (`#0052FF`) + PronoClip « Pronoclip-kun » (cohérente avec
  le canon `coherence-personnage`).
- `.mcp.json` : serveurs orchestrés déclarés (`lovable`, `rapidocms`, `rapidocrm`).
- **4 évals** (PL1/PL2, PP1/PP2). Bump 0.1.0 → 0.2.0.

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
