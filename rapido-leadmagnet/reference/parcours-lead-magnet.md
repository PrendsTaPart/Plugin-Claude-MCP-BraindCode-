# Parcours lead magnet — le pipeline canonique en 9 étapes

De la conception à la mesure. Chaque étape : **skill responsable**, **outils MCP**,
**livrable**, **critère de done**. L'usine **exécute** ; elle ne re-conçoit pas.

| # | Étape | Skill responsable | Outils / délégations | Livrable | Done |
|---|---|---|---|---|---|
| 1 | **Conception** | `rapido-marketing:lead-magnet-machine` (DÉLÉGUÉE, 7 étapes) | — | Concept validé (problème, type, format, nom, consommation, qualité, next step) | Sortie machine présente ; on ne fabrique pas un LM non conçu |
| 2 | **Fabrication** | `fabrication-lead-magnet` | `get_brand` (CMS), template `templates/lead-magnet.html` → PDF, `upload_file_tool` (CMS) | PDF brandé dans la bibliothèque CMS + URL publique | Gate qualité passé + PDF téléchargeable + inscrit au registre |
| 3 | **Page de capture** | `page-et-capture` | `rapido-lovable:usine-a-landing` (**mode B**) | Landing Lovable + formulaire → capture | Page live + copy validée + mentions RGPD |
| 4 | **Branchements CRM** | `page-et-capture` | `create_segment`, `enregistrer_prospect`, `ajouter_prospect_pipeline`, `log_activity` | Segment `LM-{slug}` + entrée pipeline + tag `leadmagnet:{slug}` | Soumission de test → prospect au bon endroit + segment |
| 5 | **Livraison** | `page-et-capture` | Email transactionnel (template CRM), page merci | Email avec le lien + page de remerciement (next step) | (Double opt-in si activé KB) email reçu + PDF accessible |
| 6 | **Diffusion organique** | `campagne-lead-magnet` | `create_campagne` (CMS), `rapidocms:pipeline-contenu-social`, LinkedIn **semi-auto** | Série de posts + post LinkedIn « commente pour recevoir » (brouillons) | Posts planifiés confirmés ; DM/réponses en brouillons |
| 7 | **Diffusion payante** | `campagne-lead-magnet` | `rapido-higgsfield:usine-video-marketing`, `rapido-meta-ads:creatifs-publicitaires` + `lancement-campagne-meta` | Vidéo 9:16 (self_ai_disclosure) + visuels + campagne Meta **PAUSED** | Tout en PAUSED, coût max récapitulé, non activé |
| 8 | **Nurturing** | `campagne-lead-magnet` | `rapido-marketing:machine-inbound` + gate `rapido-marketing:delivrabilite-email` | Séquence J0 (livraison) / J2 (bonus) / J5 (cas + CTA RDV) | Gate délivrabilité passé + chaque lot confirmé |
| 9 | **Mesure** | `campagne-lead-magnet` | `get_formulaire_soumissions`, `list_cta`, dépense ads, `scripts/stats_leadmagnet.py` | Rapport une page J+7 / J+30 (CPL, conv. landing, conv. RDV) | Chiffres **par script**, sources citées → benchmarks.md |

**Projet RH transversal** (`projet-rh-lead-magnet`) : un projet « LM — {nom} » avec
~20 tâches (une par livrable), affectées aux **agents IA users RH** (Agent CRM 292,
CMS 389, RH 391, Orchestrateur 406) via `create-task-tool`, ou en fallback
`[AGENT:{rôle}]` + responsable humain.

> **Route de la landing (décision LM0)** : **Route B (Lovable mode B)** par défaut —
> landing **et** capture via `usine-a-landing`, soumission → `enregistrer_prospect`
> (capture garantie via MCP). `create_formulaire`/`create_cta` n'existent pas côté
> CRM aujourd'hui ; la landing CRM (`create_editor_template` type `landing_page`)
> reste une option vitrine, pas le défaut.
