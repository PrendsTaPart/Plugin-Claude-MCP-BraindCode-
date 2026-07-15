# MATRICE DE COUVERTURE — marketing / vente / growth (M0)

> Audit **lecture seule**. Sources : schémas MCP **live** (RapidoCRM, RapidoCMS,
> RapidoRH + secondaires) et **SKILL.md réels** du dépôt. Aucune donnée inventée.
> Compte de test : company_id 321 (retours réels documentés au § tunnel).
> Date : 2026-07-14.

---

## 1. Inventaire MCP (serveurs Rapido)

### 1.1 RapidoCRM (~103 outils) — cœur vente/marketing
- **Prospection** : `prospecter_maps`, `prospecter_entreprise`, `prospecter_prospect`,
  `rechercher_prospects`, `rechercher_entreprise_siret`, `search_entreprises`.
- **Pipeline** : `ajouter_prospect_pipeline`, `deplacer_prospect_etape`,
  `get_pipeline`, `get_stats_pipeline`, `get_stats_pipeline_global`,
  `close_opportunity`, `get_historique_prospect`.
- **Segments** : `create_segment`, `recalculer_segment`, `list_segments`,
  `get_contacts_segment`.
- **Campagnes** : `create_campagne`, `list_campagnes`, `lancer_campagne`,
  `get_stats_campagne`.
- **Email/SMS/Newsletter** : `send_email`, `send_sms`, `schedule_email`,
  `schedule_sms`, `send_newsletter`, `create_template_email`,
  `create_template_sms`, `list_newsletters`.
- **Éditeur / tunnel** : `create_editor_template` (types :
  newsletter | site_web | **landing_page** | carte_visite | email_marketing |
  brochure), `create_editor_template` + variantes list/update/delete.
- **Capture** : `list_formulaires`, `get_formulaire_soumissions`, `list_cta`.
- **Analytics** : `get_dashboard_kpis`, `get_dashboard_general_stats`,
  `get_conversion_par_canal`, `get_revenue_summary`, `get_top_clients`,
  `get_interaction_stats`, `get_user_performance`, `get_stats_campagne`.
- **Fidélité/animation** : `get_loyalty_points`, `lancer_sondage_entreprise`,
  `lancer_jeu_concours_entreprise`, `get_sondage_resultats`, `list_sondages`,
  `list_jeux_concours`.
- **Devis/factures/produits** : `create_devis`, `create_facture`,
  `list_factures`, `list_products`, `create_product`.
- **Équipe co** : `list_commerciaux`, `update_commercial_objectifs`,
  `set_commercial_status`, `create_rdv`, `list_rdvs`, `create_evenement`.

### 1.2 RapidoCMS (~43 outils) — contenu & social
Brouillons/planif (`create_draft_tool`, `schedule_draft_tool`,
`list_scheduled_posts`, `cancel_schedules_post`), campagnes
(`create_campagne`, `add_post_campagne`, `ingishts_campagne`), insights
(`post_insights`), visuels (`generate_image`, `images_to_image`), comptes
(`list_connected_accounts`), prompts (`add_prompt`/`list_prompts`), cartes
digitales, marques/assets (couche marque). *(détail : `reference/audit-tools-*`
et `rapidocms/reference/outils-marque.md`.)*

### 1.3 RapidoRH (~22 outils) — équipe/projets
`create-project-tool`, `create-task-tool`, `get-dailies-tool`,
`get-users-list-tool`, `get-projects-list-tool`, `move-task-tool`, rôles.
Pertinent growth : capacité de l'équipe (delivery), pas d'outil marketing direct.

### 1.4 Secondaires (succinct)
| Serveur | Périmètre marketing/vente | Volume |
|---|---|---|
| **facebook-ads (Meta)** | campagnes/ad sets/créas/ads, audiences custom+lookalike, pixel, A/B (`ads_experiment_*`), insights, `ads_library_search` | ~82 |
| **n8n** | automatisation (séquences, speed-to-lead, relances) — SDK workflows | ~26 |
| **lovable** | build d'app/landing full-stack (usine-a-landing) | ~45 |
| **canva** | design visuels/supports (OAuth) | ~38 |
| **gmail** | outreach 1-à-1, brouillons | ~13 |
| **google-calendar** | RDV/discovery calls | ~8 |
| **google-drive** | documents/ressources | ~8 |
| **hyperframes** | vidéo (render) | ~6 |

---

## 2. Inventaire skills (marketing/vente/contenu/growth/analytics)

Résumé (détail complet : voir §3 pour le mapping par compétence). 305 skills
scannés. Exécuteurs principaux :
- **Acquisition** : `rapidocrm:prospection-pipeline`, `rapido-lovable:usine-a-landing`.
- **Vente/CRM** : `rapidocrm:coaching-pipeline`, `predictable-revenue`,
  `redaction-commerciale`, `negotiation`, `devis-facture-relance`, `forecast`.
- **Contenu/social** : `rapidocms:pipeline-contenu-social`, `calendrier-editorial`,
  `orchestration-campagne`, `generation-article-blog`, `funnel-tofu-mofu-bofu`.
- **Ads** : `rapido-meta-ads:*` (lancement, boost, créatifs, A/B, pixel/retargeting,
  audiences-crm, pilotage-performance).
- **Email** : `rapidocrm:campagne-marketing`, `communication-client`,
  `studio-templates`, `rapidocms:email-sequence`.
- **Fidélisation** : `rapidocrm:animation-client`, `rapidocms:contagious`.
- **Analytics** : `rapidocms:analyse-performance-contenu`, `rapido-startup:catalogue-kpi`,
  `rapido-suite:business-pulse`/`cash-flow-snapshot`.
- **Positionnement/copy** : `storybrand-messaging`, `made-to-stick`,
  `hundred-million-offers`, `one-page-marketing`.
- **Growth/méthode** : `rapido-forge` (181 skills — familles bootcamp-* 46,
  ideation-* 72, scale-* 62 + selecteur-framework).

---

## 3. Matrice des compétences cibles

Statut : **COUVERT** (skill + plugin) · **PARTIEL** (skill à étendre / MCP dispo
mais pas orchestré) · **MANQUANT** (aucun skill dédié).

| # | Compétence | Statut | Skill(s) / plugin | Outils MCP dispo | MCP manquant (→ backend Tunis) |
|---|---|---|---|---|---|
| 1 | Lead Generation | COUVERT | rapidocrm:prospection-pipeline ; forge ideation-cold-email, scale-cold-email-prospection | prospecter_*, ajouter_prospect_pipeline | — |
| 2 | Buyer Persona | COUVERT | forge bootcamp-persona-deep, scale-jtbd, ideation-persona-maker | get_contacts_segment (+ KB) | — |
| 3 | **ICP** | **MANQUANT** | approché par personas/segmentation | search_entreprises, rechercher_entreprise_siret, segments | champ/scoring firmographique ICP dédié |
| 4 | Segmentation | COUVERT | rapidocrm:campagne-marketing ; bootcamp-market-segmentation | create_segment, recalculer_segment, list_segments | — |
| 5 | Content Strategy | COUVERT | rapidocms:calendrier-editorial, content-creation-methodo | create_campagne, create_draft_tool | — |
| 6 | SEO | COUVERT | generation-article-blog ; forge scale-seo-meta, scale-semrush-audit, scale-google-search-console | (contenu via CMS) | connecteur SEO/rank (Search Console/SEMrush) — externe |
| 7 | GEO | COUVERT | generation-article-blog (E-E-A-T/GEO) | — (méthodo) | — |
| 8 | **Social Selling** | **MANQUANT** | — | rapidocms posts + rapidocrm | API social listening / DM |
| 9 | **LinkedIn Outreach** | **MANQUANT** | draft-outreach (générique) | — | connecteur LinkedIn (DM/invitations) |
| 10 | Cold/Warm Email | COUVERT | rapidocrm:redaction-commerciale, draft-outreach ; fiche ACA | send_email, schedule_email, create_template_email | — |
| 11 | **Lead Scoring** | **MANQUANT** | qualification seule (scale-bant, ANUM) | get_historique_prospect, get_interaction_stats | tool set/get score de lead |
| 12 | CRM | COUVERT | natif rapidocrm (nombreux skills) | (tout rapidocrm) | — |
| 13 | Pipeline | COUVERT | rapidocrm:coaching-pipeline, prospection-pipeline | get_pipeline, deplacer_prospect_etape, get_stats_pipeline | — |
| 14 | Sales Funnel Builder | COUVERT | rapidocms:funnel-tofu-mofu-bofu ; usine-a-landing ; scale-funnel-aarrr | create_editor_template (landing_page), list_formulaires, list_cta | — |
| 15 | Funnel Optimizer | PARTIEL | forge bootcamp-conversion-funnel (méthodo) | get_formulaire_soumissions, list_cta, get_conversion_par_canal | A/B sur étapes de funnel (hors ads) |
| 16 | Marketing Automation | COUVERT | rapido-n8n (usine-automatisations) ; campagne-marketing | n8n (workflows), schedule_email/sms | — |
| 17 | Customer Journey | COUVERT | forge scale-customer-journey | get_historique_prospect | — |
| 18 | **Attribution** | PARTIEL | aucun skill orchestrateur | get_conversion_par_canal (single-touch) | attribution **multi-touch** |
| 19 | CRO | PARTIEL | brand-review, funnel ; forge scale-heatmaps (méthodo) | get_formulaire_soumissions | heatmap / session recording |
| 20 | Landing Optimizer | PARTIEL | rapido-lovable:usine-a-landing (build) | create_editor_template, get_formulaire_soumissions | test A/B landing natif |
| 21 | Copywriting | COUVERT | redaction-commerciale, content-creation-methodo | send_email, create_template_email | — |
| 22 | Storytelling | COUVERT | rapidocms:storybrand-messaging, made-to-stick | — (méthodo) | — |
| 23 | Email Marketing | COUVERT | rapidocrm:campagne-marketing, communication-client, studio-templates | send_newsletter, schedule_email, create_editor_template | — |
| 24 | Newsletter | COUVERT | rapidocrm:campagne-marketing, studio-templates | send_newsletter, create_editor_template (newsletter), list_newsletters | — |
| 25 | Community | COUVERT | forge scale-community-building | — (méthodo) | connecteur communauté (Discord/FB groups) |
| 26 | Publicité | COUVERT | rapido-meta-ads:lancement-campagne-meta + suite | ads_create_* (PAUSED) | Google/TikTok/LinkedIn ads (forge méthodo, MCP absent) |
| 27 | Retargeting | COUVERT | rapido-meta-ads:pixel-et-retargeting ; ideation-retargeting-setup | ads_pixel_event_*, ads_create_custom_audience | — |
| 28 | Upsell | COUVERT | forge scale-upsell-crosssell | create_devis, list_products | — |
| 29 | Cross-sell | COUVERT | forge scale-upsell-crosssell | create_devis, list_products | — |
| 30 | Customer Success | COUVERT | forge scale-customer-success | rapidocrm (historique, factures) | — |
| 31 | Fidélisation | COUVERT | rapidocrm:animation-client | get_loyalty_points, lancer_sondage/jeu_concours | — |
| 32 | Referral | COUVERT | forge scale-referral-program, ideation-referral-program ; contagious | lancer_jeu_concours_entreprise, segments | tracking d'attribution referral dédié |
| 33 | Analytics | COUVERT | rapidocms:analyse-performance-contenu ; catalogue-kpi | post_insights, ingishts_campagne, get_stats_* | — |
| 34 | Dashboard KPI | COUVERT | rapido-startup:catalogue-kpi ; business-pulse ; forge scale-kpi-dashboard | get_dashboard_kpis, get_dashboard_general_stats | — |
| 35 | Forecast | COUVERT | rapidocrm:forecast ; rapido-suite:cash-flow-snapshot | get_stats_pipeline, get_revenue_summary | — |
| 36 | **RevOps** | **MANQUANT** | — | stats cross rapidocrm | orchestration RevOps (data unifiée) |
| 37 | Growth | COUVERT | forge (growth-strategy, funnel-aarrr, growth-experiments) ; loop-engine-v2 | multi-MCP | — |
| 38 | Prompt Engineering Marketing | COUVERT | rapidocms:prompt-engineering-visuel, prompts-visuels-pro, bibliotheque-prompts | generate_image, images_to_image, add_prompt/list_prompts | — |

> La liste de la mission annonce « 40 compétences » mais en énumère **38** :
> les 38 fournies sont traitées ci-dessus.

### Synthèse
- **COUVERT** : 29 · **PARTIEL** : 4 (Funnel Optimizer, Attribution, CRO,
  Landing Optimizer) · **MANQUANT** : 5 (ICP, Social Selling, LinkedIn Outreach,
  Lead Scoring, RevOps).

---

## 4. Vérification chaîne « tunnel Rapido-first » (CRM, live)

| Outil | Type | Vérifié | Retour observé / schéma |
|---|---|---|---|
| `create_editor_template` | écriture (NON exécuté) | schéma live | types = newsletter / site_web / **landing_page** / carte_visite / email_marketing / brochure ; **retourne l'URL** d'édition. → landing page = **OUI** |
| `list_formulaires` | lecture | ✅ appel réel | `{count, formulaires[], total_clics}` — 0 sur le compte test |
| `get_formulaire_soumissions` | lecture | ✅ appel réel | stats (vues, clics, **taux de conversion**, entreprise/segment liés, champs) ; `{error, disponibles[]}` si introuvable |
| `list_cta` | lecture | ✅ appel réel | `{count, ctas[]}` — 0 sur le compte test |
| `create_segment` | écriture (NON exécuté) | schéma live | in : `nom*`, `domaine_contient`, `ville_contient`, `recalculer` → crée + recalcule |
| `schedule_email` | envoi (NON exécuté) | schéma live | in : `entreprise_id*`, `date_envoi*`, `sujet*`, `contenu`, `destinataires`, `target`, `template_id` |
| `send_newsletter` | envoi (NON exécuté) | schéma live | in : `entreprise_id*`, `cible`, `contenu`, `date_envoi`, `template_id` |
| `get_conversion_par_canal` | lecture | ✅ appel réel | `{success, total, par_statut[]}` (single-touch par canal) |
| `get_stats_campagne` | lecture | ✅ appel réel | `{success, total, par_statut[]}` |

**Conclusion tunnel** : la chaîne **landing → formulaire/CTA → segment → email/
newsletter → stats/conversion** est **complète côté MCP**. Manque une brique
d'**A/B testing de landing** et l'**attribution multi-touch** (voir §3). Les
outils d'envoi/création n'ont pas été exécutés (actions réelles visibles client) ;
seuls les schémas et les lectures ont été vérifiés — aucune donnée inventée.

---

## 5. Conclusion — skills à créer/étendre + GO/NO-GO

### À CRÉER (5 manques)
1. **ICP builder** (rapido-marketing) — firmographies via `rechercher_entreprise_siret`
   + `search_entreprises` + `create_segment`.
2. **Social Selling** — nécessite un **connecteur social** (backend Tunis) avant skill.
3. **LinkedIn Outreach** — nécessite un **connecteur LinkedIn** (backend Tunis).
4. **Lead Scoring** — nécessite un **tool score** CRM (backend Tunis) ; skill
   d'orchestration ensuite (`get_interaction_stats`/`get_historique_prospect`).
5. **RevOps** — skill transverse (data CRM+ads+CMS unifiée) ; MCP existants
   suffisent partiellement.

### À ÉTENDRE (4 partiels)
- **Attribution** : skill autour de `get_conversion_par_canal` (+ demander le
  multi-touch au backend).
- **Funnel Optimizer** / **Landing Optimizer** : A/B sur étapes de funnel/landing
  (tool à demander) ; en attendant, exploiter `get_formulaire_soumissions`.
- **CRO** : connecteur heatmap/session (backend) ; méthodo `scale-heatmaps` déjà là.

### À remonter au backend Tunis (MCP manquants)
Score de lead · attribution multi-touch · A/B landing/funnel · heatmaps ·
connecteurs LinkedIn / social listening / communauté · (méthodo prête pour
Google/TikTok/LinkedIn ads, MCP absents).

### GO / NO-GO M3–M14
> Les définitions exactes de M3–M14 n'ont pas été fournies ; le GO/NO-GO est
> donné **par cluster de capacité** (à mapper sur les jalons).

| Cluster | GO/NO-GO | Justification |
|---|---|---|
| Acquisition / prospection / cold email | **GO** | skills + MCP complets |
| Contenu / social / SEO / éditorial | **GO** | pipeline CMS complet |
| Ads Meta (lancement, retargeting, A/B, pilotage) | **GO** | rapido-meta-ads complet |
| Tunnel landing → formulaire → segment → email → stats | **GO** | vérifié live (§4), `landing_page` dispo |
| Email marketing / newsletter / automation (n8n) | **GO** | MCP + skills OK |
| Fidélisation / referral / animation | **GO** | loyalty + jeux/sondages |
| Analytics / KPI / forecast / dashboard | **GO** | catalogue-kpi + stats CRM |
| Attribution multi-touch / Lead scoring | **NO-GO conditionnel** | MCP backend manquant |
| Social selling / LinkedIn outreach | **NO-GO conditionnel** | connecteurs absents |
| RevOps unifié / CRO instrumenté (heatmaps) | **NO-GO conditionnel** | outils manquants |

**Verdict** : ~29/38 compétences **GO immédiat**, 4 **GO après extension**
(MCP existants), 5 **NO-GO conditionnels** dépendants du backend Tunis. Le socle
« Rapido-first » (tunnel de conversion) est **prêt**.

---

## Fichiers produits
- `docs/MATRICE-COUVERTURE.md` (ce fichier).
