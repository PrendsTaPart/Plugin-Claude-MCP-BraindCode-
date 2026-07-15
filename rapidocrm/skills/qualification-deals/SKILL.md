---
name: qualification-deals
description: Utiliser quand l'utilisateur veut qualifier son pipeline, savoir si un deal est solide, un score BANT/MEDDIC, ou repérer les deals fragiles. Score de qualification par deal réel (Budget/Authority/Need/Timing renseignés ou pas), champs manquants à collecter, deals mono-interlocuteur signalés (multi-threading), recommandation garder/pousser/sortir.
---

# Qualification des deals — BANT/MEDDIC sur le pipeline réel

Mesure la **solidité** des deals à partir de ce qui est réellement renseigné.

## Étape 0 — Pont forge
- **Livrable forge** `scale-bant-qualification` (`./rapido-kb/startup/forge/`) comme
  grille ; absent → défauts en le disant. Voir `reference/pont-forge-operations.md`.

## Sense (pipeline réel)
- `get_pipeline`, `get_historique_prospect`, `get_contact` par deal : quels champs
  **BANT** sont renseignés (Budget chiffré ? Authority = décideur identifié ? Need
  explicite ? Timing daté ?). MEDDIC si les données le permettent (Metrics, Economic
  buyer, Decision criteria/process, Identify pain, Champion).

## Plan (score & solidité)
- **Score de qualification par deal** (part des critères renseignés) — formule affichée.
- **Champs manquants** à collecter au prochain contact (liste actionnable).
- **Deals « mono-interlocuteur »** signalés → **multi-threading** (à la Challenger :
  identifier d'autres parties prenantes) — un deal à un seul contact est fragile.
- **Recommandation** par deal : **garder / pousser / sortir** (avec la raison chiffrée).

## Act
- Champs à collecter → **tâche** ou note CRM (`log_activity`) **après confirmation**.

## Anti-collision
- `coaching-pipeline` = **revue d'activité** (deals dormants, relances, engorgements).
- **Moi = la SOLIDITÉ** des deals (BANT/MEDDIC, multi-threading). Complémentaires.

## Garde-fous
Score **sourcé** des champs réellement renseignés (jamais inventé) ; livrable forge lu ;
recommandations chiffrées ; écritures **confirmées** ; seuils KB.
