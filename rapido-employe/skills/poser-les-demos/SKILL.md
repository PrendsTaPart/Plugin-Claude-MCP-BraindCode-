---
name: poser-les-demos
description: Utiliser quand un prospect dit oui, que l'utilisateur dit « pose la démo avec le Bistrot de la Gare », « cale les rendez-vous de la semaine », « il a répondu, propose un créneau ». Regarde les créneaux, pose le rendez-vous dans le CRM et avance le prospect à l'étape démonstration.
---

# Poser les démonstrations (du oui au créneau)

Famille engagée : **preparer** (Brouillon — rendez-vous et pipeline sont des
écritures internes CRM).

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.
2. Les disponibilités de démonstration viennent des objectifs du déploiement
   (`get_deployment_plan`) ou de l'humain — jamais supposées.

## Workflow

1. **`list_rdvs`** (RapidoCRM) — les créneaux déjà pris, pour ne jamais
   doubler.
2. **Proposer** au prospect 2 créneaux compatibles avec les disponibilités
   déclarées (le message de proposition suit le skill `relancer-j3-j7` :
   brouillon sur modèle).
3. **`create_rdv`** une fois le créneau accepté — intitulé clair
   (« Démo FoodEatUp — <établissement> »), lieu ou lien, rappel des
   interlocuteurs.
4. **`deplacer_prospect_etape`** — le prospect passe en « démonstration » ;
   le pipeline reste le reflet du réel.
5. **Préparer la démo** : la journée type en vingt minutes (formation
   `demo-certifiee`), l'argumentaire du persona (skill
   `argumentaire-et-objections`), et l'exemple à montrer (site cinématique,
   Studio Print — formation `studio-print` SP3).

KPI : `demos`, `rdv-tenus`.
Formations : `demo-certifiee` (5 missions), `closing`, `soncas`.

## Garde-fous

- Un rendez-vous ne se crée qu'ACCEPTÉ par le prospect — pas de créneau
  « posé d'office ».
- Déplacement d'étape uniquement quand le fait est vrai (démo posée) — le
  pipeline ne se maquille pas.
