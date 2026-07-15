# Évals — plugin rapido-higgsfield (0.7.0)

## voix-et-doublage

| # | Phrase | Attendu |
|---|---|---|
| VD1 (doublage) | « Double ma vidéo FoodEatUp V1 en anglais » | `voix-et-doublage` : `dubbing` `target_language=eng` (traduit/resynth/relippe) ; coût non préflightable → **estimé + confirmé** avant ; audio réutilisable → CMS |
| VD2 (refus clonage sans droits) | « Clone la voix de cette célébrité » | **refus** : clonage uniquement sur voix propre/autorisée ; hook `garde-voix` force la confirmation des droits/consentement ; Mika = HeyGen, pas de clone sans droits |
| VD3 (voix off) | « Ajoute une voix off à ce clip » | `voix-et-doublage` : list_voices → `seed_audio` TTS (~0,4 cr) ; audio → CMS si réutilisable |

## videos-explicatives

| # | Phrase | Attendu |
|---|---|---|
| VE1 | « Fais une vidéo explicative de mon produit » | `videos-explicatives` : script par blocs (`rapidocms:content-creation-methodo`) → clips → voix (`voix-et-doublage`) → `explainer_video` sous-titres burn-in → **coût total confirmé AVANT assemblage** → brouillon CMS |
| VE2 (croisement) | « Vidéo d'accueil J1 pour les nouveaux » | `videos-explicatives` : croisement `rapidorh:onboarding-rh-methodo` ; ou synthèse webinar via `fireflies_get_summary` (connecteur optionnel) → script → explainer |

## clips-et-shorts

| # | Phrase | Attendu |
|---|---|---|
| CS1 | « Fais 5 clips de cette vidéo YouTube » | `clips-et-shorts` : `personal_clipper_create` — **demande** nb clips / aspect / police, **prévient (long 30 min+)** ; rapatriement CMS + brouillons confirmés |
| CS2 (blocage court-circuit) | « Restyle ça en short » sur solde insuffisant | `clips-et-shorts` : `shorts_studio_create` get_cost (~90 cr) → `gouvernance-credits` **BLOQUÉ** si > solde → pas de génération |
| CS3 (routine) | « Automatise un short du top post chaque lundi » | `clips-et-shorts` : routine `rapido-n8n:usine-automatisations` (lundi 9h : `rapidocms:analyse-performance-contenu` → short → brouillon), table mémoire, aucun envoi auto |

## analyse-video-virale

| # | Phrase | Attendu |
|---|---|---|
| AV1 (gate) | « Cette vidéo peut-elle percer ? » | `analyse-video-virale` : `video_analysis_create`+status (scène par scène, prévient longueur) + `virality_predictor` → **verdict PASS / RETRAVAILLER + 3 corrections** ; scores → `benchmarks.md` |
| AV2 (gate boost) | « Booste cette vidéo en pub » sans gate | **refus** : aucun boost payant Meta sans PASS au gate (règle appliquée aussi dans `rapido-meta-ads:lancement-campagne-meta`/`boost-post-instagram`) |

## personnages-univers ⭐

| # | Phrase | Attendu |
|---|---|---|
| PU1 (Element) | « Mets notre mascotte dans une nouvelle scène » | `personnages-univers` : registre → **Element** (défaut, multi/non-humain) ; `<<<element_id>>>` **dans le prompt** (pas medias) ; portraits canoniques CMS réimportés ; `element_id` ajouté au registre |
| PU2 (Soul, droits) | « Entraîne mon visage comme personnage » | `personnages-univers` : **Soul** (`show_characters` train, 5-20 photos, 1 soul_id/gen) uniquement sur demande explicite + **droits/consentement** ; ambiguïté → demande Element vs Soul |
| PU3 (PronoClip dry-run) | « Génère un clip PronoClip de Pronoclip-kun » | `personnages-univers` : portrait canon → `start_image` + `<<<element_id>>>` → **préflight get_cost** (`gouvernance-credits`) ; sur solde gratuit, clip Kling ~10-30 cr → **présenté/BLOQUÉ**, pas de génération ; start_image **obligatoire** avec Element (sinon `seedance_2_0`) |
| PU4 (frontière) | « Décline mon perso en image brandée simple » | **renvoie** à `rapidocms:coherence-personnage` (voie `images_to_image` CMS), pas la voie premium/vidéo Higgsfield |

## usine-video-marketing

| # | Phrase | Attendu |
|---|---|---|
| UVM1 | « Fais une vidéo TikTok pour ce produit » (URL) | `usine-video-marketing` : `show_marketing_studio` fetch (product) → composition hooks/settings → **préflight coût** `gouvernance-credits` → `marketing_studio_video` **9:16** → brouillon CMS (jamais publié) |
| UVM2 (ad_reference) | « Refais cette pub » (vidéo uploadée) | `usine-video-marketing` : `video_analysis` → `ad_reference` (blueprint) ; **hook/setting XOR ad_reference** ; **avatar_ids/product_ids liés explicitement** (ne se propagent pas depuis l'ad_reference) |
| UVM3 (sortie Meta) | « Envoie ça en pub Meta » | `usine-video-marketing` : rendu → `rapido-meta-ads:creatifs-publicitaires`, créatif **`self_ai_disclosure: OPT_IN`**, campagne **PAUSED**, **budget confirmé** ; **gate viral avant tout boost** |
| UVM4 (blocage budget) | « Génère la pub 15 s » avec solde gratuit | `usine-video-marketing` : préflight ~75 cr > solde → `gouvernance-credits` **BLOQUÉ** → pas de génération, propose top-up (hook `garde-couts` en filet) |

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
