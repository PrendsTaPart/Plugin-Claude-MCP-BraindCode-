# Imports & audit — rapido-leadmagnet (LM0)

**Date** : 2026-07-15 · **Portée** : audit uniquement — aucune création de skill,
aucune écriture. Sondes MCP = **lecture seule** (live). 5 dépôts clonés et relus
(licences vérifiées), + **inventaire des outils MCP réels** qui décide des routes.

> **Décision structurante** : côté RapidoCRM, **`create_formulaire` et `create_cta`
> n'existent pas** (seulement lecture) ; **`create_editor_template` supporte bien
> `landing_page`** (HTML/CSS) et des landings à **formulaire intégré** existent en
> prod. Côté RapidoRH, **les agents IA sont de vrais users** (assignation directe
> possible). → détails et 3 décisions en fin de document.

---

## 1. Moisson GitHub (5 dépôts MIT, relus)

Licences relues dans chaque `LICENSE` (toutes **MIT**, copyright 2026). Anti-verbatim :
on **réimplémente/francise les frameworks** (souvent des méthodes publiques : Hormozi,
Schwartz, PAS/PASTOR), on ne copie **aucun corps de texte** ; attribution `NOTICE.md`.

### 1.a `timscheuerai/content-vault` (⭐21) — 🥇 ADAPTER (source principale)
- **Structure** : 15 skills (`lead-magnet-creator`, `graphics-designer`,
  `newsletter-writer`, `linkedin-copywriter`, `researcher`, `repurpose`…).
- **`lead-magnet-creator`** : un **menu d'idées** (`ideas.md`, 30+ angles tierisés) +
  un **workflow de build** « le format est une décision, pas un défaut » (Notion / GDoc /
  PDF / Sheet / Skills repo / GPT / web tool / vidéo / vault bundle). Ancrages de voix
  dans `corpus.md`. Log Notion + Drive + chaîne vers le post LinkedIn.
- **Réutilisable** : la **taxonomie de formats**, les **angles d'idées**, la structure
  de rédaction par type, le principe « generosity is the brand ». **Verdict par élément** :
  ideas/angles = ADAPTER (francisés) · log Notion/Drive = REMPLACÉ (registre
  `rapido-kb/marketing/lead-magnets.md` + bibliothèque CMS) · chaîne LinkedIn = ADAPTER
  (semi-auto).
- **Ne pas dupliquer** : la **conception** est déjà faite par `rapido-marketing:lead-magnet-machine`
  (7 étapes). content-vault nourrit la **fabrication**, pas la conception.

### 1.b `thalesholleben/copy-thief` (⭐13) — ✅ ADAPTER (copy de la landing)
- **Contenu** : skill copy haute conversion trafic froid (PT-BR). Workflow **diagnostic
  (awareness/sophistication) → structure approuvée → copy**. `reference/` (01
  awareness-sophistication … 08 landing-page-anatomy, 09 ad-compliance), `templates/`
  (`lp-structure.md` = « lego » de 19 sections + presets PAS/PASTOR), `checklists/`
  (`briefing.md`, `qa-review.md`).
- **Réutilisable** : la **grille de structure de landing** (menu de sections + presets
  par niveau de conscience) et la **checklist QA copy**. **Verdict** : frameworks
  (Schwartz/PAS/PASTOR, publics) = ADAPTER **francisés + re-dérivés** (texte PT-BR **non
  copié**) · checklists = ADAPTER.

### 1.c `johnericforte/claude-skill-hormozi-offer-audit` (⭐4) — ✅ ADAPTER (gate qualité)
- **Contenu** : `skills/audit/SKILL.md` — **audite** une offre / un lead magnet (jamais
  ne génère). Score **/100 sur 4 leviers** (Dream Outcome, Perceived Likelihood, Time
  Delay, Effort & Sacrifice = **Value Equation**), levier le plus faible, **top 3 fixes**
  priorisés, contrôle de nommage **M.A.G.I.C.**. Dépendance optionnelle `humanizer`.
- **Réutilisable** : la **structure d'audit** (score + weakest lever + fixes) comme
  **GATE QUALITÉ** avant mise en page. **Verdict** : ADAPTER la **forme d'audit** mais
  **converger** avec le skill maison **`rapido-meta-ads:hundred-million-offers`** (les
  frameworks Hormozi y sont déjà distillés) — **référencer**, ne pas re-copier les
  frameworks.

### 1.d `cblain100-prog/lead-magnet-responder` (⭐2, FR) — 🟡 PATTERN → SEMI-AUTO
- **Contenu** : mécanique LinkedIn « commente pour recevoir » via **Unipile** (API tierce
  payante) : boucle (accepter connexions → lister commentaires → répondre + **DM** avec
  la ressource → dédup des commentaires traités), templates `MSG_REPLY_CONNECTED` /
  `MSG_REPLY_NOT_CONNECTED` / `MSG_DM` en `.env`, **délai 20 s** entre actions.
- **Verdict explicite** : **envoi automatisé LinkedIn = REJETÉ** (risque CGU LinkedIn +
  dépendance Unipile payante). **Version SEMI-AUTO retenue** : Claude prépare les 3 types
  de messages **en brouillons**, l'**humain envoie** ; dédup dans une **table n8n**
  (`memoire-operationnelle`). Cohérent avec `social-selling-linkedin`. La **mécanique
  étape par étape** est reprise ; le **code d'envoi** ne l'est pas.

### 1.e `jamnyjakub700-cloud/pdf-ebook-generator` (⭐0) — ✅ PATTERN (charte → PDF)
- **Contenu** : `brand.json` (couleurs, typographie, layout A4/marges) + `template.html`
  + `generate_ebook.py` → PDF brandé. Modes « from PDF » / « from topic ».
- **Réutilisable** : le **pattern `brand.json → template.html → PDF`**. **Verdict** :
  PATTERN — réimplémenté **maison** : charte lue via **`get_brand`** (CMS) → template HTML
  du plugin (`templates/lead-magnet.html`) → PDF via le **skill pdf maison**. Le
  `generate_ebook.py` sert de **référence de structure**, non fusionné.

### 1.f Benchmarks (non fusionnés)
- `aialvi/openfunnels` (⭐15) · `dome317/growth-quiz-engine` : 👁️ BENCHMARK — on a déjà
  RapidoCRM + `rapido-forge:ideation-quiz-generator`.
- `Mahanaicoach/competitor-x-ray` (⭐8) : 🟡 optionnel (angle du lead magnet depuis l'ICP
  concurrent) — chevauche `rapido-gmaps:veille-concurrents-gmaps`.
- `enoobis/AI-eBook-Generator` (⭐15) : ❌ **GPL-3.0** — pattern **lisible seulement**,
  **jamais** fusionné.

---

## 2. Inventaire des outils MCP réels (décisif — live, lecture seule)

### RapidoCRM — capture, CTA, landing, segment, pipeline

| Capacité | Outils exposés | Verdict |
|---|---|---|
| **Formulaire de capture** | `list_formulaires`, `get_formulaire_soumissions` (**lecture**) | ⚠️ **PAS de `create_formulaire`** — création **non exposée** via MCP. `list_formulaires` → **0** formulaire existant. |
| **CTA tracké** | `list_cta` (**lecture**, stats de clics) | ⚠️ **PAS de `create_cta`** — création **non exposée**. `list_cta` → **0**. |
| **Landing page** | `create_editor_template` (**écriture**) | ✅ supporte `type: landing_page` à partir de **HTML/CSS** ; retourne une **URL d'édition**. **Landings à formulaire intégré existantes en prod** (ex. id=7 « Formulaire integré : nom, email, ville, type de commerce »). `list_editor_templates` → types : `newsletter, site_web, landing_page, carte_visite, email_marketing, brochure`. |
| **Segment** | `create_segment` (**écriture**) | ✅ « LM-{slug} » possible. |
| **Pipeline** | `enregistrer_prospect`, `ajouter_prospect_pipeline`, `deplacer_prospect_etape` | ✅ capture → prospect → étape pipeline. |

> **Point ouvert (à trancher au 1er publish réel)** : une landing `create_editor_template`
> avec **formulaire HTML intégré** est créable, mais le **câblage automatique
> soumission → prospect** n'est pas garanti sans `create_formulaire`/webhook. Deux
> chemins de capture fiables : **(A)** landing CRM + le câblage natif du formulaire
> intégré (à confirmer côté serveur) ; **(B)** **Lovable mode B** (`usine-a-landing`) où
> la soumission appelle **`enregistrer_prospect`** (capture garantie via MCP).

### RapidoCMS — bibliothèque & URL publique

- `upload_file_tool` (retourne `file_url`) + `list_all_files` (`file_url` stable,
  filtre `doc|image|video`). **URL publique stable confirmée** à l'audit CMS antérieur
  (image de test → `file_url` partageable). Bibliothèque **doc actuellement vide** →
  `file_url` d'un **PDF** à reconfirmer au 1er upload réel (même mécanisme).

### RapidoRH — tâches & affectation aux agents IA

- `create-task-tool` : `project_id`, `tasklist_id`, `title`, `assigned_users:[ids]`,
  `priority`, `due_date`. Assignation par **IDs de users** (`get-users-list-tool`).
- **Les agents IA SONT des users RH actifs** (RH V2 en prod) :
  **🤖 Agent CRM (292)**, **Agent Stock (387)**, **🤖 Agent CMS (389)**, **🤖 Agent RH
  (391)**, **🧠 Agent Orchestrateur (406)**. → **assignation directe d'une tâche à un
  agent IA POSSIBLE** (`assigned_users:[292]`, etc.).
- **Limite** : pas d'« Agent Marketing / Contenu » dédié aujourd'hui → pour un rôle sans
  agent-user, **fallback** : convention `[AGENT:{rôle}]` dans le titre + assignation au
  responsable humain (mode dégradé documenté).

---

## 3. Outils MCP manquants (→ `docs/OUTILS-MCP-MANQUANTS.md`, backend Tunis)

1. **`create_formulaire`** — création d'un formulaire de capture (champs, **consentement
   RGPD checkbox non pré-cochée**, **webhook de soumission → prospect**). **Priorité
   haute** : sans lui, la capture native CRM n'est pas automatisable end-to-end via MCP.
2. **`create_cta`** — création d'un CTA tracké (le **suivi** de clics existe en lecture
   via `list_cta`, pas la **création**). Priorité moyenne.
3. **Confirmation du câblage formulaire intégré → prospect** d'une landing
   `create_editor_template` (ou endpoint/webhook de capture). Priorité haute (débloque la
   Route A totalement native).

---

## 4. STOP — 3 décisions requises avant LM1

**(a) Route landing par défaut (A éditeur CRM / B Lovable).**
Route A **techniquement viable** (`create_editor_template` type `landing_page` à partir
de HTML, formulaire intégré prouvé en prod). Route B (`usine-a-landing` Lovable, mode B)
garantit la **capture** via `enregistrer_prospect`.
→ **Recommandation** : **Route A par défaut pour la vitrine + tracking CRM** (tout dans
l'écosystème Rapido), **Route B (Lovable mode B) comme capture garantie** tant que le
câblage formulaire→prospect de la landing CRM n'est pas confirmé. Un mot de vous suffit
pour figer le défaut.

**(b) Mécanique LinkedIn « commente pour recevoir » : GO / NO-GO.**
→ **Recommandation : GO en semi-auto** — brouillons de réponses + DM préparés par Claude,
**envoi humain**, dédup en table n8n ; **jamais** Unipile ni envoi automatisé (CGU).
Cohérent avec `social-selling-linkedin`.

**(c) Le formulaire : natif CRM ou fallback Lovable mode B.**
→ **Recommandation** : **Lovable mode B par défaut pour la capture** (garantie via
`enregistrer_prospect`) jusqu'à ce que `create_formulaire` **ou** le câblage du formulaire
intégré CRM soit confirmé côté serveur ; la landing CRM (Route A) reste la vitrine.

*Sources : dépôts clonés (LICENSE relus) + sondes lecture seule RapidoCRM/CMS/RH (live).
Aucune donnée inventée ; les manques MCP sont explicitement listés (§3).*
