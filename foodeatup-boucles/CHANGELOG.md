# Changelog — plugin foodeatup-boucles

## 0.2.0 — 2026-07-28 — découplage RapidoCRM

- RapidoCRM retiré de `.mcp.json`, `mcp_requis`, des matchers de hooks
  (PreToolUse/PostToolUse), de la liste des outils destructifs et des
  lectures nommées des scripts.
- Agents `direction` et `marketing` : outils rapidocrm retirés du frontmatter
  `tools` ; textes réécrits FoodEatUp-only (segments via `list_rfm_segments`,
  campagnes via `create_campaign`).
- Skill `boucle-6-communication` : garde-fous côté CRM retirés (les outils
  FoodEatUp suffisent : `launch_campaign`, `submit_whatsapp_template`).
- Le pipeline B2B du CRM est explicitement hors périmètre (renvoi textuel
  seulement, aucun outil connecté).

## 0.1.0 — 2026-07-28 — version initiale

- 8 skills de boucle + croisement-service + decouvrir-le-plugin, 4 commands,
  3 subagents, 3 hooks (garde destructif fail-closed, SessionStart, journal).
