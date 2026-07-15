# VENTE-HYGIENE — hygiène des données commerciales (hebdo lundi)

```yaml
# CONFIG — interchangeable par client (les valeurs de ./rapido-kb/ PRIMENT)
routine: VENTE-HYGIENE
alias: []                              # id canonique du registre unifié
cadence: hebdomadaire — lundi matin (avant VENTE-REVUE)
perimetre: [rapidocrm]
seuils: ./rapido-kb/commercial/seuils.md   # jamais en dur (défauts ci-dessous si absent)
seuil_deal_sans_activite_jours: 14
seuil_facture_retard_jours: 30
ponderation_score: {deals: 40, devis: 30, entreprises: 20, factures: 10}
autonomie: NIVEAU 0 — diagnostic seul, aucune écriture métier — reference/autonomie.md
silence_si_vert: false
```

## Sense (lecture seule)

1. **Deals sans activité 14+ j** : `get_pipeline` / `get_stats_pipeline` → deals dont
   la dernière interaction dépasse `seuil_deal_sans_activite_jours`.
2. **Devis sans date d'expiration** : `list_devis` → devis actifs sans échéance posée.
3. **Entreprises sans contact / sans email** : `list_entreprises` croisé `list_contacts`
   → comptes sans interlocuteur ou sans email exploitable.
4. **Impayés 30+ j** : `list_factures` statut `en_retard` (ancienneté > `seuil_facture_retard_jours`).

## Plan (score /100, pondération CONFIG)

5. Score d'hygiène = 100 − pénalités pondérées (deals 40 / devis 30 / entreprises 20
   / factures 10), **formule affichée**, chaque composante avec son compte réel. Les
   seuils viennent de `./rapido-kb/commercial/seuils.md`, jamais en dur.

## Act — NIVEAU 0 (diagnostic seul)

6. **Aucune écriture** : la routine liste les anomalies par catégorie et propose les
   corrections (à traiter par `VENTE-RELANCES` ou à la main) — elle ne corrige rien elle-même.

## Feed

7. Écrire la série dans `./rapido-kb/commercial/historique-hygiene.md` (date, score,
   compte par catégorie) — la tendance du score est la valeur de la routine.

## Report

8. Une page : score /100 + son calcul, les 4 catégories chiffrées, les 3 anomalies
   les plus coûteuses à corriger cette semaine.
