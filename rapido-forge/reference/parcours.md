# Parcours StartupsForge — carte de référence

Trois parcours, un journal commun : `./rapido-kb/startup/forge/parcours.md`
(exercice, date, verdict, prochain rendez-vous — tenu par les agents).
Livrables : `./rapido-kb/startup/forge/<parcours>/<skill>.md`.

Règle de routage (agent `directeur-programme`) :
- stade **idée** → bootcamp 5 jours (`mentor-bootcamp`)
- stade **pré-lancement** → roadmap idéation (`mentor-ideation`)
- stade **lancé, premiers revenus** → roadmap scale (`mentor-scale`)

---

## 1. Bootcamp 5 jours (46 skills `bootcamp-*`)

Un exercice à la fois, timeboxé, livrable exigé avant le suivant.

**Jour 1 — Marché**
qualitative-study → quantitative-study → market-segmentation →
market-sizing-b5 → trend-analysis → stakeholder-mapping

**Jour 2 — Problème & concurrence**
problem-validation → pain-mapping → persona-deep → pestel-analysis →
porter-forces → competitive-deep → feature-benchmark → positioning-map →
competitive-advantage

**Jour 3 — Vision & modèle**
vision-mission → uvp-builder → bmc-complete → revenue-model-b5 →
growth-strategy → okr-kpi-setup

**Jour 4 — Marque & contenu**
naming-tagline → brand-platform → brand-storytelling → tone-of-voice →
visual-identity → content-strategy-b5 → editorial-calendar →
social-media-strategy → email-setup → conversion-funnel

**Jour 5 — Finance, juridique & lancement**
financial-projections → cash-flow-plan → launch-budget → funding-strategy →
legal-status → legal-documents → ip-protection → certification-b5 →
pitch-deck-b5 → pitch-script-b5 → investor-faq → press-release-b5 →
landing-copy-b5 → mvp-wireframes → launch-plan

Après le J5 : bilan, puis passage à la roadmap idéation ou au
`coach-startup` (rapido-startup) pour un dossier bancable.

---

## 2. Roadmap idéation (72 skills `ideation-*`) — 6 phases

**Phase 1 — Valider**
business-model-canvas, lean-canvas, persona-maker, competitive-analysis,
swot, value-proposition, usp-statement, feedback-analysis

**Phase 2 — Structurer**
naming-generator, legal-structure, legal-docs, financial-forecast,
cash-flow, advisory-board, north-star-metric, kpi-dashboard, certification

**Phase 3 — Construire**
specs-generator, mvp-wireframes, lovable-prompt, ui-guidelines,
sitemap-generator, roadmap-product, iteration-planning, qa-checklist,
changelog-setup, gamification

**Phase 4 — Présence**
landing-page, landing-copy, pricing-page, about-page, contact-form,
hero-image, logo-prompt, color-palette, seo-meta, analytics-setup,
export-pdf

**Phase 5 — Lancer**
launch-checklist, launch-plan, pre-launch-campaign, product-hunt-strategy,
ph-page-copy, hunter-outreach, launch-post, press-release, pitch-deck,
pitch-script, investor-faq, demo-script, lessons-learned

**Phase 6 — Premiers moteurs**
cold-email, email-sequence, email-marketing-setup, lead-magnet,
referral-program, first-ad-campaign, paid-acquisition, retargeting-setup,
blog-outline, linkedin-posts, social-strategy, video-script, avatar-video,
voiceover, video-edit, course-outline, quiz-generator, testimonial-request,
growth-experiments, automation-workflow, webhook-setup, legal-docs

---

## 3. Roadmap scale (62 skills `scale-*`) — 6 chantiers

Le chantier prioritaire découle des KPI réels (`catalogue-kpi`), pas de
l'envie du moment.

**Mesurer** : funnel-aarrr, north-star-metric, kpi-dashboard,
google-analytics-4, google-search-console, google-trends, heatmaps,
nps-survey, user-tests, ab-testing, semrush-audit

**Vendre** : sales-call-script, spin-selling, soncas, bant-qualification,
objections-playbook, commercial-proposal, negotiation-batna,
upsell-crosssell, customer-success, customer-journey

**Acquérir** : cold-email-prospection, meta-ads-campaign, meta-pixel,
google-ads-setup, linkedin-ads-b2b, linkedin-pixel, tiktok-ads-creator,
tiktok-pixel, seo-meta, content-pillar, influencer-marketing,
community-building, referral-program, pr-media-kit

**Prioriser** : rice-prioritization, impact-effort, eisenhower-matrix,
user-story-mapping, okrs-q1, public-roadmap, scenarios-planning,
wireframes, prototype, design-system

**Financer** : unit-economics, burn-rate, break-even,
financial-projections, cost-waterfall, cap-table, fundraising-plan,
pricing-strategy

**Positionner** : jtbd, blue-ocean, ansoff-matrix, bcg-matrix,
golden-circle, marketing-4p, marketing-4c, adoption-curve, porter-5-forces

---

## Passerelles vers l'exécution réelle

Les skills forge PRÉPARENT ; les plugins métier EXÉCUTENT (renvois « Voir
aussi » dans chaque skill) :

| Besoin | Plugin d'exécution |
|---|---|
| Posts, articles, calendrier, vidéos | rapidocms |
| Cold email, pipeline, sondages, négo | rapidocrm |
| Landing, site, agent IA produit | rapido-lovable |
| Ads Meta, pixel, A/B, audiences | rapido-meta-ads (argent réel — PAUSED puis accord) |
| Workflows récurrents | rapido-n8n |
| Visuels, menus, decks | rapido-canva |
| KPI, prévisionnel, business plan, Loop Engine | rapido-startup |
| Projets, tâches, recrutement | rapidorh |

Plateformes SANS MCP (Google Ads, TikTok, LinkedIn Ads, Semrush, GA4…) :
préparer plan et assets, l'utilisateur exécute dans l'outil — le dire
explicitement.

---

## Catalogue & recherche

- **`reference/catalogue.json`** — l'index machine-readable des 180
  exercices : `{name, parcours, jour?, description, tags, niveau,
  prerequis, voir_aussi, livrable_path}`. Généré et validé (graphe de
  prérequis sans cycle) par `scripts/forge_catalogue.py` à la racine du
  dépôt — rejoué en CI.
- **Recherche** :
  `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/forge_recherche.py" "<besoin>"`
  (filtres `--tags`, `--niveau`, `--parcours` ; hors-ligne, TF-IDF stdlib ;
  `--embeddings` optionnel avec repli silencieux). Skill dédié :
  `selecteur-framework`.
- **Convention du journal** — pour que le script détecte les exercices
  faits, chaque exercice terminé s'inscrit dans
  `./rapido-kb/startup/forge/parcours.md` sur UNE ligne :
  `- [x] <skill> — <date> — <verdict>`
  (ex. `- [x] bootcamp-persona-deep — 2026-07-10 — persona validé,
  2 interviews à refaire`). Les agents tiennent ce journal ; les prérequis
  cochés ne sont plus signalés comme manquants.
