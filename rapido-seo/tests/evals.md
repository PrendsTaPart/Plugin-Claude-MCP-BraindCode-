# Évals — plugin rapido-seo (0.1.0)

## Déclenchement (5 phrases → skill)
| Phrase | Skill |
|---|---|
| « Fais un audit SEO de mon site » / « pourquoi je ne ranke pas » | `audit-seo-technique` |
| « Recherche de mots-clés sur la digitalisation des restaurants » | `recherche-mots-cles` |
| « Analyse mes backlinks / le netlinking de mes concurrents » | `netlinking` |
| « Ma performance SEO / mes positions Google / pages qui convertissent en organique » | `performance-organique` |
| « Tendances / qu'est-ce qui monte / saisonnalité de mes mots-clés » | `tendances-marche` |
| « Pilote mon SEO / fais le point SEO » | `pilotage-seo` |

## Anti-déclenchements (contre-exemples)
- « Comment être cité par ChatGPT / optimise pour les moteurs génératifs » → **`rapido-marketing:geo-optimization`** (GEO, pas search classique).
- « Fais le point marketing global » → **`rapido-marketing:pilotage-marketing`** (transverse ; il invoque pilotage-seo pour l'organique).
- « Tendances créatives TikTok / quels formats de pub marchent » → **`rapido-tiktok-ads:tendances-creatives-tiktok`** (créatif, pas recherche).
- « Analyse la performance de mes contenus publiés » → **`rapidocms:analyse-performance-contenu`** (contenu social, pas SEO).

## Garde-fous
- `garde-couts-seo` : requête DataForSEO facturée (backlinks/serp/labs…) sans `cout_confirme` → **ask** (coût annoncé). GSC/GA4 → allow.
- Fraîcheur GSC précisée dans les rapports ; GA4/Google Ads lecture seule ; contenu publié modifié seulement après confirmation.
