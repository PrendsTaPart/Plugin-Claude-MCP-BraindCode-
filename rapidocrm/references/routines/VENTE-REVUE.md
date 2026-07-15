# VENTE-REVUE — revue commerciale hebdomadaire (lundi, après VENTE-HYGIENE)

```yaml
# CONFIG — interchangeable par client (les valeurs de ./rapido-kb/ PRIMENT)
routine: VENTE-REVUE
cadence: hebdomadaire — lundi matin (APRÈS VENTE-HYGIENE)
perimetre: [rapidocrm]
objectif_source: ./rapido-kb/commercial/objectifs.md   # objectif de période
benchmarks: ./rapido-kb/commercial/benchmarks.md
autonomie: niveau 1 max — revue et décisions PRÉPARÉES, aucune écriture d'office — reference/autonomie.md
silence_si_vert: false
```

## Sense (lecture seule)

1. **Pipeline par étape** : `get_stats_pipeline` / `get_stats_pipeline_global`
   (nombre et montant par étape).
2. **Objectif restant** : lire `./rapido-kb/commercial/objectifs.md` (objectif de
   période − déjà signé/encaissé).
3. **Conversion par étape** : taux de passage d'étape (données CRM) — matière du calcul.

## Plan (calculs via catalogue-kpi UNIQUEMENT)

4. **Couverture = pipeline pondéré ÷ objectif restant** — calcul par
   `rapido-startup:catalogue-kpi` (formule affichée, jamais de tête ni en local).
5. **Taux de conversion par étape vs `benchmarks.md`** (calcul catalogue-kpi) :
   repérer l'étape qui fuit (conversion sous le benchmark).
6. **3 décisions maximum** pour la semaine (format : contexte → options →
   recommandation) — ex. renforcer l'étape qui fuit, arbitrer un deal à risque.

## Act (niveau 1 max)

7. **Préparer** les décisions et les actions associées (via `pilotage-commercial` →
   skills d'exécution) ; **aucune écriture d'office** — tout attend l'accord.

## Feed

8. Journal `./rapido-kb/commercial/apprentissages.md` (couverture, étape faible,
   décisions) ; `benchmarks.md` mis à jour si un taux structurel change.

## Report

9. Une page : pipeline par étape, **couverture vs objectif** (formule), la conversion
   par étape vs benchmarks (l'étape qui fuit nommée), les 3 décisions à valider.
