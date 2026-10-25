# Changelog — plugin braindcode-build

## 0.1.0 — 2026-10-25 — Le chef de chantier Build

Première version, bâtie sur le serveur MCP BraindCode Build
(https://build.braindcode.com/api/mcp — ressource OAuth Supabase,
authentification au premier appel, aucun jeton dans le dépôt). Inventaire :
**44 outils** (docs/inventaires/braindcode-build-tools-live.txt), relevés
depuis le manifeste MCP publié du projet (serveur
« braindcode-extensions-hub » 1.0.0) — la fiche Academy du 2026-10-07 n'en
listait que 37 : elle date, consigné dans les pièges. Huit serveurs
déclarés (Build, Lovable, Plan'It, marketplace, FoodEatUp, RapidoCRM,
RapidoCMS, RapidoRH) + deux optionnels (Academy, Tutoriel) ; Figma reste
un serveur de SESSION (précédent rapido-design).

- **22 skills** : le chantier complet (tableau-de-bord-build,
  choisir-une-idee, demarrer-le-projet, cahier-des-charges,
  maquettes-figma, creer-le-projet-lovable, executer-le-plan,
  brancher-le-mcp-produit, base-de-donnees, tester-et-rapporter,
  exposer-et-valider-son-mcp, declarer-dans-planit, routine-et-boucle,
  agents-du-projet, plugin-du-projet, publier-la-vitrine,
  completer-les-vitrines, suivi-kanban, hackathon-et-demoday,
  catalogue-de-connecteurs, mesurer-la-demo, skills-dans-lovable).
- **6 agents** : chef-de-projet-build, designer-build, batisseur-lovable,
  integrateur-mcp-securite, testeur-build, publicateur-build.
- **17 commandes** : /build, /idee, /demarrer, /cdc, /figma,
  /lovable-nouveau, /etape, /brancher-mcp, /tests, /mon-mcp,
  /planit-declarer, /routine-projet, /plugin-projet, /publier, /vitrines,
  /hackathon, /blocage.
- **8 widgets HTML** à la charte BraindCode (vérifiée dans le design
  system du projet Build : Poppins, #0098F3, #161B2C) +
  scripts/render_widget.py (stdlib, sortie gitignorée) ;
  render_project_widget (Lovable) pour suivre une construction.
- **8 hooks testés en CI (33 cas allow/ask/deny)** : garde-build (6
  écritures visibles → ask), garde-credits-lovable (crédits → ask ;
  send_message hors plan → ask), garde-mise-en-ligne (deploy_project
  REFUSÉ sans validation mise_en_ligne lue), garde-lovable-ecritures
  (knowledge lu d'abord, SQL hors SELECT → ask, DROP/TRUNCATE → deny),
  anti-secret (deny sur tout motif de clé/jeton/mot de passe dans 7
  outils), audit-credentials-front (PostToolUse sur get_diff/read_file :
  rappel bloquant — critère n° 3), SessionStart (dix étapes + cinq
  critères), journal masqué (+ état de session lu par les gardes).
- **Référence** : methode-build.md (dix étapes, cinq critères, trois
  parcours), regles-lovable.md (IA intégrée, e-mails intégrés, MCP côté
  serveur, pauses, crédits, CTA FoodEatUp), carte-des-interconnexions.md,
  pieges-verifies.md (hackathon aux dates périmées, vitrines sans
  tutoriel, Daily Brief en brouillon…), outils-sensibles.json.
- CI : 6 catalogues branchés (braindcode-build 44, lovable 42 — liste
  versionnée qui remplace le relevé embarqué, marketplace-prompts 53,
  + academy/planit/foodeatup-tutoriel repris des branches sœurs) ;
  périmètre OUTILS strict pour braindcode-build/.
