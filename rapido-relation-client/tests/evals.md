# Évals — plugin rapido-relation-client (0.1.0)

## Déclenchement (5 phrases → skill)
| Phrase | Skill |
|---|---|
| « Pilote mon service client / fais le point support / mon SLA » | `pilotage-service-client` |
| « Lance un NPS / segmente promoteurs-détracteurs / mesure la satisfaction » | `boucle-nps` |
| « Health score / quels clients sont à risque / santé du portefeuille » | `sante-client` |
| « Pilote l'onboarding / les 100 premiers jours de ce client » | `cent-premiers-jours` |
| « Segmentation RFM / mes champions et clients endormis » | `segmentation-rfm` |

## Anti-déclenchements (contre-exemples)
- « Traite ce ticket précis / classe ce ticket » → **`rapidocrm:ticket-triage`** (UN ticket, pas le système).
- « Écris la réponse à ce client » → **`rapidocrm:draft-response`** (rédaction).
- « Lance ce sondage / ce jeu concours » → **`rapidocrm:animation-client`** (exécution).
- « Gère cette réclamation resto » → **`foodeatup:handle-complaint`**.
- « Relance mes factures impayées » → **`rapido-suite:invoice-chase`** / `devis-facture-relance`.
- « Pilote ma vente / mon commercial » → **`rapidocrm:pilotage-commercial`** (boucle vente, pas support).

## Garde-fous
- `garde-envois` : envoi client (`send_email`/`send_sms`/`send_newsletter`/`lancer_campagne`…) → **ask**.
- Scores `health_score.py` / `rfm.py` : formule affichée, facteurs réels (absent = exclu), jamais de tête.
