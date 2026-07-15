# IMPORTS — Plugin « prompteur » (directeur de prompts)

> **Nature du document : AUDIT. Aucune création de skill.** Ce fichier inventorie
> 7 dépôts clonés en local, statue par élément `{ADAPTER | S'INSPIRER | IGNORER}`,
> vérifie les licences, l'anti-verbatim et les références IP tierces / artistes
> vivants à **exclure de toute francisation**, propose un squelette `directeur-prompts`
> (structure copiée, jamais le texte), et croise avec l'existant maison.
>
> **STOP prévu : validation de ce document avant PR1.** Rien n'est écrit dans un
> plugin tant que l'utilisateur n'a pas validé.

Date de l'audit : 2026-07-15 · Clones `--depth 1` en dépôts frères `/home/user/imp_<owner>_<name>`
(hors du dépôt marketplace ; jamais commités ici). Poids des images ignoré (lecture
des fichiers texte uniquement — `imp_wuyoscar_GPT-Image2-Skill` pèse 825 Mo d'images).

---

## 0. Synthèse — verdict par dépôt

| Dépôt | Licence (lue dans LICENSE) | Ce qu'on en retient | Verdict global |
|---|---|---|---|
| **wshobson/agents** | **MIT** © 2024 Seth Hobson | `prompt-engineer.md` = squelette de référence pour `directeur-prompts` | **ADAPTER (structure)** |
| **Hao0321/ai-media-generator** | **MIT** © 2026 contributors | Taxonomie « reference / template / selector », grille qualité 10 points, model-picker | **S'INSPIRER** (⚠️ purge IP) |
| **rediumvex/ai-video-generator-claude** | **MIT** © 2026 Roman Knox | 10 skills « format-objectif » avec `description` déclenchable exemplaire | **S'INSPIRER** |
| **ZeroLu/awesome-nanobanana-pro** | **MIT** © 2025 ZeroLu | Format de fiche prompt (titre + intention + bloc JSON) | **S'INSPIRER** (⚠️ purge IP lourde) |
| **KingLeoJr/prompts** | **MIT** © 2025 KingLeoJr | 1 dossier = 1 brief structuré (dev web, hors média) | **IGNORER** (sauf idée « brief nommé ») |
| **contains-studio/agents** | **AUCUN fichier LICENSE** → tous droits réservés | Squelette d'agent par département (name/description/examples/color/tools) | **S'INSPIRER (structure only, ZÉRO vendoring)** |
| **wuyoscar/GPT-Image2-Skill** | à confirmer (dépôt lourd, non ouvert en détail) | non audité en profondeur (825 Mo images) — **hors périmètre lecture** | **IGNORER pour l'instant** |

> **Principe maison rappelé** : le plugin prompteur **ORCHESTRE**, il ne remplace
> pas les skills existants. On importe des **structures et des idées** (non
> protégeables), **jamais du texte** (anti-verbatim), **jamais une référence à une
> IP tierce ou un artiste vivant** dans nos patterns francisés.

---

## 1. Inventaire par dépôt

### 1.1 `wshobson/agents` — MIT © 2024 Seth Hobson · ADAPTER (structure)

- **Structure** : mono-repo de 749 fichiers `.md`, organisé en `plugins/<domaine>/{agents,skills,commands}/`.
  Agent cible localisé : **`plugins/llm-application-dev/agents/prompt-engineer.md`**.
  Skill jumeau : `plugins/llm-application-dev/skills/prompt-engineering-patterns/`
  (avec `references/`, `assets/`, `scripts/optimize-prompt.py`). Variante :
  `plugins/meigen-ai-design/agents/prompt-crafter.md`.
- **Taxonomie du prompt-engineer** (rubriques, pas le texte) : `Purpose` →
  `Capabilities` (Advanced Prompting Techniques : CoT, Constitutional AI, Meta-
  prompting ; Model-Specific Optimization ; Production Prompt Systems ; RAG ;
  Multi-Agent ; Specialized Applications ; Evaluation & Testing ; Advanced Patterns)
  → `Behavioral Traits` → `Knowledge Base` → `Response Approach` (8 étapes) →
  `Required Output Format` (**« The Prompt » en bloc copiable** + Implementation
  Notes + Testing & Evaluation + Usage Guidelines) → `Example Interactions` →
  `Before Completing Any Task` (checklist ☐).
- **Fiche / format** : frontmatter YAML minimal `name` + `description` (déclenchable :
  « Use when… ») + `model: inherit`. Règle forte reprise chez nous : **toujours
  AFFICHER le prompt complet en bloc, jamais le décrire**.
- **Verdict par élément** :
  | Élément | Verdict |
  |---|---|
  | Squelette de sections (Purpose→…→checklist) | **ADAPTER** (structure — cf. §2) |
  | Règle « display the full prompt » | **ADAPTER** (principe, reformulé FR) |
  | `Required Output Format` (4 sous-sections) | **ADAPTER** (structure) |
  | Listes de techniques (CoT, ToT, self-consistency…) | **S'INSPIRER** (noms de méthodes = non protégeables ; rédiger en propre) |
  | Noms de modèles tiers (GPT-5.4, Llama, Mixtral…) | **IGNORER** (on cible nos MCP : Higgsfield / RapidoCMS) |
  | `scripts/optimize-prompt.py` | **S'INSPIRER** (idée d'un scorer de prompt ; réécrire nous-mêmes) |

### 1.2 `Hao0321/ai-media-generator` — MIT © 2026 · S'INSPIRER (⚠️ purge IP)

- **Structure** : `SKILL.md` racine + `references/` (34 fiches modèles : `veo.md`,
  `kling.md`, `sora.md`, `midjourney.md`, `flux.md`, `nano-banana.md`, `runway.md`,
  `seedance.md`, `suno.md`… + fiches méthode : `prompt-craft-engine.md`,
  `concept-first-prompting.md`, `quality-control.md`, `model-picker.md`,
  `director-style-library.md`, `camera-language.md`) + `templates/` (`storyboard.md`,
  `negative-bank.md`, `preset-packs.md`, `token-efficient-mode.md`, `user-flags.md`…)
  + `automation/` (browser guide, site-profiles).
- **Taxonomie** : entrée par **plateforme** (Step 1 choix plateforme → Step 2 lecture
  de la reference correspondante → Step 3 template selon type de tâche → Step 4
  assemblage du prompt → Step 5 automatisation optionnelle). **Meta priority /
  hard-rules** + **grille d'auto-notation 10 points avant envoi** + **negative-bank**
  (banque de tokens négatifs) + **model-picker** (arbre de décision modèle).
- **Fiche** : par modèle, une reference documente specs d'entrée, grammaire de prompt,
  anti-modèles, bonnes pratiques — **structure très proche de nos `pieges-outils.md`**.
- **⚠️ Références IP tierces / artistes vivants (À EXCLURE de la francisation)** :
  - `references/director-style-library.md` : **31 réalisateurs nommés** (Christopher
    Nolan, Wong Kar-wai, Park Chan-wook, Quentin Tarantino, Wes Anderson, David
    Lynch, Darren Aronofsky, Paul Thomas Anderson, Miyazaki, Lynne Ramsay…) avec la
    consigne `in the style of {Director Name}`. **Artistes vivants → interdit dans nos patterns.**
  - `references/proven-prompts.md` : « **Apple**-style product reveal », « iPhone
    selfie look », grammaire **Midjourney** (`--sref/--sw/--ar/--oref`). **IP tierces.**
- **Verdict par élément** :
  | Élément | Verdict |
  |---|---|
  | Taxonomie plateforme→reference→template (workflow 5 étapes) | **S'INSPIRER** |
  | Grille d'auto-notation 10 points avant envoi | **S'INSPIRER** (concept ; réécrire) |
  | `negative-bank` / `model-picker` (idées) | **S'INSPIRER** |
  | Fiches par modèle (structure ≈ `pieges-outils`) | **S'INSPIRER** (structure) |
  | `director-style-library.md` (31 réalisateurs vivants) | **IGNORER — EXCLU** (artiste vivant / droit à l'image du style) |
  | Grammaire propriétaire Midjourney (`--sref` etc.) | **IGNORER** (on ne cible pas MJ ; cibler Higgsfield/RapidoCMS) |
  | Mentions « Apple / iPhone-style » | **IGNORER — EXCLU** (IP tierce) |

### 1.3 `rediumvex/ai-video-generator-claude` — MIT © 2026 Roman Knox · S'INSPIRER

- **Structure** : `install.py` + `skills/01-viral-hook … 10-podcast-visual/` (10
  dossiers, chacun un `SKILL.md`). Pas de `plugin.json`/marketplace.
- **Taxonomie** : 1 skill = **1 couple (format × objectif marketing)** : viral-hook,
  saas-launch, personal-brand, course-promo, faceless-channel, luxury-aesthetic,
  before-after, testimonial-story, ai-avatar, podcast-visual.
- **Fiche exemplaire** : `description` **très déclenchable** (liste explicite de
  triggers : « viral, hook, scroll-stop, retention, Reels, Shorts, TikTok… ») —
  modèle du style « Utiliser quand… » qu'on impose déjà en maison. Corps :
  specs d'entrée du modèle (Seedance/Higgsfield) → « attention economy » (budget
  temps 0-2 s / 2-5 s / 5-15 s) → structure de prompt.
- **Verdict par élément** :
  | Élément | Verdict |
  |---|---|
  | Style de `description` déclenchable (liste de triggers) | **S'INSPIRER** (conforte notre règle « Utiliser quand… ») |
  | Découpage « format × objectif » comme grille de presets | **S'INSPIRER** |
  | Budget temporel du hook (0-2/2-5/5-15 s) | **S'INSPIRER** (concept ; recouvre déjà `rapido-higgsfield:analyse-video-virale`) |
  | Ciblage produit (Seedance/Higgsfield-spécifique) | **IGNORER** pour le prompteur (déjà couvert par `rapido-higgsfield`) |

### 1.4 `ZeroLu/awesome-nanobanana-pro` — MIT © 2025 ZeroLu · S'INSPIRER (⚠️ purge IP lourde)

- **Structure** : `README.md` (catalogue « awesome ») + `assets/` (images). Contenu =
  liste numérotée de recettes (`1. Photorealism & Aesthetics`, `2. Creative
  Experiments`, …).
- **Fiche** : `### N.M. Titre` → *intention en italique* → image d'exemple →
  `**Prompt:**` en **bloc JSON structuré** (subject/expression/hair/clothing/face/
  accessories…), avec `preserve_original` pour les selfies.
- **Apport** : le **format de fiche prompt** (titre + intention + bloc structuré) et
  l'idée d'un **prompt JSON schématisé** pour Nano Banana Pro (modèle qu'on utilise
  déjà via Higgsfield/RapidoCMS).
- **⚠️ Références IP tierces (À EXCLURE de la francisation)** : « **Victoria's Secret**
  Style Photoshoot », « **Star Wars** Where's Waldo », « **iPhone 17 Pro** », « Movie
  Character Selfie », « Museum Art Exhibition ». Nombreuses marques / franchises.
- **Verdict par élément** :
  | Élément | Verdict |
  |---|---|
  | Format de fiche (titre + intention + bloc prompt) | **S'INSPIRER** (structure) |
  | Idée de prompt JSON schématisé Nano Banana | **S'INSPIRER** |
  | Recettes nommées d'après des marques/franchises | **IGNORER — EXCLU** (Victoria's Secret, Star Wars, iPhone…) |
  | Images `assets/` (visages, exemples) | **IGNORER** (poids + droit à l'image) |

### 1.5 `KingLeoJr/prompts` — MIT © 2025 KingLeoJr · IGNORER (hors périmètre média)

- **Structure** : ~45 dossiers « 1 projet = 1 prompt » (WooCommerce, LMS, SEO,
  SAASDashboard, DirectoryWebsite…). Chaque entrée = brief **développement web**
  (specs pages, images, plugins WP), pas de prompt média/visuel.
- **Fiche** : texte libre à puces (specs fonctionnelles + « Image Specifications »).
- **Verdict par élément** :
  | Élément | Verdict |
  |---|---|
  | Contenu (briefs dev web) | **IGNORER** (hors sujet « directeur de prompts média ») |
  | Idée « 1 dossier nommé = 1 brief réutilisable » | **S'INSPIRER** (faible — recoupe `bibliotheque-prompts`) |

### 1.6 `contains-studio/agents` — **AUCUN LICENSE** · S'INSPIRER (structure only, ZÉRO vendoring)

- **Adjudication licence (demandée)** : **il n'existe AUCUN fichier `LICENSE`/`LICENCE`
  dans le dépôt** (le seul fichier contenant « legal » est
  `studio-operations/legal-compliance-checker.md`, un agent sans rapport). Le README
  ne comporte **aucune section licence**, uniquement « Installation / Quick Start /
  Contributing ». **Conséquence juridique : en l'absence de licence explicite, le
  code est « tous droits réservés » par défaut** (le dépôt public n'accorde PAS de
  droit de redistribution/modification).
  → **On ne vendorise RIEN** (aucun fichier copié dans notre dépôt). On peut
  **s'inspirer de la structure** d'un fichier d'agent — une idée/mise en page
  (frontmatter `name/description/examples/color/tools` + corps « You are a [role]… /
  responsibilities / goal ») n'est **pas** protégeable — **mais jamais le texte**.
- **Structure** : agents `.md` classés par **département** (`design/`, `engineering/`,
  `marketing/`, `product/`, `project-management/`, `studio-operations/`, `testing/`,
  `bonus/`). Frontmatter : `name`, `description` (avec `<example>…<commentary>`),
  `color`, `tools`.
- **⚠️ Référence IP tierce** : exemples citant « **Headspace** » (marque vivante) dans
  `design/brand-guardian.md`. À ne pas reprendre.
- **Verdict par élément** :
  | Élément | Verdict |
  |---|---|
  | Rangement des agents par département | **S'INSPIRER** (idée d'organisation) |
  | Frontmatter `name/description/examples` déclenchable | **S'INSPIRER** (structure — déjà notre standard) |
  | **Tout texte de prompt** | **IGNORER — INTERDIT de copier** (pas de licence) |
  | Exemples « Headspace », concurrents nommés | **IGNORER — EXCLU** |

### 1.7 `wuyoscar/GPT-Image2-Skill` — dépôt lourd · IGNORER (non audité en profondeur)

- **825 Mo** (essentiellement des images). Conformément à la consigne « ignore le
  poids des images », **non ouvert en détail** dans cet audit. LICENSE non lue.
  → **IGNORER pour l'instant** ; ré-auditer plus tard si un besoin précis émerge
  (lecture des seuls fichiers texte, sans les assets).

---

## 2. Squelette proposé pour `directeur-prompts` (STRUCTURE copiée de `wshobson/prompt-engineer`, PAS le texte)

> Reprise de la **charpente** MIT de `wshobson/agents` (attribution due dans un
> futur `NOTICE.md`), **entièrement à rédiger en français maison**. Ceci est une
> **proposition d'ossature**, pas un skill créé.

```
---
name: directeur-prompts
description: >-
  Utiliser quand… l'utilisateur veut concevoir, améliorer, débuguer ou
  standardiser un prompt (image/vidéo/audio/3D via Higgsfield ou RapidoCMS,
  ou copy). Le directeur ORCHESTRE les skills prompts existants — il ne les
  remplace pas.
model: inherit
---

## Rôle                     ← (≈ « You are… », réécrit FR)
## Règle d'or               ← TOUJOURS afficher le prompt complet en bloc copiable, jamais le décrire
## Capacités                ← techniques (CoT, few-shot, structured output, méta-prompt),
                              cadrées sur NOS cibles (Higgsfield/RapidoCMS), pas GPT/Llama
## Démarche (étapes)        ← comprendre le besoin → lire la grammaire outil en live
                              (models_explore / get_brand / pieges-outils) → concevoir →
                              AFFICHER le prompt → notes → tests → garde-fous
## Format de sortie imposé  ← 1) LE PROMPT (bloc)  2) Notes d'implémentation
                              3) Tests & évaluation  4) Mode d'emploi
## Garde-fous               ← anti-verbatim ; AUCUNE IP tierce / artiste vivant ;
                              données réelles seulement (manque → « backend Tunis »)
## Exemples de sollicitation
## Checklist avant de rendre ← ☐ prompt affiché ☐ testable ☐ sans IP tierce ☐ charte respectée
```

**Écarts volontaires vs wshobson** : (a) cibles = nos MCP, pas les modèles tiers ;
(b) ajout d'un garde-fou **IP tierce / artiste vivant** (absent de l'original) ;
(c) lecture **live** de la grammaire outil avant rédaction (principe maison) ;
(d) rôle d'**orchestrateur** (renvoi vers les skills existants, cf. §3).

---

## 3. « Qui fait quoi demain » — le prompteur ORCHESTRE, il ne remplace pas

| Skill existant (plugin) | Rôle aujourd'hui | Demain, sous `directeur-prompts` |
|---|---|---|
| **`prompt-engineering-visuel`** (rapidocms) | Méthode de construction d'un prompt image conforme charte | **Exécutant** appelé par le directeur pour la couche « image » |
| **`prompts-visuels-pro`** (rapidocms) | Recettes/presets visuels avancés | **Bibliothèque de patterns** que le directeur sélectionne |
| **`bibliotheque-prompts`** (rapidocms) | Capitalisation (`add_prompt`, réutilisation) | **Mémoire** : le directeur y enregistre/relit les prompts validés |
| **`ideation-lovable-prompt`** (rapido-forge) | Génère le brief/prompt d'app Lovable | **Exécutant** couche « produit/app » |
| *(gén. média)* `rapido-higgsfield:*` (studio-image-pro, usine-video-marketing, analyse-video-virale…) | Génération image/vidéo/voix, grille de coûts | **Cible d'exécution** : le directeur prépare le prompt, Higgsfield génère |

**Règle d'orchestration** : `directeur-prompts` (a) **détecte l'intention** (image /
vidéo / voix / 3D / app / copy), (b) **lit la grammaire de l'outil cible en live**
(`models_explore`, `get_brand`, `pieges-outils`), (c) **compose** le prompt en
délégant à la méthode maison adéquate, (d) **capitalise** via `bibliotheque-prompts`.
Il **n'écrit pas** les prompts image « à la place » de `prompt-engineering-visuel` :
il les **cadre, standardise et route**.

---

## 4. Contrôles (licence · anti-verbatim · IP tierces / artistes vivants)

### 4.1 Licences (lues dans `LICENSE`)
| Dépôt | Verdict licence | Vendoring autorisé ? |
|---|---|---|
| wshobson/agents | MIT © 2024 Seth Hobson | ✅ (attribution NOTICE) — mais on ne copie que la **structure** |
| Hao0321/ai-media-generator | MIT © 2026 contributors | ✅ (attribution) — on ne prend que des **idées/structures** |
| rediumvex/ai-video-generator-claude | MIT © 2026 Roman Knox | ✅ (attribution) — idées seulement |
| ZeroLu/awesome-nanobanana-pro | MIT © 2025 ZeroLu | ✅ (attribution) — format de fiche seulement, **pas les recettes IP** |
| KingLeoJr/prompts | MIT © 2025 KingLeoJr | ✅ — mais hors périmètre |
| **contains-studio/agents** | **AUCUNE licence → tous droits réservés** | ❌ **VENDORING INTERDIT** — structure/idée uniquement |
| wuyoscar/GPT-Image2-Skill | non lue (dépôt lourd) | ⏸️ à statuer avant tout usage |

### 4.2 Anti-verbatim (règle transverse)
- **Zéro copier-coller** de texte de prompt, de description ou de corps d'agent.
- On importe des **structures** (rubriques, ordre, format de fiche, checklist) et des
  **concepts** (grille d'auto-notation, negative-bank, budget temporel du hook) —
  tous **non protégeables** — puis on **rédige en français maison**.
- Attribution obligatoire des sources MIT dans un futur `NOTICE.md` du plugin
  prompteur (Seth Hobson, Roman Knox, ZeroLu, Hao0321 contributors).

### 4.3 IP tierces / artistes vivants — **À EXCLURE de toute francisation**
| Source | Éléments interdits dans nos patterns |
|---|---|
| Hao0321 `director-style-library.md` | **31 réalisateurs vivants** nommés + `in the style of {Director}` |
| Hao0321 `proven-prompts.md` | « Apple-style », « iPhone look », grammaire Midjourney propriétaire |
| ZeroLu README | « Victoria's Secret », « Star Wars », « iPhone 17 Pro », « Movie Character » |
| contains-studio brand-guardian | « Headspace » et autres concurrents nommés |

> **Politique maison** : nos prompts décrivent des **styles génériques** (« symétrie,
> pastel, plans larges IMAX-like » **sans nommer** un réalisateur ou une marque). On
> ne référence **jamais** un artiste vivant ni une IP tierce — on **décrit l'effet
> visuel**, pas l'auteur.

---

## 5. Lisibilité des grammaires outils — vérifiée EN LIVE, coût nul

| Grammaire | Vérif live | Résultat | Coût |
|---|---|---|---|
| **`models_explore` (Higgsfield) par type** | `action:list, type:image` et `type:video` | Renvoie params + `options`/`min`/`max`, `aspect_ratios`, `durations`/`duration_range`, `tags` par modèle (Nano Banana 2/Pro, Soul 2.0, GPT Image 2, Cinema Studio Video 3.0, Marketing Studio, Personal Clipper…). `action:get`, `search`, `recommend` disponibles. | **0 crédit** (lecture) |
| **`get_brand` (RapidoCMS)** | Schéma outil chargé | 1 paramètre `nom` (string) ; outil de **lecture** → renvoie la marche (nom, slogan, langue, couleurs, font, logo, assets). | **0 crédit** |
| **`pieges-outils` des plugins** | Lecture disque | 8 fichiers présents : `rapido-marketing`, `rapidocrm`, `rapido-higgsfield`, `foodeatup`, `rapidorh`, `rapidocms`, `rapido-suite`, `rapido-startup`. | **0** (fichiers dépôt) |

**Solde Higgsfield avant/après l'audit : 80 crédits (plan basic) — inchangé.**
→ **Toutes les grammaires sont lisibles à coût nul.** `models_explore` fournit
la source d'autorité pour cadrer les prompts vidéo/image (le directeur la lit en
live avant chaque composition, jamais « de tête »).

---

## 6. Récapitulatif & STOP

- **7 dépôts clonés** (frères, `--depth 1`), **0 fichier importé** dans le dépôt
  marketplace (audit pur). Aucun crédit consommé (solde 80 inchangé).
- **Licences** : 5 MIT (attribution due), **contains-studio sans licence → vendoring
  interdit**, wuyoscar non statué (dépôt lourd).
- **À importer** : la **structure** du `prompt-engineer` wshobson (§2), des **idées**
  (grille 10 points, negative-bank, format de fiche, `description` déclenchable),
  **jamais de texte**, **jamais d'IP tierce / artiste vivant** (§4.3).
- **Rôle du plugin prompteur** : **orchestrateur** des skills prompts existants (§3).
- **Grammaires outils** : lisibles **à coût nul**, vérifiées en live (§5).

> **STOP — en attente de validation de `docs/IMPORTS-PROMPTEUR.md` avant PR1.**
> Aucun skill/plugin ne sera créé tant que ce document n'est pas validé.
