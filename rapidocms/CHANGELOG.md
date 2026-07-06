# Changelog — plugin rapidocms

## 0.5.0 — 2026-07-06

- Utilisation de la base de connaissance `./rapido-kb/` : règle de chargement
  dans les directives ; `responsable-marketing`, `community-manager` et
  `directeur-artistique` puisent ton, accroches et charte dans la KB (avec
  citation de source) ; `prompt-engineering-visuel` : palette depuis
  rapido-kb/charte-graphique.md en priorité (get_brand en vérification) ;
  `calendrier-editorial` : piliers depuis ton-et-accroches.md et
  propositions-valeur.md.

## 0.4.0 — 2026-07-06

- Script de calcul `skills/analyse-performance-contenu/scripts/content_scores.py`
  (stdlib) : engagement par format/réseau/créneau, top/flop, tendance,
  signal_faible < 3 posts — le skill impose « utiliser le script pour tout
  calcul ; ne jamais calculer de tête ».
- `reference/pieges-outils.md` : tableau des pièges (account_id par réseau,
  media_source "biblio", formats Y-m-d/H-i-s, max 10 insights,
  ingishts_campagne, formats visuels par réseau…), référencé par les
  directives.

## 0.3.0 — 2026-07-06

- Hooks déterministes (`hooks/hooks.json` + `hooks/scripts/`) :
  - PreToolUse `garde-destructif` : confirmation forcée (ask) sur `delete_*`,
    `cancel_schedules_post` et `remove_post_campagne` ;
  - Stop `récap-actions` (hook prompt) : bloque la fin de tour si des écritures
    MCP ont eu lieu sans récapitulatif des IDs dans la réponse.

## 0.2.0 — 2026-07-06

- Ajout de la couche métier :
  - Agents : `responsable-marketing` (objectif avant production, calendrier
    éditorial, boucle publier → mesurer → ajuster), `community-manager`
    (adaptation native par réseau, créneaux de publication) et
    `directeur-artistique` (charte avant création, checklist contraste/
    lisibilité/hiérarchie, formats par réseau, refus des visuels hors charte).
  - Skills d'expertise : `prompt-engineering-visuel` (structure de prompt en
    6 blocs, variantes, critique vs charte, itération),
    `calendrier-editorial` (piliers, répartition par réseau, formats variés,
    rattachement campagne) et `analyse-performance-contenu` (patterns gagnants,
    3 recommandations actionnables).
- Les agents connaissent et invoquent les skills du plugin au bon moment.

## 0.1.0 — 2026-07-06

- Version initiale : `.mcp.json` (serveur rapidocms), références
  `directives-outils.md` et `charte-graphique.md`, skills workflow
  `pipeline-contenu-social`, `orchestration-campagne`, `carte-digitale`,
  `contenu-conforme-marque`.
