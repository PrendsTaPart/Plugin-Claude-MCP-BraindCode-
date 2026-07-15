---
name: preparation-rdv
description: Utiliser quand l'utilisateur dit « prépare mon RDV », « je vois [client] demain », veut un profil SONCAS d'un contact, ou une fiche de préparation d'entretien commercial. Charge la fiche CRM réelle (entreprise, contact, historique, deals), le profil SONCAS type du persona depuis les livrables forge, et les objections connues ; produit profil SONCAS probable, argumentaire adapté, questions SPIN, objections+réponses et objectif de sortie.
---

# Préparation de RDV — SONCAS opérationnel

Transforme la méthode SONCAS (forge) en **fiche de prépa sur données réelles**.

## Étape 0 — Pont forge + charte
- **Livrable forge** : chercher le profil SONCAS des personas dans
  `./rapido-kb/startup/forge/` (`scale-soncas`). Présent → base ; absent → le dire
  (proposer l'exercice ou continuer aux défauts). Voir `reference/pont-forge-operations.md`.
- Objections connues : `./rapido-kb/commercial/objections.md` (playbook vivant).

## Sense (CRM réel)
- `get_entreprise`, `get_contact`, `get_historique_prospect`, deals en cours
  (`get_pipeline`) — interactions réelles, jamais inventées.

## Plan (la fiche de prépa)
1. **Profil SONCAS probable du contact** — Sécurité / Orgueil / Nouveauté / Confort /
   Argent / Sympathie — avec les **indices tirés des interactions réelles** (ce qu'il a
   dit/fait), pas une supposition hors-sol. Manque d'indices → le dire.
2. **Argumentaire adapté** au(x) levier(s) SONCAS dominant(s).
3. **3 questions SPIN d'ouverture** (Situation, Problème, Implication, Need-payoff).
4. **Objections probables + réponses** (depuis le playbook vivant).
5. **Objectif de sortie** = l'étape suivante du pipeline à obtenir.

## Act
- **Notes de préparation loggées au CRM** (`log_activity`) **après confirmation**.

## Anti-collision
- `coaching-pipeline` = revue d'activité du pipeline ; **moi = préparer UN entretien**.
- `redaction-commerciale` = rédige le copy ; **moi = la stratégie d'entretien**.

## Garde-fous
Profil SONCAS **sourcé** des interactions réelles (jamais inventé) ; livrable forge lu
(ou absence dite) ; notes loggées **après confirmation** ; seuils KB.
