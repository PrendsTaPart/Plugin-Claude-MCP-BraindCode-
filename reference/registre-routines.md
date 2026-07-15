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
| `OPS-*` | Workflows événementiels de vente (n8n) | `rapido-n8n` (`recettes-metier`) | actif |
| `SEO-*` | Acquisition organique (positions, backlinks, audit) | `rapido-seo` (`pilotage-seo`) | actif |
| `SEA-*` | Acquisition payante Google (gaspillage, synergie) | `rapido-google-ads` | actif |
| `TIKTOK-*` | Acquisition payante TikTok | `rapido-tiktok-ads` | actif (si compte) |
| `RC-*` | Relation client (support, NPS, santé) | `rapido-relation-client` | actif |

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

### OPS-LEAD-CHAUD
- **Noms parlés** : « réponds au lead chaud », « lead à fort intent », « nouvelle soumission chaude ».
- **Cadence** : **événementiel** — webhook sur soumission de formulaire CRM à fort intent.
- **Propriétaire** : `rapido-n8n` (`recettes-metier`) · **Fichier** : `rapido-n8n/reference/recettes-vente.md`.
- **Skills délégués** : `usine-automatisations` (installation) ; actions CRM/Calendar/Gmail en brouillon.
- **Autonomie** : alerte + brouillon — **jamais de réponse directe au prospect**.
- **Mémoire n8n** : `ops_leads_chauds` (obligatoire).

### OPS-CLIENT-GAGNE
- **Noms parlés** : « onboarde le client gagné », « devis accepté → lance l'onboarding ».
- **Cadence** : **événementiel** — devis passé à « accepté ».
- **Propriétaire** : `rapido-n8n` (`recettes-metier`) · **Fichier** : `rapido-n8n/reference/recettes-vente.md`.
- **Skills délégués** : `usine-automatisations` ; deal gagné, acompte, projet RapidoRH, kick-off, relance ambassadeur J+60.
- **Autonomie** : facture/emails en **brouillon confirmé**.
- **Mémoire n8n** : `ops_onboardings` (obligatoire).

### OPS-ALERTE-CHURN
- **Noms parlés** : « alerte churn », « clients qui décrochent », « rétention ».
- **Cadence** : hebdomadaire (Schedule) — mais logique événementielle (signal d'inactivité).
- **Propriétaire** : `rapido-n8n` (`recettes-metier`) · **Fichier** : `rapido-n8n/reference/recettes-vente.md`.
- **Skills délégués** : `usine-automatisations` ; alerte interne priorisée + plan de sauvetage.
- **Autonomie** : alerte **interne** seulement, aucun contact client d'office.
- **Mémoire n8n** : `ops_churn_alertes` (obligatoire, anti-re-signalement).

### SEO-HEBDO
- **Noms parlés** : « positions de la semaine », « striking distance », « point SEO hebdo ».
- **Cadence** : hebdomadaire — lundi (cron n8n). **Mémoire n8n** : `seo_positions_journal`.
- **Propriétaire** : `rapido-seo:pilotage-seo` · **Recette** : `rapido-n8n/reference/recettes-seo.md`.
- **Contenu** : positions GSC + striking distance + 3 actions contenu. **Rank-tracking
  récurrent = n8n obligatoire** (coût DataForSEO gouverné).
- **Autonomie** : alerte + brouillons ; écriture CMS confirmée.

### SEO-MENSUEL
- **Noms parlés** : « backlinks du mois », « audit technique mensuel », « delta SEO ».
- **Cadence** : mensuelle. **Mémoire n8n** : `seo_backlinks_journal`.
- **Propriétaire** : `rapido-seo:pilotage-seo` · **Recette** : `recettes-seo.md`.
- **Contenu** : backlinks new/lost + delta d'audit technique. Coût DataForSEO annoncé.

### SEA-HEBDO
- **Noms parlés** : « gaspillage Google Ads », « synergie SEO/SEA de la semaine ».
- **Cadence** : hebdomadaire. **Mémoire n8n** : `sea_synergie_journal`.
- **Propriétaire** : `rapido-google-ads` · **Recette** : `recettes-seo.md`.
- **Contenu** : gaspillage + croisement SEO/SEA (économies, opportunités). **Lecture
  seule** → actions manuelles.

### TIKTOK-HEBDO (si compte actif)
- **Noms parlés** : « perf TikTok de la semaine », « arbitrage TikTok/Meta ».
- **Cadence** : hebdomadaire. **Mémoire n8n** : `tiktok_perf_journal`.
- **Propriétaire** : `rapido-tiktok-ads` · **Recette** : `recettes-seo.md`.
- **Contenu** : CPM/CPC/CPA + comparatif vs Meta. Écriture **verrouillée** (inactif + confirmation).

### RC-HEBDO
- **Noms parlés** : « point service client hebdo », « SLA de la semaine ».
- **Cadence** : hebdomadaire — lundi. **Mémoire n8n** : `rc_support_journal`.
- **Propriétaire** : `rapido-relation-client:pilotage-service-client` · **Recette** : `rapido-n8n/reference/recettes-relation-client.md`.

### RC-NPS-TRIMESTRE
- **Noms parlés** : « vague NPS », « mesure la satisfaction ce trimestre ».
- **Cadence** : trimestrielle. **Mémoire n8n** : `rc_nps_vagues`.
- **Propriétaire** : `rapido-relation-client:boucle-nps` · **Recette** : `recettes-relation-client.md`.

### RC-SANTE-MENSUEL
- **Noms parlés** : « santé du portefeuille », « health score du mois ».
- **Cadence** : mensuelle. **Mémoire n8n** : `rc_sante_journal`.
- **Propriétaire** : `rapido-relation-client:sante-client` · **Recette** : `recettes-relation-client.md`.

---

> **Toutes les routines/recettes du marketplace sont désormais enregistrées.** Ajout
> futur : lui donner un id `PRÉFIXE-NOM` et l'inscrire ci-dessus.
- **`OPS-*`** — workflows événementiels de vente (`rapido-n8n`) : `OPS-LEAD-CHAUD`,
  `OPS-CLIENT-GAGNE`, `OPS-ALERTE-CHURN` (PROMPT 4).

> Ajout d'une routine : lui donner un id `PRÉFIXE-NOM`, l'inscrire ici (avec ses
> noms parlés, sa cadence, son propriétaire, ses skills délégués, son autonomie et sa
> table mémoire), puis pointer son plugin propriétaire vers ce registre. Les seuils
> et cadences réels vivent dans `./rapido-kb/` — jamais en dur.

## Registre des KPIs

> **Source unique des formules : `rapido-startup:catalogue-kpi`**
> (`scripts/calcul_kpi.py`). Aucun autre script ne recalcule un KPI déjà couvert
> avec une formule différente — sinon chiffres divergents en CODIR. Un skill peut
> **citer** un KPI ; il ne redéfinit pas sa formule.

| KPI | Formule canonique | Script propriétaire | Skills autorisés à le citer |
|---|---|---|---|
| MRR | Σ montants (annuel ÷ 12) | `catalogue-kpi/calcul_kpi.py` | loop-engine (FIN-*), pilotage-* |
| CAC | dépenses acquisition ÷ nouveaux clients | `catalogue-kpi` | `attribution-kpi-marketing` (par canal, **même formule**), `money-math-acquisition`, pilotage-* |
| LTV | ARPU × marge brute ÷ churn mensuel | `catalogue-kpi` | money-math, board |
| LTV:CAC | LTV ÷ CAC | `catalogue-kpi` | money-math, board |
| CAC payback | CAC ÷ (ARPU × marge), en mois | `catalogue-kpi` | money-math |
| Marge brute | (CA − coûts directs) ÷ CA | `catalogue-kpi` | FIN-*, food-cost |
| Burn net | dépenses − encaissements | `catalogue-kpi` | FIN-CFO-HEBDO, FIN-CASH-SENTINELLE |
| Runway | trésorerie ÷ burn net | `catalogue-kpi` | FIN-CASH-SENTINELLE, board |
| DSO | créances ÷ CA × jours | `catalogue-kpi` | FIN-CFO-HEBDO |
| Vélocité pipeline | opp × conv × panier ÷ cycle | `catalogue-kpi` | GROWTH-LOOP, pilotage-commercial |
| Couverture pipeline | pipeline pondéré ÷ objectif | `catalogue-kpi` | `pilotage-commercial`, VENTE-REVUE |
| **Propres au marketing** (hors catalogue-kpi) | | | |
| LTGP (par canal) | (revenu − coût) ÷ clients | `attribution-kpi-marketing/kpi_marketing.py` | marketing seulement (≠ LTV) |
| ROI (par canal) | (revenu − dépense) ÷ dépense | `attribution-kpi-marketing` | marketing |
| Attribution % (par canal) | contacts (1er/dernier point) ÷ total × 100 | `attribution-kpi-marketing` | marketing |
| Part organique vs payante du CA | CA attribué organique ÷ CA total (et part payante) | `catalogue-kpi` (données `attribution-kpi-marketing` : GA4/GSC/Ads/TikTok) | marketing, board |

> **Frontière** : `catalogue-kpi` = formules & calculs · `attribution-kpi-marketing`
> = répartition/attribution par canal · `money-math-acquisition` = cadrage décisionnel
> (calculs délégués).

## Audit des seuils en dur (2026-07-15)
Passe `grep '€|%|mois'` sur les `SKILL.md` : la grande majorité des occurrences sont
**pédagogiques** (les 181 skills d'incubateur `rapido-forge` enseignent des
heuristiques : « runway confortable 12-18 mois », « garde 50 %+ au seed » — ce sont
des **leçons**, pas des seuils de décision client) ou déjà **sourcées KB** (« seuils :
`./rapido-kb/` prime »). **Aucun seuil de décision opérationnel** n'a été trouvé codé
en dur là où il devrait vivre dans `./rapido-kb/` : les skills opérationnels
(loop-engine, pilotage-*, VENTE-*) lisent déjà leurs seuils depuis la KB (défauts
explicitement étiquetés « défaut si absent »). Règle maintenue : un seuil de
**décision** vit dans `./rapido-kb/` ; un seuil **pédagogique** reste dans le texte.
