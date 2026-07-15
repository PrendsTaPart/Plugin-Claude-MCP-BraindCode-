# NOTICE — rapido-leadmagnet

Ce plugin **s'inspire de frameworks** de dépôts open source **sous licence MIT** :
il **francise et réimplémente** des méthodes (souvent publiques : Hormozi, Schwartz,
PAS/PASTOR) — il **ne redistribue aucun corps de texte** ni code source de ces
dépôts. Attribution ci-dessous.

## Sources MIT (frameworks adaptés, non redistribués)

| Dépôt | Licence | Ce qui est repris |
|---|---|---|
| `timscheuerai/content-vault` | MIT | Taxonomie de **formats** de lead magnet + angles d'idées + structure de rédaction par type (francisés) |
| `thalesholleben/copy-thief` | MIT | **Structure de landing** (menu de sections + presets par niveau de conscience) + checklist QA copy (francisés, re-dérivés ; texte PT-BR **non copié**) |
| `johnericforte/claude-skill-hormozi-offer-audit` | MIT | **Forme d'audit** d'offre (score / levier faible / fixes) — les frameworks Hormozi eux-mêmes viennent du skill maison `rapido-meta-ads:hundred-million-offers` |
| `cblain100-prog/lead-magnet-responder` | MIT | **Mécanique** LinkedIn « commente pour recevoir » (adaptée en **semi-auto** ; le code d'envoi Unipile n'est **pas** repris) |
| `jamnyjakub700-cloud/pdf-ebook-generator` | MIT | **Pattern** `charte → template → PDF` (réimplémenté maison via `get_brand` + skill pdf ; `generate_ebook.py` **non fusionné**) |

## Exclusions

- `enoobis/AI-eBook-Generator` (**GPL-3.0**) : pattern **lu uniquement**, **jamais**
  fusionné ni copié.
- Aucune clé, aucune donnée client dans le dépôt. Le service tiers **Unipile**
  (LinkedIn) n'est **pas** utilisé (envoi humain).
