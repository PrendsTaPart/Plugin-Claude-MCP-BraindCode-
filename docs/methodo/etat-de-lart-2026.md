# État de l'art marché 2025-2026 — compléments aux fiches méthodo

> Recherche web, chaque affirmation **sourcée (URL) et datée**. Les chiffres
> issus d'éditeurs/blogs (non primaires) sont marqués **INCERTAIN**. Accès :
> 2026-07. À croiser avec `docs/MATRICE-COUVERTURE.md` (M0) pour l'applicabilité
> MCP, et les fiches `docs/methodo/100m-leads/` (M1).

---

## 1. HubSpot — lifecycle & lead scoring IA

**Pratiques 2025-2026.** Le nouveau *Lead Scoring* HubSpot modélise séparément
le **Fit** (qui est le contact) et l'**Engagement** (ce qu'il fait), score
contacts/entreprises/deals, et ajoute délais, *decay*, seuils et **scoring
assisté par IA** ; le *predictive scoring* (Breeze AI) analyse l'historique de
conversion mais reste **réservé au palier Enterprise** et nécessite ~6 mois de
données.
- Sources : [knowledge.hubspot.com — Build lead scores with AI](https://knowledge.hubspot.com/scoring/build-lead-scores-with-ai) (doc éditeur, 2025) ; [xcellimark — HubSpot Lead Scoring 2025 Update](https://www.xcellimark.com/blog/how-to-build-lead-scoring-in-hubspot-2025-update) (2025) ; [yourhubspotexpert — 2025 Update](https://yourhubspotexpert.com/hubspot-lead-scoring-2025-update-what-you-need-to-know-and-how-to-prepare/) (2025).
- **Vs M1** : complète un **manque** — aucune fiche M1 ni skill ne fait de lead
  scoring (M0 = MANQUANT). Le modèle Fit×Engagement est un patron réutilisable.
- **MCP Rapido** : pas d'outil de score natif dans RapidoCRM (M0 → à demander au
  backend Tunis). Un score **règles** est faisable à partir de
  `get_interaction_stats` + `get_historique_prospect`. Seuil déclencheur → n8n.

## 2. Salesforce — RevOps

**Pratiques 2025-2026.** RevOps = aligner ventes + marketing + CS + finance
autour d'une **source unique de vérité (SSoT)**, KPI partagés, process
standardisés ; Salesforce pousse *Agentforce Revenue Management* pour unifier
devis/contrats/facturation/forecast.
- Sources : [salesforce.com — What is RevOps](https://www.salesforce.com/sales/revenue-lifecycle-management/what-is-revenue-operations/) (éditeur, 2025) ; [salesforce.com — RevOps best practices](https://www.salesforce.com/sales/revenue-lifecycle-management/revops-best-practices/) (2025).
- Chiffre **INCERTAIN** : « +36 % de croissance de revenus » pour les entreprises
  avec fonction RevOps (Qwilr 2026, cité par [salesmotion.io](https://salesmotion.io/blog/revops-best-practices)) — recherche éditeur, non vérifiable indépendamment.
- **Vs M1** : complète un **manque** (RevOps = MANQUANT en M0). Le principe SSoT
  rejoint notre `./rapido-kb/` + lecture multi-MCP.
- **MCP Rapido** : pas de hub revenu unifié ; agrégation partielle possible via
  `get_revenue_summary` + `get_stats_pipeline` + insights ads.

## 3. Clay & Apollo — enrichissement waterfall & signaux d'intention

**Pratiques 2025-2026.** L'**enrichissement waterfall** empile plusieurs
fournisseurs en cascade (Clay interroge 100+ sources jusqu'à trouver la donnée) ;
Apollo fait de même sur ses sources. L'**outbound par signaux d'intention**
(changement de poste, visites site, actualités entreprise) déclenche le contact
au bon moment. Patron hybride répandu : **Apollo source → Clay enrichit/score →
séquenceur exécute**.
- Sources : [clay.com — Clay + Apollo](https://www.clay.com/blog/clay-apollo) (éditeur, 2025) ; [devcommx — Waterfall enrichment](https://www.devcommx.com/blogs/waterfall-enrichment-clay-vs-zoominfo-vs-apollo) (2025) ; [factors.ai — Clay vs Apollo](https://www.factors.ai/blog/clay-vs-apollo-for-outbound) (2026).
- Chiffres **INCERTAIN** : « ~5 % d'emails en plus, ~7 % de téléphones, 45 % de
  bounces en moins » (revendication éditeur, non primaire).
- **Vs M1** : **nuance** la fiche `06-aca` et `03-regle-des-100` — Hormozi mise
  sur le **volume** ; le marché 2025-2026 mise sur le **signal + l'enrichissement**
  (moins de volume, meilleur ciblage). Les deux se combinent : signal pour cibler,
  volume pour tenir la règle des 100.
- **MCP Rapido** : `prospecter_maps`/`prospecter_entreprise` +
  `rechercher_entreprise_siret` = enrichissement **basique** ; pas de waterfall
  ni de signaux d'intention (M0 → backend).

## 4. Délivrabilité cold email — Lemlist / Instantly

**Pratiques 2025-2026.**
- **Warmup** : démarrer un domaine neuf à **5-10 emails/jour**, monter sur
  **4-6 semaines** ; les comptes qui envoient **20-50/boîte/jour** puis montent
  ont les meilleurs résultats.
- **Plafonds par boîte** : ~**500/jour Gmail**, ~**300/jour Outlook** — au-delà,
  **rotation de boîtes/domaines** (répartir l'envoi sur plusieurs boîtes chauffées).
- **Taux de réponse de référence** : moyenne ~**3,4 %**, top 10 % **≥ 10,7 %**,
  fourchette « industrie » **3-8 %**. Cible de **placement en boîte de réception
  ≥ 85 %**.
- Sources : [instantly.ai — 90%+ deliverability](https://instantly.ai/blog/how-to-achieve-90-cold-email-deliverability-in-2025/) (éditeur, 2025) ; [mailpool.ai — 1M cold emails 2025](https://www.mailpool.ai/blog/deliverability-lessons-from-1-million-cold-emails-sent-in-2025) (2025) ; [lemlist — Email warmup](https://www.lemlist.com/blog/warm-up-email-account) (éditeur, 2025).
- **INCERTAIN** : les plafonds exacts et les taux de réponse **varient fortement**
  selon secteur/liste/offre — à traiter comme **directionnels**, jamais comme des
  garanties (les éditeurs sont juge et partie).
- **Vs M1** : **complète et corrige** — l'anti-trou de `INDEX.md` signalait déjà
  l'absence de déliverabilité chez Hormozi (SPF/DKIM/DMARC). Ces plafonds
  **bornent** la « règle des 100 » en email : 100 envois/jour se répartissent sur
  plusieurs boîtes chauffées, pas une seule.
- **MCP Rapido** : `schedule_email`/`send_newsletter` **n'incluent pas** de
  warmup, rotation de domaines ni mesure de placement (M0 → backend, ou outil
  externe type Instantly/Lemlist). **Honnêteté** : ne pas promettre un envoi
  froid à volume via le seul CRM sans infra de délivrabilité.

## 5. ActiveCampaign / GoHighLevel — automatisation & nurturing

**Pratiques 2025-2026.**
- **GoHighLevel** : multicanal (email + SMS + voicemail drop + chatbot + notif) ;
  patrons phares : **réponse instantanée < 60 s** à un lead, **rappel après appel
  manqué** (~15 s), **séquence de nurture 14 jours**, série de rappels de RDV,
  demande d'avis post-visite.
- **ActiveCampaign** : logique **if/else imbriquée jusqu'à 6 niveaux**, **goal
  tracking** (sortie automatique de la séquence quand l'objectif est atteint),
  scoring par points (ouvertures/clics/visites/tags).
- Sources : [grow-highlevel.com — Nurturing workflows](https://grow-highlevel.com/post/gohighlevel-lead-nurturing-automation-workflows) (2026) ; [clixoai — AC vs GHL](https://clixoai.com/blog/activecampaign-vs-gohighlevel) (2025) ; [autoesta — GHL workflows](https://autoesta.com/gohighlevel-workflows-vs-triggers-vs-campaigns/) (2025).
- **Vs M1** : renforce la règle Hormozi « **la vitesse gagne** » (`SKILL.md`
  source) avec un chiffre opérationnel (**< 60 s**). La séquence 14 j = patron
  concret de nurture (absent des fiches M1).
- **MCP Rapido** : réalisable via **n8n** (`usine-automatisations`) + RapidoCRM
  `schedule_email`/`send_sms` + notifications FoodEatUp ; le « speed-to-lead » se
  câble en **webhook n8n** sur soumission de formulaire (`get_formulaire_soumissions`).

## 6. n8n / Zapier / Make — patrons d'orchestration

**Pratiques 2025-2026.** n8n = graphe de nœuds, webhooks first-class, files,
**retries**, nœuds *code* ; **70+ nœuds IA** + LangChain pour l'orchestration
d'agents. Bonnes pratiques : **idempotence** (writes rejouables sans doublon),
**retries avec jitter**, **dead-letter** pour revue manuelle, **circuit
breakers**, nommage/versioning, revue mensuelle.
- Sources : [hatchworks — n8n vs Zapier](https://hatchworks.com/blog/ai-agents/n8n-vs-zapier/) (2026) ; [zapier.com — n8n vs Zapier](https://zapier.com/blog/n8n-vs-zapier/) (éditeur, 2026) ; [infralovers — n8n self-hosted](https://www.infralovers.com/blog/2025-05-09-n8n-workflow-automation/) (2025-05-09).
- **Vs M1** : hors périmètre des fiches leads, mais **valide** notre agent
  `rapido-n8n:architecte-automatisations` et ajoute des garde-fous concrets
  (idempotence, dead-letter) à intégrer aux recettes n8n.
- **MCP Rapido** : **n8n MCP en direct** (déjà utilisé pour la sentinelle R7).
  Directement applicable — ces patrons devraient enrichir `recettes-metier`.

## 7. Anthropic / OpenAI — ingénierie d'agents

**Pratiques 2024-2026 (source PRIMAIRE).** Anthropic décrit **6 patrons** :
*prompt chaining, routing, parallelization, orchestrator-workers,
evaluator-optimizer, autonomous agents*. Principe cœur : **« commencer simple,
n'ajouter de la complexité que si elle améliore démontrablement les
résultats »** ; commencer par un appel LLM optimisé avant tout système
multi-agents. L'orchestrateur-workers (workers isolés, coordination via le
superviseur) est le patron de la recherche Claude.
- Source **primaire** : [anthropic.com — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) (**2024-12-19**).
- Chiffre **INCERTAIN** : « +90,2 % vs agent unique » sur un eval interne
  Anthropic (cité par des tiers, non re-vérifiable).
- **Vs M1** : **méta** — valide notre propre architecture (skills = routing,
  agents = orchestrator/evaluator, hooks = vérification déterministe, Loop Engine
  = Sense→Plan→Act→Feed→Report). Le duo `directeur-artistique` (exécute) +
  `gardien-de-marque` (évalue) = patron **evaluator-optimizer**.
- **MCP Rapido** : sans objet (guide d'architecture, pas d'outil).

## 8. GEO — Generative Engine Optimization

**Pratiques 2025-2026.** Être **cité** par les moteurs génératifs (AI Overviews,
ChatGPT, Perplexity, Copilot) : **réponse directe en 40-60 premiers mots**,
**densité de faits** (une stat toutes les ~150-200 mots), citer des sources
autoritaires, **schema markup**, **ancres `id`** sur chaque bloc pour des
citations précises, **fraîcheur** (mise à jour récente favorisée), **supprimer
les tournures subjectives** (« je pense ») qui augmentent la perplexité. Nuances
par moteur : ChatGPT = encyclopédique, Perplexity = récence, AI Overviews =
contenu déjà bien classé.
- Sources : [seotuners — GEO 2025 playbook](https://seotuners.com/blog/seo/generative-engine-optimization-geo-in-2025-the-complete-playbook-to-win-ai-overviews-chatgpt-copilot-perplexity/) (2025) ; [frase.io — What is GEO](https://www.frase.io/blog/what-is-generative-engine-optimization-geo) (2026) ; [digitalapplied — GEO guide 2026](https://www.digitalapplied.com/blog/geo-guide-generative-engine-optimization-2026) (2026).
- Chiffres **INCERTAIN** : « contenu mis à jour < 30 j → 3,2× plus de citations
  IA » et « sessions référées par IA +527 % sur H1 2025 » (revendications
  éditeurs, non primaires).
- **Vs M1** : hors fiches leads, mais **complète** le skill
  `rapidocms:generation-article-blog` (qui a déjà E-E-A-T/GEO) avec des tactiques
  concrètes (réponse 40-60 mots, ancres, fraîcheur).
- **MCP Rapido** : contenu via `create_draft_tool`/`generation-article-blog` ;
  schema/ancres = niveau contenu, pas d'outil MCP dédié.

---

## Synthèse — ce que le marché ajoute à M1

| Thème | Apport principal vs M1 | Bloquant MCP (M0) |
|---|---|---|
| Lead scoring IA (HubSpot) | modèle Fit×Engagement + seuils | tool score (backend) |
| RevOps (Salesforce) | source unique de vérité, KPI partagés | hub unifié (backend) |
| Enrichissement/intent (Clay/Apollo) | signal-led > volume brut | waterfall + intent (backend) |
| Délivrabilité (Lemlist/Instantly) | warmup, plafonds, rotation, placement | warmup/rotation (backend/externe) |
| Nurturing (AC/GHL) | speed-to-lead < 60 s, séquence 14 j | n8n + CRM (dispo) |
| Orchestration (n8n) | idempotence, dead-letter, retries | n8n MCP (dispo) |
| Agents (Anthropic) | start simple ; orchestrator/evaluator | sans objet |
| GEO | réponse 40-60 mots, ancres, fraîcheur | contenu (dispo) |

> Tout point non étayé par une source solide est marqué **INCERTAIN** ci-dessus.
> Aucune donnée n'a été créée sans source.
