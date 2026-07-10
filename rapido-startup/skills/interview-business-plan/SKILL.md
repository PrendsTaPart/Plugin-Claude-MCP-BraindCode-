---
name: interview-business-plan
description: Utiliser quand l'utilisateur veut créer un business plan, structurer son projet de startup, préparer une levée de fonds, un dossier banque/BPI, ou dit « aide-moi à créer mon entreprise », « valide mon idée », « prépare mon prévisionnel ». Mène l'interview en 9 phases et construit le dossier complet.
---

# Interview business plan — 9 phases, un dossier complet

Construit un business plan crédible par interview guidée, avec l'agent
`coach-startup` comme persona. Zéro chiffre inventé : chaque hypothèse est
sourcée, datée, et consignée.

## Étape 0 — Références et contexte (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`,
   `${CLAUDE_PLUGIN_ROOT}/reference/seuils-defaut.md` et les trois annexes du
   skill : `references/questionnaire-9-phases.md` (les questions),
   `references/frameworks.md` (BMC, TAM/SAM/SOM, SWOT…),
   `references/template-bp.md` (le document final).
2. Lire `./rapido-kb/` en entier — et SURTOUT `./rapido-kb/startup/` s'il
   existe (construit par le skill `dossier-startup-360` : vision, persona,
   marché, offre, traction, pitch, roadmap). **Ne JAMAIS reposer une question
   dont la réponse est déjà dans la KB** : la reformuler pour validation
   (« Votre persona est X — toujours exact ? ») au lieu de la redemander.
3. Croiser avec les MCP disponibles pour pré-remplir : `get_company` +
   `get_brand` (rapidocms), `get_revenue_summary` / `list_products` /
   `get_stats_pipeline_global` (rapidocrm), `get-users-list-tool` (rapidorh
   — l'équipe), `finance_summary` (foodeatup si restaurant), lectures Stripe
   (`stripe_api_read` — encaissements réels, montants en CENTIMES).
   Un serveur absent : dégrader proprement, ne rien estimer.

## Workflow — l'interview en 9 phases

Dérouler `references/questionnaire-9-phases.md` dans l'ordre :

1. **Executive summary** — rempli en DERNIER (synthèse des 8 autres phases),
   même s'il ouvre le document final.
2. **Entreprise & équipe** 3. **Problème & proposition de valeur**
4. **Marché (TAM/SAM/SOM)** 5. **Concurrence** 6. **Business model (BMC)**
7. **Go-to-market & traction** 8. **Plan opérationnel** 9. **Plan financier**

Règles de conduite de l'interview :

- **UNE question à la fois.** Jamais de rafale. Reformuler chaque réponse et
  la faire valider avant de l'écrire.
- **Mom Test** (voir aussi le skill `mom-test`, plugin rapidocrm) : demander
  du PASSÉ et du CONCRET (« la dernière fois que… », « combien avez-vous payé
  pour… »), jamais des opinions sur le futur (« achèteriez-vous ? »).
- **Relancer toute réponse faible** avec la relance type du questionnaire :
  « tout le monde est mon client » → construire le persona précis ;
  « on n'a pas de concurrent » → chercher la solution actuelle du client ;
  « le marché fait X milliards » → sourcer et descendre au SOM.
- **Phase 4 (marché)** : proposer une recherche web pour SOURCER TAM/SAM/SOM
  (études sectorielles, INSEE, rapports publics — citer chaque source avec
  date). **REFUSER le raisonnement « on prendra 1 % du marché »** : le SOM se
  construit bottom-up (clients atteignables × panier × taux de conversion).
- **Phase 5 (concurrence)** : analyse concurrentielle structurée (tableau
  forces/faiblesses/prix/parade, voir frameworks.md) ; croiser avec le skill
  `veille-ads-concurrents` (plugin rapido-meta-ads) s'il est disponible pour
  les angles publicitaires réels, et avec `./rapido-kb/concurrents.md`.

## Consignation des hypothèses (en continu)

**Chaque chiffre collecté** (prix, coûts, salaires, panier moyen, churn
estimé, taux de conversion…) va IMMÉDIATEMENT dans
`./rapido-kb/startup/business-plan/hypotheses.md`, une ligne par hypothèse :

```
| Hypothèse | Valeur | Source | Date | Confiance |
| Panier moyen B2B | 89 €/mois | 12 clients Stripe réels (stripe_api_read) | 2026-07-10 | haute |
| Churn mensuel estimé | 3 % | hypothèse fondateur, aucun historique | 2026-07-10 | faible |
```

Une hypothèse sans source se marque « hypothèse fondateur, confiance faible »
— elle n'est jamais présentée comme un fait dans le document final.

## Sortie — le dossier

1. **9 fichiers markdown** dans `./rapido-kb/startup/business-plan/`
   (01-executive-summary.md … 09-plan-financier.md), un par phase, validés
   au fil de l'eau.
2. **BUSINESS-PLAN.md** assemblé depuis `references/template-bp.md` — avec la
   **section Risques & parades OBLIGATOIRE** (marché, exécution, financier,
   réglementaire — jamais de business plan sans risques nommés).
3. À la fin, proposer les suites :
   - (a) générer le prévisionnel financier 3 ans — skill
     `plan-financier-previsionnel` (36 mois, 3 scénarios, sensibilité) ;
   - (b) générer le plan d'exécution — skill `plan-execution-startup`
     (WBS 6 phases, projet RapidoRH, jalons Calendar) ;
   - (c) exporter en docx/slides (plugin rapido-canva : presentation-codir
     comme base de mise en forme, ou export brut du markdown).

## Garde-fous

- Jamais de projection non sourcée présentée comme un fait — c'est
  l'interdit n°1 de l'agent `coach-startup`.
- Les benchmarks de `reference/seuils-defaut.md` ne servent que si la KB n'a
  pas la valeur, et sont cités comme « défaut secteur ».
- La KB s'écrit dans le RÉPERTOIRE DE TRAVAIL du client
  (`./rapido-kb/startup/business-plan/`), jamais dans le plugin.
- Interview interrompue = état sauvegardé (les fichiers de phase déjà validés
  restent) ; à la reprise, relire et reprendre à la phase suivante.
