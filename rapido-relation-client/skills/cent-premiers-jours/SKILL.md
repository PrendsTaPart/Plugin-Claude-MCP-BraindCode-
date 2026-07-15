---
name: cent-premiers-jours
description: Utiliser quand l'utilisateur veut piloter l'onboarding d'un nouveau client, ses 100 premiers jours, un plan d'accueil, ou réduire le churn précoce. Traduit les 8 phases de l'expérience nouveau client (Assess → Advocate) en plan concret BraindCode par produit, avec jalons J+1/J+7/J+30/J+60/J+90 en tâches Kanban RH (après confirmation) et messages de jalon en brouillon.
---

# Les 100 premiers jours — piloter l'accueil client

Inspiré de *Never Lose a Customer Again* (Joey Coleman) — **réécrit en français, aucun
texte de livre verbatim**. Les 100 premiers jours décident de la fidélité.

## Étape 0 — Pont forge
- Livrable forge `scale-customer-journey` comme cadre du parcours ; absent → défauts en
  le disant.

## Les 8 phases (traduites en plan BraindCode par produit)
1. **Assess** (avant achat : attentes) · 2. **Admit** (décision, félicitation) ·
3. **Affirm** (rassurer, anti-remords) · 4. **Activate** (kickoff, première valeur) ·
5. **Acclimate** (prise en main guidée) · 6. **Accomplish** (1er résultat concret) ·
7. **Adopt** (usage régulier) · 8. **Advocate** (recommander).

## Plan (jalons datés)
- Traduire les phases en **jalons J+1 / J+7 / J+30 / J+60 / J+90** concrets selon le
  **produit** (Studio / Agence / SaaS / FoodEatUp) : pour chaque jalon, l'objectif, le
  message, le signe de réussite.

## Act (Kanban + messages, confirmés)
- Créer les jalons comme **tâches Kanban RapidoRH** (`create-task-tool`) **après
  confirmation** ; **messages de chaque jalon en brouillon**.
- Le **jalon J+60** déclenche la **proposition ambassadeur** (`rapidocrm:programme-ambassadeurs`).

## Branche
- **`onboarding-client-360`** installe le client (setup) ; **moi = pilote ses 100
  premiers jours** (expérience, jalons, adoption). Complémentaires.

## Garde-fous
Plan par **produit réel** ; jalons Kanban **après confirmation** ; messages en
**brouillon** ; aucun texte de livre verbatim ; J+60 → ambassadeur.
