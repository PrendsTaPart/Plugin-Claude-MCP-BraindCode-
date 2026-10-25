# La méthode Build — dix étapes, cinq critères, trois parcours

Source : fiche `get_build_braindcode` de l'Academy (relevé serveur du
2026-10-07) croisée avec le manifeste MCP live de Build (2026-10-25,
44 outils). À relire au début de chaque skill du plugin.

## Les cinq critères (règles maison, non négociables)

1. Toute extension expose son **propre serveur MCP** pour être orchestrable
   par Plan'It.
2. Toute extension publie son **plugin sur la marketplace**.
3. **Aucun credential MCP n'atteint le navigateur.**
4. Le **rapport de test** est obligatoire.
5. Une extension ne vaut que par la **routine qu'elle fait tourner**.

## Les dix étapes

| # | Étape | Où ça se joue dans ce plugin |
|---|---|---|
| 01 | Connecter ses outils (Figma, Lovable, MCP produit, Academy/Tutoriel) | SessionStart + skill `tableau-de-bord-build` |
| 02 | Récupérer le contexte du produit SANS supposer un outil : tools/list | skill `cahier-des-charges` (découverte réelle) |
| 03 | Expliquer l'idée, demander une critique honnête | skill `choisir-une-idee` |
| 04 | Écrire les prompts Figma (écrans, états, composants, charte) | skill `maquettes-figma` |
| 05 | Écrire les prompts Lovable qui reprennent maquettes et charte | skill `creer-le-projet-lovable` |
| 06 | Brancher le MCP : modèle « Connexion MCP + auth », rien au navigateur | skill `brancher-le-mcp-produit` |
| 07 | Construire et tester : parcours manuel, appels MCP et erreurs automatisés, rapport | skills `executer-le-plan` + `tester-et-rapporter` |
| 08 | Exposer et faire valider son MCP : une tâche complète sans aide, trace jointe | skill `exposer-et-valider-son-mcp` |
| 09 | Déclarer le MCP dans Plan'It, finaliser le dépôt | skills `declarer-dans-planit` + `plugin-du-projet` |
| 10 | Transformer en routine : objectif chiffré, déclencheur, outils, garde-fous, point d'arrêt humain, mesure | skill `routine-et-boucle` |

## Les validations humaines

OAuth, clé d'accès, paiement et mise en ligne passent TOUJOURS par
`request_human_validation`, suivies par `get_pending_validations` — on ne
continue jamais sans la validation lue comme accordée. **Jamais de secret**
dans une demande, un blocage (`report_blocker`), un message Lovable ou une
trace. **On ne devine jamais un identifiant** : on le retrouve
(`list_projects`, `list_my_projects`).

## Le journal d'exécution

`register_ai_developer` (mode `ia` ou `hybride`) crée le projet, réserve
l'idée et ouvre le journal. Il passe AVANT `get_prompt_execution_plan`, qui
crée le tableau et renvoie les étapes (prompts, livrables, conditions de
passage, validations exigées). `start_prompt_step` passe une carte « en
cours » ; `complete_prompt_step` la termine, ou la met « à valider » avec
`needs_review`.

## Les trois parcours

- **Talents** : étudiants, stage ou alternance chez BraindCode — déposer
  une extension, entretien technique de trente minutes.
- **Partenaires** : apporteur d'affaires, intégrateur, éditeur d'extension
  — commission récurrente sur les abonnements apportés, licences ; barème
  communiqué à la validation du partenariat (jamais inventé ici).
- **Contributeurs** : un prompt devient une skill, une skill devient une
  routine, une routine s'orchestre dans Plan'It — publiés sur
  plugin.braindcode.com.
