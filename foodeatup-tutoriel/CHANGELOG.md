# Changelog — plugin foodeatup-tutoriel

## 0.2.0 — 2026-10-25 — reconstruction sur le vrai serveur Académie

Le plugin 0.1.0 avait été bâti sur l'inventaire Academy_FoodEatUp de
juillet (26 outils `academy_*`/`admin_*`, serveur injoignable au moment de
l'écriture). Le serveur réel « FoodEatUp tutoriel » est public, en lecture
seule et expose une toute autre surface : **36 outils pédagogiques**
(v0.7.0, session live du 2026-10-25, endpoint
`https://tutoriel.foodeatup.com/mcp` confirmé par la page publique de
l'Académie). Reconstruction complète sous le même slug (0.x : l'interface
peut bouger — docs/POLITIQUE-VERSIONS.md).

- **16 skills** : demarrer-academie, parcours-sur-mesure, lecon-guidee,
  trouver-un-tuto, explorer-un-module, comprendre-foodeatup, journee-metier,
  former-mon-equipe, carnet-de-reprise, prompts-ia-restaurant,
  passer-a-l-action, decouvrir-l-offre, devenir-partenaire, espace-convive,
  developpeur-api, studio-production-tutos — étape 0 commune
  (reference/directives-outils.md) + pièges vérifiés en live
  (reference/pieges-verifies.md).
- **4 agents** : chef-formateur, responsable-formation, conseiller-academie,
  producteur-tutos — périmètre limité au serveur Académie.
- **7 commandes** : /academie, /lecon, /quiz, /parcours, /former-equipe,
  /carnet, /tutos-manquants.
- **5 widgets HTML** + scripts/render_widget.py (stdlib, formule de calcul
  affichée) : carte-tutoriel, lecteur-chapitres, quiz-interactif,
  progression-parcours, plan-formation-equipe. Aucune ressource MCP Apps
  (ui://) sur le serveur (vérifié) : gabarits locaux en repli officiel.
- **4 hooks testés** : garde-perimetre-academie (fail-closed sur
  l'inventaire embarqué, égalité CI avec la liste versionnée),
  anti-lien-invente (slugs kebab-case, URLs des domaines Académie
  uniquement), garde-tarifs-et-commissions (montant sans date de
  vérification → ask ; rappel de règle sur les questions de prix),
  contexte-academie (SessionStart).
- **Retirés** (surface de juillet disparue) : skills se-former-foodeatup,
  enseigner-foodeatup, fabriquer-des-cours, prompts-academie ; agent
  professeur-foodeatup ; hook garde-academie ; inventaire
  academy-foodeatup-tools-live.txt (remplacé par
  foodeatup-tutoriel-tools-live.txt, 36 outils).
- CI : catalogue fail-closed `foodeatup-tutoriel` (36), périmètre OUTILS
  « Académie seule » pour ce répertoire (les autres périmètres inchangés),
  tests allow/ask/deny des 4 hooks.
- `.mcp.json` : serveur public en URL directe (pas de variable
  d'environnement — aucun secret requis) ; `mcp_requis:
  ["foodeatup-tutoriel"]`.

## 0.1.0 — 2026-10-25 — l'Académie FoodEatUp dans Claude (surface de juillet)

- 4 skills par rôle couvrant les 26 outils du serveur Academy FoodEatUp :
  se-former-foodeatup, enseigner-foodeatup, fabriquer-des-cours,
  prompts-academie ; agent professeur-foodeatup ; hook garde-academie.
- Remplacé le jour même par la 0.2.0 (serveur réel enfin joignable).
