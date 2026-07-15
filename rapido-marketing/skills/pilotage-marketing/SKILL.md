---
name: pilotage-marketing
description: Utiliser quand l'utilisateur dit « pilote mon marketing », « fais le point marketing », veut une boucle de pilotage marketing (Sense → Plan → Act → Feed → Report) ou un rapport de pilotage hebdo. Orchestre le marketing de bout en bout — diagnostic KPI/pipeline/contenus/pubs, priorisation ICE des actions, délégation aux machines et agents, capitalisation, rapport une page — gouverné par la politique d'autonomie.
---

# Pilotage marketing — le Loop Engine du marketing

Orchestrateur : il **ne fait rien lui-même**, il diagnostique, priorise, délègue
aux skills/agents d'exécution, capitalise et rend compte. Boucle **Sense → Plan →
Act → Feed → Report**.

## Anti-collision
- **`rapido-suite:pilotage-entreprise`** (au-dessus) : voir ci-dessous.
- **`rapido-seo:pilotage-seo`** (en dessous) : le **sous-domaine SEO/organique**. Si
  `rapido-seo` est installé, ce skill **invoque `pilotage-seo`** pour son volet
  organique (SENSE + ACT organique) **au lieu de le dupliquer** — même règle miroir
  que `pilotage-entreprise ↔ pilotage-marketing`.

## Anti-collision avec `rapido-suite:pilotage-entreprise`
Ce skill est le **sous-domaine marketing** du pilotage transverse. **Si
`rapido-suite` est installé**, `rapido-suite:pilotage-entreprise` **invoque ce
skill** pour son volet marketing (SENSE + PLAN + ACT marketing) **au lieu de le
dupliquer**. Invoqué seul, il pilote le marketing de bout en bout. (Règle miroir
documentée dans les deux README.)

## Gouvernance (obligatoire)
- **Si `rapido-suite` est installé** : charger `rapido-suite/reference/autonomie.md`
  — lecture en autonomie totale ; **écriture confirmée par système** ; **actions
  sensibles (envoi, publication, activation pub, lancement, suppression) confirmées
  une par une** ; en cas d'échec, arrêt à l'étape + récap des IDs déjà créés.
- **Sinon (mode prudent par défaut)** : **tout écrit = confirmation explicite**.
- Le hook `garde-envois` reste le filet dans les deux cas.

## SENSE — lecture seule (le carburant)
Collecter, même période partout, sans rien inventer (serveur absent = volet sauté
en le disant) :
- **KPI réels** → `attribution-kpi-marketing` (attribution par canal, CAC/LTV/ROI).
- **Pipeline** → `rapidocrm:coaching-pipeline` (deals dormants, étapes, prévision).
- **Contenus** → `rapidocms:analyse-performance-contenu` (posts, portée, engagement).
- **Pubs Meta** → `rapido-meta-ads:pilotage-performance-ads` (dépense, ROAS, alertes).
- **SEO / organique** → `rapido-seo:pilotage-seo` (positions, striking distance,
  netlinking) — **si installé**, serveur absent = volet sauté en le disant.
- **SEA Google** → `rapido-google-ads:pilotage-performance-google-ads` (CPA/ROAS
  Google, lecture seule) — **si installé**, sinon sauté en le disant.
- **TikTok** → `rapido-tiktok-ads:pilotage-performance-tiktok` (CPM/CPC/CPA) — **si
  installé**, sinon sauté en le disant.
- **Automatisations** → `rapido-n8n:surveillance-automatisations` (échecs n8n récents).
- **Mémoire** → `./rapido-kb/marketing/apprentissages.md` **récents** (les leçons
  priment) + `benchmarks.md`.

## PLAN — priorisation chiffrée
1. **Score ICE des actions candidates** (jamais de tête) :
   `python3 "${CLAUDE_PLUGIN_ROOT}/skills/pilotage-marketing/scripts/prioriser_actions.py"`
   → actions triées (impact×confidence×ease), **allocation par machine**
   (inbound / outbound / tunnel / paid).
2. **Anti-doublon** : AVANT de créer une tâche, **lire le Kanban RapidoRH**
   (`get-projects-list-tool` puis `get-project-tasks-tool`) et passer les titres
   existants au script (`taches_kanban`) — une action déjà au Kanban n'est **pas
   recréée**.
3. **Estimation du coût IA** (`reference/cout-ia.md`) : calculs → script ; jugement
   → modèle ; **volume → routine n8n**. Une action de volume restée manuelle est
   requalifiée en routine (voir `reference/routines.md`).

## ACT — délégation (chaque action sensible confirmée)
- Router par machine vers les **agents / skills** :
  - inbound → agent `inbound-manager` / skill `machine-inbound` ;
  - outbound → agent `outbound-manager` / skill `machine-outbound` ;
  - tunnel → agent `funnel-builder` / skill `tunnel-de-vente-360` ;
  - paid → **Meta** (`rapido-meta-ads`) **OU Google** (`rapido-google-ads`, lecture →
    actions manuelles) **OU TikTok** (`rapido-tiktok-ads`, verrouillé) selon
    l'arbitrage de l'agent `directeur-marketing` (mêmes KPIs via `catalogue-kpi`) ;
  - organique → `rapido-seo:pilotage-seo` (sous-domaine SEO — voir Anti-collision) ;
  - lecture/analyse → agent `growth-analyst`.
- Arbitrage stratégique global → agent `directeur-marketing`.
- **Tout envoi / publication / activation / lancement = confirmation** (garde-envois
  + autonomie.md). Créer les tâches retenues au Kanban (`create-task-tool`) après
  vérification anti-doublon.

## FEED — capitalisation & réaffectation
- **Capitalisation** : 1-3 leçons datées et **sourcées** (chiffre du script) dans
  `apprentissages.md`, `benchmarks.md` mis à jour si un taux change — via
  `rapido-suite:mise-a-jour-kb`. Pas de leçon sans preuve chiffrée.
- **Échec d'une action** : réaffecter (autre machine / autre angle). **2 échecs sur
  la même action → escalade humaine** avec diagnostic (ce qui a été tenté, données,
  hypothèse) — ne pas boucler à l'infini.
- **Kanban** : mettre à jour l'état des tâches traitées.

## REPORT — une page
- **📊 KPI vs objectifs** (formules) | **✅ actions menées** | **🔴 décisions à
  prendre** | **⏭️ prochaine itération** | **📋 récap des IDs** (tâches, campagnes,
  workflows créés).

## Routines récurrentes (proposées, installées sur confirmation)
Proposer les 3 routines de `reference/routines.md` via
`rapido-n8n:usine-automatisations` : **R-MKT-HEBDO** (lundi : rapport pilotage),
**R-MKT-QUOTIDIEN** (sentinelle leads > 24 h + soumissions orphelines),
**R-MKT-MENSUEL** (board attribution + benchmarks + décisions). Ces trois noms sont
des **alias** des identifiants canoniques `MKT-HEBDO` / `MKT-QUOTIDIEN` / `MKT-MENSUEL`
du registre unifié `reference/registre-routines.md` (racine du monorepo, fait foi) —
les deux formes déclenchent la même routine. Chaque routine a
sa table mémoire ; installer **seulement** celles confirmées.

## Garde-fous
Gouvernance `autonomie.md` (sinon mode prudent = tout écrit confirmé) ;
priorisation et KPI **par script**, jamais de tête ; **anti-doublon Kanban avant
création** ; 2 échecs → escalade ; données live > KB > défauts, jamais inventées ;
sous-domaine de `rapido-suite:pilotage-entreprise` (pas de duplication).
