---
name: generation-article-blog
description: Utiliser quand l'utilisateur veut écrire un article de blog, un article SEO, un contenu long pour son site, un brief d'article, réécrire/optimiser un article existant, ou dit « écris-moi un article sur… », « génère un article de blog », « optimise cet article ». Produit un article complet (plan → rédaction → score qualité → visuel → publication → relais social) optimisé Google (E-E-A-T) et citations IA (GEO/AEO), dans le ton de la KB.
source: AgriciDaniel/claude-blog (commit 49842ea9), MIT — skill d'origine « blog » renommé, SKILL.md réécrit en français et câblé sur les MCP Rapido ; references/ et templates/ non modifiés
license: MIT
---

# Génération d'article de blog (moteur E-E-A-T / GEO)

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.
2. KB (`./rapido-kb/` si présente — elle PRIME) : `ton-et-accroches.md`
   (ton, vocabulaire, interdits), `cibles-personas.md` (pour qui on écrit),
   `propositions-valeur.md` (arguments), `concurrents.md` (angles à
   différencier), `charte-graphique.md` (visuel de couverture).
3. Annexes du skill, à charger À LA DEMANDE selon l'étape (jamais toutes) :
   `references/content-rules.md` (règles de rédaction),
   `references/editorial-heuristics.md` et `references/ai-slop-detection.md`
   (anti-texte-robotique), `references/eeat-signals.md` (crédibilité),
   `references/geo-optimization.md` (citations IA),
   `references/quality-scoring.md` (grille 100 points),
   `references/internal-linking.md`, `references/schema-stack.md` (balisage),
   `references/platform-guides.md` (plateforme de publication).

## Templates disponibles (`templates/`)

how-to-guide · listicle · comparison · case-study · pillar-page · faq-knowledge ·
data-research · product-review · news-analysis · roundup — choisir selon
l'intention de recherche, jamais par défaut.

## Workflow

1. **Cadrage (brief)** — sujet, persona visé (KB), intention de recherche,
   mot-clé principal, template, objectif mesurable (trafic ? leads ? — en cas
   de doute, invoquer l'agent `responsable-marketing`). Longueur cible selon
   le template. Pas de brief validé = pas de rédaction.
2. **Recherche & faits** — collecter les faits via la recherche web et les
   données MCP (ex. vrais chiffres du CRM/CMS du client si l'article parle de
   son activité). RÈGLE ANTI-DONNÉE-INVENTÉE : toute statistique citée a une
   source vérifiable datée ; une donnée introuvable est omise ou marquée
   `### À COMPLÉTER` — jamais estimée. Charger `references/research-quality.md`.
3. **Plan (outline)** — H1 unique, H2/H3 alignés sur l'intention, réponse
   directe en tête (featured snippet / citations IA), FAQ si pertinent.
   Valider le plan avec l'utilisateur AVANT de rédiger.
4. **Rédaction** — suivre le template choisi + `content-rules.md` +
   `ai-slop-detection.md`. Le TON vient de la KB (`ton-et-accroches.md`),
   pas des références génériques. Français par défaut. E-E-A-T : auteur réel,
   expérience concrète, exemples du client.
5. **Score qualité** — auditer l'article avec la grille de
   `references/quality-scoring.md` (5 catégories, 100 points). < 80/100 :
   itérer sur les catégories faibles avant de livrer. Annoncer le score.
6. **Visuel de couverture** — `generate_image` (rapidocms) avec un prompt
   conforme au skill `prompts-visuels-pro` et à la charte (KB) — ou déléguer
   à l'agent `directeur-artistique`. Jamais de texte incrusté généré.
   `upload_file_tool` pour les médias fournis par l'utilisateur.
7. **Publication** — selon l'endroit où vit le blog du client :
   - **Site construit avec Lovable** : déléguer au plugin `rapido-lovable`
     (le serveur lovable n'est pas déclaré par ce plugin) — repérer le projet
     du client puis demander à l'agent Lovable d'ajouter l'article au blog ;
     CONFIRMATION avant tout déploiement public ;
   - **Autre CMS (WordPress, Next.js, Hugo…)** : livrer le markdown complet
     + le balisage de `references/schema-stack.md`, avec les instructions de
     `references/platform-guides.md` — le client publie ;
   - Aucun canal de publication disponible : livrer l'article en markdown
     dans la conversation (dégradation propre, le travail n'est jamais perdu).
8. **Relais social** — décliner l'article en posts via le skill
   `pipeline-contenu-social` : `create_draft_tool` (brouillons LinkedIn /
   Facebook / Instagram, comptes via `list_connected_accounts`), programmation
   `schedule_draft_tool` UNIQUEMENT après validation (garde-fou publication).
   Renvoi : `calendrier-editorial` pour la planification récurrente.
9. **Mesure** — au cycle suivant, `analyse-performance-contenu` (insights
   RapidoCMS) + retours de trafic pour ajuster les prochains sujets ;
   consigner les accroches gagnantes dans la KB (`mise-a-jour-kb`).

## Règles métier

- **Un article = un objectif + un mot-clé + une intention.** Deux sujets =
  deux articles.
- La KB PRIME sur toutes les références génériques du skill (qui sont des
  standards du secteur, en anglais, signalés comme tels).
- Jamais de publication publique ni de programmation sociale sans validation
  explicite de l'utilisateur.
- Concurrence : vérifier `concurrents.md` avant de choisir l'angle — ne pas
  écrire l'article que tout le monde a déjà écrit (charger
  `references/google-landscape-2026.md` pour le contexte SERP).
- Multilingue / réécriture / audit approfondi : le dépôt source
  (AgriciDaniel/claude-blog) contient des skills spécialisés non importés à
  ce jour (réécriture, multilingue, audit, images) — le signaler plutôt que
  d'improviser.

## Pièges

- `create_draft_tool` exige TOUS les champs (media_type/media_url vides pour
  un brouillon texte) et un `account_id` réel issu de `list_connected_accounts`.
- La publication via l'agent Lovable consomme les crédits du workspace du
  client — un message détaillé vaut dix itérations ; vérifier les crédits
  restants avant un gros chantier (voir plugin `rapido-lovable`).
- Les références de ce skill sont datées (paysage Google/IA de fin 2025-2026) :
  croiser avec une recherche web récente pour tout ce qui est volatil.
