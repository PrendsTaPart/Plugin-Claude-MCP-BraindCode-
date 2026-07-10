# Évals — plugin rapidocrm

## Éval 1 — animation-client (déclenchement)

| Phrase | Attendu |
|---|---|
| « Lance un sondage de satisfaction chez Dupont SA » | `animation-client` (sondage) |
| « Les résultats de mon dernier sondage ? » | `animation-client` (résultats + verbatims) |
| « Organise un jeu concours pour mes clients » | `animation-client` (concours + rappel légal FR) |
| « Combien de points de fidélité a Martin ? » | `animation-client` (fidélité) |
| « Envoie l'invitation au sondage par email » | délégué au skill `communication-client` |
| « Sondage à tout mon segment restaurateurs » | envoi de masse → `campagne-marketing` |

## Éval 2 — animation-client (comportement)

- ATTENDU : `list_sondages` / `list_jeux_concours` AVANT tout lancement
  (jamais de `modele_sondage_id` / `modele_jeu_id` inventé) ; entreprise
  vérifiée ; CONFIRMATION explicite avant `lancer_*` (visible clients) — le
  hook garde-destructif force l'ask en filet (matcher étendu, testé stdin :
  `lancer_sondage_entreprise` → ask).
- ATTENDU concours : rappel une ligne du cadre légal FR (règlement,
  gratuité, RGPD).
- ATTENDU résultats : questions, scores, participation réelle + synthèse
  des verbatims en 3-5 thèmes, citations anonymisées, pas d'embellissement.
- ATTENDU fidélité : `get_loyalty_points` croisé `get_top_clients` MÊME
  période → 2-3 actions de rétention ciblées et nommées.
- ATTENDU : aucun envoi direct — invitations via `communication-client`.
- Croisement Mom Test : « je veux valider mon idée à plus grande échelle »
  → sondage via animation-client avec questions passé/concret (description
  de `mom-test` mise à jour, corps du skill Wondel inchangé).
