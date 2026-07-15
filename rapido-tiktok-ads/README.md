# rapido-tiktok-ads

**TikTok Ads — VERROUILLÉ (argent réel).** MCP officiel TikTok Ads (annoncé 05/2026)
en **lecture/écriture** sur tout le cycle campagne → ce plugin hérite des verrous
« argent réel » de `rapido-meta-ads`, **en plus stricts** (plateforme récente).

> **MCP TikTok Ads non encore connecté** : skills écrits d'après le cycle campagne
> documenté ; noms d'outils exacts confirmés à la connexion.

## Connecteurs (`.mcp.json`) — clés en variables d'env
| Serveur | Config | Env |
|---|---|---|
| **tiktok-ads** (officiel, R/W) | passerelle HTTP | `TIKTOK_ADS_MCP_URL` (+ OAuth TikTok Business côté serveur) |
| rapidocms / rapidocrm | ponts brief créatif / données | — |

## Checklist (une fois)
- [ ] **TikTok Ads** : compte TikTok Business + OAuth du serveur officiel.
- [ ] **Plafonds** `./rapido-kb/` : budget pub max/jour TikTok (le « X €/jour »).

## Skills
- **`pilotage-performance-tiktok`** — CPM/CPC/CPA, perf par créatif, comparatif TikTok vs Meta (arbitrage).
- **`lancement-campagne-tiktok`** — campagne → ad group → créatif → ad **100 % inactif** ; activation séparée confirmée.
- **`tendances-creatives-tiktok`** — formats/hooks performants ; brief délégué à rapidocms/rapido-video (≠ tendances de recherche).

## Garde-fous (les plus stricts du marketplace)
`reference/garde-fous-tiktok.md` : **création toujours inactive** (hook
`garde-argent-reel-tiktok` **DENY** sur création active ; si un outil n'a pas d'état
pausé → lecture seulement) ; **activation = confirmation écrite séparée** ; **budget
max annoncé**, plafond KB, jamais > X €/jour sans validation ; récap Stop (IDs,
statuts en toutes lettres, budgets, coût max). Calculs via `catalogue-kpi`.
