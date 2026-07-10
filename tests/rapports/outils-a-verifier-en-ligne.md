# Outils MCP vérifiés en ligne — checklist COMPLÉTÉE

Vérification faite le 2026-07-10 contre les CATALOGUES LIVE des connecteurs
réellement branchés à la session (facebook-ads 83 outils, gmail 13,
google-calendar 8, google-drive 8, n8n 26, stripe 9). Chaque outil cité par
un skill a été confronté au nom exact du schéma serveur.

Bilan : **68 citations, 49 outils uniques — 0 introuvable(s)**.

## Serveur(s) réel(s) : facebook-ads

- [x] `ads_activate_entity` — cité par rapido-meta-ads/agents/media-buyer.md
- [x] `ads_activate_entity` — cité par rapido-meta-ads/skills/boost-post-instagram/SKILL.md
- [x] `ads_activate_entity` — cité par rapido-meta-ads/skills/lancement-campagne-meta/SKILL.md
- [x] `ads_boost_ig_post` — cité par rapido-meta-ads/skills/boost-post-instagram/SKILL.md
- [x] `ads_create_ad` — cité par rapido-meta-ads/skills/lancement-campagne-meta/SKILL.md
- [x] `ads_create_ad_set` — cité par rapido-meta-ads/skills/lancement-campagne-meta/SKILL.md
- [x] `ads_create_campaign` — cité par rapido-meta-ads/skills/lancement-campagne-meta/SKILL.md
- [x] `ads_create_creative` — cité par rapido-meta-ads/skills/creatifs-publicitaires/SKILL.md
- [x] `ads_create_custom_audience` — cité par rapido-meta-ads/skills/audiences-crm/SKILL.md
- [x] `ads_create_custom_audience` — cité par rapido-meta-ads/skills/pixel-et-retargeting/SKILL.md
- [x] `ads_experiment_abtest_create_test` — cité par rapido-meta-ads/skills/tests-ab-meta/SKILL.md
- [x] `ads_experiment_abtest_get_test` — cité par rapido-meta-ads/skills/tests-ab-meta/SKILL.md
- [x] `ads_experiment_check_eligibility` — cité par rapido-meta-ads/skills/tests-ab-meta/SKILL.md
- [x] `ads_experiment_lift_create_test` — cité par rapido-meta-ads/skills/tests-ab-meta/SKILL.md
- [x] `ads_get_ad_account_pages` — cité par rapido-meta-ads/skills/creatifs-publicitaires/SKILL.md
- [x] `ads_get_ad_account_pages` — cité par rapido-meta-ads/skills/lancement-campagne-meta/SKILL.md
- [x] `ads_get_ad_accounts` — cité par rapido-meta-ads/skills/lancement-campagne-meta/SKILL.md
- [x] `ads_get_ad_entities` — cité par rapido-meta-ads/skills/pilotage-performance-ads/SKILL.md
- [x] `ads_get_ad_entities` — cité par rapido-suite/skills/comite-de-direction/SKILL.md
- [x] `ads_get_ad_entities` — cité par rapido-suite/skills/revue-hebdo-business/SKILL.md
- [x] `ads_get_ad_preview` — cité par rapido-meta-ads/skills/creatifs-publicitaires/SKILL.md
- [x] `ads_get_ad_preview` — cité par rapido-meta-ads/skills/lancement-campagne-meta/SKILL.md
- [x] `ads_get_custom_audience_adsets` — cité par rapido-meta-ads/skills/audiences-crm/SKILL.md
- [x] `ads_get_dataset_details` — cité par rapido-meta-ads/skills/pixel-et-retargeting/SKILL.md
- [x] `ads_get_datasets` — cité par rapido-meta-ads/skills/pixel-et-retargeting/SKILL.md
- [x] `ads_get_field_context` — cité par rapido-meta-ads/skills/pilotage-performance-ads/SKILL.md
- [x] `ads_get_ig_accounts` — cité par rapido-meta-ads/skills/boost-post-instagram/SKILL.md
- [x] `ads_get_ig_media` — cité par rapido-meta-ads/skills/boost-post-instagram/SKILL.md
- [x] `ads_get_opportunity_score` — cité par rapido-meta-ads/skills/lancement-campagne-meta/SKILL.md
- [x] `ads_get_opportunity_score` — cité par rapido-meta-ads/skills/pilotage-performance-ads/SKILL.md
- [x] `ads_insights_anomaly_signal` — cité par rapido-meta-ads/skills/pilotage-performance-ads/SKILL.md
- [x] `ads_insights_anomaly_signal` — cité par rapido-suite/skills/comite-de-direction/SKILL.md
- [x] `ads_insights_anomaly_signal` — cité par rapido-suite/skills/revue-hebdo-business/SKILL.md
- [x] `ads_insights_industry_benchmark` — cité par rapido-meta-ads/skills/pilotage-performance-ads/SKILL.md
- [x] `ads_insights_performance_trend` — cité par rapido-meta-ads/skills/pilotage-performance-ads/SKILL.md
- [x] `ads_library_search` — cité par rapido-meta-ads/skills/veille-ads-concurrents/SKILL.md
- [x] `ads_pixel_event_create` — cité par rapido-meta-ads/skills/pixel-et-retargeting/SKILL.md
- [x] `ads_pixel_event_update` — cité par rapido-meta-ads/skills/pixel-et-retargeting/SKILL.md
- [x] `ads_update_custom_audience_users` — cité par rapido-meta-ads/skills/audiences-crm/SKILL.md

## Serveur(s) réel(s) : gmail

- [x] `create_draft` — cité par rapido-direction/agents/assistant-direction.md
- [x] `create_draft` — cité par rapido-direction/skills/secretariat-commercial/SKILL.md
- [x] `create_draft` — cité par rapido-direction/skills/tri-boite-mail/SKILL.md
- [x] `create_label` — cité par rapido-direction/skills/tri-boite-mail/SKILL.md
- [x] `get_thread` — cité par rapido-direction/skills/secretariat-commercial/SKILL.md
- [x] `get_thread` — cité par rapido-direction/skills/tri-boite-mail/SKILL.md
- [x] `list_labels` — cité par rapido-direction/skills/tri-boite-mail/SKILL.md

## Serveur(s) réel(s) : google-calendar

- [x] `create_event` — cité par rapido-direction/skills/secretariat-commercial/SKILL.md
- [x] `create_event` — cité par rapido-startup/skills/plan-execution-startup/SKILL.md
- [x] `list_events` — cité par rapido-direction/skills/journee-du-dirigeant/SKILL.md

## Serveur(s) réel(s) : google-drive

- [x] `create_file` — cité par rapido-direction/skills/coffre-documents/SKILL.md
- [x] `get_file_permissions` — cité par rapido-direction/skills/coffre-documents/SKILL.md

## Serveur(s) réel(s) : n8n

- [x] `add_data_table_column` — cité par rapido-n8n/skills/memoire-operationnelle/SKILL.md
- [x] `add_data_table_rows` — cité par rapido-n8n/skills/memoire-operationnelle/SKILL.md
- [x] `create_data_table` — cité par rapido-n8n/skills/memoire-operationnelle/SKILL.md
- [x] `create_workflow_from_code` — cité par rapido-n8n/skills/usine-automatisations/SKILL.md
- [x] `delete_data_table_column` — cité par rapido-n8n/skills/memoire-operationnelle/SKILL.md
- [x] `execute_workflow` — cité par rapido-n8n/skills/surveillance-automatisations/SKILL.md
- [x] `execute_workflow` — cité par rapido-n8n/skills/usine-automatisations/SKILL.md
- [x] `get_execution` — cité par rapido-n8n/skills/surveillance-automatisations/SKILL.md
- [x] `get_execution` — cité par rapido-n8n/skills/usine-automatisations/SKILL.md
- [x] `get_node_types` — cité par rapido-n8n/skills/memoire-operationnelle/SKILL.md
- [x] `get_node_types` — cité par rapido-n8n/skills/surveillance-automatisations/SKILL.md
- [x] `get_node_types` — cité par rapido-n8n/skills/usine-automatisations/SKILL.md
- [x] `get_sdk_reference` — cité par rapido-n8n/skills/usine-automatisations/SKILL.md
- [x] `get_suggested_nodes` — cité par rapido-n8n/skills/usine-automatisations/SKILL.md
- [x] `publish_workflow` — cité par rapido-n8n/skills/usine-automatisations/SKILL.md
- [x] `update_workflow` — cité par rapido-n8n/skills/surveillance-automatisations/SKILL.md
- [x] `update_workflow` — cité par rapido-n8n/skills/usine-automatisations/SKILL.md

Règle de maintenance : tout nouvel outil cité vers un serveur distant
réapparaît en INFO dans `scripts/tester-skills.py --verbose` — re-vérifier et
re-cocher ici avant release.
