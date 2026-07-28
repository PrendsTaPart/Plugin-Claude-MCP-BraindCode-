# Faisabilité — Iris (Higgsfield × FoodEatUp × RapidoCMS)

> Analyse du cahier des charges « CDC Iris — agent communication » (v1.0,
> 21 juillet 2026) contre les outils MCP réellement disponibles (listes live :
> foodeatup 177, rapidocms 44, huggsfield 81). Verdict global : **le
> comportement d'Iris est implémentable dès maintenant en plugin** (agent +
> skills + garde-fous) ; **la persistance serveur et les écrans restent côté
> produit** (lots L1-L6 du CDC).

## 1. Ce qui est faisable MAINTENANT (implémenté dans le plugin foodeatup-iris)

| Étage CDC | Besoin | Outils MCP réels | Verdict |
|---|---|---|---|
| ① Capteurs | stock, DLC, plats, avis, créneaux, segments, productions, clients | `list_stocks`, `list_haccp_labels`, `list_dishes`, `list_top_productions`, `list_reviews`, `reservation_availability`, `list_orders`, `list_happy_hours`, `list_rfm_segments`, `list_production_plans`, `list_clients`, `get_recipe` (marge) | ✅ tous exposés |
| ② Moteur | scoring urgence × valeur × fraîcheur, dédup | raisonné par l'agent ; historique 14 jours dans `./rapido-kb/iris/journal-signaux.md` | ✅ (état local, pas de table serveur) |
| ③ Fabrique | visuel aux couleurs + copy + raison | `get_brand` (gate charte + hook rapidocms), `generate_image`, `images_to_image` (3 réf. max, URLs http), `create_draft_tool` | ✅ |
| ③bis Vidéo plats | photos réelles → vidéo virale | Higgsfield : `media_import_url`, `models_explore`, `generate_video` (image-to-video), `reframe` 9:16/1:1, `upscale_video`, `virality_predictor` ; hébergement photo : `upload_file_tool` (CMS) | ✅ — **à condition d'avoir de vraies photos** (règle : pas de photo → pas de vidéo du plat) |
| ④ Diffusion | brouillon → validation humaine → planification | `create_draft_tool` → `schedule_draft_tool` ; garde-iris force `ask` sur toute planification (aucun réglage pour contourner) | ✅ |
| ⑤ Mesure | insights, attribution, capitalisation | `post_insights`, `ingishts_campagne` (nom réel de l'outil), `list_scheduled_posts`, croisement `list_orders` 48 h, `add_prompt` | ✅ avec réserve d'attribution (voir §2) |
| Garde-fous | jamais de publication auto ; crédits avant ; avis négatif silencieux | hook garde-iris (ask publication, deny génération sans `cout_confirme`), règle avis négatif dans le moteur, `create_notification` pour l'alerte | ✅ |

## 2. Ce qui n'est PAS faisable via MCP (backlog produit — lots du CDC)

| Besoin CDC | Pourquoi c'est bloqué | Contournement plugin | Lot |
|---|---|---|---|
| Tables `iris_signals` / `iris_proposals` / `iris_results` / `iris_learning` | aucune API de persistance Iris côté serveur | fichiers `./rapido-kb/iris/` (journal, calendrier, apprentissage) — mono-poste, non partagé entre appareils | L2-L5 |
| `establishment_brand_map` serveur | pas d'outil de mapping côté FoodEatUp | `./rapido-kb/iris/marque.md` + resynchro à chaque session | **L1** |
| Écrans FoodEatUp (calendrier, fiche, journal, performance, paramétrage) | UI produit, hors périmètre plugin | restitution conversationnelle des mêmes vues | L4 |
| Recalcul automatique chaque matin | un plugin ne s'exécute pas seul | routine/planification côté utilisateur (Claude Code Routines) ou demande explicite « le calendrier d'Iris » | L4 |
| Quota de crédits serveur (blocage avant dépassement) | pas d'API de solde exposée dans les listes live | annonce du coût + `cout_confirme` obligatoire (garde) ; blocage dur côté produit | L6 |
| Opt-in RGPD horodaté par segment | `list_clients` / `list_rfm_segments` n'exposent pas de champ opt-in vérifié | AVANT toute campagne personnelle : demander à l'utilisateur de confirmer que le segment est opt-in ; jamais d'envoi automatique | L6 |
| Attribution certaine (code promo / lien tracké) | pas de génération de codes promo ni de liens trackés côté MCP | corrélation commandes 48 h vs moyenne, présentée comme corrélation | L5 |

## 3. Les photos de plats — le vrai point d'attention

La vidéo « virale » ne vaut que si la matière première est vraie :

1. **Sources réelles** : assets de marque RapidoCMS (`list_all_files` →
   `file_url` publiques) ou photo fournie par le restaurateur (smartphone),
   hébergée via `upload_file_tool` puis importée côté Higgsfield
   (`media_import_url`).
2. **`list_dishes` n'expose pas d'URL de photo exploitable** dans
   l'introspection actuelle → le stock de photos vit côté CMS, pas côté
   FoodEatUp. L'appairage (skill `appairage-marque-iris`) inventorie ce stock
   et liste les plats SANS photo.
3. **Règle d'honnêteté** : jamais de plat photoréaliste inventé présenté comme
   le vrai plat — vidéo d'ambiance ou typographique en repli.

## 4. Coûts (ordres de grandeur à valider contre la grille réelle)

- Visuel RapidoCMS : ~2 crédits (~0,04 €) ; avec assets (`images_to_image`) :
  ~3 crédits (CDC §9). Vidéo Higgsfield : voir la grille du dépôt
  (docs/GRILLE-COUTS-HIGGSFIELD.md) — une vidéo 6-10 s + reframe + éventuel
  upscale coûte plusieurs dizaines de crédits : c'est la raison du
  `cout_confirme` obligatoire et de la limite « une seule régénération après
  `virality_predictor` ».

## 5. Critères d'acceptation du CDC — état plugin

| Critère | État |
|---|---|
| Surstock DLC 3 jours → proposition | ✅ moteur (à la demande ou via routine) |
| Raison en une phrase sur chaque proposition | ✅ + hook Stop qui bloque sans raison |
| Dédup deux signaux même plat | ✅ règle du moteur |
| Aucune publication sans validation humaine | ✅ garde-iris (ask, non contournable par le modèle) |
| Visuel hors charte régénéré, jamais proposé | ✅ gate charte, 2 tentatives max |
| Avis négatif → alerte, zéro contenu | ✅ règle absolue du moteur |
| Motif de refus obligatoire et appris | ✅ calendrier + apprentissage.md |
| Recalcul chaque matin | ⚠️ via routine utilisateur (pas d'exécution autonome d'un plugin) |
| Génération décrémente les crédits | ⚠️ annonce + confirmation ; décompte serveur = backlog L6 |
| Campagne sans opt-in bloquée | ⚠️ confirmation humaine exigée ; vérification serveur = backlog L6 |
| Publications reliées aux commandes | ✅ en corrélation 48 h (attribution certaine = backlog L5) |
| Sujet < 14 jours déclassé | ✅ journal-signaux.md |
