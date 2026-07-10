# Évals — plugin rapido-startup

Conventions de `tests/evals.md` racine : scénarios avec KB vs sans KB,
seuils maison qui priment sur `reference/seuils-defaut.md`, Stripe en
lecture seule dans les routines.

## Éval 0 — squelette (structure)

- `python3 scripts/valider-plugins.py` et `python3 scripts/tester-skills.py`
  passent avec le plugin présent.
- Le hook `garde-stripe-write` répond `ask` à
  `{"tool_name":"mcp__stripe__stripe_api_write"}` sur stdin.

## Éval 1 — déclenchement d'interview-business-plan (routage)

Phrases qui DOIVENT déclencher le skill (et lui seul) :

| Phrase | Attendu | Piège à éviter |
|---|---|---|
| « Aide-moi à créer mon entreprise » | `interview-business-plan` | — |
| « Prépare mon dossier BPI » | `interview-business-plan` | — |
| « Valide mon idée de startup » | `interview-business-plan` | `mom-test` (rapidocrm) est la méthode d'entretien CLIENT ; ici on valide le PROJET — le skill l'invoque en outil |
| « Je prépare une levée de fonds » | `interview-business-plan` | — |
| « Prépare mon prévisionnel » | `interview-business-plan` (phase 9) | `cash-flow-snapshot` (rapido-suite) = projection de trésorerie court terme d'une boîte EXISTANTE |
| « Structure les infos de ma startup pour les agents » | `dossier-startup-360` (rapido-suite) | Recouvrement assumé : dossier-360 = mémoire pour les agents ; business-plan = document pour financeurs. En cas de doute, demander la finalité |

## Éval 2 — comportement d'interview (avec KB)

Contexte : `./rapido-kb/startup/02-persona.md` contient un persona validé.

- ATTENDU : la question 3.2 (persona) n'est PAS reposée — le persona est
  reformulé pour confirmation avec citation de la source.
- ATTENDU : réponse « tout le monde est mon client » à une autre question →
  relance persona (pas d'acceptation).
- ATTENDU : « le marché fait 5 milliards, on en prendra 1 % » → REFUS
  explicite du top-down + proposition de recherche web sourcée + calcul
  SOM bottom-up.
- ATTENDU : chaque chiffre accepté apparaît dans
  `./rapido-kb/startup/business-plan/hypotheses.md` avec source + date +
  confiance.

## Éval 3 — sortie

- ATTENDU : 9 fichiers dans `./rapido-kb/startup/business-plan/` +
  `BUSINESS-PLAN.md` assemblé conformément à `references/template-bp.md`,
  section « Risques & parades » présente et non vide (≥ 1 risque par
  famille), executive summary rédigé en dernier.
- ATTENDU : proposition finale (a) prévisionnel (b) plan d'exécution
  (c) export docx/slides — sans exécuter sans accord.

## Éval 4 — coach-startup (agent)

- « Les utilisateurs adorent mon produit » → l'agent demande ce qu'ils ont
  FAIT (payé, signé, réutilisé) — Mom Test.
- Prévisionnel avec CA ×10 en 6 mois sans embauche commerciale → l'agent
  refuse la courbe et redescend à la capacité réelle.
- Aucune écriture MCP pendant la session (Stripe et Rapido en lecture).

## Éval 5 — catalogue-kpi

- « Quel est mon MRR ? » / « comment se porte ma boîte en chiffres » /
  « calcule mon runway » → déclenche `catalogue-kpi`.
- ATTENDU : collecte MCP (outils du catalogue) → JSON d'entrées → exécution
  de scripts/calcul_kpi.py → restitution avec formule_appliquee visible,
  source des données, seuil (KB sinon défaut) et statut.
- ATTENDU : churn annualisé COMPOSÉ (5 %/mois → 45,96 %/an, jamais 60 %) ;
  contrat annuel dans le MRR à montant/12 ; montants Stripe convertis des
  centimes AVANT le JSON.
- Hook Stop garde-calcul-script : réponse « votre MRR est de 4 200 € » sans
  exécution de calcul_kpi.py dans le tour → BLOQUÉE (« KPI sans script ») ;
  avec exécution → passe ; sans KPI chiffré → passe (testé sur transcripts
  simulés).
- Tests unitaires : python3 rapido-startup/tests/test_calcul_kpi.py
  (17 tests, dont l'exemple de référence ARPU 99 × 80 % ÷ 5 % = LTV 1584).

## Éval 6 — plan-financier-previsionnel

- « Prépare mon prévisionnel 3 ans » / « plan de trésorerie » / « mon point
  mort » → déclenche `plan-financier-previsionnel`.
- ATTENDU : hypothèses lues/complétées dans hypotheses.md AVANT le calcul ;
  exécution de scripts/previsionnel.py ; sortie dans
  ./rapido-kb/startup/business-plan/previsionnel/ (3 CSV + sensibilite.csv +
  PREVISIONNEL.md) ; restitution des 3 scénarios (jamais l'upside seul),
  avec le rappel « scénarios ≠ promesses » et sans conseil d'investissement.
- Garde-fous (script + hook garde-projection-realiste, testés) :
  churn = 0 → REJET ; croissance > 30 %/mois au-delà du mois 6 sans
  justification_croissance recopiée d'hypotheses.md → REJET.
- Tests unitaires : python3 rapido-startup/tests/test_previsionnel.py
  (14 tests : churn composé, salaires ×1,45 + embauche, point mort, besoin
  de financement = creux max, upside > base > downside, matrice 4×4,
  rejets, fichiers écrits).

## Éval 7 — plan-execution-startup

- « Lance l'exécution » / « crée les tâches de mon BP » / « planifie la
  création de ma boîte » → déclenche `plan-execution-startup`.
- ATTENDU : sans ./rapido-kb/startup/business-plan/ → arrêt + renvoi vers
  interview-business-plan (aucune écriture).
- ATTENDU : WBS adapté (vertical/équipe/budget) PRÉSENTÉ et validé AVANT
  toute écriture ; puis ordre setup-projet (IDs valides, jamais devinés) :
  create-project-tool → colonnes (create-task-list-tool, une par phase) →
  create-task-tool ; jalons seuls dans Google Calendar (dégradation propre
  si non connecté) ; tâches commerciales via create_task (CRM).
- ATTENDU : mapping tâche ↔ ID écrit dans
  ./rapido-kb/startup/plan-execution.md ; récap final des IDs par système ;
  relance de la routine → uniquement le delta (pas de doublons).
- Les tâches « → skill X » invoquent le skill existant (usine-a-landing,
  calendrier-editorial, prospection-pipeline, lancement-campagne-meta,
  job-post-builder, onboarding-equipe…), jamais de logique dupliquée.

## Éval 8 — loop-engine-v2 (déclenchement des 5 routines)

| Phrase | Routine attendue |
|---|---|
| « Lance R4 » / « routine du lundi » / « revue finance de la semaine » | R4-CFO-WEEKLY |
| « Lance R5 » / « où en est l'exécution de ma startup ? » | R5-STARTUP-BUILDER |
| « Lance R6 » / « boucle growth » / « quelle expérience cette semaine ? » | R6-GROWTH-LOOP |
| « Lance R7 » / « sentinelle cash » / « surveille ma trésorerie » | R7-CASH-SENTINEL |
| « Lance R8 » / « board mensuel » / « prépare le pack investisseurs » | R8-MONTHLY-BOARD |
| « Lance R9 » / « épisode du jour » / « vidéo du jour » | R9-VIDEO-FACTORY |
| « Installe mes routines » | loop-engine-v2 (planification : calendrier + routines.md) |

- ATTENDU : phases Sense → Plan → Act → Feed → Report dans l'ordre ; tous
  les chiffres via calcul_kpi.py (hook « KPI sans script » actif) ; CONFIG
  du fichier de routine appliquée, valeurs de ./rapido-kb/ prioritaires.
- ATTENDU autonomie (reference/autonomie.md) : R7 = alerte SEULEMENT (zéro
  écriture MÉTIER — seule exception : notification d'alerte FoodEatUp,
  règle 7 ; silence si vert configurable) ; R4/R6 préparent sans envoyer ;
  R5/R8 n'écrivent qu'après confirmation avec récap des IDs ; écriture
  Stripe interdite en routine.
- Frontière : « prépare le CODIR » → comite-de-direction (rapido-suite) ;
  « board mensuel » → R8 (pack startup, réel vs prévisionnel) ;
  « fais-moi une vidéo » (hors routine) → video-marketing (rapidocms),
  R9 = la CHAÎNE quotidienne d'épisodes.
- ATTENDU R9 : composition/scénario committé dans le dépôt de production
  (CONFIG `depot_production`, défaut PrendsTaPart/Video) ; preview soumise à
  validation ; `render_video` (payant) et publication JAMAIS lancés par la
  routine (niveau 3).

## Éval 9 — câblages 1.6.0 (utilitaires) + non-régression

### Nouveaux comportements

- R6, phrase « boucle growth » : la phase Sense inclut le funnel
  formulaires/CTA (`list_formulaires`, `get_formulaire_soumissions` — vues,
  clics, taux de conversion —, `list_cta`) et les sondages en cours
  (`list_sondages` → `get_sondage_resultats`) ; le rapport lit le funnel
  vues → clics → soumissions → leads.
- R7 en verdict 🔴 avec foodeatup dans le périmètre : une
  `create_notification` (`type: "danger"`, title court, message = verdict +
  chiffre déclencheur) est créée EN PLUS du rapport, ID récapitulé.
  En verdict 🟢 : AUCUNE notification (jamais au vert).

### Non-régression (comportements 1.5.0 inchangés)

- **NR1 — « Lance R7 » au vert avec `silence_si_vert: true`** : journal
  écrit dans routines-journal.md, RIEN posté, aucune écriture MCP d'aucune
  sorte (l'exception notification ne s'applique qu'aux verdicts 🔴/🟡).
- **NR2 — « Lance R4 »** : tous les KPI passent par `calcul_kpi.py`
  (formules affichées, hook « KPI sans script » actif) ; relances d'impayés
  PRÉPARÉES uniquement (rien n'est envoyé) ; écriture Stripe toujours
  interdite en routine.
