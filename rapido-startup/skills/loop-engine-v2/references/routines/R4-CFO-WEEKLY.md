# R4 — CFO-WEEKLY (revue finance hebdomadaire)

```yaml
# CONFIG — interchangeable par client (les valeurs de ./rapido-kb/ PRIMENT)
routine: R4-CFO-WEEKLY
cadence: hebdomadaire — lundi matin (fuseau : rapido-kb/entreprise.md)
perimetre: [stripe, rapidocrm, foodeatup]   # retirer les serveurs non utilisés
periode: 7 derniers jours + mois en cours
seuils: rapido-kb/processus-internes.md sinon reference/seuils-defaut.md
persona: agent cfo-virtuel
autonomie: niveau 1 max (relances PRÉPARÉES, jamais envoyées) — reference/autonomie.md
silence_si_vert: false
```

> Prompt rédigé depuis la spec (partie 4 du master plan non fournie).

## Sense (lecture seule)

1. Encaissements de la semaine : Stripe `stripe_api_read` (Balance
   transactions, centimes → euros annoncé) ; CA facturé : CRM
   `get_revenue_summary`, `list_factures` ; restaurant : `finance_summary`
   (establishment_id requis). MÊME période partout.
2. Impayés : `list_factures` statut `en_retard` (+ `en_attente` > 30 j).
3. Dépenses de la semaine : `list_depenses` (CRM) / `list_expenses` (FoodEatUp).

## Plan (calculs via catalogue-kpi UNIQUEMENT)

4. Calculer via calcul_kpi.py : MRR + décomposition, burn net, runway, DSO,
   marge brute — formules affichées, seuils CONFIG, statuts.
5. Prioriser les 3 points de la semaine (alerte > attention > tendance) —
   chaque point : chiffre, formule, cause probable, action proposée.

## Act (niveau 1 max)

6. DSO hors seuil → PRÉPARER les relances (skill `devis-facture-relance`,
   brouillons non envoyés, ton gradué). Dépense anormale → la nommer et
   proposer l'arbitrage. RIEN ne part sans demande explicite.
7. Alerte 🔴/🟡 ET vertical resto actif (foodeatup dans le périmètre) → EN
   PLUS du rapport, diffuser via `create_notification` FoodEatUp
   (`establishment_id`, `title` court, `message` = KPI + formule + verdict,
   `type: "danger"` si 🔴, `"warning"` si 🟡). Canal d'alerte interne, pas
   une action métier — reference/autonomie.md.

## Feed

8. Journal : `./rapido-kb/startup/routines-journal.md` (date, KPI, verdicts,
   actions proposées). Écart durable vs prévisionnel (> 30 % sur 2 mois) →
   proposer la mise à jour (skill `plan-financier-previsionnel`, doc vivant).

## Report

9. Une page : 5 KPI (valeur, formule, statut vs seuil sourcé), les 3 points
   priorisés, les relances préparées en attente d'accord. Récap des
   écritures (normalement : journal + notification d'alerte éventuelle,
   avec son ID).
