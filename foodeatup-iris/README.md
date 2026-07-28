# foodeatup-iris

**Iris** — le quatrième agent : la communication. Le restaurant lui-même, qui
tient son image et parle en son nom. Iris **n'invente pas de contenu : elle
trouve des raisons de publier** dans les données d'exploitation FoodEatUp, puis
fabrique le visuel (RapidoCMS) ou la vidéo du plat (Higgsfield) aux couleurs de
la maison — et ne publie **jamais** sans validation humaine.

> Il reste 12 kg de saumon. Iris l'a vu, elle a fait le visuel, écrit le post,
> et proposé le tout pour demain 11h — avec sa raison. Vous validez d'un doigt.

## La boucle (5 étages)

| Étage | Skill | Ce qui s'y passe |
|---|---|---|
| ⓪ Prérequis | `appairage-marque-iris` | établissement FoodEatUp ↔ marque RapidoCMS (charte, comptes, assets) |
| ① + ② Capteurs & moteur | `moteur-opportunites-iris` | 11 signaux d'exploitation, score urgence × valeur × fraîcheur, dédup, raison |
| ③ Fabrique | `fabrique-contenu-iris` | visuel + copy + raison, gate charte (2 tentatives max) |
| ③bis Vidéo | `video-virale-plats` | vraies photos de plats → vidéo courte Higgsfield (9:16), `virality_predictor`, coûts confirmés |
| ④ Diffusion | `calendrier-iris` | 7 jours glissants, valider / modifier / refuser (motif), planification confirmée |
| ⑤ Mesure | `mesure-apprentissage-iris` | insights réels, commandes corrélées 48 h, prompts capitalisés, refus appris |

Agent : **`iris`** (persona). État local : `./rapido-kb/iris/` (marque,
journal des signaux, calendrier, apprentissage, paramètres).

## Garde-fous (hook `garde-iris.py`, testé en CI)

- **Publication/planification** (`schedule_draft_tool`, `tiktok_publish`…) →
  confirmation humaine TOUJOURS, aucun réglage pour la contourner.
- **Génération vidéo payante** sans coût confirmé (`cout_confirme`) → refus
  avec marche à suivre. Les crédits s'annoncent avant, jamais après.
- Avis négatif → alerte au patron, **zéro** proposition de contenu (règle du
  moteur + hook Stop qui exige la raison sur chaque proposition).

## Prérequis

- MCP **FoodEatUp** (signaux) et **RapidoCMS** (charte, brouillons,
  planification) connectés.
- MCP **Higgsfield** pour la vidéo : `export HIGGSFIELD_MCP_URL=…` (génération
  payante en crédits — voir docs/GRILLE-COUTS-HIGGSFIELD.md). Sans lui, Iris
  fonctionne en mode visuel seul (dégradation propre, annoncée).
- De **vraies photos de plats** (assets CMS ou photos fournies) : pas de
  photo → pas de vidéo du plat (règle d'honnêteté).

## Installation

```
/plugin marketplace add PrendsTaPart/Plugin-Claude-MCP-BraindCode-
/plugin install foodeatup-iris@rapido
```

Faisabilité détaillée vs cahier des charges (ce qui est plugin, ce qui reste
produit) : `docs/FAISABILITE-IRIS.md`.
