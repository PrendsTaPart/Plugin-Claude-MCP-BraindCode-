# Catalogue des KPI — formules, sources MCP, fréquences, seuils, pièges

> Catalogue construit depuis la spécification du propriétaire (la « Partie 3 »
> du master plan n'ayant pas été fournie, ce fichier fait foi — à réconcilier
> si le master plan diverge). Convention validée par l'exemple de référence :
> ARPU 99 € × marge 80 % ÷ churn 5 % → **LTV 1 584 €**.

Règles transverses :
- **Seuil** : `./rapido-kb/processus-internes.md` PRIME ; sinon la colonne
  ci-dessous (= `reference/seuils-defaut.md`), citée « défaut secteur ».
- **Montants Stripe en CENTIMES** (plus petite unité) : ÷ 100 avant le JSON
  d'entrées, conversion annoncée.
- **Calcul via `scripts/calcul_kpi.py` uniquement** — la fonction à appeler
  est indiquée par KPI.

## Revenus récurrents

| KPI | Formule exacte | Fonction | Outils MCP | Fréquence | Seuil défaut | Pièges |
|---|---|---|---|---|---|---|
| **MRR** | Σ abonnements actifs normalisés au mois (annuel ÷ 12) | `mrr` | Stripe : `stripe_api_read` (List Subscriptions, status=active) ; RapidoCRM : `list_contrats` (contrats récurrents) | hebdo | — (suivi de tendance) | Contrat ANNUEL = montant ÷ 12, pas encaissement du mois ; exclure les one-shot ; centimes Stripe |
| **Décomposition MRR** | net new = nouveau + expansion − contraction − churn | `decompose_mrr` | Stripe : `stripe_api_read` (Subscriptions créées/modifiées/annulées sur la période) | mensuel | net new > 0 | Une remise n'est pas un churn (contraction) ; upgrade = expansion, pas nouveau |
| **ARPU** | MRR ÷ clients actifs | `arpu` | MRR ci-dessus + Stripe `stripe_api_read` (List Customers actifs) ou CRM `list_contacts` | mensuel | — | Clients actifs ≠ comptes créés (exclure les inactifs/gratuits) |
| **NRR** | (MRR début + expansion − contraction − churn MRR) ÷ MRR début | `nrr` | Stripe : `stripe_api_read` (Subscriptions, cohorte début de période) | mensuel | > 100 % | Ne compte QUE la base existante — le nouveau MRR n'entre pas dans le NRR |

## Rétention

| KPI | Formule exacte | Fonction | Outils MCP | Fréquence | Seuil défaut | Pièges |
|---|---|---|---|---|---|---|
| **Churn (mensuel)** | clients perdus ÷ clients en début de mois | `churn_rate` | Stripe : `stripe_api_read` (Subscriptions annulées) ; CRM : `list_contrats` (résiliés) | mensuel | dérivé du seuil annuel | Base = clients DÉBUT de mois, pas fin ; distinguer churn clients et churn MRR |
| **Churn annualisé** | `1 − (1 − churn_mensuel)^12` | `churn_annualise_compose` | (dérivé) | mensuel | B2B sain 3–8 %/an | **COMPOSÉ, JAMAIS ×12** : 5 %/mois → 46 %/an, pas 60 % |

## Unit economics

| KPI | Formule exacte | Fonction | Outils MCP | Fréquence | Seuil défaut | Pièges |
|---|---|---|---|---|---|---|
| **CAC** | dépenses d'acquisition période ÷ nouveaux clients période | `cac` | CRM : `list_depenses` (marketing/commercial) + `get_stats_pipeline_global` (clients gagnés) ; Meta : dépense pub (plugin rapido-meta-ads) | mensuel | — | Inclure salaires commerciaux chargés, pas seulement la pub ; même période au numérateur et dénominateur |
| **LTV** | ARPU × marge brute ÷ churn mensuel | `ltv` | (dérivé : ARPU, marge, churn ci-dessus) | mensuel | — | Utiliser la MARGE, pas le CA ; churn MENSUEL au dénominateur (ex. réf. : 99 × 0,80 ÷ 0,05 = 1 584 €) |
| **LTV:CAC** | LTV ÷ CAC | `ltv_cac` | (dérivé) | mensuel | sain ≥ 3:1 | Un ratio > 5 peut signifier sous-investissement en acquisition |
| **CAC payback** | CAC ÷ (ARPU × marge brute), en mois | `cac_payback` | (dérivé) | mensuel | 5–12 mois | Sur la MARGE mensuelle par client, pas le CA |

## Rentabilité & trésorerie

| KPI | Formule exacte | Fonction | Outils MCP | Fréquence | Seuil défaut | Pièges |
|---|---|---|---|---|---|---|
| **Marge brute** | (CA − coûts directs) ÷ CA | `marge_brute` | CRM : `get_revenue_summary`, `list_depenses` ; FoodEatUp : `finance_summary` | mensuel | SaaS 70–85 % | COGS SaaS = hébergement + support + frais de paiement (Stripe ~1,5–3 %) |
| **Burn net** | dépenses du mois − encaissements du mois | `burn_net` | Stripe : `stripe_api_read` (Balance transactions) ; CRM : `list_depenses` ; FoodEatUp : `list_expenses` | mensuel | — | NET (encaissements déduits) ; exclure les éléments exceptionnels |
| **Runway** | trésorerie disponible ÷ burn net mensuel | `runway` | Stripe : `stripe_api_read` (Balance) + relevés bancaires fournis par l'utilisateur | mensuel | cible 12–18 mois ; **ALERTE < 6 mois** | Burn ≤ 0 → runway « infini » (rentable), le dire tel quel ; trésorerie = disponible, pas promis |
| **Rule of 40** | croissance CA % + marge % ≥ 40 (en points) | `rule_of_40` | CRM : `get_revenue_summary` (2 périodes) + marge ci-dessus | trimestriel | ≥ 40 % | Points de pourcentage, pas ratios ; même définition de marge d'un trimestre à l'autre |
| **Point mort (MRR)** | coûts fixes mensuels ÷ marge brute ; en clients : ÷ ARPU | `break_even_mrr` | coûts : `list_depenses` (CRM) / `list_expenses` (FoodEatUp) | trimestriel | — | Coûts FIXES seulement au numérateur ; les variables sont dans la marge |
| **DSO** | créances clients ÷ CA période × jours période | `dso` | CRM : `list_factures` (statut en_attente/en_retard) + `get_revenue_summary` | mensuel | < 45 jours | Créances = factures ÉMISES non payées ; DSO > seuil → skill devis-facture-relance |

## Commercial

| KPI | Formule exacte | Fonction | Outils MCP | Fréquence | Seuil défaut | Pièges |
|---|---|---|---|---|---|---|
| **Vélocité pipeline** | (opportunités × taux de conversion × panier moyen) ÷ durée de cycle (jours) | `velocite_pipeline` | CRM : `get_pipeline`, `get_stats_pipeline_global`, `list_devis` | hebdo | — (tendance) | Les 4 termes sur la MÊME fenêtre ; cycle en jours calendaires |
| **Pipeline coverage** | pipeline pondéré ÷ objectif de la période | `pipeline_coverage` | CRM : `get_stats_pipeline_global` + objectif (KB : processus-internes.md) | hebdo | 3–4× | Pipeline PONDÉRÉ par probabilité d'étape, pas brut |

## Restauration (FoodEatUp)

| KPI | Formule exacte | Fonction | Outils MCP | Fréquence | Seuil défaut | Pièges |
|---|---|---|---|---|---|---|
| **Food cost** | coût matières ÷ CA nourriture | `food_cost` | FoodEatUp : `list_recipes`/`get_recipe` (coûts), `finance_summary`, `list_orders` — `establishment_id` requis | hebdo | 28–35 % | CA NOURRITURE seul (hors boissons si suivi séparé) ; croiser avec analyse-rentabilite-carte |
| **Ticket moyen** | CA ÷ nombre de commandes (ou couverts) | `ticket_moyen` | FoodEatUp : `finance_summary`, `list_orders` | hebdo | — | Choisir commandes OU couverts et s'y tenir |

## Services & équipe (RapidoRH)

| KPI | Formule exacte | Fonction | Outils MCP | Fréquence | Seuil défaut | Pièges |
|---|---|---|---|---|---|---|
| **Charge vs contrat** | heures réalisées ÷ heures contractuelles | `charge_vs_contrat` | RH : `get-dailies-tool` (heures) ; FoodEatUp : `list_employee_contracts`, `list_attendances` | hebdo | ~100 % (alerte durable > 110 %) | Croiser avec detection-surcharge (rapidorh) ; heures des dailies = déclaratif |
| **Coût de revient projet** | heures × taux horaire chargé + coûts directs | `cout_revient_projet` | RH : `get-project-tasks-tool`, `get-dailies-tool` ; salaires chargés : KB | par projet | — | Taux CHARGÉ (~brut × 1,45 France) ; inclure les coûts directs (outils, sous-traitance) |
