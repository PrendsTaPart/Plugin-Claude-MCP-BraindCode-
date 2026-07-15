# Évals — plugin rapido-marketing (0.2.0)

Chaque skill méthodo : 2 déclenchements + 1 anti-déclenchement.

## core-four-strategie

| # | Phrase | Attendu |
|---|---|---|
| CF1 | « Par où je commence pour trouver des clients ? » | `core-four-strategie` : Étape 0 (fiches 01/03/05/08 + garde-fous) → diagnostic ressources → recommande **UN** canal + cadence (règle des 100) ; délègue l'exécution |
| CF2 | « Ma pub marche, comment je scale ? » | `core-four-strategie` : More Better New (plus → mieux → nouveau) + critère de maîtrise avant d'ajouter un canal ; scaling pub délégué à `lancement-campagne-meta` |
| CF3 (anti) | « Écris-moi le cold email » | PAS core-four-strategie → skill d'exécution `redaction-commerciale` (rapidocrm) |

## lead-magnet-machine

| # | Phrase | Attendu |
|---|---|---|
| LM1 | « Je veux un cadeau gratuit pour capter des emails » | `lead-magnet-machine` : 7 étapes, type (révéler/échantillon/étape), **nom** résultat+délai+public ; capture déléguée (landing + formulaires) |
| LM2 | « Trouve un meilleur nom pour mon ebook gratuit » | `lead-magnet-machine` : formule de nommage, 3 propositions, plan de distribution |
| LM3 (anti) | « Génère le visuel de couverture » | PAS lead-magnet-machine → skill `studio-visuel-marque` (rapidocms) |

## money-math-acquisition

| # | Phrase | Attendu |
|---|---|---|
| MM1 | « Combien je peux dépenser pour acquérir un client ? » | `money-math-acquisition` : cadre LTGP/CAC/ratio ; **calcul délégué à `catalogue-kpi`** (jamais de tête) ; verdict scaler/corriger |
| MM2 | « Mon ratio LTGP:CAC est-il bon ? » | `money-math-acquisition` : seuils 3:1, données via `get_revenue_summary`/`list_depenses`, formule affichée |
| MM3 (anti) | « Fais ma prévision de trésorerie sur 90 jours » | PAS money-math → skill `cash-flow-snapshot` (rapido-suite) |

## lead-getters-systeme

| # | Phrase | Attendu |
|---|---|---|
| LG1 | « Je veux un programme de parrainage » | `lead-getters-systeme` : bienveillance d'abord, mécanique mutuelle traçable ; exécution déléguée à `animation-client` (rapidocrm) |
| LG2 | « Comment faire générer des leads par mes clients ? » | `lead-getters-systeme` : choix du type (clients→employés→affiliés→agences) selon maturité |
| LG3 (anti) | « Lance une pub Meta » | PAS lead-getters → skill `lancement-campagne-meta` (rapido-meta-ads) |

## Garde-fous transverses (rappel)
- Tout envoi/publication/activation → hook `garde-envois` (confirmation forcée).
- RGPD (consentement/effacement) avant séquence ou audience.
- KPI/score par script (`catalogue-kpi`), jamais de tête.
