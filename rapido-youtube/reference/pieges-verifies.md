# Pièges vérifiés — serveur Rapido YouTube (relevé du 2026-10-25)

| Piège | Constat vérifié | Parade |
|---|---|---|
| Appeler un ancien nom d'outil | le serveur expose 172 outils : 86 `yt_` + 86 alias dépréciés, « retiré le 2026-12-31 » dans chaque description | inventaire yt_ seul, contrôle CI des alias, hook alias-deprecies (deny avec le bon nom) |
| Croire le serveur ouvert | https://youtube.rapidocms.com/mcp répond 401 (OAuth Supabase, `.well-known/oauth-protected-resource`, ressource « YouTube Publisher Bot ») | OAuth au premier appel ; aucun jeton dans le dépôt ; sans session connectée, pas de recette live |
| Publier « vers la bonne chaîne » sans la nommer | sans channel_id : chaîne ACTIVE, sinon FAVORITE ; divergence signalée par yt_get_channel_status | règle du plugin : channel_id explicite + nom annoncé (hook garde-chaine) |
| Lancer une campagne sans lire le quota | au relevé du propriétaire (2026-10-25) : risque **will_fail** — 6 400/10 000 consommées + 4 800 réservées aux 3 publications sous 24 h = 1 200 au-dessus du plafond, disponible à la demande ZÉRO ; au moins une des 3 publications risque d'échouer | yt_get_quota_status AVANT tout ; hook garde-quota (deny sans lecture < 30 min ou sur will_fail, ask sur tight) ; vérifier le planning du soir |
| Compter sur la distribution | AUCUN compte de distribution connecté au relevé | yt_list_connected_accounts d'abord ; sinon page Distribution de l'application, ou délégation rapidocms |
| Chercher la chaîne RapidoRH | 4 chaînes connectées : FoodEatUp (active ET favorite), RapidoCMS, RapidoCRM, Formation Braindcode — il n'y a PAS de chaîne RapidoRH | reference/chaines.md ; les vidéos RapidoRH tuto partent sur la chaîne qui les porte réellement, à confirmer avec l'humain |
| Double envoi sur erreur réseau | client_request_id rend l'opération idempotente | toujours le poser sur publish/schedule ; ne jamais ré-émettre sans lui |
| Publier public par défaut | la privacy vaut private par défaut côté serveur | public UNIQUEMENT sur accord (hook garde-public) |
| Gros fichier en upload direct | au-delà d'un fichier volumineux l'envoi direct échoue | yt_create_upload_url puis yt_register_uploaded_video |
| Lot > 10 | yt_bulk_schedule accepte 10 vidéos au plus ; yt_create_bulk_job jusqu'à 500 | découper ; preview_only AVANT tout job réel (hook garde-lot) |
| Créneaux « magiques » | les suggestions viennent de l'historique réel ; sans historique l'outil le dit | restituer tel quel, ne jamais broder |
| Publier un clip non rendu | le rendu se fait dans l'APPLICATION avant yt_publish_clip | yt_get_clip jusqu'au statut rendu ; le dire à l'humain |
| Lire un score comme une mesure | scores de titres et score viral des clips = estimations | les présenter comme telles, toujours |
| Conclure un A/B trop tôt | gagnant seulement si confiance > 95 % ET 100 impressions/phase ; sinon non concluant, miniature A restaurée ; donnée absente ≠ zéro | annoncer exactement le verdict de l'outil |
| Réessayer dans le mur | uploadLimitExceeded < 24 h : yt_retry_videos refuse et donne l'heure de réarmement | attendre l'heure donnée, la dire |
| Effacer la grille par accident | yt_set_schedule_slots REMPLACE toute la grille ; liste vide = effacement | lire yt_list_schedule_slots avant, montrer la nouvelle grille, confirmation explicite pour vider (hook garde-grille) |
| Croire la vidéo supprimée | yt_delete_video supprime l'entrée et le fichier DANS L'APPLICATION — la vidéo publiée reste sur YouTube | le rappeler dans chaque confirmation (hook garde-destructif-youtube) |
| Visage d'autrui | yt_swap_face et face_model_id : uniquement un modèle de visage de l'utilisateur, listé dans la session (yt_list_face_models) | hook garde-visage (deny hors liste) ; yt_clone_style_from_url = ambiance, jamais marque/logo/personnage/visage d'autrui |
| Liens de miniatures en dur | les aperçus sont des liens signés TEMPORAIRES | jamais copiés dans un contenu durable (description, page, widget commité) |
