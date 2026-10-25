---
name: onboarding-client-j90
description: Utiliser quand un restaurateur vient de signer, que l'utilisateur dit « on onboarde le nouveau client », « prépare le J+90 du Bistrot », « où en est l'installation du client signé ». Déroule le parcours de la signature au J+90 enseigné par l'Academy — jalons, gestes, relances — sans jamais agir sur le compte du client à sa place.
---

# Onboarding client J+90 (de la signature à l'habitude)

Famille engagée : **service-client** (Brouillon) — les gestes sur le compte
client appartiennent au client ou au plugin `foodeatup` (son onboarding).

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow

1. **La méthode** : missions de la formation `onboarding-client`
   (5 missions — `list_missions` filtré, `get_mission` pour le détail) :
   les jalons de la signature au J+90, ce qui se vérifie à chaque jalon.
2. **Le plan du client** : jalons datés depuis la signature (J0 config,
   J+7 premiers gestes, J+30 routines en place, J+90 autonomie) ; tâches
   suivies dans RapidoCRM (`create_task`) et RapidoRH si le projet d'équipe
   existe.
3. **Les gestes d'installation eux-mêmes** : DÉLÉGUER — le plugin
   `foodeatup` (skill `onboarding-restaurateur`) outille la mise en place
   réelle ; la formation du client passe par le plugin `foodeatup-tutoriel`
   (l'Académie publique). Ce skill TIENT LE FIL, il ne configure pas le
   restaurant.
4. **Les relances de jalon** : brouillons Gmail sur modèle (skill
   `relancer-j3-j7` pour la mécanique) — « où en êtes-vous, que bloquons
   nous » ; un silence à J+30 s'escalade.
5. **Mesurer** : jalons tenus, usage réel (le client fait ses relevés, sa
   caisse) — c'est la santé du compte.

KPI : `objectifs-atteints`, `premiere-reponse` (support du nouveau client).
Formations : `onboarding-client` (5 missions), `customer-success`,
`support-client`.

## Garde-fous

- Jamais un geste sur le compte du client à sa place sans son accord écrit —
  l'onboarding APPREND au client, il ne le remplace pas.
- Un jalon raté se dit et se traite — pas de J+90 « décrété ».
