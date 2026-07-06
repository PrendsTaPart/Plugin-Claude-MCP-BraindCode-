# Outils MCP à vérifier en ligne avant release

Ces outils sont cités par les skills mais leur catalogue vit sur un serveur
distant (facebook-ads, n8n, gmail, google-calendar, google-drive) : le test
hors-ligne `scripts/tester-skills.py` les compte en INFO, il ne peut pas les
valider. Vérification MANUELLE en conditions réelles (MCP connectés) : pour
chaque outil, confirmer que le nom existe tel quel dans le schéma du serveur,
puis cocher. Tout écart = corriger le skill AVANT la release.

Généré par `python3 scripts/tester-skills.py --verbose` le 2026-07-06 — 67 citations, 49 outils uniques.

## Serveur(s) candidat(s) : facebook-ads

- [ ] `ads_activate_entity` — cité par rapido-meta-ads/agents/media-buyer.md
- [ ] `ads_activate_entity` — cité par rapido-meta-ads/skills/boost-post-instagram/SKILL.md
- [ ] `ads_activate_entity` — cité par rapido-meta-ads/skills/lancement-campagne-meta/SKILL.md
- [ ] `ads_boost_ig_post` — cité par rapido-meta-ads/skills/boost-post-instagram/SKILL.md
- [ ] `ads_create_ad` — cité par rapido-meta-ads/skills/lancement-campagne-meta/SKILL.md
- [ ] `ads_create_ad_set` — cité par rapido-meta-ads/skills/lancement-campagne-meta/SKILL.md
- [ ] `ads_create_campaign` — cité par rapido-meta-ads/skills/lancement-campagne-meta/SKILL.md
- [ ] `ads_create_creative` — cité par rapido-meta-ads/skills/creatifs-publicitaires/SKILL.md
- [ ] `ads_create_custom_audience` — cité par rapido-meta-ads/skills/audiences-crm/SKILL.md
- [ ] `ads_create_custom_audience` — cité par rapido-meta-ads/skills/pixel-et-retargeting/SKILL.md
- [ ] `ads_experiment_abtest_create_test` — cité par rapido-meta-ads/skills/tests-ab-meta/SKILL.md
- [ ] `ads_experiment_abtest_get_test` — cité par rapido-meta-ads/skills/tests-ab-meta/SKILL.md
- [ ] `ads_experiment_check_eligibility` — cité par rapido-meta-ads/skills/tests-ab-meta/SKILL.md
- [ ] `ads_experiment_lift_create_test` — cité par rapido-meta-ads/skills/tests-ab-meta/SKILL.md
- [ ] `ads_get_ad_account_pages` — cité par rapido-meta-ads/skills/creatifs-publicitaires/SKILL.md
- [ ] `ads_get_ad_account_pages` — cité par rapido-meta-ads/skills/lancement-campagne-meta/SKILL.md
- [ ] `ads_get_ad_accounts` — cité par rapido-meta-ads/skills/lancement-campagne-meta/SKILL.md
- [ ] `ads_get_ad_entities` — cité par rapido-meta-ads/skills/pilotage-performance-ads/SKILL.md
- [ ] `ads_get_ad_entities` — cité par rapido-suite/skills/comite-de-direction/SKILL.md
- [ ] `ads_get_ad_entities` — cité par rapido-suite/skills/revue-hebdo-business/SKILL.md
- [ ] `ads_get_ad_preview` — cité par rapido-meta-ads/skills/creatifs-publicitaires/SKILL.md
- [ ] `ads_get_ad_preview` — cité par rapido-meta-ads/skills/lancement-campagne-meta/SKILL.md
- [ ] `ads_get_custom_audience_adsets` — cité par rapido-meta-ads/skills/audiences-crm/SKILL.md
- [ ] `ads_get_dataset_details` — cité par rapido-meta-ads/skills/pixel-et-retargeting/SKILL.md
- [ ] `ads_get_datasets` — cité par rapido-meta-ads/skills/pixel-et-retargeting/SKILL.md
- [ ] `ads_get_field_context` — cité par rapido-meta-ads/skills/pilotage-performance-ads/SKILL.md
- [ ] `ads_get_ig_accounts` — cité par rapido-meta-ads/skills/boost-post-instagram/SKILL.md
- [ ] `ads_get_ig_media` — cité par rapido-meta-ads/skills/boost-post-instagram/SKILL.md
- [ ] `ads_get_opportunity_score` — cité par rapido-meta-ads/skills/lancement-campagne-meta/SKILL.md
- [ ] `ads_get_opportunity_score` — cité par rapido-meta-ads/skills/pilotage-performance-ads/SKILL.md
- [ ] `ads_insights_anomaly_signal` — cité par rapido-meta-ads/skills/pilotage-performance-ads/SKILL.md
- [ ] `ads_insights_anomaly_signal` — cité par rapido-suite/skills/comite-de-direction/SKILL.md
- [ ] `ads_insights_anomaly_signal` — cité par rapido-suite/skills/revue-hebdo-business/SKILL.md
- [ ] `ads_insights_industry_benchmark` — cité par rapido-meta-ads/skills/pilotage-performance-ads/SKILL.md
- [ ] `ads_insights_performance_trend` — cité par rapido-meta-ads/skills/pilotage-performance-ads/SKILL.md
- [ ] `ads_library_search` — cité par rapido-meta-ads/skills/veille-ads-concurrents/SKILL.md
- [ ] `ads_pixel_event_create` — cité par rapido-meta-ads/skills/pixel-et-retargeting/SKILL.md
- [ ] `ads_pixel_event_update` — cité par rapido-meta-ads/skills/pixel-et-retargeting/SKILL.md
- [ ] `ads_update_custom_audience_users` — cité par rapido-meta-ads/skills/audiences-crm/SKILL.md

## Serveur(s) candidat(s) : gmail/google-calendar/google-drive/n8n

- [ ] `create_draft` — cité par rapido-direction/agents/assistant-direction.md
- [ ] `create_draft` — cité par rapido-direction/skills/secretariat-commercial/SKILL.md
- [ ] `create_draft` — cité par rapido-direction/skills/tri-boite-mail/SKILL.md
- [ ] `create_event` — cité par rapido-direction/skills/secretariat-commercial/SKILL.md
- [ ] `create_file` — cité par rapido-direction/skills/coffre-documents/SKILL.md
- [ ] `create_label` — cité par rapido-direction/skills/tri-boite-mail/SKILL.md
- [ ] `get_file_permissions` — cité par rapido-direction/skills/coffre-documents/SKILL.md
- [ ] `get_thread` — cité par rapido-direction/skills/secretariat-commercial/SKILL.md
- [ ] `get_thread` — cité par rapido-direction/skills/tri-boite-mail/SKILL.md
- [ ] `list_events` — cité par rapido-direction/skills/journee-du-dirigeant/SKILL.md
- [ ] `list_labels` — cité par rapido-direction/skills/tri-boite-mail/SKILL.md

## Serveur(s) candidat(s) : n8n

- [ ] `add_data_table_column` — cité par rapido-n8n/skills/memoire-operationnelle/SKILL.md
- [ ] `add_data_table_rows` — cité par rapido-n8n/skills/memoire-operationnelle/SKILL.md
- [ ] `create_data_table` — cité par rapido-n8n/skills/memoire-operationnelle/SKILL.md
- [ ] `create_workflow_from_code` — cité par rapido-n8n/skills/usine-automatisations/SKILL.md
- [ ] `delete_data_table_column` — cité par rapido-n8n/skills/memoire-operationnelle/SKILL.md
- [ ] `execute_workflow` — cité par rapido-n8n/skills/surveillance-automatisations/SKILL.md
- [ ] `execute_workflow` — cité par rapido-n8n/skills/usine-automatisations/SKILL.md
- [ ] `get_execution` — cité par rapido-n8n/skills/surveillance-automatisations/SKILL.md
- [ ] `get_execution` — cité par rapido-n8n/skills/usine-automatisations/SKILL.md
- [ ] `get_node_types` — cité par rapido-n8n/skills/memoire-operationnelle/SKILL.md
- [ ] `get_node_types` — cité par rapido-n8n/skills/surveillance-automatisations/SKILL.md
- [ ] `get_node_types` — cité par rapido-n8n/skills/usine-automatisations/SKILL.md
- [ ] `get_sdk_reference` — cité par rapido-n8n/skills/usine-automatisations/SKILL.md
- [ ] `get_suggested_nodes` — cité par rapido-n8n/skills/usine-automatisations/SKILL.md
- [ ] `publish_workflow` — cité par rapido-n8n/skills/usine-automatisations/SKILL.md
- [ ] `update_workflow` — cité par rapido-n8n/skills/surveillance-automatisations/SKILL.md
- [ ] `update_workflow` — cité par rapido-n8n/skills/usine-automatisations/SKILL.md

