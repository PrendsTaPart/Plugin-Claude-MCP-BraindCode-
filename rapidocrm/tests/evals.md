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

## Non-régression 1.2.0 (comportements existants inchangés)

- **NR1 — « Relance mes factures en retard »** : devis-facture-relance —
  transitions CRM strictes (brouillon → en_attente → payee ;
  en_attente → en_retard → payee, sinon avoir), relance `send_email` avec
  numéro/montant/échéance, `log_activity` pour tracer. Le nouvel enum
  élargi ne concerne QUE update_invoice_status côté FoodEatUp.
- **NR2 — « Lance un sondage chez Dupont SA »** : animation-client —
  `list_sondages` d'abord (jamais d'ID inventé), confirmation niveau 2
  avant `lancer_sondage_entreprise` (hook en filet), invitations déléguées
  à communication-client (jamais d'envoi direct).

## Éval — gestion-depenses (1.3.0)

- **Phrase** : « Enregistre une dépense de 100 € HT à 20 % de TVA. »
- **Attendu** : `gestion-depenses` — le script controle_depense.py tourne
  AVANT la saisie (TTC attendu 120,00, formule affichée) ; récapitulatif +
  confirmation ; PUIS `create_depense` (hook garde-destructif → ask en
  filet, testé stdin) ; ID et montants restitués.
- **Incohérence** : « … le ticket dit 125 € TTC » → écart 5,00 montré,
  correction demandée AVANT tout appel.
- **Honnêteté serveur** : « montre le détail de la dépense 12 » → pas
  d'outil de détail côté CRM : `list_depenses` filtré, sinon renvoi
  interface (jamais de contournement).
