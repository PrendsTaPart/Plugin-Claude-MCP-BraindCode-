# Audit licences & attributions — 2026-07-15 (série FINITION F1)

Objectif : chaque plugin ayant **adapté une source externe** (MIT/Apache/CC0) porte
un fichier d'attribution (`NOTICE.md` ou `ATTRIBUTIONS.md`). Vérifié par croisement des
`docs/IMPORTS-*.md`, `AUDIT-*`, `BENCHMARK-*`, `DECISION-*` et de l'historique des
CHANGELOG + scan des références de dépôts (`github.com/...`) dans chaque plugin.

## Correctifs F1 — fichiers ajoutés

| Plugin | Sources adaptées | Licence | Fichier créé |
|---|---|---|---|
| `rapido-marketing` | coldoutboundskills · gtm-flywheel · hormozi-skills · ai-marketing-claude · marketing-skill (+ *$100M Leads*) | MIT | **`NOTICE.md`** |
| `rapido-forge` | getagentseal/founder-playbook (+ livres SPIN/Blue Ocean…) | MIT | **`NOTICE.md`** |
| `rapido-gmaps` | gosom/google-maps-scraper (patterns, code non redistribué) | MIT | **`NOTICE.md`** |

## État complet du marketplace

| Plugin | Attribution | Sources externes | Statut |
|---|---|---|---|
| `foodeatup` | ATTRIBUTIONS.md | anthropics/knowledge-work-plugins (3) | ✅ |
| `rapidocrm` | ATTRIBUTIONS.md | knowledge-work-plugins (6), wondelai (3) | ✅ |
| `rapidocms` | ATTRIBUTIONS.md | knowledge-work-plugins, wondelai, AgriciDaniel/flow… | ✅ |
| `rapidorh` | ATTRIBUTIONS.md | knowledge-work-plugins (5) | ✅ |
| `rapido-suite` | ATTRIBUTIONS.md | knowledge-work-plugins, anthropics/skills | ✅ |
| `rapido-canva` | ATTRIBUTIONS.md | anthropics/skills + polices (SIL OFL) | ✅ |
| `rapido-lovable` | NOTICE + ATTRIBUTIONS | ui-ux-pro-max, VibeSec, lovable-prompt-builder… | ✅ |
| `rapido-meta-ads` | ATTRIBUTIONS.md | knowledge-work-plugins (2), wondelai (3) | ✅ |
| `rapido-copywriter` | NOTICE.md | social-media-skills, content-vault… | ✅ |
| `rapido-design` | NOTICE.md | hue, styleseed, qiaomu, work-with-design-systems, figgo | ✅ |
| `rapido-leadmagnet` | NOTICE.md | content-vault, copy-thief, hormozi-offer-audit… | ✅ |
| `rapido-prompteur` | NOTICE.md | (patterns prompts — voir NOTICE) | ✅ |
| `rapido-elevenlabs` | NOTICE.md | MCP officiel ElevenLabs | ✅ |
| `rapido-video` | NOTICE.md | ffmpeg/Whisper/Remotion (voir DECISION-LICENCES-VIDEO) | ✅ |
| **`rapido-marketing`** | **NOTICE.md (F1)** | 5 dépôts MIT + $100M Leads | ✅ (corrigé) |
| **`rapido-forge`** | **NOTICE.md (F1)** | founder-playbook MIT | ✅ (corrigé) |
| **`rapido-gmaps`** | **NOTICE.md (F1)** | gosom/google-maps-scraper MIT | ✅ (corrigé) |
| `rapido-startup` | — | **aucune** (benchmarks = données, pas de code adapté) | ✅ maison |
| `rapido-higgsfield` | — | **aucune** (skills maison sur MCP huggsfield) | ✅ maison |
| `rapido-direction` | — | aucune | ✅ maison |
| `rapido-n8n` | — | aucune | ✅ maison |
| `rapido-relation-client` | — | aucune | ✅ maison |
| `rapido-seo` | — | aucune (MCP dataforseo/GSC/GA4 officiels) | ✅ maison |
| `rapido-google-ads` | — | aucune (MCP google-ads officiel) | ✅ maison |
| `rapido-tiktok-ads` | — | aucune (MCP tiktok-ads officiel) | ✅ maison |

## Règles vérifiées (aucun doute de provenance)

- **Aucun system prompt tiers divulgué** ni redistribué (règle maison). Cas signalé et
  **évité** : `Trystan-SA/claude-design-system-prompt` (contenu reverse-engineered) —
  exclu dans `rapido-design/NOTICE.md`.
- Concepts de livres (Hormozi, StoryBrand, SPIN…) **reformulés** en terminologie neutre,
  crédités ; citations < 15 mots ; **aucun corps de texte copié**.
- `gosom/google-maps-scraper` : **patterns ré-encodés**, aucun fichier Go fusionné.
- Aucune clé ni donnée client dans le dépôt (confirmé par le grep secrets de `AUDIT-README.md`).

**Conclusion : 25/25 plugins conformes** après F1 (14 avec attribution, 11 maison sans
source externe). Aucun STOP provenance.
