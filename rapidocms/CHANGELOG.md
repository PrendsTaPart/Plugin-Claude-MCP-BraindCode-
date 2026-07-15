# Changelog — plugin rapidocms

## 1.7.0 — 2026-07-14

- Nouveau skill `coherence-personnage` : cohérence visuelle d'un personnage
  récurrent (mascotte, avatar, personnage anime) via un registre de portraits
  canoniques `./rapido-kb/personnages.json` (côté client) + génération TOUJOURS
  guidée par 1-3 portraits en référence à `images_to_image`. Interdit de
  générer un personnage récurrent sans référence (dérive). Versionnage du canon
  (vN, ancien conservé), critique vs canon + boucle corrective (max 2, comme
  studio-visuel-marque).
- Exemple annoté `reference/personnages.exemple.json` (le vrai registre reste
  dans la KB client, jamais dans le dépôt).
- tests/evals.md : 3 scénarios (création canon, nouvelle scène, boucle
  corrective).

## 1.6.0 — 2026-07-14

- Nouveau skill `studio-visuel-marque` (vitrine) : génère des visuels qui
  intègrent le VRAI logo et les VRAIS assets de la marque via
  `images_to_image` — résolution marque (`get_brand`), sélection minimale de
  références (logo + 1-2 assets, ≤3, <5 Mo, URL publique), prompt décrivant
  le rôle de chaque image (délégué à prompt-engineering-visuel /
  prompts-visuels-pro), critique PASS/FAIL vs charte, boucle corrective
  chirurgicale (max 2 itérations), capitalisation (upload/add_asset/add_prompt)
  et brouillon via pipeline-contenu-social — jamais de publication directe.
- Routage encodé : références → images_to_image ; aucune → generate_image ;
  Canva cité → plugin rapido-canva.
- tests/evals.md : 4 scénarios (dont boucle corrective + 2 de routage).

## 1.5.0 — 2026-07-14

- Nouveau skill `bibliotheque-assets` : import (URL publique, nommage imposé
  `{marque}-{type}-{variante}-vN`), inventaire, rattachement/détachement des
  assets à la bonne marque, et **audit de complétude** par script. Fondé sur
  une vérification live des outils (upload sans id → `list_all_files` pour
  résoudre l'`asset_id` ; `remove_asset` prend l'id du LIEN, pas du fichier).
- Nouveau `reference/outils-marque.md` : contrat live du cluster marque &
  assets (get_brand renvoie un tableau + `assets[]`, create_brand renvoie
  l'`id`, pas de validation hex serveur, `search` de list_all_files ne filtre
  pas, aucun outil de suppression de fichier).
- Nouveau `scripts/audit_assets.py` (stdlib) : compare la checklist canonique
  des 9 types d'assets aux assets rattachés, sort manquants / non conformes /
  plan d'import — l'écart n'est jamais calculé de tête.
- tests/evals.md : 3 scénarios bibliotheque-assets (import→rattachement,
  audit complétude, détachement) + frontière vs gestion-marques.

## 1.4.1 — 2026-07-11

- Vestige d'import retiré : la ligne « see CONNECTORS.md » (lien mort,
  le fichier n'a jamais été porté) supprimée de brand-review et email-sequence.
- generation-article-blog : nettoyage de la chaîne d'import —
  blog-delivery-contract.md et cognitive-load.md retirés (ils imposaient
  6 scripts et un agent blog-reviewer jamais portés dans ce dépôt),
  ai-slop-detection.md corrigé (revue à la lecture, pas par script),
  note d'attribution du SKILL.md mise à jour.

## 1.4.0 — 2026-07-10

- Réconciliation de la branche parallèle `claude/rapidocms-gestion-marques`
  (implémentation concurrente du cluster marques, non mergée) avec la
  version de main :
  - skill `gestion-marques` enrichi (corps de la branche adopté) : note
    « schéma vivant » (ré-introspection avant écriture), mapping
    typographique vers l'enum web-safe expliqué à l'utilisateur,
    `delete_brand` = nom exact retapé, convention de nommage des assets
    `"<Marque> — <type> — <variante>"`, flux « ajouter un logo » complet ;
  - **nouvel agent `gestionnaire-marques`** : gardien de la cohérence
    multi-enseignes — refuse tout contenu sans marque cible identifiée,
    checklist couleurs/police/logo/ton avant publication, propose la
    création de la marque manquante ; complémentaire du
    directeur-artistique ;
  - multi-marques câblé dans contenu-conforme-marque, video-marketing et
    prompts-visuels-pro (logos = ASSETS de marque, plus de repo GitHub) ;
  - portabilité : les noms d'enseignes clientes codés en dur dans la
    branche ont été remplacés par le renvoi à `./rapido-kb/entreprise.md`
    + `get_brand` (dépôt produit, aucune donnée client) ;
  - tests/test-routage.md : 6 cas cluster marques + 3 contre-exemples.

## 1.3.0 — 2026-07-10 (vague post-audit — consolidé)

- Nouveau skill `gestion-marques` (multi-marques, schémas vérifiés
  serveur) : get_brand d'abord (anti-doublon), `create_brand` (requis
  nom/langue/slogan ; couleurs hex séparées par virgules ; font_family =
  enum web-safe ; logo URL publique), `edit_brand` (brand_id + champs qui
  changent, avant/après confirmé), `delete_brand` (irréversible, hook
  garde-destructif + confirmation). Frontière : les assets et l'application
  de la charte restent dans contenu-conforme-marque.
- Éditions unitaires câblées (fin des orphelins CMS — 43/43 outils cités) :
  `edit_draft_tool` (pipeline-contenu-social — corriger avant planifier),
  `edit_campagne` (orchestration-campagne), `edit_digital_card`
  (carte-digitale), `list_all_files` (contenu-conforme-marque —
  bibliothèque média anti-doublon).
- pipeline-contenu-social : convention post TEXTE (vérifiée par appel réel)
  inscrite dans le workflow.
- tests/evals.md : gestion-marques + non-régression (2 scénarios existants).

## 1.2.1 — 2026-07-10

- Correction documentaire (audit) : piège `create_draft_tool` — les champs
  `media_type`/`media_source`/`media_url`/`media_caption` sont REQUIS même
  en `post_type: "text"`. Convention VÉRIFIÉE PAR APPEL RÉEL (brouillon
  jetable créé puis supprimé le 2026-07-10) : `media_type: ""`,
  `media_url: ""`, `media_source: "biblio"`, `media_caption` = le texte du
  post ; `social_type` ∈ linkedin, facebook, instagram, tiktok.
- `delete_prompt` : couverture par le hook garde-destructif explicitée
  (attrapé par le motif `delete_.*` du matcher — testé stdin → ask, test
  figé dans scripts/tester-skills.py).

## 1.2.0 — 2026-07-10

- Skill `bibliotheque-prompts` : gestion centrale de la bibliothèque —
  list_prompts AVANT toute génération (un prompt gagnant proche sert de
  base), add_prompt PROPOSÉ à chaque visuel validé (titre normalisé
  « type — sujet — style », content = prompt complet négatifs inclus,
  placeholders généralisés), edit_prompt pour versionner, delete_prompt sur
  confirmation. Piège vérifié serveur : type ∈ text | visuel uniquement
  (pas de type vidéo — préfixe de titre « vidéo — »).
- Intégration : prompt-engineering-visuel et prompts-visuels-pro consultent
  la bibliothèque en Étape 0 et PROPOSENT la sauvegarde en étape finale
  (renvois croisés vers bibliotheque-prompts).
- `contenu-conforme-marque` : section Assets de marque — logos officiels
  (fond transparent) uploadés (upload_file_tool type image) puis rattachés
  via add_asset (brand_id de get_brand), référencés dans toute génération ;
  remove_asset sur confirmation (matcher du hook garde-destructif étendu) ;
  note pipeline vidéo (kit « Mika ») : les logos viennent désormais des
  assets de marque CMS, plus du repo GitHub.
- tests/evals.md : scénarios de déclenchement et de comportement.

## 1.1.0 — 2026-07-09

- Skill `generation-article-blog` (importé de AgriciDaniel/claude-blog,
  commit `49842ea9`, MIT — skill `blog` renommé) : moteur d'articles de blog
  E-E-A-T/GEO — brief, recherche sourcée, plan, rédaction au ton de la KB,
  grille qualité 100 points, visuel via `generate_image`, publication
  (Lovable `send_message` ou markdown livré), relais social via
  `pipeline-contenu-social`. SKILL.md réécrit en français et câblé MCP ;
  `references/` (21 annexes) et `templates/` (10 gabarits) non modifiés.
- Agent `responsable-marketing` : invoque `generation-article-blog` (valide
  le brief avant rédaction).

## 1.0.0 — 2026-07-06

- Première version publique.

## 0.8.0 — 2026-07-06

- Agent `prompt-designer` : ingénieur de prompts visuels — charte chargée
  avant tout prompt, positif 6 blocs + négatif jamais optionnel, protocole
  zéro faute sur le texte incrusté, capitalisation via `add_prompt`.
- Skill `prompts-visuels-pro` : bibliothèque de prompts négatifs (base
  commune + 5 types de visuel) et protocole zéro faute (texte exact entre
  guillemets, épellation validée, 5 mots max, 2 itérations puis post-prod).
- Skill `funnel-tofu-mofu-bofu` : stratégie de contenu par étape du funnel —
  répartition 60/30/10, frameworks AIDA/PAS/4U/BAB, CTA et KPI par étape,
  fausse urgence interdite (rareté vérifiable dans les MCP).
- Liens croisés : `prompt-engineering-visuel` renvoie vers
  `prompts-visuels-pro` (bloc 6) ; `directeur-artistique` et
  `community-manager` lisent `./rapido-kb/startup/` (01-vision, 02-persona,
  05-identite) avant toute production quand il existe.

## 0.7.0 — 2026-07-06

- Intégration de 6 skills externes (LICENSE dans chaque dossier, provenance
  dans ATTRIBUTIONS.md) :
  - anthropics/knowledge-work-plugins (Apache 2.0) :
    `content-creation-methodo` (renommé depuis content-creation),
    `email-sequence`, `brand-review` ;
  - wondelai/skills (MIT, contenu non modifié — skills basés sur des
    livres) : `storybrand-messaging`, `made-to-stick`, `contagious`.

## 0.6.0 — 2026-07-06

- Nouveau skill `video-marketing` (serveur HyperFrames by HeyGen ajouté au
  `.mcp.json`) : compose (designSource blockframe pop/promo, signal
  corporate ; itérations avec projectId) → get_project_status (polling au
  rythme retry_after_seconds, statut waiting = question de l'agent) → preview
  validée → render_video PAYANT (confirmation niveau 3 obligatoire) →
  get_render_status (videoId) → URL MP4 livrée → post CMS d'accompagnement.
- `prompt-engineering-visuel` : bibliothèque de prompts vivante —
  `list_prompts` consulté AVANT toute création, chaque prompt gagnant
  sauvegardé via `add_prompt` (placeholders [entre crochets], type visuel).

## 0.5.0 — 2026-07-06

- Utilisation de la base de connaissance `./rapido-kb/` : règle de chargement
  dans les directives ; `responsable-marketing`, `community-manager` et
  `directeur-artistique` puisent ton, accroches et charte dans la KB (avec
  citation de source) ; `prompt-engineering-visuel` : palette depuis
  rapido-kb/charte-graphique.md en priorité (get_brand en vérification) ;
  `calendrier-editorial` : piliers depuis ton-et-accroches.md et
  propositions-valeur.md.

## 0.4.0 — 2026-07-06

- Script de calcul `skills/analyse-performance-contenu/scripts/content_scores.py`
  (stdlib) : engagement par format/réseau/créneau, top/flop, tendance,
  signal_faible < 3 posts — le skill impose « utiliser le script pour tout
  calcul ; ne jamais calculer de tête ».
- `reference/pieges-outils.md` : tableau des pièges (account_id par réseau,
  media_source "biblio", formats Y-m-d/H-i-s, max 10 insights,
  ingishts_campagne, formats visuels par réseau…), référencé par les
  directives.

## 0.3.0 — 2026-07-06

- Hooks déterministes (`hooks/hooks.json` + `hooks/scripts/`) :
  - PreToolUse `garde-destructif` : confirmation forcée (ask) sur `delete_*`,
    `cancel_schedules_post` et `remove_post_campagne` ;
  - Stop `récap-actions` (hook prompt) : bloque la fin de tour si des écritures
    MCP ont eu lieu sans récapitulatif des IDs dans la réponse.

## 0.2.0 — 2026-07-06

- Ajout de la couche métier :
  - Agents : `responsable-marketing` (objectif avant production, calendrier
    éditorial, boucle publier → mesurer → ajuster), `community-manager`
    (adaptation native par réseau, créneaux de publication) et
    `directeur-artistique` (charte avant création, checklist contraste/
    lisibilité/hiérarchie, formats par réseau, refus des visuels hors charte).
  - Skills d'expertise : `prompt-engineering-visuel` (structure de prompt en
    6 blocs, variantes, critique vs charte, itération),
    `calendrier-editorial` (piliers, répartition par réseau, formats variés,
    rattachement campagne) et `analyse-performance-contenu` (patterns gagnants,
    3 recommandations actionnables).
- Les agents connaissent et invoquent les skills du plugin au bon moment.

## 0.1.0 — 2026-07-06

- Version initiale : `.mcp.json` (serveur rapidocms), références
  `directives-outils.md` et `charte-graphique.md`, skills workflow
  `pipeline-contenu-social`, `orchestration-campagne`, `carte-digitale`,
  `contenu-conforme-marque`.
