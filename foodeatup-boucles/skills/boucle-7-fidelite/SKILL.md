---
name: boucle-7-fidelite
description: Utiliser quand l'utilisateur veut l'état de la boucle ⑦ Fidélité — « où en est ma boucle fidélité », « mon programme de fidélité rapporte-t-il », « bilan points, récompenses et jeux », « ma roue cadeaux tourne-t-elle ». Diagnostic programme/récompenses/jeux avec vérification systématique que le programme est actif, pas la gestion d'un compte client.
---

# Boucle ⑦ — Fidélité (programme, récompenses, jeux)

## Quand l'utiliser

Pour l'**état du moteur de fidélisation** : programme, catalogue de récompenses,
bons émis, cartes cadeaux, roues cadeaux et sondages. La question de la boucle :
« mes clients ont-ils une raison de revenir ? »

## Enchaînement d'outils MCP (l'ordre compte)

1. **OBLIGATOIRE en premier : `get_loyalty_program`.** Lire le champ `active`.
   Si `active: false`, le signaler AVANT toute autre action et s'arrêter là pour
   les propositions : un catalogue de récompenses actif sur un programme éteint
   ne produit rien. Proposer la réactivation (`update_loyalty_program`,
   confirmation obligatoire) ou l'expliquer, mais ne rien construire par-dessus
   un programme inactif.
2. Si le programme est actif : `list_loyalty_rewards` (catalogue, stocks de
   récompenses), `list_redemptions` (bons émis vs utilisés — un taux d'usage
   nul signale un catalogue inadapté).
3. `list_gift_cards` (encours de cartes cadeaux = dette), `check_gift_card` au
   cas par cas ; `get_loyalty_capture` (part des tickets rattachés à une fiche
   client — le KPI d'amont : un taux bas se traite AVANT de toucher aux
   récompenses).
4. Jeux : `list_wheel_games` + `get_wheel_stats`, `list_surveys` +
   `get_survey_results`. La **création est possible par MCP depuis 2026-10**
   (`create_wheel_game`, `create_survey` — créés INACTIFS, l'activation reste
   une décision du restaurateur, en back-office) : pour créer, passer par le
   skill `campagnes-restaurant` (plugin foodeatup) ; détail des limites dans
   docs/couverture-fidelite-jeux.md à la racine du dépôt.
5. Comptes : `get_loyalty_account` par client ; `adjust_points` seulement en
   geste commercial motivé (plafond serveur ±1000, motif obligatoire).

## Règles métier

- Programme inactif + récompenses actives = incohérence à remonter (détection
  partagée avec le skill `croisement-service`).
- Une récompense dont le stock est épuisé mais toujours affichée frustre plus
  qu'elle ne fidélise : proposer `upsert_loyalty_reward` pour la retirer.
- Ne jamais promettre au client un gain de roue ou un solde de points sans
  l'avoir lu dans l'outil.

## Garde-fous (opérations exigeant confirmation)

Interceptés par le hook du plugin (confirmation humaine obligatoire) :
- `update_loyalty_program` — modifie les règles pour TOUS les clients ;
- `adjust_points` — modifie un solde client.
`validate_redemption` est à usage unique (dédup serveur) : valider seulement
un bon physiquement présenté.

## Sortie attendue

D'abord une ligne d'état : « programme ACTIF/INACTIF (mode, taux) ». Puis un
tableau `[levier | volumétrie | état | action proposée]` pour : récompenses,
bons, cartes cadeaux, roue, sondages.

## Ce que ce skill NE fait PAS

- Gérer les points d'un client au fil du service → skill `fidelite-restaurant`
  (plugin foodeatup).
- Créer une roue cadeaux ou un sondage → skill `campagnes-restaurant` (plugin
  foodeatup) ; l'ACTIVATION reste en back-office (créés inactifs).
- Communiquer sur le programme → skill `boucle-6-communication`.
