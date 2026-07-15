#!/usr/bin/env python3
"""Batterie de tests des skills, agents et hooks de la marketplace Rapido.

Python stdlib uniquement. Exit 0 = tout est vert (warnings tolérés) ;
exit 1 = au moins un FAIL bloquant.

Catégories par plugin :
- STRUCTURE (bloquant)  : frontmatter name+description, unicité des name,
  convention « Utiliser quand… » (avertissement pour les skills tiers listés
  dans ATTRIBUTIONS.md ; pour les agents, la convention maison est
  « Utiliser pour… » dans la description → avertissement seulement),
  placeholders (REMPLACER / À COMPLÉTER / TODO / lorem ipsum) hors code
  (les occurrences entre backticks ou dans un bloc ``` décrivent la
  convention, elles sont ignorées).
- RÉFÉRENCES (bloquant) : chemins ${CLAUDE_PLUGIN_ROOT}/… existants,
  scripts référencés existants et compilables (py_compile / bash -n),
  skills/agents mentionnés (« skill `x` », « agent `y` ») existants.
- MCP (avertissement)   : outils MCP cités vs serveurs déclarés dans
  .mcp.json, via un catalogue embarqué relevé sur les serveurs live
  (foodeatup, rapidocrm, rapidocms, rapidorh, canva, lovable, hyperframes).
  Les serveurs sans catalogue embarqué (facebook-ads, n8n, gmail,
  google-calendar, google-drive) sont signalés « à vérifier », sans échec.
- HOOKS (bloquant)      : hooks.json parse, scripts présents, et tests
  fonctionnels sur stdin (ask/deny/allow attendus par script de garde).
"""
import json
import os
import py_compile
import re
import subprocess
import sys
import tempfile

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- catalogue
# Noms d'outils relevés sur les serveurs MCP live (session du 2026-07-06).
# Les catalogues vivent côté serveur : ces listes servent aux AVERTISSEMENTS,
# jamais à un échec bloquant.
CATALOGUE = {
    "foodeatup": set("""add_temperature add_waitlist adjust_stock approve_leave assign_task
cancel_reservation checkin_reservation confirm_reservation create_category create_client
create_dish create_dish_category create_employee create_employee_contract create_expense
create_haccp_label create_haccp_reception create_haccp_tracabilite
create_hygiene_checklist_validation create_ingredient create_invoice create_notification
create_order create_product create_production_plan create_quote create_recipe
create_reservation create_shift create_supplier create_supplier_order create_table
create_tva create_zone delete_category delete_client delete_dish delete_employee
delete_ingredient delete_product delete_recipe finance_summary floor_plan_status
get_client get_employee get_expense get_ingredient get_invoice get_order get_product
get_production_ingredients get_quote get_recipe get_supplier import_storefront_menu
list_attendances list_categories list_cleaning_actions list_cleaning_zones list_clients
list_deliveries list_dishes list_employee_contracts list_employee_documents
list_employees list_expenses list_haccp_labels list_haccp_reception
list_haccp_temperatures list_haccp_tracabilite list_hygiene_checklists
list_ingredients list_invoices list_leaves list_low_stocks list_notifications
list_orders list_plannings list_production_alerts list_production_plans list_products
list_quotes list_recipes list_reservations list_stocks list_suppliers list_tables
list_top_productions list_tva list_units list_waitlist list_zones no_show_reservation
record_cleaning_action reject_leave reservation_availability search_entities seat_waitlist
update_category update_client update_dish update_employee update_employee_schedule
update_ingredient update_invoice_status update_kds_item_status update_order_status update_product
update_quote_status update_recipe update_table_status validate_production""".split()),
    "rapidocrm": set("""ajouter_prospect_pipeline close_opportunity create_campagne
create_commercial create_contact create_contrat create_contrat_template create_depense
create_devis create_editor_template create_entreprise create_evenement create_facture
create_product create_rdv create_segment create_task create_template_email
create_template_sms create_user delete_commercial delete_contact delete_contrat
delete_contrat_template delete_editor_template delete_entreprise delete_product
delete_template_email delete_template_sms deplacer_prospect_etape enregistrer_prospect
enregistrer_tous_prospects get_commercial get_contact get_contacts_segment get_contrat
get_conversion_par_canal get_dashboard_general_stats get_dashboard_kpis get_entreprise
get_facture get_formulaire_soumissions get_historique_prospect get_interaction_stats
get_loyalty_points get_pipeline get_product get_revenue_summary get_sondage_resultats
get_stats_campagne get_stats_pipeline get_stats_pipeline_global get_template
get_today_schedule get_top_clients get_user get_user_performance lancer_campagne
lancer_jeu_concours_entreprise lancer_sondage_entreprise list_campagnes
list_commerciaux list_contacts list_contrat_templates list_contrats list_cta
list_depenses list_devis list_editor_templates list_entreprises list_evenements
list_factures list_formulaires list_jeux_concours list_newsletters list_products
list_rdvs list_segments list_sondages list_templates_email list_templates_sms
list_users log_activity prospecter_entreprise prospecter_maps prospecter_prospect
recalculer_segment rechercher_entreprise_siret rechercher_prospects schedule_email
schedule_sms search_entreprises send_email send_newsletter send_sms
set_commercial_status update_commercial_objectifs update_commercial_profil
update_contact update_contrat_status update_contrat_template update_entreprise
update_product""".split()),
    "rapidocms": set("""add_asset add_card_page_link add_digital_card add_post_campagne add_prompt
assign_card_template cancel_schedules_post create_campagne create_draft_tool
create_post_template delete_campagne delete_card_page_link delete_digital_card
create_brand delete_brand delete_draft_tool delete_prompt edit_brand
edit_campagne edit_card_page edit_digital_card
edit_draft_tool edit_prompt generate_image get_brand get_company get_profile
ingishts_campagne list_all_files list_campagnes list_card_page list_card_templates
list_connected_accounts list_digital_card list_drafts_tool list_posts_campagne
list_prompts list_scheduled_posts post_insights remove_asset remove_post_campagne
schedule_draft_tool upload_file_tool""".split()),
    "rapidorh": set("""create-daily-tool create-project-link-tool create-project-tool
create-role-tool create-task-list-tool create-task-tool create-user-tool
delete-project-link-tool delete-user-tool get-dailies-tool get-departments-list-tool
get-permissions-list-tool get-project-documents-tool get-project-links-tool
get-project-tasks-tool get-projects-list-tool get-roles-list-tool get-task-lists-tool
get-users-list-tool move-task-tool update-project-link-tool update-user-tool""".split()),
    "canva": set("""cancel-editing-transaction comment-on-design commit-editing-transaction
copy-design create-brand-template-draft create-design-from-brand-template
create-design-from-candidate create-folder export-design generate-design
generate-design-structured get-assets get-brand-template-dataset get-design
get-design-content get-design-pages get-design-thumbnail get-export-formats
get-presenter-notes help import-design-from-url list-brand-kits list-comments
list-folder-items list-replies merge-designs move-item-to-folder
perform-editing-operations publish-brand-template reply-to-comment
request-outline-review resize-design resolve-shortlink search-brand-templates
search-designs search-folders start-editing-transaction upload-asset-from-url""".split()),
    "lovable": set("""add_connector create_project create_workspace_skill
delete_workspace_skill deploy_project disable_project_skill enable_database
enable_project_skill get_database_status get_diff get_file_upload_url get_me
get_message get_project get_project_analytics get_project_analytics_trend
get_project_knowledge get_workspace get_workspace_knowledge get_workspace_skill
list_available_connectors list_connections list_connectors list_custom_connectors
list_design_systems list_edits list_files list_messages list_project_skills
list_projects list_template_projects list_workspace_skills list_workspaces
move_projects_to_folder query_database read_file remix_project render_project_widget
send_message set_folder_visibility set_project_knowledge set_project_visibility
set_workspace_knowledge update_workspace_skill""".split()),
    "hyperframes": set("compose get_project get_project_status get_render_status "
                       "list_projects render_video".split()),
    "gmail": set("""apply_sensitive_message_label apply_sensitive_thread_label
create_draft create_label get_message get_thread label_message label_thread
list_drafts list_labels search_threads unlabel_message unlabel_thread""".split()),
    "google-calendar": set("""create_event delete_event get_event list_calendars
list_events respond_to_event suggest_time update_event""".split()),
    "google-drive": set("""copy_file create_file download_file_content
get_file_metadata get_file_permissions list_recent_files read_file_content
search_files""".split()),
    "n8n": set("""add_data_table_column add_data_table_rows archive_workflow
create_data_table create_workflow_from_code delete_data_table_column
execute_workflow get_execution get_node_types get_sdk_reference
get_suggested_nodes get_workflow_details prepare_test_pin_data publish_workflow
rename_data_table rename_data_table_column search_data_tables search_executions
search_folders search_nodes search_projects search_workflows test_workflow
unpublish_workflow update_workflow validate_workflow""".split()),
    "facebook-ads": set("""ads_account_get_activity_logs ads_activate_entity
ads_boost_ig_post ads_catalog_create ads_catalog_create_feed_rule
ads_catalog_create_product_feed ads_catalog_create_product_feed_upload_session
ads_catalog_create_product_set ads_catalog_delete_product
ads_catalog_get_catalogs ads_catalog_get_data_sources ads_catalog_get_details
ads_catalog_get_diagnostics ads_catalog_get_dynamic_ads_health
ads_catalog_get_event_source_catalogs ads_catalog_get_feed_rules
ads_catalog_get_product_details ads_catalog_get_product_feed_details
ads_catalog_get_product_feed_upload_sessions
ads_catalog_get_product_product_sets ads_catalog_get_product_set_details
ads_catalog_get_product_set_products ads_catalog_get_product_sets
ads_catalog_search_product ads_catalog_update_catalog ads_catalog_update_product
ads_catalog_update_product_feed ads_catalog_update_product_set ads_create_ad
ads_create_ad_set ads_create_campaign ads_create_creative
ads_create_custom_audience ads_delete_custom_audience
ads_experiment_abtest_create_test ads_experiment_abtest_get_test
ads_experiment_abtest_update_test ads_experiment_check_eligibility
ads_experiment_lift_create_test ads_experiment_lift_get_test
ads_experiment_list_tests ads_get_ad_account_custom_audiences
ads_get_ad_account_pages ads_get_ad_accounts ads_get_ad_entities
ads_get_ad_images ads_get_ad_preview ads_get_ad_videos ads_get_creative_ads
ads_get_creatives ads_get_custom_audience ads_get_custom_audience_adsets
ads_get_customconversions ads_get_dataset_details ads_get_dataset_quality
ads_get_dataset_stats ads_get_datasets ads_get_errors ads_get_field_context
ads_get_help_article ads_get_ig_accounts ads_get_ig_media
ads_get_opportunity_score ads_get_pages_for_business ads_get_user_pages
ads_insights_advertiser_context ads_insights_anomaly_signal
ads_insights_auction_ranking_benchmarks ads_insights_industry_benchmark
ads_insights_performance_trend ads_library_search ads_pixel_event_create
ads_pixel_event_delete ads_pixel_event_read ads_pixel_event_update
ads_pixel_parameter_create ads_pixel_parameter_delete ads_pixel_parameter_read
ads_pixel_parameter_update ads_update_custom_audience
ads_update_custom_audience_users ads_update_entity""".split()),
    "stripe": set("""fetch_stripe_resources search_stripe_documentation
search_stripe_resources send_stripe_mcp_feedback stripe_api_details
stripe_api_read stripe_api_search stripe_api_write
stripe_implementation_planner""".split()),
}
# Serveurs dont le catalogue d'outils vit à distance : un outil qui leur est
# attribuable passe en INFO (à vérifier en ligne, MCP connectés), pas en WARN.
# canva : OAuth non connecté dans la session du 2026-07-10 — seul catalogue
# non re-vérifiable en live (relevé du 2026-07-06 embarqué ci-dessus).
SERVEURS_CATALOGUE_DISTANT = ["canva"]
SERVEURS_SANS_CATALOGUE = set()
PREFIXES_OUTIL = ("create", "list", "get", "update", "delete", "add", "edit", "send",
                  "schedule", "cancel", "remove", "upload", "generate", "assign", "move",
                  "publish", "unpublish", "archive", "execute", "activate", "ads")

# --------------------------------------------------- tests fonctionnels hooks
# base : par nom de script ; extras : par (plugin, script).
TESTS_HOOKS = {
    "garde-destructif.py": [
        ({"tool_name": "mcp__test__delete_x", "tool_input": {}}, "ask"),
    ],
    "anti-donnee-inventee.py": [
        ({"tool_name": "mcp__foodeatup__add_temperature", "tool_input": {"temperature": 150, "equipment_id": 12}}, "deny"),
        ({"tool_name": "mcp__foodeatup__add_temperature", "tool_input": {"temperature": 4, "equipment_id": 12}}, "allow"),
        ({"tool_name": "mcp__foodeatup__add_temperature", "tool_input": {"temperature": 4}}, "deny"),
    ],
    "garde-argent-reel.py": [
        ({"tool_name": "mcp__facebook-ads__ads_activate_entity", "tool_input": {}}, "ask"),
        ({"tool_name": "mcp__facebook-ads__ads_boost_ig_post", "tool_input": {"confirmed": False}}, "allow"),
    ],
    "plafond-budget.py": [
        ({"tool_name": "mcp__facebook-ads__ads_create_entity", "tool_input": {"daily_budget": 999900}}, "deny"),
        ({"tool_name": "mcp__facebook-ads__ads_create_entity", "tool_input": {"daily_budget": 1000}}, "allow"),
    ],
    "garde-production.py": [
        ({"tool_name": "mcp__n8n__execute_workflow", "tool_input": {}}, "ask"),
        ({"tool_name": "mcp__n8n__execute_workflow", "tool_input": {"executionMode": "manual"}}, "allow"),
        ({"tool_name": "mcp__n8n__publish_workflow", "tool_input": {}}, "ask"),
    ],
    "garde-ecriture-kb.py": [
        ({"tool_name": "Write", "tool_input": {"file_path": "./rapido-kb/startup/forge/bootcamp/jour1.md"}}, "allow"),
        ({"tool_name": "Write", "tool_input": {"file_path": "foodeatup/skills/x/SKILL.md"}}, "deny"),
        ({"tool_name": "Write", "tool_input": {"file_path": "/tmp/entrees.json"}}, "allow"),
    ],
    "rappel-argent-reel.py": [
        ({"tool_name": "mcp__facebook-ads__ads_create_campaign", "tool_input": {}}, "ask"),
    ],
    "garde-irreversible.py": [
        ({"tool_name": "mcp__google-calendar__delete_event", "tool_input": {}}, "ask"),
    ],
}
TESTS_HOOKS_EXTRAS = {
    ("rapidocrm", "garde-destructif.py"): [
        ({"tool_name": "mcp__rapidocrm__update_invoice_status",
          "tool_input": {"statut": "brouillon"}}, "deny"),
        ({"tool_name": "mcp__rapidocrm__update_invoice_status",
          "tool_input": {"statut": "payee"}}, "ask"),
        ({"tool_name": "mcp__rapidocrm__create_depense",
          "tool_input": {"entreprise_id": 1, "total_ht": 100}}, "ask"),
    ],
    ("rapido-suite", "garde-destructif.py"): [
        ({"tool_name": "mcp__rapidocrm__update_invoice_status",
          "tool_input": {"statut": "brouillon"}}, "deny"),
    ],
    # delete_prompt / delete_brand sont attrapés par le motif delete_.* du
    # matcher rapidocms ; remove_asset est explicite — tests pour figer la
    # couverture (audit 2026-07-10, étendu couche marque 2026-07-14).
    ("rapidocms", "garde-destructif.py"): [
        ({"tool_name": "mcp__rapidocms__delete_prompt",
          "tool_input": {"prompt_id": 1}}, "ask"),
        ({"tool_name": "mcp__rapidocms__delete_brand",
          "tool_input": {"brand_id": 14}}, "ask"),
        ({"tool_name": "mcp__rapidocms__remove_asset",
          "tool_input": {"asset_id": 12}}, "ask"),
    ],
    ("rapido-higgsfield", "garde-couts.py"): [
        ({"tool_name": "mcp__huggsfield__generate_video", "tool_input": {}}, "deny"),
        ({"tool_name": "mcp__huggsfield__generate_video",
          "tool_input": {"get_cost": True}}, "allow"),
        ({"tool_name": "mcp__huggsfield__generate_image",
          "tool_input": {"cout_confirme": True}}, "allow"),
        ({"tool_name": "mcp__huggsfield__show_medias", "tool_input": {}}, "allow"),
    ],
    ("rapido-higgsfield", "garde-voix.py"): [
        ({"tool_name": "mcp__huggsfield__create_voice", "tool_input": {}}, "ask"),
        ({"tool_name": "mcp__huggsfield__dubbing", "tool_input": {}}, "ask"),
        ({"tool_name": "mcp__huggsfield__generate_image", "tool_input": {}}, "allow"),
    ],
    ("rapido-marketing", "garde-envois.py"): [
        ({"tool_name": "mcp__rapidocrm__send_newsletter",
          "tool_input": {"entreprise_id": 1}}, "ask"),
        ({"tool_name": "mcp__rapidocrm__schedule_email",
          "tool_input": {"entreprise_id": 1, "date_envoi": "2026-07-20 09:00:00", "sujet": "x"}}, "ask"),
        ({"tool_name": "mcp__rapidocms__schedule_draft_tool",
          "tool_input": {"draft_id": 1}}, "ask"),
        ({"tool_name": "mcp__facebook-ads__ads_activate_entity",
          "tool_input": {}}, "ask"),
    ],
    ("rapido-google-ads", "garde-ecriture-google-ads.py"): [
        ({"tool_name": "mcp__google-ads__mutate_campaign", "tool_input": {}}, "ask"),
        ({"tool_name": "mcp__google-ads__create_campaign_budget", "tool_input": {}}, "ask"),
        ({"tool_name": "mcp__google-ads__search", "tool_input": {}}, "allow"),
        ({"tool_name": "mcp__analytics__run_report", "tool_input": {}}, "allow"),
    ],
    ("rapido-seo", "garde-couts-seo.py"): [
        ({"tool_name": "mcp__dataforseo__backlinks_bulk_summary", "tool_input": {}}, "ask"),
        ({"tool_name": "mcp__dataforseo__serp_organic_live", "tool_input": {}}, "ask"),
        ({"tool_name": "mcp__dataforseo__backlinks_bulk_summary",
          "tool_input": {"cout_confirme": True}}, "allow"),
        ({"tool_name": "mcp__gsc__search_analytics", "tool_input": {}}, "allow"),
        ({"tool_name": "mcp__analytics__run_report", "tool_input": {}}, "allow"),
    ],
    ("rapido-elevenlabs", "garde-couts.py"): [
        ({"tool_name": "mcp__ElevenLabs__text_to_speech", "tool_input": {}}, "ask"),
        ({"tool_name": "mcp__ElevenLabs__text_to_speech",
          "tool_input": {"cout_confirme": True}}, "allow"),
        ({"tool_name": "mcp__ElevenLabs__list_voices", "tool_input": {}}, "allow"),
    ],
    ("rapido-elevenlabs", "garde-voix.py"): [
        ({"tool_name": "mcp__ElevenLabs__voice_clone", "tool_input": {}}, "ask"),
        ({"tool_name": "mcp__ElevenLabs__voice_design", "tool_input": {}}, "ask"),
        ({"tool_name": "mcp__ElevenLabs__text_to_speech", "tool_input": {}}, "allow"),
    ],
    ("rapido-elevenlabs", "garde-appels.py"): [
        ({"tool_name": "mcp__ElevenLabs__make_outbound_call", "tool_input": {}}, "ask"),
        ({"tool_name": "mcp__ElevenLabs__text_to_speech", "tool_input": {}}, "allow"),
    ],
    ("rapido-prompteur", "anti-ip.py"): [
        # prompt propre → allow
        ({"tool_name": "mcp__huggsfield__generate_image",
          "tool_input": {"params": {"prompt": "a cute cat, soft light, studio backdrop"}}}, "allow"),
        # IP/marque présente → ask (confirmation avec avertissement)
        ({"tool_name": "mcp__huggsfield__generate_image",
          "tool_input": {"params": {"prompt": "a stormtrooper from Star Wars"}}}, "ask"),
        # formule « style de [artiste] » → ask
        ({"tool_name": "mcp__RapidoCMS__images_to_image",
          "tool_input": {"prompt": "portrait in the style of Wes Anderson",
                         "images": "https://x/a.png"}}, "ask"),
        # brief web propre (Lovable) → allow
        ({"tool_name": "mcp__Lovable__send_message",
          "tool_input": {"message": "build a landing page for a local bakery"}}, "allow"),
        # outil non génératif (défense en profondeur) → allow
        ({"tool_name": "mcp__huggsfield__show_medias", "tool_input": {}}, "allow"),
    ],
    ("rapidocms", "valide_charte_hook.py"): [
        # couleurs
        ({"tool_name": "mcp__rapidocms__create_brand",
          "tool_input": {"couleurs": "bleu"}}, "deny"),
        ({"tool_name": "mcp__rapidocms__create_brand",
          "tool_input": {"couleurs": "#00F"}}, "deny"),
        ({"tool_name": "mcp__rapidocms__create_brand",
          "tool_input": {"couleurs": "#0055FF,#FFFFFF"}}, "allow"),
        # font_family
        ({"tool_name": "mcp__rapidocms__create_brand",
          "tool_input": {"font_family": "Montserrat"}}, "deny"),
        ({"tool_name": "mcp__rapidocms__edit_brand",
          "tool_input": {"brand_id": 1, "font_family": "Arial, sans-serif"}}, "allow"),
        # logo / site_web http(s)
        ({"tool_name": "mcp__rapidocms__create_brand",
          "tool_input": {"logo": "/tmp/logo.png"}}, "deny"),
        # images_to_image
        ({"tool_name": "mcp__rapidocms__images_to_image",
          "tool_input": {"images": "/tmp/a.png"}}, "deny"),
        ({"tool_name": "mcp__rapidocms__images_to_image",
          "tool_input": {"images": "https://x/a.png,https://x/b.png"}}, "allow"),
        ({"tool_name": "mcp__rapidocms__images_to_image",
          "tool_input": {"images": "https://x/a.png,https://x/b.png,https://x/c.png,https://x/d.png"}}, "deny"),
        # upload_file_tool
        ({"tool_name": "mcp__rapidocms__upload_file_tool",
          "tool_input": {"type": "audio", "file_url": "https://x/a.mp3"}}, "deny"),
        ({"tool_name": "mcp__rapidocms__upload_file_tool",
          "tool_input": {"type": "image", "file_url": "https://x/a.png"}}, "allow"),
    ],
}

RX_FRONT = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
# le span peut se replier sur la ligne suivante (listes de termes longues)
RX_INLINE_CODE = re.compile(r"`[^`]{1,400}`", re.S)
# une citation courte entre guillemets droits est un EXEMPLE pédagogique
# (ex. « never "Lorem ipsum" » dans made-to-stick), pas un placeholder
RX_QUOTED = re.compile(r'"[^"\n]{1,80}"')
RX_FENCE = re.compile(r"^```.*?^```", re.S | re.M)
RX_PLACEHOLDERS = [("REMPLACER", re.compile(r"\bREMPLACER\b")),
                   ("À COMPLÉTER", re.compile(r"À COMPLÉTER")),
                   ("TODO", re.compile(r"\bTODO\b")),
                   ("lorem ipsum", re.compile(r"lorem ipsum", re.I))]
RX_PLUGIN_ROOT = re.compile(r"\$\{CLAUDE_PLUGIN_ROOT\}/([\w\-./]+)")
RX_SCRIPT = re.compile(r"`([\w\-./]+\.(?:py|sh|cjs))`")
RX_MENTION = re.compile(r"(?:\bskills?|\bagents?)\s+`([a-z0-9][a-z0-9\-]*)`", re.I)
RX_TOKEN = re.compile(r"`([a-z][a-z0-9_\-]{2,})`")


def lire(chemin):
    with open(chemin, encoding="utf-8") as f:
        return f.read()


def frontmatter(texte):
    """Retourne (name, description) ou (None, None). Gère les scalaires pliés."""
    m = RX_FRONT.match(texte)
    if not m:
        return None, None
    bloc = m.group(1)
    valeurs = {}
    for cle in ("name", "description"):
        mm = re.search(rf"^{cle}:\s*(.*)$", bloc, re.M)
        if not mm:
            continue
        val = mm.group(1).strip()
        if val in (">", ">-", "|", "|-"):  # scalaire multi-lignes
            suite, pos = [], bloc.find(mm.group(0)) + len(mm.group(0))
            for ligne in bloc[pos:].splitlines():
                if ligne.startswith((" ", "\t")) and ligne.strip():
                    suite.append(ligne.strip())
                elif ligne.strip():
                    break
            val = " ".join(suite)
        valeurs[cle] = val.strip("\"'")
    return valeurs.get("name"), valeurs.get("description")


def sans_code(texte):
    return RX_QUOTED.sub("", RX_INLINE_CODE.sub("", RX_FENCE.sub("", texte)))


def skills_externes(plugin_dir):
    """Names des skills tiers d'après ATTRIBUTIONS.md (racine ou skills/)."""
    noms = set()
    for cand in (os.path.join(plugin_dir, "ATTRIBUTIONS.md"),
                 os.path.join(plugin_dir, "skills", "ATTRIBUTIONS.md")):
        if os.path.isfile(cand):
            for ligne in lire(cand).splitlines():
                m = re.match(r"\|\s*`([a-z0-9\-]+)", ligne)
                if m:
                    noms.add(m.group(1))
    return noms


def executer_hook(chemin, payload):
    """Retourne 'ask' / 'deny' / 'allow' / 'erreur:…' pour un script de garde."""
    interp = ["python3"] if chemin.endswith(".py") else ["bash"]
    try:
        r = subprocess.run(interp + [chemin], input=json.dumps(payload),
                           capture_output=True, text=True, timeout=10, cwd=RACINE)
    except Exception as e:  # noqa: BLE001
        return f"erreur:{e}"
    if r.returncode == 2:
        return "deny" if r.stderr.strip() else "erreur:exit 2 sans stderr"
    if r.returncode != 0:
        return f"erreur:exit {r.returncode} ({r.stderr.strip()[:80]})"
    if r.stdout.strip():
        try:
            decision = (json.loads(r.stdout)["hookSpecificOutput"]["permissionDecision"])
            return decision  # "ask" attendu
        except Exception:  # noqa: BLE001
            return "erreur:stdout non-JSON"
    return "allow"


def main():
    os.chdir(RACINE)
    plugins = sorted(d for d in os.listdir(".")
                     if os.path.isfile(os.path.join(d, ".claude-plugin", "plugin.json")))
    # Index global des names (skills + agents), pour le test des mentions.
    index_global, fichiers_md = {}, {}
    for p in plugins:
        for genre, dossier in (("skill", "skills"), ("agent", "agents")):
            base = os.path.join(p, dossier)
            if not os.path.isdir(base):
                continue
            cibles = ([os.path.join(base, d, "SKILL.md") for d in sorted(os.listdir(base))]
                      if genre == "skill" else
                      [os.path.join(base, f) for f in sorted(os.listdir(base)) if f.endswith(".md")])
            for chemin in cibles:
                if os.path.isfile(chemin) and os.path.basename(chemin) != "ATTRIBUTIONS.md":
                    fichiers_md.setdefault(p, []).append((genre, chemin))
                    nom, _ = frontmatter(lire(chemin))
                    if nom:
                        index_global[nom] = chemin

    verbose = "--verbose" in sys.argv
    total = {"FAIL": 0, "WARN": 0, "INFO": 0}
    details_fail, details_warn = [], []
    infos_globales = []  # (plugin, fichier, outil, serveurs candidats)

    print("=" * 72)
    print("RAPPORT tester-skills.py — marketplace Rapido")
    print("=" * 72)

    for p in plugins:
        externes = skills_externes(p)
        serveurs = []
        mcp_path = os.path.join(p, ".mcp.json")
        if os.path.isfile(mcp_path):
            serveurs = list(json.load(open(mcp_path)).get("mcpServers", {}).keys())
        cat_plugin = {"STRUCTURE": "OK", "RÉFÉRENCES": "OK", "MCP": "OK", "HOOKS": "OK"}
        lignes = []

        def est_externe(chemin):
            m = re.search(rf"{re.escape(p)}/skills/([^/]+)/", chemin + "/")
            return bool(m) and m.group(1) in externes

        def probleme(cat, niveau, msg):
            cat_plugin[cat] = "FAIL" if niveau == "FAIL" else (
                "WARN" if cat_plugin[cat] != "FAIL" else "FAIL")
            total[niveau] += 1
            lignes.append(f"    [{niveau}] {cat} — {msg}")
            (details_fail if niveau == "FAIL" else details_warn).append(f"{p}: {msg}")

        # ---------------- STRUCTURE
        noms_vus = {}
        for genre, chemin in fichiers_md.get(p, []):
            texte = lire(chemin)
            nom, desc = frontmatter(texte)
            rel = os.path.relpath(chemin)
            if not nom or not desc:
                probleme("STRUCTURE", "FAIL", f"{rel} : frontmatter sans name/description valides")
                continue
            if nom in noms_vus:
                probleme("STRUCTURE", "FAIL",
                         f"doublon de name `{nom}` : {noms_vus[nom]} et {rel}")
            noms_vus[nom] = rel
            if genre == "skill":
                # Convention BLOQUANTE pour tous, skills tiers compris : leurs
                # descriptions sont francisées (voir ATTRIBUTIONS.md), seul le
                # corps reste l'original attribué.
                if not desc.startswith("Utiliser quand"):
                    probleme("STRUCTURE", "FAIL",
                             f"{rel} : description ne commence pas par « Utiliser quand »")
            elif "Utiliser pour" not in desc and "Utiliser quand" not in desc:
                probleme("STRUCTURE", "WARN",
                         f"{rel} : description d'agent sans « Utiliser pour/quand »")
        # placeholders : tous les .md du plugin, hors code
        for root, dirs, files in os.walk(p):
            for f in sorted(files):
                if not f.endswith(".md"):
                    continue
                chemin = os.path.join(root, f)
                nu = sans_code(lire(chemin))
                for etiquette, rx in RX_PLACEHOLDERS:
                    n = len(rx.findall(nu))
                    if n:
                        niveau_ph = "WARN" if est_externe(chemin) else "FAIL"
                        probleme("STRUCTURE", niveau_ph,
                                 f"{chemin} : placeholder « {etiquette} » ×{n} (hors code)"
                                 + (" (skill tiers, contenu non modifié)"
                                    if niveau_ph == "WARN" else ""))

        # ---------------- RÉFÉRENCES
        for genre, chemin in fichiers_md.get(p, []):
            texte = lire(chemin)
            rel = os.path.relpath(chemin)
            for cible in RX_PLUGIN_ROOT.findall(texte):
                cible = cible.rstrip(".,;:")
                if not os.path.exists(os.path.join(p, cible)):
                    probleme("RÉFÉRENCES", "FAIL",
                             f"{rel} : ${{CLAUDE_PLUGIN_ROOT}}/{cible} introuvable")
            for script in set(RX_SCRIPT.findall(texte)):
                base_dir = os.path.dirname(chemin)
                candidats = [os.path.join(base_dir, script), os.path.join(p, script)]
                trouve = next((c for c in candidats if os.path.isfile(c)), None)
                if trouve is None:  # dernier essai : même nom quelque part dans le skill
                    for root, _, files in os.walk(base_dir):
                        if os.path.basename(script) in files:
                            trouve = os.path.join(root, os.path.basename(script))
                            break
                # Contenu tiers : on ne modifie pas les skills importés, un
                # exemple de nom de fichier dans leur prose ne bloque pas.
                niveau_ref = "WARN" if est_externe(chemin) else "FAIL"
                if trouve is None:
                    probleme("RÉFÉRENCES", niveau_ref,
                             f"{rel} : script `{script}` introuvable"
                             + (" (skill tiers)" if niveau_ref == "WARN" else ""))
                elif trouve.endswith(".py"):
                    try:
                        with tempfile.NamedTemporaryFile(suffix=".pyc", delete=True) as tmp:
                            py_compile.compile(trouve, doraise=True, cfile=tmp.name)
                    except Exception as e:  # noqa: BLE001
                        probleme("RÉFÉRENCES", "FAIL", f"{trouve} : py_compile échoue ({e})")
                elif trouve.endswith(".sh"):
                    r = subprocess.run(["bash", "-n", trouve], capture_output=True, text=True)
                    if r.returncode:
                        probleme("RÉFÉRENCES", "FAIL",
                                 f"{trouve} : bash -n échoue ({r.stderr.strip()[:80]})")
            for mention in set(RX_MENTION.findall(texte)):
                if mention not in index_global:
                    probleme("RÉFÉRENCES", "FAIL",
                             f"{rel} : mention du skill/agent `{mention}` qui n'existe pas")

        # ---------------- MCP (avertissements)
        catalogues_declares = set().union(*(CATALOGUE.get(s, set()) for s in serveurs)) \
            if serveurs else set()
        tous_outils = set().union(*CATALOGUE.values())
        distants = [s for s in serveurs if s in SERVEURS_CATALOGUE_DISTANT]
        infos_plugin = 0
        for genre, chemin in fichiers_md.get(p, []):
            if os.path.join(p, "skills") not in chemin and genre != "agent":
                continue
            rel = os.path.relpath(chemin)
            for token in set(RX_TOKEN.findall(lire(chemin))):
                if "." in token or token in index_global:
                    continue
                ressemble = (token.split("_")[0].split("-")[0] in PREFIXES_OUTIL
                             or token.endswith(("_tool", "-tool")))
                if token in catalogues_declares:
                    continue  # outil connu d'un serveur déclaré : OK
                if token in tous_outils:
                    ou = [s for s, c in CATALOGUE.items() if token in c]
                    probleme("MCP", "WARN",
                             f"{rel} : `{token}` appartient à {'/'.join(ou)}, "
                             f"serveur(s) non déclaré(s) dans {p}/.mcp.json")
                elif ressemble:
                    if distants:
                        # attribuable à un serveur au catalogue distant : INFO
                        total["INFO"] += 1
                        infos_plugin += 1
                        candidats = [s for s in distants
                                     if s in SERVEURS_SANS_CATALOGUE] or distants
                        infos_globales.append((p, rel, token, "/".join(candidats)))
                        if verbose:
                            lignes.append(f"    [INFO] MCP — {rel} : `{token}` à vérifier "
                                          f"en ligne (serveur(s) candidat(s) : "
                                          f"{'/'.join(candidats)})")
                    else:
                        probleme("MCP", "WARN",
                                 f"{rel} : `{token}` introuvable dans les catalogues des "
                                 f"serveurs déclarés ({', '.join(serveurs)})")
        if infos_plugin and not verbose:
            lignes.append(f"    (INFO) MCP — {infos_plugin} outil(s) à vérifier en ligne "
                          "(catalogues distants) — relancer avec --verbose pour le détail, "
                          "checklist : tests/rapports/outils-a-verifier-en-ligne.md")

        # ---------------- HOOKS
        hooks_json = os.path.join(p, "hooks", "hooks.json")
        if os.path.isfile(hooks_json):
            try:
                contenu = json.load(open(hooks_json))
            except Exception as e:  # noqa: BLE001
                probleme("HOOKS", "FAIL", f"{hooks_json} ne parse pas ({e})")
                contenu = {}
            scripts_ref = re.findall(r"\$\{CLAUDE_PLUGIN_ROOT\}/([\w\-./]+)",
                                     json.dumps(contenu))
            for s in sorted(set(scripts_ref)):
                chemin_s = os.path.join(p, s)
                if not os.path.isfile(chemin_s):
                    probleme("HOOKS", "FAIL", f"{hooks_json} référence {s} qui n'existe pas")
                    continue
                base = os.path.basename(s)
                cas = list(TESTS_HOOKS.get(base, [])) + \
                    list(TESTS_HOOKS_EXTRAS.get((p, base), []))
                if base.endswith(".sh"):
                    r = subprocess.run(["bash", "-n", chemin_s], capture_output=True, text=True)
                    if r.returncode:
                        probleme("HOOKS", "FAIL", f"{chemin_s} : bash -n échoue")
                for payload, attendu in cas:
                    obtenu = executer_hook(chemin_s, payload)
                    if obtenu != attendu:
                        probleme("HOOKS", "FAIL",
                                 f"{chemin_s} : {json.dumps(payload['tool_name'])} "
                                 f"+ {json.dumps(payload.get('tool_input', {}), ensure_ascii=False)} "
                                 f"→ attendu {attendu}, obtenu {obtenu}")

        etat = " | ".join(f"{k}:{v}" for k, v in cat_plugin.items())
        print(f"\n{p}  [{etat}]")
        for ligne in lignes:
            print(ligne)
        if not lignes:
            print("    (aucun problème)")

    print("\n" + "=" * 72)
    print(f"RÉSUMÉ GLOBAL : {len(plugins)} plugins — "
          f"{total['FAIL']} FAIL, {total['WARN']} WARN, {total['INFO']} INFO "
          "(outils de serveurs à catalogue distant, à vérifier en ligne)")
    print("=" * 72)
    return 1 if total["FAIL"] else 0


if __name__ == "__main__":
    sys.exit(main())
