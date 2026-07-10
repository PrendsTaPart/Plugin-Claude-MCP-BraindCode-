# R8 — MONTHLY-BOARD (board mensuel)

```yaml
# CONFIG — interchangeable par client (les valeurs de ./rapido-kb/ PRIMENT)
routine: R8-MONTHLY-BOARD
cadence: mensuelle — 1er lundi du mois
perimetre: [stripe, rapidocrm, rapidocms, rapidorh, foodeatup, google-calendar]
destinataires: board / associés / soi-même   # adapter le ton au destinataire
sortie: ./rapido-kb/startup/board/BOARD-AAAA-MM.md
autonomie: niveau 2 max (board écrit dans la KB, jalon Calendar confirmé) — reference/autonomie.md
silence_si_vert: false
```

> Prompt rédigé depuis la spec (partie 4 du master plan non fournie).

## Sense (lecture seule — MOIS COMPLET, même période partout)

1. Finance : MRR + décomposition, churn, burn, runway, DSO (Stripe + CRM).
2. Exécution : avancement du plan (plan-execution.md + `get-project-tasks-tool`),
   jalons atteints/glissés.
3. Croissance : CAC par canal, pipeline, expériences du mois
   (growth-experiences.md).
4. Réel vs prévisionnel : comparer aux CSV de
   `./rapido-kb/startup/business-plan/previsionnel/` (scénario base).

## Plan (calculs via catalogue-kpi)

5. Le pack board : 6-8 KPI (valeur, formule, vs mois précédent, vs plan),
   2 réussites, 2 échecs assumés, risques (registre du BP mis à jour),
   **3 décisions maximum** à soumettre (format : contexte → options →
   recommandation).

## Act (niveau 2 — après confirmation)

6. Écrire `BOARD-AAAA-MM.md` dans le dossier de sortie (le montrer avant).
7. Jalon Calendar du prochain board (`create_event`, confirmé).
8. Option : slides via le skill `presentation-codir` (plugin rapido-canva)
   si demandé — jamais d'envoi automatique aux destinataires.

## Feed

9. Mettre à jour 06-traction.md et 08-roadmap.md (skill `mise-a-jour-kb`) ;
   écart > 30 % vs plan sur 2 mois → proposer la mise à jour du prévisionnel
   (document vivant) ; journal des routines.

## Report

10. Le board une-page dans la conversation + chemin du fichier + récap des
    écritures (fichier, event, mises à jour KB). Rappel systématique :
    chiffres sourcés et datés, scénarios ≠ promesses, pas de conseil
    d'investissement.
