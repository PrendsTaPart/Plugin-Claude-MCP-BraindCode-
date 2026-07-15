# Registre unifié des routines — le catalogue canonique du marketplace

> **Ce fichier fait foi.** Le marketplace comptait trois numérotations qui se
> chevauchaient (`loop-engine-v2` R4-R9, `rapido-marketing` R-MKT-*, un playbook
> externe R0-R12) — « lance R5 » devenait ambigu. Chaque routine reçoit ici un
> **identifiant unique préfixé par domaine**. Les **anciens noms restent des alias
> reconnus** (rétrocompatibilité) : aucun déclencheur existant n'est cassé.

## Préfixes de domaine

| Préfixe | Domaine | Plugin propriétaire | État |
|---|---|---|---|
| `FIN-*` | Finance (trésorerie, board, CFO) | `rapido-startup` (`loop-engine-v2`) | actif |
| `STARTUP-*` | Exécution produit / startup | `rapido-startup` (`loop-engine-v2`) | actif |
| `GROWTH-*` | Acquisition / croissance | `rapido-startup` (`loop-engine-v2`) | actif |
| `VIDEO-*` | Production vidéo éditoriale | `rapido-startup` (`loop-engine-v2`) | actif |
| `MKT-*` | Marketing (pilotage, sentinelle, board) | `rapido-marketing` | actif |
| `VENTE-*` | Boucle commerciale (hygiène, relances, revue, expansion) | `rapidocrm` (`pilotage-commercial`) | actif (expansion : PROMPT 3) |
| `OPS-*` | Workflows événementiels de vente (n8n) | `rapido-n8n` | **réservé** (PROMPT 4) |

## Table des alias (rétrocompatibilité)

| Ancien nom | Identifiant canonique |
|---|---|
| `R4`, `R4-CFO-WEEKLY` | `FIN-CFO-HEBDO` |
| `R5`, `R5-STARTUP-BUILDER` | `STARTUP-BUILDER` |
| `R6`, `R6-GROWTH-LOOP` | `GROWTH-LOOP` |
| `R7`, `R7-CASH-SENTINEL` | `FIN-CASH-SENTINELLE` |
| `R8`, `R8-MONTHLY-BOARD` | `FIN-BOARD-MENSUEL` |
| `R9`, `R9-VIDEO-FACTORY` | `VIDEO-FACTORY` |
| `R-MKT-HEBDO` | `MKT-HEBDO` |
| `R-MKT-QUOTIDIEN` | `MKT-QUOTIDIEN` |
| `R-MKT-MENSUEL` | `MKT-MENSUEL` |

> Les fichiers de routine gardent leur nom de fichier historique (`R4-CFO-WEEKLY.md`…) :
> seul l'**identifiant parlé** est unifié. `loop-engine-v2` et `pilotage-marketing`
> reconnaissent les deux.

---

## Catalogue

### FIN-CFO-HEBDO  *(alias R4)*
- **Noms parlés** : « lance R4 », « routine du lundi », « revue finance », « CFO weekly ».
- **Cadence** : hebdomadaire — lundi matin.
- **Propriétaire** : `rapido-startup:loop-engine-v2` · **Fichier** : `.../references/routines/R4-CFO-WEEKLY.md`.
- **Skills délégués** : `gestion-depenses`, `devis-facture-relance` (rapidocrm), `catalogue-kpi`, `plan-financier-previsionnel` · **Agent** : `cfo-virtuel`.
- **Autonomie** : **niveau 1 max** (relances préparées, jamais envoyées).
- **Mémoire n8n** : — (journal `rapido-kb/startup/routines-journal.md`).

### STARTUP-BUILDER  *(alias R5)*
- **Noms parlés** : « lance R5 », « avancement startup », « delta d'exécution ».
- **Cadence** : hebdomadaire — mardi matin.
- **Propriétaire** : `rapido-startup:loop-engine-v2` · **Fichier** : `R5-STARTUP-BUILDER.md`.
- **Skills délégués** : `plan-execution-startup`, `setup-projet`, `mise-a-jour-kb` (+ RapidoRH tasks/dailies).
- **Autonomie** : **niveau 2 max** (tâches delta après confirmation).
- **Mémoire n8n** : — (`plan-execution.md` + journal).

### GROWTH-LOOP  *(alias R6)*
- **Noms parlés** : « lance R6 », « boucle growth », « expérience de la semaine ».
- **Cadence** : hebdomadaire — jeudi.
- **Propriétaire** : `rapido-startup:loop-engine-v2` · **Fichier** : `R6-GROWTH-LOOP.md`.
- **Skills délégués** : `calendrier-editorial`, `lancement-campagne-meta`, `usine-a-landing`, `animation-client`, `catalogue-kpi`, `mise-a-jour-kb`.
- **Autonomie** : **niveau 1 max** (expérience préparée : brouillons, campagne PAUSED).
- **Mémoire n8n** : — (`growth-experiences.md` + journal).

### FIN-CASH-SENTINELLE  *(alias R7)*
- **Noms parlés** : « lance R7 », « sentinelle cash », « surveille ma trésorerie ».
- **Cadence** : quotidienne (ou 2×/sem) — matin.
- **Propriétaire** : `rapido-startup:loop-engine-v2` · **Fichier** : `R7-CASH-SENTINEL.md`.
- **Skills délégués** : `gestion-depenses`, `cash-flow-snapshot` (rapido-suite), `catalogue-kpi` · **Agent** : `cfo-virtuel`.
- **Autonomie** : **niveau 0 STRICT** — alerte seulement, aucune écriture.
- **Mémoire n8n** : version autonome dans `rapido-n8n/reference/recette-r7-cash-sentinel.md` (Schedule → Stripe → runway → alerte).

### FIN-BOARD-MENSUEL  *(alias R8)*
- **Noms parlés** : « lance R8 », « board mensuel », « pack investisseurs ».
- **Cadence** : mensuelle — 1er lundi du mois.
- **Propriétaire** : `rapido-startup:loop-engine-v2` · **Fichier** : `R8-MONTHLY-BOARD.md`.
- **Skills délégués** : `catalogue-kpi`, `mise-a-jour-kb`, `presentation-codir` (rapido-canva), `plan-financier-previsionnel`.
- **Autonomie** : **niveau 2 max** (board écrit dans la KB, jalon Calendar confirmé).
- **Mémoire n8n** : — (sortie `rapido-kb/startup/board/BOARD-AAAA-MM.md`).

### VIDEO-FACTORY  *(alias R9)*
- **Noms parlés** : « lance R9 », « épisode du jour », « vidéo du jour », « video factory ».
- **Cadence** : quotidienne (jours ouvrés) — ou rythme éditorial KB.
- **Propriétaire** : `rapido-startup:loop-engine-v2` · **Fichier** : `R9-VIDEO-FACTORY.md`.
- **Skills délégués** : `calendrier-editorial`, `video-marketing`, `prompts-visuels-pro` (rapidocms) · **Agent** : `gestionnaire-marques`.
- **Autonomie** : **niveau 1 max** — tout préparé ; **rendu (payant) et publication = accords explicites (niveau 3)**.
- **Mémoire n8n** : — (dépôt de production `PrendsTaPart/Video` + `videos-episodes.md`).

### MKT-HEBDO  *(alias R-MKT-HEBDO)*
- **Noms parlés** : « rapport marketing du lundi », « pilotage marketing hebdo ».
- **Cadence** : hebdomadaire — lundi 07:00 (cron `0 7 * * 1`).
- **Propriétaire** : `rapido-marketing` · **Fichier** : `rapido-marketing/reference/routines.md`.
- **Skills délégués** : `pilotage-marketing` (+ attribution/pipeline/contenus/pubs en lecture).
- **Autonomie** : préparé/alerte — email interne **en brouillon** (`garde-envois`).
- **Mémoire n8n** : `mkt_pilotage_journal`.

### MKT-QUOTIDIEN  *(alias R-MKT-QUOTIDIEN)*
- **Noms parlés** : « sentinelle leads », « leads non traités », « soumissions orphelines ».
- **Cadence** : quotidienne — 08:00 (cron `0 8 * * *`).
- **Propriétaire** : `rapido-marketing` · **Fichier** : `rapido-marketing/reference/routines.md`.
- **Skills délégués** : `pilotage-marketing` (détection ; leads > 24 h, formulaires orphelins).
- **Autonomie** : alerte seulement, action **jamais exécutée d'office**.
- **Mémoire n8n** : `mkt_sentinelle_leads` (anti-double-alerte).

### MKT-MENSUEL  *(alias R-MKT-MENSUEL)*
- **Noms parlés** : « board marketing », « attribution du mois », « arbitrage budget canaux ».
- **Cadence** : mensuelle — 1er du mois 07:00 (cron `0 7 1 * *`).
- **Propriétaire** : `rapido-marketing` · **Fichier** : `rapido-marketing/reference/routines.md`.
- **Skills délégués** : `attribution-kpi-marketing`, `pilotage-marketing` (benchmarks, décisions).
- **Autonomie** : board une-page — notification interne **en brouillon**.
- **Mémoire n8n** : `mkt_board_mensuel`.

---

### VENTE-HYGIENE
- **Noms parlés** : « hygiène des données », « nettoie mon pipeline », « qualité CRM ».
- **Cadence** : hebdomadaire — lundi (avant VENTE-REVUE).
- **Propriétaire** : `rapidocrm:pilotage-commercial` · **Fichier** : `rapidocrm/references/routines/VENTE-HYGIENE.md`.
- **Skills délégués** : `coaching-pipeline`, `devis-facture-relance` (lecture) ; score /100.
- **Autonomie** : **niveau 0** — diagnostic seul, aucune écriture.
- **Mémoire n8n** : — (série `rapido-kb/commercial/historique-hygiene.md`).

### VENTE-RELANCES
- **Noms parlés** : « relances du jour », « devis qui expirent », « relance mes deals dormants ».
- **Cadence** : quotidienne — 14h.
- **Propriétaire** : `rapidocrm:pilotage-commercial` · **Fichier** : `rapidocrm/references/routines/VENTE-RELANCES.md`.
- **Skills délégués** : `devis-facture-relance`, `redaction-commerciale`, `coaching-pipeline`.
- **Autonomie** : **niveau 1 max** — relances en brouillon confirmé.
- **Mémoire n8n** : `vente_relances_journal` (anti-double-relance, obligatoire).

### VENTE-REVUE
- **Noms parlés** : « revue commerciale », « couverture pipeline », « point ventes du lundi ».
- **Cadence** : hebdomadaire — lundi (après VENTE-HYGIENE).
- **Propriétaire** : `rapidocrm:pilotage-commercial` · **Fichier** : `rapidocrm/references/routines/VENTE-REVUE.md`.
- **Skills délégués** : `forecast`, `performance-commerciale` ; calculs → `rapido-startup:catalogue-kpi`.
- **Autonomie** : **niveau 1 max** — décisions préparées, aucune écriture d'office.
- **Mémoire n8n** : — (journal `rapido-kb/commercial/apprentissages.md`).

### VENTE-EXPANSION
- **Noms parlés** : « opportunités d'expansion », « qui faire monter en gamme », « upsell de la semaine », « éligibles ambassadeurs ».
- **Cadence** : hebdomadaire — jeudi.
- **Propriétaire** : `rapidocrm:pilotage-commercial` (skills `expansion-clients` + `programme-ambassadeurs`) · **Fichier** : `rapidocrm/references/routines/VENTE-EXPANSION.md`.
- **Skills délégués** : `expansion-clients`, `programme-ambassadeurs`, `redaction-commerciale`.
- **Autonomie** : **niveau 1 max** — propositions préparées, aucune écriture d'office.
- **Mémoire n8n** : — (journal `rapido-kb/commercial/apprentissages.md`).

---

## Réservé (prochains lots)

- **`OPS-*`** — workflows événementiels de vente (`rapido-n8n`) : `OPS-LEAD-CHAUD`,
  `OPS-CLIENT-GAGNE`, `OPS-ALERTE-CHURN` (PROMPT 4).
- **`OPS-*`** — workflows événementiels de vente (`rapido-n8n`) : `OPS-LEAD-CHAUD`,
  `OPS-CLIENT-GAGNE`, `OPS-ALERTE-CHURN` (PROMPT 4).

> Ajout d'une routine : lui donner un id `PRÉFIXE-NOM`, l'inscrire ici (avec ses
> noms parlés, sa cadence, son propriétaire, ses skills délégués, son autonomie et sa
> table mémoire), puis pointer son plugin propriétaire vers ce registre. Les seuils
> et cadences réels vivent dans `./rapido-kb/` — jamais en dur.

## Registre des KPIs

> Rempli par le **PROMPT 5** (source unique des formules : `rapido-startup:catalogue-kpi`).
> Chaque KPI y aura sa formule canonique, son script propriétaire et les skills
> autorisés à le citer.
