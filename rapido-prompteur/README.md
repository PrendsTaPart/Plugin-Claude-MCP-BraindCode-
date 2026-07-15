# rapido-prompteur

**Directeur de prompts.** Orchestre la conception de prompts (image, vidéo, web,
audio, design) pour **Higgsfield, RapidoCMS, Lovable et Canva**. Il **ORCHESTRE,
il ne remplace pas** les skills prompts existants (cf. `docs/IMPORTS-PROMPTEUR.md`).

> **Prérequis utilisateur : AUCUN.** `marketplace add` + `install` + MCP connectés.

## La RÈGLE D'OR

> **On ne mémorise jamais les paramètres d'un moteur. On les LIT à chaque session,
> en direct, avant d'écrire le prompt.** Résolutions, ratios, durées et options
> changent sans préavis — la seule source fiable est le moteur lui-même. Détail :
> `reference/grammaire-des-moteurs.md` (tableau moteur → où lire, à **coût nul**).

## Contenu (0.2.0)

| Élément | Rôle |
|---|---|
| `skills/prompt-lovable/` | Brief Lovable structuré (rôle → pages → design charte → mode B CRM → interdits → critères testables) |
| `skills/prompt-personnage/` | Banque de traits combinatoire → prompts de scène cohérents avec le canon (routage CMS/Higgsfield) |
| `reference/grammaire-des-moteurs.md` | Règle d'or + tableau moteur → où lire ses contraintes en live |
| `reference/regles-de-construction.md` | Anatomie d'un prompt par média + INTERDITS (IP/artistes) + délégations |
| `reference/ip-a-risque.md` | Liste maison des IP/marques/artistes à risque (source du garde anti-IP) |
| `assets/patterns/` | 8 patterns francisés par usage (packshot, portrait, food, ugc-ad, cinématique, personnage, hooks-viraux, web-apps) |
| `hooks/` | `Stop` (récap prompts) + `PreToolUse` `anti-ip.py` (scan anti-IP → confirmation) |
| `NOTICE.md` | Licences MIT des sources distillées + exclusions |

## Ce que le prompteur délègue (pas de doublon)

- **Négatifs + protocole zéro faute** → `rapidocms:prompts-visuels-pro`.
- **Structure 6 blocs image + capitalisation** → `rapidocms:prompt-engineering-visuel`,
  `rapidocms:bibliotheque-prompts`.
- **Brief app Lovable** → `rapido-forge:ideation-lovable-prompt`.
- **Génération média + coûts** → `rapido-higgsfield:*` ; **montage libre** →
  `rapido-video:*` ; **analyse virale** → `rapido-higgsfield:analyse-video-virale`.

## Garde-fous

- **Anti-IP automatique** : le hook `anti-ip.py` scanne les prompts sortants vers
  les moteurs de génération (Higgsfield / RapidoCMS / Lovable / Canva). Détection
  d'une marque/franchise/artiste (liste `reference/ip-a-risque.md`) ou d'une formule
  « style de [artiste] » → **confirmation avec avertissement** (ne bloque pas).
- **Aucune IP tierce, aucun style d'artiste vivant, aucun personnage sous licence.**
- **Données réelles uniquement** (charte via `get_brand`/KB ; manque → « backend Tunis »).

## Skills

- **`prompt-lovable`** — « prompt Lovable », « brief pour le site/app/landing ».
  Brief structuré branché marque (`get_brand`) + CRM (mode B). Distinct de
  `rapido-forge:ideation-lovable-prompt` (idéation) et des builders `rapido-lovable`.
- **`prompt-personnage`** — banque de traits combinatoire (canon verrouillé + axes
  de scène) → prompts cohérents ; routage `rapidocms:coherence-personnage` (image)
  ou `rapido-higgsfield:personnages-univers` (réaliste/vidéo) ; boucle d'apprentissage.

D'autres skills (ex. `directeur-prompts` orchestrateur) pourront s'ajouter.
