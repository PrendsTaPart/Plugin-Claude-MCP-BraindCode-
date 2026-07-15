# Recette réelle — rapido-design (runbook)

Le pipeline complet sur **une landing de démo** : de la charte au **MVP Lovable animé**,
avec **les mêmes tokens du début à la fin**.

> **Statut : à exécuter côté opérateur.** Le pipeline produit des **fichiers Figma**
> (FigJam, maquettes, design system) et un **projet Lovable** — écritures réelles qui
> consomment des crédits et touchent le workspace du client. Différé ici pour ne pas
> polluer un espace de prod sans accord. Les seuls writes CMS (`create_brand`/`edit_brand`,
> `upload_file_tool`) se font **après confirmation** (le CMS = source de vérité). Ci-dessous
> le mode opératoire + la grille de relevé du **fil rouge des tokens**.

## Prérequis

- **Figma MCP** connecté en session (`figma-*`), **Lovable** (workspace + droit de créer un
  design system), **RapidoCMS** (charte, `get_brand`).
- Une **marque** avec sa charte (couleurs hex, police, logo). Personnalisation dans
  `./rapido-kb/` (`charte-graphique.md`) — **rien d'inventé** : un manque se signale
  « à confirmer côté backend Tunis ».
- Rappel : le CMS ne stocke que **9 polices web-safe** ; la vraie police vit dans le DS
  Figma/Lovable (cf. `rapido-design/reference/passerelles.md`).

## Déroulé (les 7 étapes)

| # | Étape | Skill / agent | Attendu | À relever |
|---|---|---|---|---|
| a | **Charte** | `get_brand` + KB | Tokens de départ chargés (la charte existante **prime**) | couleurs hex, police |
| b | **Direction artistique** | `direction-artistique` | 3 directions filtrées par le jugement (ou déclinaison si charte imposée) + **un écran de principe Figma** ; mini-charte page « Fondations » | direction retenue, tokens nommés |
| c | **Sync CMS** (si évolution) | `direction-artistique` → `rapidocms:gestion-marques` | `edit_brand`/`create_brand` **après confirmation** + `charte-graphique.md` | diff charte confirmé |
| d | **Structure** | `architecture-info` | Sitemap + 2-3 user flows (FigJam) + wireframes **gris**, **validés avant hi-fi** | validation structure (O/N) |
| e | **Design system + hi-fi** | `studio-maquette` | DS Figma **d'abord** (variables des tokens, clair/sombre) → écrans hi-fi qui **consomment les variables** → **gates** critique + a11y (WCAG AA) | 0 valeur en dur ; verdicts gates |
| f | **Handoff Lovable** | `studio-maquette` → `rapido-lovable:mvp-lovable` | DS poussé en **projet design system Lovable** (confirmé/versionné) ; le MVP **démarre du DS** | ID projet DS Lovable |
| g | **Animations** | `animations-web` | Motion sobre (2-3 surfaces/écran) ; **`prefers-reduced-motion` sur chaque animation** ; perf `transform`/`opacity` 60 fps | recette avant/après |

Orchestration de bout en bout : agent **`directeur-ux`** (tient le fil rouge, arbitre à
2 itérations max, rapporte à `rapido-lovable:architecte-lovable`).

## Grille de relevé — fil rouge des tokens (à remplir à l'exécution)

| Token | Charte CMS | Variable Figma | DS Lovable | Identiques ? |
|---|---|---|---|---|
| Couleur primaire | #…… | var/primaire | token/primaire | O / N |
| Couleur secondaire | #…… | var/secondaire | token/secondaire | O / N |
| Fond / surface | #…… | var/surface | token/surface | O / N |
| Police (titres) | (9 web-safe) | famille réelle | famille réelle | vigilance* |
| Spacing (échelle) | — | échelle | échelle | O / N |

\* La police est le **seul point de divergence toléré** : CMS = la plus proche des 9
web-safe, DS = la vraie police. Tout le reste : **zéro divergence**.

## Garde-fous rappelés

- **Charte d'abord** (hook `garde-charte`) : aucune création Figma/Lovable sans charte
  chargée ; la maquette **consomme les tokens**, jamais de valeur en dur.
- **Structure validée avant tout pixel joli** ; **hi-fi refusée** sans wireframes validés.
- **Gates bloquants** : jugement anti-goût-IA, accessibilité **WCAG AA**,
  **`prefers-reduced-motion`** sur chaque animation.
- **Écritures confirmées** : sync CMS (niveau 2), **push DS Lovable** confirmé et versionné.
- **Provenance** : principes francisés (dépôts MIT, `NOTICE.md`) ; **aucune copie** de
  maquettes/shots de designers réels, aucune IP tierce dans les visuels.
