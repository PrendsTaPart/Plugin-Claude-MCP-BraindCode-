---
name: machine-inbound
description: Utiliser quand l'utilisateur veut mettre en place l'inbound, une machine à leads entrants, une stratégie de contenu qui convertit, ou un lead magnet de bout en bout. Orchestre la chaîne CMS-first du contenu au RDV — contenu, capture, nurturing, scoring, handoff, mesure — en déléguant chaque étape et en confirmant tout envoi.
---

# Machine inbound — du contenu au RDV, CMS-first

Skill **orchestrateur** : il ne réexécute rien, il **enchaîne** les skills
d'exécution et pose les garde-fous, KPI et modes dégradés. Voie Rapido d'abord
(CMS/CRM), secondaires (Lovable/n8n) seulement si la capacité manque.

## Étape 0 — Charger (obligatoire)
- `${CLAUDE_PLUGIN_ROOT}/reference/priorite-mcp.md` et `garde-fous-marketing.md`.
- `./rapido-kb/marketing/icp.md` **OBLIGATOIRE** (cible de tout l'inbound) — s'il
  est absent, invoquer le skill `icp-generator` **d'abord**, puis revenir.
- **Lire `./rapido-kb/marketing/apprentissages.md` et `benchmarks.md` AVANT de
  proposer un plan** — les leçons passées et les taux de référence **priment**
  sur les valeurs par défaut. Fichiers absents → créés depuis
  `${CLAUDE_PLUGIN_ROOT}/reference/kb-templates/` (voir `reference/memoire.md`).

## Pipeline (chaque étape : outils MCP + garde-fous + KPI + mode dégradé)

### 1. Pilier contenu
- **Plan éditorial** → skill `calendrier-editorial` (rapidocms :
  `create_campagne`, `create_draft_tool`, `schedule_draft_tool`).
- **Articles SEO + GEO** → skill `generation-article-blog`, puis **checklist**
  via skill `geo-optimization` (son script d'audit).
- **Relais social** → skill `pipeline-contenu-social`.
- Tout **rattaché à une campagne CMS** → skill `orchestration-campagne`
  (`add_post_campagne`, `ingishts_campagne`).
- **Garde-fous** : toute publication/planification **confirmée** (hook
  `garde-envois`). **KPI** : posts publiés vs planifiés, portée.
- **Mode dégradé** : RapidoCMS indisponible → le dire, produire les contenus en
  brouillon local (markdown), ne pas bloquer le reste.

### 2. Lead magnet
- **Conception** → skill `lead-magnet-machine` (méthodo M4).
- **Production du document** (docx/pdf) : rédiger le contenu ; hébergement via
  `upload_file_tool` (URL publique).
- **Page de capture** : **voie 1 (Rapido)** `create_editor_template` type
  `landing_page` (rapidocrm) ; **voie 2** skill `usine-a-landing` (Lovable) **si
  disponible**. Formulaire CRM branché.
- **KPI** : taux de conversion visiteur → lead (via `get_formulaire_soumissions`).
- **Mode dégradé** : **Lovable absent** → rester en voie 1
  (`create_editor_template`), le signaler ; jamais bloquer faute de Lovable.

### 3. Capture → CRM
- À chaque soumission (`get_formulaire_soumissions`), création/màj du contact et
  du prospect : `create_contact` / `enregistrer_prospect` (rapidocrm) —
  **après confirmation** (ou automatisé, ci-dessous).
- **Version récurrente** → déléguer au skill `usine-automatisations` (n8n :
  webhook soumission → create_contact → enregistrer_prospect).
- **Garde-fous** : consentement **RGPD** vérifié avant tout ajout à une séquence.
- **Mode dégradé** : n8n absent → capture **manuelle confirmée** au fil de l'eau.
- **Source de capture référencée** : un lead magnet
  (`rapido-leadmagnet:page-et-capture`) est une source de capture branchée sur cette
  tuyauterie (soumission → prospect + tag `leadmagnet:{slug}` + segment).

### 4. Nurturing
- **Séquence conçue** par skill `email-sequence` (rapidocms, méthodo), **exécutée**
  par `schedule_email` / `send_newsletter` avec templates CRM
  (`create_template_email`).
- **Sortie de séquence** dès **réponse** ou **RDV** (ne pas continuer à relancer).
- **Garde-fous** : chaque envoi **confirmé** (hook `garde-envois`) ; désinscription
  présente ; volumes progressifs. **KPI** : ouverture, clic, réponse.
- **Mode dégradé** : envoi de masse indisponible → prioriser les leads chauds en
  1-à-1 (`send_email` unitaire confirmé).

### 5. Scoring & handoff
- **Scoring hebdo** → skill `lead-scoring` (son script de scoring).
- **Leads chauds** → skill `secretariat-commercial` (RDV Google Calendar + CRM
  `create_rdv`) ; consigner l'étape via `deplacer_prospect_etape`.
- **KPI** : nombre de leads chauds, taux lead → RDV.

### 6. Mesure (entonnoir article → visite → lead → RDV)
- Insights contenu : `post_insights`, `ingishts_campagne` (rapidocms) ;
  conversion : `get_conversion_par_canal`, `get_stats_pipeline` (rapidocrm).
- **Tout chiffre par script** (skill `catalogue-kpi`) — jamais de tête.
- **Livrable** : **rapport une page** (entonnoir chiffré + 3 prochaines actions).

### 7. Projet RH (la machine EST un projet suivi)
- Créer le **projet Kanban** de la machine → skill `setup-projet` puis
  `flux-kanban` (rapidorh) avec les **tâches récurrentes** (publier, capturer,
  nurturer, scorer, mesurer).

## Capitalisation automatique (obligatoire)
À chaque **clôture de campagne/expérience** : ajouter **1 à 3 leçons datées et
SOURCÉES** (chiffre issu du script) dans `./rapido-kb/marketing/apprentissages.md`
(format `date | contexte | leçon | preuve | skill source`), et **mettre à jour
`benchmarks.md`** si un taux de référence change — le tout via `mise-a-jour-kb`.
Pas de leçon sans preuve chiffrée.


## Livrable type
Un **plan de machine inbound opérationnel** : campagne CMS + lead magnet + page de
capture + séquence + scoring + projet RH + rapport une page — chaque brique
déléguée, chaque envoi confirmé.

## Garde-fous
Aucun envoi ni publication sans **confirmation** (hook `garde-envois`) ; RGPD ;
voie Rapido d'abord ; KPI par script ; `icp.md` prérequis ; modes dégradés
documentés (jamais bloquer, toujours signaler).
