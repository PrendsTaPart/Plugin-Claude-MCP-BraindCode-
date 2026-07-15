# NOTICE — rapido-design

Ce plugin **s'inspire de** dépôts open source **sous licence MIT** : il **francise et
réimplémente des principes** (jugement design, audits, motifs d'animation) — il **ne
redistribue aucun corps de texte** ni exemple citant un designer/marque réel.

## Sources MIT (adaptées, non redistribuées)

| Dépôt | Licence | Ce qui est repris |
|---|---|---|
| [dominikmartn/hue](https://github.com/dominikmartn/hue) | MIT | Principe **charte → design system** (marque comme input) → direction-artistique / studio-maquette |
| [bitjaru/styleseed](https://github.com/bitjaru/styleseed) | MIT | **Jugement design** (anti-goût-IA) → `reference/jugement-design.md` |
| [joeseesun/qiaomu-design](https://github.com/joeseesun/qiaomu-design) | MIT | Conseiller anti-goût-IA (francisé du chinois) → `jugement-design.md` |
| [natdexterra/work-with-design-systems](https://github.com/natdexterra/work-with-design-systems) | MIT | Audits **WCAG** + scoring de design system Figma → gate a11y de studio-maquette |
| [B3nnyL/figgo](https://github.com/B3nnyL/figgo) | MIT | Pattern de **sync tokens** Figma ↔ code (référence) |

## Exclusions (règle maison)

- **`Trystan-SA/claude-design-system-prompt`** : licence MIT **mais contenu
  reverse-engineered** d'un produit tiers (« system prompt of Claude Design from
  Anthropic ») → **ÉVITÉ**, aucune reprise (benchmark de concepts seulement).
- `plugin87/ux-ui-agent-skills` (**sans licence**) : benchmark seul, **zéro copie**.
- **Bibliothèques d'animation** (magicui, motion-primitives, animata) : **aucun code
  embarqué** ; seuls des **motifs génériques** (durées/easings) sont référencés. Toute
  reprise de code exigerait une confirmation de licence.

Aucune clé, aucune donnée client dans le dépôt. La charte vit dans RapidoCMS (source de
vérité) et `./rapido-kb/`.
