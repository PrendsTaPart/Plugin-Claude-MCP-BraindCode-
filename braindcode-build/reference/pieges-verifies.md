# Pièges vérifiés — Build, Lovable et leurs voisins (relevé du 2026-10-25)

| Piège | Constat vérifié | Parade |
|---|---|---|
| Croire le serveur Build ouvert | https://build.braindcode.com/api/mcp répond 401 (OAuth Supabase, audience authenticated — manifeste du projet) | authentification au premier appel ; aucun jeton dans le dépôt ; sans session connectée, pas de recette Build |
| Se fier au compte d'outils de l'Academy | la fiche get_build_braindcode (2026-10-07) liste 37 outils ; le manifeste live en expose 44 | l'inventaire versionné (44) fait foi ; l'Academy sert la MÉTHODE, pas l'inventaire |
| Supposer les outils d'un MCP produit | la méthode (étape 02) l'interdit explicitement | tools/list à chaque session, manifeste en cache, capacité absente SIGNALÉE |
| Prendre le statut Lovable de premier niveau pour terminal | create_project est asynchrone ; le vrai état est response.status | suivre par get_message / get_project / render_project_widget |
| Répondre à une pause par un send_message | un nouveau send_message ANNULE la pause en cours | respond_to_approval avec l'event_id et le message_id de la pause, décision humaine seulement |
| Écraser le knowledge | set_project_knowledge REMPLACE tout le contenu | get_project_knowledge d'abord, fusion, puis écriture (hook) |
| Ajouter un connecteur Lovable « par outil » | add_connector renvoie un lien profond vers le tableau de bord | l'humain finit la connexion ; request_human_validation (oauth/api_key) |
| Catalogue Lovable périmé | 5 outils du relevé embarqué ont disparu (enable/disable_project_skill, list_available_connectors, list_connections, list_project_skills) ; 3 nouveaux (initiate_project, respond_to_approval, import-claude-design-from-url) | docs/inventaires/lovable-tools-live.txt (2026-10-25) fait foi |
| Inventer une image d'agent | add_project_agent attend les photos OFFICIELLES de get_project_agents | jamais d'URL d'image inventée |
| register_ai_developer oublié | get_prompt_execution_plan suppose le projet créé et l'idée réservée | register_ai_developer (mode hybride par défaut) passe AVANT |
| Hackathon « ouvert » qui ne l'est plus | braindcode-2026 marqué ouvert alors qu'il s'est terminé le 14 octobre (jury le 16) — relevé du propriétaire | vérifier les dates de get_hackathon avant de proposer join_hackathon ; signaler l'écart |
| Vitrines « lauréat » incomplètes | les 20 réalisations publiées n'ont pas de tutoriel ; RapidoRH Ascend et PodForge Collective n'ont pas de démo ; Daily Brief est en brouillon (démo, tutoriel, fonctionnement, modèle économique manquants) — relevé du propriétaire | skill `completer-les-vitrines`, projet par projet, republication sur accord |
| business_model inventé | la vitrine attend un modèle économique et un pricing | UNIQUEMENT sur indication de l'humain — sinon champ laissé vide et dit |
| Secret dans une trace | les demandes, blocages et traces sont relus par des humains | hook anti-secret (deny) + journal masqué ; les secrets vivent dans l'éditeur Lovable |
