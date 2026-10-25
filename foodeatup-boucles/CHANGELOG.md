# Changelog — plugin foodeatup-boucles

## 0.3.0 — 2026-10-25 — diagnostics alignés sur le serveur 2026-10 (264 outils)

- Les 8 skills de boucle lisent les nouveaux registres : horaires/fermetures et
  HubRise (①), tâches et objectifs de vente (②), liste de courses et cadencier
  (③), huiles de friture et cycles thermiques (④), appels entrants, bornes,
  rotation des tables et réconciliation SmilePay (⑤), calendrier marketing et
  écrans de la salle (⑥), taux de capture fidélité (⑦), rapport consolidé,
  analytics caisse et top/flop (⑧).
- `boucle-7-fidelite` : création de roue/sondage désormais possible par MCP
  (créés inactifs, via campagnes-restaurant) — l'affirmation « back-office
  uniquement » était périmée. Carte marketplace corrigée de même.

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
