# Changelog — plugin foodeatup-tutoriel

## 0.1.0 — 2026-10-25 — l'Académie FoodEatUp dans Claude

- 4 skills par rôle couvrant les 26 outils du serveur Academy FoodEatUp :
  `se-former-foodeatup` (recherche, parcours, progression, favoris, achats,
  sessions), `enseigner-foodeatup` (apprenants, agenda, revenus),
  `fabriquer-des-cours` (créations en brouillon, publication confirmée,
  comptes, candidatures, paiements, audit), `prompts-academie` (marketplace
  de prompts, liens publics).
- Agent `professeur-foodeatup` : la formation part du symptôme observé dans
  l'exploitation, 1 à 3 cours recommandés avec leur raison, pratique via les
  skills foodeatup.
- Hook garde-academie : `admin_publish_toggle` et `admin_user_role_set` en
  confirmation humaine ; la règle serveur « contenus IA en brouillon,
  un humain publie » est relayée dans tous les skills.
- Liste versionnée docs/inventaires/academy-foodeatup-tools-live.txt
  (26 outils, session du 2026-07-28 — serveur injoignable le 2026-10-25,
  à re-vérifier).
