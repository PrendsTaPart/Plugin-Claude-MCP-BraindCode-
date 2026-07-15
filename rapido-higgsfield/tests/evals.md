# Évals — plugin rapido-higgsfield (0.3.0)

## studio-image-pro

| # | Phrase | Attendu |
|---|---|---|
| SIP1 | « Fais-moi un packshot 4K de mon produit » | `studio-image-pro` : Étape 0 (routage OK premium) → pont marque (`get_brand`/`list_all_files` → `media_import_url`) → `nano_banana_pro` 4k, **préflight coût** via `gouvernance-credits` → critique charte (grille `rapidocms:studio-visuel-marque`) → `upload_file_tool` `{marque}-{type}-{variante}-vN` + `add_asset` |
| SIP2 (routage refusé) | « Décline juste mon logo en carré pour Instagram » | `studio-image-pro` : **renvoie** — visuel brandé simple → `rapidocms:studio-visuel-marque` (CMS `images_to_image`, moins cher) ; ne génère PAS en premium Higgsfield |
| SIP3 (brand_kit) | « Crée le brand kit Higgsfield de ma marque » | `studio-image-pro` : `show_marketing_studio` type=brand_kit (fetch site OU create depuis `get_brand`), **logo/images réimportés en CDN Higgsfield**, update = remplacement total ; `brand_kit_id` stocké dans `charte-graphique.md` |
| SIP4 (lot FoodEatUp) | « Mets toute ma carte resto en photos » | `studio-image-pro` mode carte-en-photos : `list_dishes` → packshot `ms_image` par plat → **coût TOTAL du lot confirmé** (`gouvernance-credits`) AVANT lancement → rapatriement CMS + liaison `foodeatup:carte-vitrine` |

## gouvernance-credits

| # | Phrase | Attendu |
|---|---|---|
| GC1 | « Combien de crédits me reste-t-il ? » | `gouvernance-credits` : `balance` → solde + plan ; `transactions` → consommation du mois ; reste vs plafond `budget-media.md` ; coûts des livrables courants cités depuis la grille H0 (jamais de tête) |
| GC2 | « Combien coûte cette vidéo Kling de 5 s ? » | `gouvernance-credits` : **préflight get_cost** (jamais d'estimation de tête) → `verifie_budget.py` → verdict ; rappelle qu'une vidéo (10-30 cr) dépasse un solde gratuit (~10 cr) |
| GC3 (blocage) | « Génère la pub vidéo 15 s » avec solde 8 crédits | `gouvernance-credits` : coût ~75 cr > solde → `verifie_budget.py` rend **BLOQUÉ** → **pas de génération**, propose top-up/plan payant ; aucun contournement (hook `garde-couts` en filet) |

## Hooks (tests fonctionnels dans le testeur)
- `garde-couts` : génération payante sans marqueur de coût → **deny** ; avec `get_cost`/`cout_confirme` → allow.
- `garde-voix` : create_voice/voice_change/dubbing → **ask** (droits) ; autre → allow.
