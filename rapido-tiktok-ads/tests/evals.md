# Évals — plugin rapido-tiktok-ads (0.1.0)

## Déclenchement (5 phrases → skill)
| Phrase | Skill |
|---|---|
| « Comment vont mes TikTok Ads / ma perf TikTok / CPM TikTok » | `pilotage-performance-tiktok` |
| « Arbitre mon budget TikTok vs Meta » | `pilotage-performance-tiktok` |
| « Lance une campagne TikTok / monte un ad group TikTok » | `lancement-campagne-tiktok` |
| « Quels formats/hooks TikTok marchent / idées de créatifs TikTok » | `tendances-creatives-tiktok` |
| « Prépare une pub TikTok en brouillon » | `lancement-campagne-tiktok` |

## Anti-déclenchements (collisions avec les homonymes Meta + rapido-seo)
- « Comment vont mes pubs **Meta/Facebook** » → **`rapido-meta-ads:pilotage-performance-ads`**.
- « Lance une campagne **Meta** » → **`rapido-meta-ads:lancement-campagne-meta`**.
- « **Tendances de recherche** / saisonnalité de mes mots-clés » → **`rapido-seo:tendances-marche`** (recherche, pas créatif).

## Garde-fous (hook `garde-argent-reel-tiktok`)
| Payload | Attendu |
|---|---|
| `create_campaign` avec `status: ENABLE` | **deny** (création active refusée) |
| `create_campaign` avec `status: DISABLE` | allow (création inactive) |
| `update_status` → `ENABLE` | **ask** (activation confirmée) |
| `create_adgroup` avec `budget` | **ask** (argent réel) |
| `get_report` (lecture) | allow |
