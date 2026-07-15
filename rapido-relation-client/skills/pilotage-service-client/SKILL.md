---
name: pilotage-service-client
description: Utiliser quand l'utilisateur dit « pilote mon service client », « fais le point support », veut une boucle de pilotage du support (Sense → Plan → Act → Feed → Report) ou un rapport SLA/CSAT. Orchestre le support en boucle — tickets par priorité/ancienneté vs SLA, réclamations, priorisation par SLA dépassé × valeur client, délégation triage/réponses, consolidation des problèmes récurrents.
---

# Pilotage service client — le Loop Engine du support

Orchestrateur : il **ne traite pas un ticket**, il **pilote le système**. Boucle
**Sense → Plan → Act → Feed → Report**.

## Étape 0 — Pont forge + SLA
- Livrable forge `scale-customer-success` comme cadre ; absent → défauts en le disant.
- **SLA** : `./rapido-kb/relation-client/sla.md` (délais cibles P1-P4), jamais en dur.

## SENSE (lecture)
- **Tickets ouverts** par priorité et **ancienneté** — via `rapidocrm:ticket-triage`
  (délégation du triage) + liste des tickets CRM.
- **Délais de première réponse vs SLA** (KB).
- **Réclamations FoodEatUp** (`foodeatup:handle-complaint` en délégation).

## PLAN
- Priorisation par **SLA dépassé × valeur client** (formule affichée ; valeur via CRM).

## ACT (délégation, brouillons confirmés)
- Réponses → `rapidocrm:draft-response` (rédaction). Réclamations resto →
  `foodeatup:handle-complaint`. **Tout envoi = brouillon confirmé** (`garde-envois`).

## FEED (récurrences)
- Problèmes récurrents consolidés dans `./rapido-kb/relation-client/problemes-recurrents.md` :
  chaque récurrence = **candidate à un correctif produit ou une FAQ** → routée vers le
  **Kanban RapidoRH** (tâche) **après confirmation**.

## REPORT — une page
SLA (respectés/dépassés), volumes par priorité, délai moyen de 1re réponse, top
récurrences, récap des IDs (tâches, brouillons).

## Anti-collision
- `rapidocrm:ticket-triage` = traite **UN** ticket ; **moi = pilote LE SYSTÈME**.
- `rapidocrm:pilotage-commercial` = boucle **vente** ; moi = boucle **support**.

## Garde-fous
SLA depuis la KB ; priorisation **par formule** ; réponses **déléguées** (brouillons
confirmés) ; récurrences → Kanban **après confirmation** ; données réelles.
