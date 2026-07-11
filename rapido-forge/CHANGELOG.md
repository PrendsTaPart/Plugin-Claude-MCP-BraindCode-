# Changelog — plugin rapido-forge

## 1.0.0 — 2026-07-10

- Version initiale : 180 exercices d'incubateur StartupsForge
  (PrendsTaPart) mis aux conventions du marketplace rapido, en 3 parcours —
  bootcamp 5 jours (46 skills `bootcamp-*`, enrichis d'une méthode pas à
  pas), roadmap idéation (72 skills `ideation-*`), roadmap scale (62 skills
  `scale-*`).
- 4 agents : `directeur-programme` (diagnostic de maturité + routage vers
  le bon parcours), `mentor-bootcamp`, `mentor-ideation`, `mentor-scale`.
- `reference/parcours.md` : cartographie des 3 parcours et du journal.
- Livrables TOUJOURS dans `./rapido-kb/startup/forge/` (journal :
  `parcours.md`) — hook garde-ecriture-kb en filet ; exécution réelle
  déléguée aux plugins métier (~146 renvois croisés vérifiés, 2 corrigés :
  `design:*` → `rapido-lovable:frontend-design` / `rapidocrm:mom-test`).
- `.mcp.json` : rapidocrm, rapidocms, rapidorh (les serveurs que les
  skills nomment pour les données réelles, lecture d'abord).
- Hook rappel « argent réel » sur les outils Meta Ads engageant une
  dépense (création en PAUSED, activation après accord explicite).
