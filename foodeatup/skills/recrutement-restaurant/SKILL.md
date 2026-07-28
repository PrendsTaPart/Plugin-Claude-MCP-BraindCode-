---
name: recrutement-restaurant
description: Utiliser quand l'utilisateur recrute pour son restaurant — « publie une offre de serveur », « où en sont les candidatures », « passe ce candidat en entretien », « refuse cette candidature », « modifie l'annonce ». Cycle offre d'emploi → candidatures → statuts, jusqu'à la décision d'embauche (l'embauche elle-même relève du planning-équipe).
---

# Recrutement restaurant (offres & candidatures)

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et l'appliquer.
2. S'assurer d'avoir l'`establishment_id` (le demander si absent).

## 1. Publier et entretenir les offres

- Avant de créer : `list_job_applications` — une offre équivalente déjà ouverte
  avec des candidatures en attente ne se double pas, elle se traite.
- `create_job_offer` : poste, type de contrat, temps de travail, rémunération
  (fourchette réelle donnée par l'utilisateur, jamais inventée), description.
- `update_job_offer` : modifier ou clore l'offre. Une offre pourvue se ferme
  le jour même — une annonce fantôme coûte des candidatures ignorées.

## 2. Traiter les candidatures

- `list_job_applications` : nouvelles candidatures d'abord, puis en attente
  depuis plus de 7 jours (à traiter en priorité : un candidat sans réponse
  est perdu).
- `update_application_status` : faire avancer chaque candidature une par une
  (reçue → entretien → acceptée/refusée), jamais en lot. Un refus se motive
  en une ligne dans le suivi.
- Données personnelles des candidats : consultées, pas recopiées dans les
  synthèses.

## 3. De la candidature acceptée à l'embauche

Passer la main au skill `planning-equipe` :
- `create_employee` (fiche), puis `create_employee_contract` (acte juridique →
  confirmation obligatoire par le garde-fou du plugin), puis premiers shifts.

## Ce que ce skill NE fait PAS

- Contrats, planning, congés, pointages → skill `planning-equipe`.
- Le diagnostic RH d'ensemble → skill `boucle-2-equipe` (plugin
  foodeatup-boucles).
- Les projets/Kanban d'équipe → plugin rapidorh.
