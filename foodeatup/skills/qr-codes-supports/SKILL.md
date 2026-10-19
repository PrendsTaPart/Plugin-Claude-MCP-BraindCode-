---
name: qr-codes-supports
description: Utiliser quand l'utilisateur veut un QR code (menu de table, réservation, avis Google, fidélité, roue cadeaux, sondage, carte cadeau, paiement à table) pour un chevalet, une affiche ou un support imprimé, ou signale un QR de table volé ou détourné. Liste les adresses publiques du restaurant, génère les QR codes et les chevalets de table, régénère un QR compromis.
---

# QR codes & supports imprimés

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
   règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).
2. S'assurer d'avoir l'`establishment_id` (le demander si absent) avant tout appel.
3. Règle « Résolution des noms » (directives § 1 ter) : tout nom parlé ou
   écrit (produit, ingrédient, plat, équipement, table, recette) se résout
   via `search_entities` AVANT tout autre appel — si `ambiguous=true`,
   présenter les candidats et DEMANDER confirmation. Jamais d'ID deviné.

## Workflow

1. **Inventaire des destinations** — `get_qr_destinations` (`famille`
   optionnelle ∈ commander | reserver | jouer | fidelite | avis | infos | payer ;
   `actifs_seulement`) : chaque adresse publique, active ou non (et pourquoi),
   le module d'abonnement requis, `url`, `url_stable` et `qr_image_url`.
   Ne proposer sur un support que des destinations **actives**.
2. **Générer un QR** — `get_qr_code` : `type` + `reference_id` (obligatoire
   pour page, table, reservation, roue, sondage, payer_a_table) OU `url`
   appartenant au restaurant (toute autre adresse est refusée) ; `format`
   `svg` (impression, défaut) ou `png` ; `size` 128–2048. Garder
   `encoder: url_stable` pour l'imprimé : il survit à un changement de domaine.
3. **Chevalets de table** — `generer_qr_table` (`table_id`, ou rien = toutes
   les tables) : adresse `/t/...`, image du QR et lien d'impression de tous
   les chevalets. N'invalide aucun QR déjà imprimé.
4. **QR compromis** — `regenerer_qr_table` (`table_id`) change l'adresse :
   **le chevalet imprimé ne fonctionne plus** et devra être réimprimé ; refusé
   si une note est ouverte sur la table. Appeler d'abord sans `confirm`
   (l'outil décrit la conséquence), la relire, puis `confirm: true`.

## Passerelles

- Visuel du support (affiche, flyer, menu) → plugins rapido-canva / rapidocms ;
  ce skill fournit les QR et les URL exactes, jamais une URL reconstruite.
- Roue cadeaux, sondage → `campagnes-restaurant` ; fidélité →
  `fidelite-restaurant`.

## Garde-fous

- Jamais d'URL inventée ou raccourcie à la main : seules celles rendues par
  le serveur.
- `regenerer_qr_table` = irréversible pour le support imprimé → confirmation
  (hook `garde-destructif`).
