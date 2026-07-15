# Recette réelle — rapido-leadmagnet (runbook client)

Lead magnet FoodEatUp de bout en bout :
**« Checklist HACCP : les 15 contrôles quotidiens d'un restaurant en règle »**.

> **Statut : à exécuter côté client.** Cette recette crée de la **donnée de
> production réelle** (landing Lovable, projet + tâches RapidoRH, segment + prospects
> CRM, vidéo Higgsfield **payante**, campagne Meta) et engage des **coûts** (crédits
> Higgsfield, budget Meta). Elle n'est **pas** jouée dans l'environnement de build
> pour ne pas polluer la prod ni dépenser sans votre accord. Chaque étape ci-dessous
> est le **mode opératoire** + la grille de relevé. Aucun résultat n'est simulé.

## Prérequis

- MCP connectés : RapidoCRM, RapidoCMS, RapidoRH (natifs) ; **Lovable** (landing) ;
  **Higgsfield** (vidéo, `HIGGSFIELD_MCP_URL`) ; **Meta/Facebook Ads** (pub).
- Charte FoodEatUp dans le CMS (`get_brand`) ; `rapido-kb/` renseignée (ton, ICP).
- **Un seul lead magnet en production à la fois** (garde-fou focus).

## Déroulé

| # | Étape | Skill | Attendu | À relever |
|---|---|---|---|---|
| a | **Conception** | `rapido-marketing:lead-magnet-machine` | Concept validé (type=checklist, promesse, next step=RDV démo FoodEatUp) | — |
| b | **Fabrication** | `fabrication-lead-magnet` | Gate qualité passé → PDF brandé FoodEatUp → `upload_file_tool` → **URL vérifiée** → registre | Durée · score gate · URL PDF |
| c | **Page + capture** | `page-et-capture` | Landing Lovable (mode B) + formulaire consentement + segment `LM-checklist-haccp` + **test de bout en bout** (email test → prospect + email + PDF) | URL landing · résultat test · IDs (segment, prospect test) |
| d | **Campagne** | `campagne-lead-magnet` | 2 posts CMS (annonce + valeur) + 1 **vidéo Higgsfield** (9:16, self_ai_disclosure, **coût confirmé**) + campagne Meta **PAUSED non activée** | Coût vidéo · IDs posts/campagne · budget max Meta (non activé) |
| e | **Projet RH** | `projet-rh-lead-magnet` | Projet « LM — Checklist HACCP » + ~20 tâches **affectées aux agents IA** (résolus via `get-users-list-tool`) | ID projet · nb tâches · agents assignés |
| f | **Mesure J0** | `campagne-lead-magnet` | `scripts/stats_leadmagnet.py` sur les premières soumissions → CPL/conv. (ou « — » si J0 vide) | Soumissions J0 · CPL |

## Grille de relevé (à remplir à l'exécution)

| Étape | Durée | Coût réel | Frictions | IDs / URLs |
|---|---|---|---|---|
| a Conception | | 0 | | |
| b Fabrication (PDF) | | 0 | | |
| c Page + capture | | 0 | | landing / segment / prospect test |
| d Campagne (vidéo + Meta) | | **crédits Higgsfield + budget Meta (non activé)** | | posts / campagne |
| e Projet RH | | 0 | | projet / tâches |
| f Mesure J0 | | 0 | | |

## Garde-fous rappelés

- **Meta en PAUSED**, activation **écrite séparée** (hook `garde-budget-ads`).
- **Vidéo Higgsfield = coût** → confirmation avant génération ; `self_ai_disclosure`
  activé sur Meta.
- **Gate délivrabilité** avant toute séquence de nurturing ; envois confirmés.
- **RGPD** : consentement non pré-coché, désinscription honorée.
- **Rien d'inventé** : preuves = données CRM réelles ; stats par script.

> Une fois cette grille remplie sur un run réel, le passage **rapido-leadmagnet
> 1.0.0** est justifié. Jusque-là, le plugin est livré **feature-complete en 0.5.0**
> (4 skills + 1 agent), la recette réelle **déférée** à votre environnement connecté.
