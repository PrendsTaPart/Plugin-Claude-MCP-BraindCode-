# R7 — CASH-SENTINEL (sentinelle trésorerie)

```yaml
# CONFIG — interchangeable par client (les valeurs de ./rapido-kb/ PRIMENT)
routine: R7-CASH-SENTINEL
cadence: quotidienne (ou 2×/semaine) — matin
perimetre: [stripe, rapidocrm]     # + foodeatup si vertical resto actif (canal d'alerte)
seuil_alerte_runway_mois: 6        # défaut secteur — surcharger dans processus-internes.md
seuil_facture_retard: 30 jours     # au-delà : nommée dans l'alerte
autonomie: NIVEAU 0 STRICT — alerte seulement, AUCUNE écriture — reference/autonomie.md
silence_si_vert: true              # au vert : journal seul, pas de message
```

> **Version autonome (sans Claude)** : la même sentinelle existe en
> workflow n8n — recette et activation dans
> `rapido-n8n/reference/recette-r7-cash-sentinel.md` (Schedule 08:00 →
> Stripe Balance → runway → alerte webhook ; publication confirmée).

> Prompt rédigé depuis la spec (partie 4 du master plan non fournie).

## Sense (lecture seule)

1. Solde disponible : Stripe `stripe_api_read` (Balance — centimes → euros
   annoncé) + trésorerie bancaire si fournie (KB/CSV, datée).
2. Encaissements attendus : factures `en_attente` (CRM), échéances sous 14 j.
3. Retards : `list_factures` statut `en_retard` (montant, ancienneté).
4. Sorties récentes : burn du mois glissant — dépenses via le skill
   `gestion-depenses` (plugin rapidocrm, SOURCE PRIMAIRE : `list_depenses`
   `periode: "month"`) − encaissements.

## Plan (calculs via catalogue-kpi)

5. Runway (formule affichée) vs `seuil_alerte_runway_mois` ; DSO ; total en
   retard ; **projection 30/60/90 jours** via le skill `cash-flow-snapshot`
   (plugin rapido-suite) s'il est installé — sinon runway seul, en le
   disant. Verdict : 🟢 (tout dans les seuils) / 🟡 (runway < cible OU retard
   > seuil) / 🔴 (runway < seuil d'alerte OU trésorerie négative projetée
   sous 60 j d'après le prévisionnel s'il existe).
   Relances : R7 n'en prépare JAMAIS — il recommande de lancer R4, qui les
   prépare (brouillons, ton gradué).

## Act — NIVEAU 0 : ALERTE SEULEMENT

6. AUCUNE écriture métier, AUCUN brouillon, AUCUNE relance — même « pour
   aider ». La sentinelle DÉTECTE et ALERTE ; l'action appartient à R4 ou à
   une demande explicite. C'est la routine la plus verrouillée du moteur.
   - SEULE exception (canal d'alerte, pas action métier) : verdict 🔴/🟡 ET
     vertical resto actif (foodeatup dans le périmètre) → diffuser l'alerte
     via `create_notification` FoodEatUp (`establishment_id`, `title` court,
     `message` = verdict + chiffre déclencheur, `type: "danger"` si 🔴,
     `"warning"` si 🟡). Jamais au vert, jamais pour autre chose —
     reference/autonomie.md.

## Feed

7. Journal `routines-journal.md` : date, solde, runway, verdict — MÊME au
   vert (la série journalière est la valeur de la sentinelle).

## Report

8. 🔴/🟡 : 5 lignes max — verdict, runway (formule), LE chiffre qui a
   déclenché, factures en retard nommées (client, montant, ancienneté),
   action recommandée (« lancer R4 » / « relances » / « revoir le
   prévisionnel »). 🟢 + `silence_si_vert: true` : rien n'est posté.
