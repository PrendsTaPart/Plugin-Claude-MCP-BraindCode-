---
name: enseigner-foodeatup
description: Utiliser quand un formateur de l'Académie FoodEatUp suit son activité — « où en sont mes apprenants », « mon agenda de formation », « mes revenus de formateur », « qui a décroché dans mon parcours ». Tableau de bord formateur : apprenants, agenda, revenus.
---

# Enseigner sur l'Académie FoodEatUp (tableau de bord formateur)

## Enchaînement d'outils MCP (lecture seule)

1. **Apprenants** : `formateur_apprenants_list` — qui suit quoi, qui avance,
   qui a décroché (aucune progression depuis longtemps = à relancer en
   priorité : un apprenant perdu ne revient pas seul).
2. **Agenda** : `formateur_agenda_list` — sessions à venir, trous de planning,
   conflits éventuels.
3. **Revenus** : `formateur_revenus_summary` — chiffres réels du serveur,
   jamais extrapolés ; une période incomplète se dit.

## Sortie attendue

Un tableau `[sujet | état | signal | action proposée]` sur trois lignes :
apprenants (actifs / décrochés), agenda (prochaines sessions), revenus
(période, total). UNE priorité : l'apprenant ou la session qui a le plus
besoin d'attention, avec sa raison.

## Règles

- Les données d'apprenants sont personnelles : restituer des agrégats et des
  prénoms, pas des coordonnées recopiées.
- Relance d'un apprenant : proposer le message, l'envoi reste à l'utilisateur
  (aucun outil d'envoi côté Académie — le dire plutôt que simuler).

## Ce que ce skill NE fait PAS

- Suivre SA propre formation → skill `se-former-foodeatup`.
- Créer ou publier des contenus → skill `fabriquer-des-cours`.
- La paie ou la comptabilité du formateur → hors périmètre (plugin
  rapido-startup pour la finance).
