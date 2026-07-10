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
