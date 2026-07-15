# Évals — plugin rapido-google-ads (0.1.0)

## Déclenchement (5 phrases → skill)
| Phrase | Skill |
|---|---|
| « Comment vont mes pubs Google / ma performance Google Ads » | `pilotage-performance-google-ads` |
| « Sur quels mots-clés enchérir / CPC estimés / structure de campagne SEA » | `recherche-mots-cles-sea` |
| « Audit de mon compte Google Ads / où je gaspille / mon Quality Score » | `audit-compte-google-ads` |
| « Où est-ce que je paie alors que je ranke déjà / arbitrage SEO vs SEA » | `synergie-seo-sea` |
| « Mes conversions Google Ads collent-elles à GA4 » | `audit-compte-google-ads` |

## Anti-déclenchements (contre-exemples)
- « Comment vont mes pubs **Meta/Facebook/Instagram** » → **`rapido-meta-ads:pilotage-performance-ads`** (Meta, pas Google).
- « Sur quels mots-clés **organiques** me positionner » → **`rapido-seo:recherche-mots-cles`** (organique, pas payant).
- « Lance/active ma campagne Google Ads » → **refus d'exécution** : ce plugin est lecture seule → instructions manuelles écran par écran (hook `garde-ecriture-google-ads` si écriture).

## Garde-fous
- `garde-ecriture-google-ads` : outil `mutate`/`create` Google Ads → **ask** ; lecture (`search`) → allow.
- Lecture seule : toute recommandation sourcée, actions présentées comme manuelles, budgets plafonds KB.
