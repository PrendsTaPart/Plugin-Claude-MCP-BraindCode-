# foodeatup-tutoriel

L'**Académie FoodEatUp** dans Claude, branchée sur le vrai serveur public
« FoodEatUp tutoriel » (`https://tutoriel.foodeatup.com/mcp`, lecture seule,
sans compte — 36 outils vérifiés en session live du 2026-10-25, serveur
v0.7.0). Le contrat : **le serveur enseigne, il n'agit pas** — agir sur un
compte réel passe par le connecteur produit `https://foodeatup.com/api/mcp`,
que ce plugin n'appelle jamais.

## Les 16 skills

| Besoin | Skills |
|---|---|
| Se former | `demarrer-academie` (cadrage secteur → métier), `parcours-sur-mesure`, `lecon-guidee` (vidéo → quiz → exercice), `carnet-de-reprise` |
| Trouver et explorer | `trouver-un-tuto`, `explorer-un-module`, `comprendre-foodeatup`, `journee-metier` |
| Équipe | `former-mon-equipe` (plan par postes — rien n'est « envoyé ») |
| Pratiquer avec l'IA | `prompts-ia-restaurant`, `passer-a-l-action` (le pont vers le connecteur produit) |
| Avant-vente & écosystème | `decouvrir-l-offre` (tarifs datés), `devenir-partenaire`, `espace-convive` (vidéos non tournées : jamais de lien), `developpeur-api` |
| Production de contenu | `studio-production-tutos` (manques, briefs, scripts) |

## Les 4 agents

- **`chef-formateur`** — mène la séance : une leçon à la fois, vignette,
  quiz, exercice, code de reprise.
- **`responsable-formation`** — pense équipe et calendrier : plans par
  postes, onboarding, suivi des carnets.
- **`conseiller-academie`** — l'avant-formation : offre, secteurs, convive,
  partenaires, API — chaque chiffre sourcé et daté.
- **`producteur-tutos`** — pilote les manques du catalogue et les briefs de
  tournage (ton imposé : aucun concurrent, aucune promesse chiffrée).

Tous limités au périmètre du serveur Académie (36 outils).

## Les 7 commandes

`/academie` (sommaire ou cadrage) · `/lecon <slug|sujet>` · `/quiz
<tutoriel|module>` · `/parcours <métier|module>` · `/former-equipe
<postes>` · `/carnet [code]` · `/tutos-manquants [module]`.

## Les 5 widgets HTML

`widgets/` + `scripts/render_widget.py` (stdlib) : `carte-tutoriel`,
`lecteur-chapitres` (repli `etapes` vérifié), `quiz-interactif` (réponses
repliées), `progression-parcours` (formule de durée affichée),
`plan-formation-equipe` (imprimable). Le serveur n'expose **aucune ressource
MCP Apps (`ui://`)** — vérifié le 2026-10-25 — ces gabarits locaux sont le
repli officiel. Jetons CSS neutres, surchargables par la charte client
(`./rapido-kb/charte-graphique.md`, jamais versionnée ici).

## Les 4 hooks (testés en CI)

- `garde-perimetre-academie` — **fail-closed** : un outil hors de
  l'inventaire vérifié (copie embarquée `outils-academie.txt`, égalité avec
  `docs/inventaires/foodeatup-tutoriel-tools-live.txt` contrôlée en CI) →
  confirmation humaine.
- `anti-lien-invente` — un slug est en kebab-case et vient d'une réponse du
  serveur ; une URL hors domaines de l'Académie est refusée (deny).
- `garde-tarifs-et-commissions` — écrire un montant FoodEatUp sans date de
  vérification → ask ; question de prix → rappel de la règle en contexte.
- `contexte-academie` — SessionStart : le contrat du plugin en tête de
  session (n'interfère jamais ailleurs).

## Règles non négociables (reference/)

`reference/directives-outils.md` (étape 0 de chaque skill) : méthode du
serveur (secteur avant métier, une leçon à la fois, vignette en bloc image,
quiz puis exercice, carnet en fin de séance), rien d'inventé (sujets,
liens, chiffres — toujours l'outil + la date), convive sans lien vidéo,
partenaires sans montant hors réponse. `reference/pieges-verifies.md` :
comportements constatés en session live (paramètre `question`, `niveau`
obligatoire, `videosEnLigne` ≠ `videosPrevues`, deux totaux d'outils selon
la source…).

## Prérequis

Aucun secret : le serveur Académie est public (`.mcp.json` embarqué). La
charte graphique et les données client vivent dans `./rapido-kb/` (jamais
versionnées).
