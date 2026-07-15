# LTGP:CAC et l'acquisition financée par le client

> **Idées** : Alex Hormozi, *$100M Leads* (2023). **Distillation source** :
> founder-playbook (MIT © 2026 AgentSeal). Reformulation FR — voir `NOTICE.md`.

## Les deux nombres

- **LTGP** = *Lifetime Gross Profit* = marge brute totale d'un client sur sa
  durée de vie (revenus − coût de livraison). **Attention** : Hormozi utilise le
  LTGP, **pas** la LTV — le LTGP retire le coût de livraison, image plus honnête.
- **CAC** = *Customer Acquisition Cost* = coût pour acquérir un client.

## Le ratio LTGP:CAC

| Ratio | Lecture |
|---|---|
| < 3:1 | difficile de scaler |
| 3:1 | minimum viable |
| > 3:1 | prêt à scaler |

- CAC **au-dessus de 3× la moyenne du secteur** → corriger les **pubs**.
- CAC en dessous mais ratio faible → corriger le **modèle** (augmenter le LTGP :
  upsells, rétention, prix).

## Acquisition financée par le client (Client Financed Acquisition)

Si un client **rembourse son coût d'acquisition en ~30 jours**, on peut financer
l'acquisition à la carte de crédit et réinvestir à l'infini → **scaling
illimité**. Comment accélérer l'encaissement : prix d'entrée plus élevé, order
bumps, upsell jour 1, paiement annuel, frais de mise en route.

## Exemple Rapido / FoodEatUp
Un abonnement « menu du midi » à 12 €/semaine, marge brute 55 %. Si le CAC via
Meta est de 8 €, il est remboursé en ~1,5 semaine → acquisition financée par le
client, on peut pousser la dépense pub.

## Outils MCP Rapido pressentis

| Besoin | Outils MCP Rapido |
|---|---|
| **Calculer** LTGP:CAC (formule affichée) | skill `catalogue-kpi` (rapido-startup, `calcul_kpi.py`) — jamais de tête (hook « KPI sans script ») |
| Coûts d'acquisition (dépense pub) | rapido-meta-ads `ads_insights_*` ; rapidocrm `list_depenses` |
| Revenus / marge par client | rapidocrm `get_revenue_summary`, `get_top_clients`, `list_factures` ; foodeatup `finance_summary` |
| Surveiller le remboursement 30 j | rapido-startup routine **R7 CASH-SENTINEL** (runway), `cash-flow-snapshot` |

> Le ratio et le point de remboursement se calculent **par script**
> (`catalogue-kpi`), formule visible — c'est une règle du plugin.

## Frontières
- **Budgets** et seuils de pub → `paid-ads` (voir `01-core-four.md` case pub).
- **Prix / packaging** de l'offre → benchmark `monetizing-innovation` /
  `100m-offers`.
