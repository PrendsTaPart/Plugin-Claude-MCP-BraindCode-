# Imports GitHub — préparation rapido-marketing (audit, STOP avant intégration)

> Import **intelligent** de 5 dépôts MIT, en français, **sans copie aveugle**.
> Chaque skill reçoit un verdict **ADAPTER / S'INSPIRER / IGNORER**, sa cible
> rapido-marketing (M4-M10), les outils MCP Rapido correspondants (croisés avec
> `docs/MATRICE-COUVERTURE.md`), et un contrôle anti-verbatim. **STOP** : à valider
> avant intégration aux prompts M5-M11. Licences : `docs/methodo/ops/NOTICE.md`.

## Dépôts (tous MIT © 2026)
| Clé | Dépôt | Détenteur | Nature |
|---|---|---|---|
| COLD | growthenginenowoslawski/coldoutboundskills | GrowthEngineX | 28 skills cold outbound (vraies API tierces) |
| GTM | kenny589/gtm-flywheel | ColdIQ | 15 skills GTM (outils tiers cités en EXEMPLE, pas d'API) |
| HORMOZI | alexsmedile/hormozi-skills | Alessandro Smedile | 18 skills offre + orchestrateur 5 sous-agents |
| AIMKT | zubair-trabzada/ai-marketing-claude | Zubair Trabzada | 15 skills market-* + 3 templates email |
| GEO | arturseo-geo/marketing-skill | The GEO Lab | **1 skill marketing généraliste** (voir ⚠️) |

## ⚠️ Écarts constatés vs l'énoncé de la mission (signalés, non inventés)
1. **Le dépôt « GEO » n'est PAS un skill GEO** (Generative Engine Optimization) :
   frontmatter `name: marketing`, zéro occurrence de « GEO »/« generative
   engine ». C'est un skill marketing généraliste mono-fichier. Notre
   `geo-optimization` (sourcé de l'état de l'art) reste supérieur.
2. **« 8 templates email »** (ai-marketing-claude) : il y a **3** fichiers de
   templates (`email-welcome`, `email-nurture`, `email-launch`). Le « 8 »
   correspond aux **8 emails de la séquence de lancement** (`email-launch`).
3. **`client-profile.yaml`** : existe bien, mais comme **sortie générée** du
   skill `icp-onboarding` (COLD), pas comme fichier statique. Correspondance en
   fin de document.

## Contrôle anti-verbatim (global)
**Aucun verbatim de livre** (pas de prose narrative recopiée). En revanche,
usage de **termes/marques déposés** à reformuler pour un plugin commercial :
« Grand Slam Offer », « Value Equation », « $100M Offers », « StoryBrand », et le
nom **« Hormozi »** (HORMOZI, GEO). Nos fiches françaises **reformulent** ces
concepts sous une terminologie neutre et **créditent** la source (en-tête +
NOTICE). Aucun bloc copié.

---

## Inventaire & verdicts

Verdict : **ADAPTER** (fiche FR créée) · **S'INSPIRER** (idée notée, déjà couvert
chez nous) · **IGNORER** (lié à un outil tiers hors scope, ou doublon).

### COLD — cold outbound
| Skill | Verdict | Cible rapido-marketing | MCP Rapido / note |
|---|---|---|---|
| icp-onboarding | **ADAPTER** | `icp-generator` (M5) | `prospecter_*` ; profil → `rapido-kb/marketing/icp.md` (voir corresp.) |
| campaign-strategy, campaign-copywriting | **ADAPTER** | `machine-outbound` (M9) | `redaction-commerciale`, `schedule_email` |
| cold-email-weekly-rhythm | **ADAPTER** | `machine-outbound` (M9) | cadence J0/J3/J7/J14 |
| email-deliverability-audit, deliverability-incident-response, spam-word-checker, smartlead-inbox-manager (warmup) | **ADAPTER** | **nouveau `delivrabilite-email`** | pas d'outil Rapido de warmup → **MCP manquant** (infra email) |
| list-quality-scorecard, positive-reply-scoring | **S'INSPIRER** | `lead-scoring` | scoring déjà couvert |
| lead-magnet-brainstorm | **S'INSPIRER** | `lead-magnet-machine` (M4) | déjà couvert |
| auto-research-public, blitz-list-builder, google-maps-list-builder | **S'INSPIRER** | `machine-outbound` sourcing | remplacer scraping tiers par `prospecter_maps`/`prospecter_entreprise` |
| smartlead-api, smartlead-campaign-upload, smartlead-spintax, prospeo-*, zapmail-*, disco-like, deliverability-test-public | **IGNORER** | — | références d'API tierces (Smartlead/Prospeo/Zapmail/DiscoLike) hors scope |
| personalization-subagent-pattern, icp-prompt-builder, cold-email-kickoff | **S'INSPIRER** | pattern d'orchestration | déjà couvert par nos orchestrateurs |

### GTM — go-to-market flywheel
| Skill | Verdict | Cible | MCP Rapido / note |
|---|---|---|---|
| icp-matrix-builder, persona-development, account-qualification | **ADAPTER** | `icp-generator` (M5) | matrice ICP 5 dimensions → `icp.md` |
| signal-scoring/intent-signals, lead-prioritization, trigger-mapping | **ADAPTER** | **volet signaux de `lead-scoring`** (M5) | signaux d'intention ; providers tiers = **MCP manquant** |
| sales-intelligence/transcript-analysis, objection-mining | **ADAPTER** | **nouveau `sales-intelligence-fireflies`** | **MCP Fireflies déjà dispo** ; Gong/Otter → Fireflies |
| deal-patterns | **S'INSPIRER** | `attribution-kpi-marketing` | analyse closed-won/lost |
| cold-email/copy-frameworks, personalization-engine, sequence-architecture | **ADAPTER** | `machine-outbound` (M9) | frameworks de séquence |
| campaign-analytics/* (benchmarking, performance, winning-copy) | **S'INSPIRER** | `attribution-kpi-marketing` / `growth-experiments` | déjà couvert |

### HORMOZI — offre
| Skill | Verdict | Cible | Note |
|---|---|---|---|
| hormozi-offer, audit-offer, bonus-stack, value-*, pricing-strategy, objection-destroyer, offer-angles, productize, dfy-dwy-diy, business-model, market-research, idea-to-product | **S'INSPIRER** | `hundred-million-offers` (existant) + `lead-magnet-machine` | **déjà couvert** ; reformuler les termes déposés |
| hormozi-hooks, landing-page-copy, hormozi-pitch | **S'INSPIRER** | `storybrand-messaging` / `redaction-commerciale` | déjà couvert |
| agents/orchestrator + 5 sub-agents | **ADAPTER (note)** | **note M11** (`ops/note-agents-m11.md`) | pattern hub-and-spoke → notre équipe d'agents |
| create-plugin (méta) | **IGNORER** | — | scaffolding, hors scope |

### AIMKT — marketing généraliste
| Skill | Verdict | Cible | Note |
|---|---|---|---|
| market-emails + templates/ (3) | **ADAPTER** | `docs/methodo/templates-email/` + `email-sequence` | 3 séquences traduites (welcome/nurture/launch) |
| market-funnel, market-landing | **S'INSPIRER** | `tunnel-de-vente-360` | déjà couvert |
| market-ads | **S'INSPIRER** | `lancement-campagne-meta` | déjà couvert |
| market-seo, market-social, market-competitors, market-brand, market-copy, market-audit, market-report(-pdf), market-launch, market-proposal | **IGNORER / S'INSPIRER** | skills CMS existants | doublons de nos skills contenu/analytics |

### GEO — marketing généraliste (mal nommé)
| Skill | Verdict | Cible | Note |
|---|---|---|---|
| marketing (mono-fichier) | **IGNORER** | — | pas de GEO ; notre `geo-optimization` (sourcé) est supérieur |

---

## Correspondance profil client → `rapido-kb/`

Le `client-profile.yaml` (sortie de `icp-onboarding`, COLD) et la matrice ICP
5 dimensions (GTM) se mappent ainsi :

| Champ source (COLD/GTM) | Équivalent `rapido-kb/` |
|---|---|
| `business.{name,website,one_liner,tone}` | `entreprise.md` + `ton-et-accroches.md` |
| `offer.{primary_cta,lead_magnet,value_prop}` | `rapido-kb/marketing/offres.md` + `propositions-valeur.md` |
| `icp_hard_filters.{job_titles,industries_in/out,headcount,countries}` | `rapido-kb/marketing/icp.md` § segments (critères durs) |
| `icp_soft_preferences.triggers[]` | `icp.md` § signaux d'achat (volet signaux `lead-scoring`) |
| `legal.{banned_words,regulated_industry}` | `ton-et-accroches.md` (mots interdits) + garde-fous |
| Matrice GTM : firmographic/technographic/intent/persona/engagement + tiering | `icp.md` (segments priorisés + disqualification) |

> Notre `icp.md` (déjà livré) couvre l'essentiel ; l'apport à ADAPTER = la
> distinction **critères durs vs préférences souples** et le **tiering**.

---

## Nouveaux skills à ajouter au plan (M5-M11)
1. **`delivrabilite-email`** — warmup, plafonds, rotation, audit SPF/DKIM/DMARC,
   incident-response, spam-words. ⚠️ dépend d'une **infra email (MCP manquant :
   Zapmail/Dynadot type)** — à remonter à Tunis ; la partie méthodo/audit est
   livrable sans.
2. **`sales-intelligence-fireflies`** — analyse de transcripts d'appels +
   objection mining, **branché sur le MCP Fireflies (déjà disponible)**.
3. **Volet « signaux »** de `lead-scoring` — intent signals + trigger-mapping ;
   les providers d'intent (ZoomInfo/Bombora/6sense) sont des **MCP manquants**.

## MCP manquants à remonter à Tunis (nets)
Infra email (warmup/domaines/inboxes) · lookalike (DiscoLike) · intent data
(ZoomInfo/Bombora/6sense) · visitor tracking (RB2B/Leadfeeder) · scraping
LinkedIn. **Déjà disponibles** : Fireflies, n8n. **Remplacés par Rapido** :
Smartlead/Instantly/Apollo/HubSpot/Salesforce → RapidoCRM ; scraping Maps →
`prospecter_maps`.

## Fiches ADAPTER produites (`docs/methodo/ops/`)
`delivrabilite-email.md` · `icp-intake.md` · `signaux-intention.md` ·
`sales-intelligence.md` · `cold-email-cadence.md` · `sequences-email.md` ·
`note-agents-m11.md` — chacune avec attribution en tête. Templates traduits :
`docs/methodo/templates-email/`.
