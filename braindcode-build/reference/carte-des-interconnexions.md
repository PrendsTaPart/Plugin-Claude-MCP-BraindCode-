# Carte des interconnexions — qui fait quoi, à quelle étape

Huit serveurs coopèrent autour d'une extension. Ce plugin est le CHEF DE
CHANTIER : il orchestre, il ne refait pas ce qu'un autre sait faire.

| Étape | Serveur(s) | Outils clés | Plugin délégué |
|---|---|---|---|
| Idée et contexte | braindcode-build | list_projects, get_project, get_project_context, get_published_project | — |
| Cahier des charges | braindcode-build + MCP produit + foodeatup-tutoriel | get_spec_prompt, save_project_spec ; tools/list du produit ; documentation_api_foodeatup | — |
| Maquettes | braindcode-build + Figma (serveur de SESSION, non déclaré — précédent rapido-design) | get_brand_guidelines, get_project_prompts (kind figma) | rapido-design (critique UX) |
| Construction | lovable | create_project, send_message, get_message, get_diff, render_project_widget | rapido-prompteur (prompts), rapido-lovable (apps) |
| Branchement MCP | lovable + braindcode-build | list_custom_connectors, add_connector ; request_human_validation (oauth/api_key) | rapido-lovable (kit connecteur) |
| Base de données | lovable | get_database_status, enable_database, query_database | — |
| Tests | lovable + academy | read_file, get_project (preview_url) ; formations recette | — |
| MCP de l'extension | lovable (edge function) + braindcode-build | save_project_progress (mcp_server_url, mcp_tools_count, mcp_auth_type, ai_validation_trace) | — |
| Déclaration orchestrateur | planit + marketplace-prompts | add_mcp_server, test_mcp_server, get_mcp_server_tools ; declarer_mcp | planit |
| Routine et boucle | braindcode-build + planit + academy + marketplace-prompts | get_project_routine_plan, attach_project_routine ; select_routine_tools, estimate_routine_cost, propose_routine ; check_routine_prompt ; auditer_routines | planit (exécution) |
| Plugin Claude Code | braindcode-build + ce dépôt | generate_plugin_scaffold ; normes marketplace | — (c'est ici) |
| Vitrine | braindcode-build + lovable | check_project_readiness, publish_project ; deploy_project, get_project_analytics | rapidocms (promotion en brouillon), rapido-prospector (calendrier) |
| Hackathon | braindcode-build + academy | list_hackathons, join_hackathon, register_pitch, get_clash_arena ; get_pitch_training | — |

## Serveurs optionnels

Figma (session), academy (`${ACADEMY_MCP_TOKEN}`), foodeatup-tutoriel :
absents, le skill saute le volet EN LE DISANT — rien ne casse, rien n'est
simulé.

## Ce qui ne se décide JAMAIS ici

Les secrets (éditeur Lovable ou tableau de bord), les paiements, la mise
en ligne et les validations OAuth : toujours `request_human_validation`
puis `get_pending_validations`.
