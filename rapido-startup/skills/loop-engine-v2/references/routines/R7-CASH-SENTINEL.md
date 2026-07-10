# R7 — CASH-SENTINEL (sentinelle trésorerie)

```yaml
# CONFIG — interchangeable par client (les valeurs de ./rapido-kb/ PRIMENT)
routine: R7-CASH-SENTINEL
cadence: quotidienne (ou 2×/semaine) — matin
perimetre: [stripe, rapidocrm]
seuil_alerte_runway_mois: 6        # défaut secteur — surcharger dans processus-internes.md
seuil_facture_retard: 30 jours     # au-delà : nommée dans l'alerte
autonomie: NIVEAU 0 STRICT — alerte seulement, AUCUNE écriture — reference/autonomie.md
silence_si_vert: true              # au vert : journal seul, pas de message
```

> Prompt rédigé depuis la spec (partie 4 du master plan non fournie).

## Sense (lecture seule)

1. Solde disponible : Stripe `stripe_api_read` (Balance — centimes → euros
   annoncé) + trésorerie bancaire si fournie (KB/CSV, datée).
2. Encaissements attendus : factures `en_attente` (CRM), échéances sous 14 j.
3. Retards : `list_factures` statut `en_retard` (montant, ancienneté).
4. Sorties récentes : burn du mois glissant (dépenses − encaissements).

## Plan (calculs via catalogue-kpi)

5. Runway (formule affichée) vs `seuil_alerte_runway_mois` ; DSO ; total en
   retard. Verdict : 🟢 (tout dans les seuils) / 🟡 (runway < cible OU retard
   > seuil) / 🔴 (runway < seuil d'alerte OU trésorerie négative projetée
   sous 60 j d'après le prévisionnel s'il existe).

## Act — NIVEAU 0 : ALERTE SEULEMENT

6. AUCUNE écriture, AUCUN brouillon, AUCUNE relance — même « pour aider ».
   La sentinelle DÉTECTE et ALERTE ; l'action appartient à R4 ou à une
   demande explicite. C'est la routine la plus verrouillée du moteur.

## Feed

7. Journal `routines-journal.md` : date, solde, runway, verdict — MÊME au
   vert (la série journalière est la valeur de la sentinelle).

## Report

8. 🔴/🟡 : 5 lignes max — verdict, runway (formule), LE chiffre qui a
   déclenché, factures en retard nommées (client, montant, ancienneté),
   action recommandée (« lancer R4 » / « relances » / « revoir le
   prévisionnel »). 🟢 + `silence_si_vert: true` : rien n'est posté.
