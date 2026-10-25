# Pièges vérifiés — serveur Plan'It (session live du 2026-10-25)

Comportements relevés sur le serveur réel (descriptions de `get_tools`,
`list_destructive_tools`, `list_mcp_servers`). À relire avant d'écrire un
workflow qui en dépend.

| Sujet | Piège | Parade |
|---|---|---|
| Tâche ou routine | Une tâche simple (rappel, action ponctuelle, fréquence `custom` autorisée) n'est PAS une routine. La routine (`is_routine`) est récurrente, pilotée par un objectif chiffré, **refuse `once` et `custom`**, et elle seule accepte une boucle KPI. | Qualifier la demande AVANT de choisir l'outil ; `attach_kpi_to_routine` échoue sur une tâche simple. |
| Référence figée | `attach_kpi_to_routine` FIGE la valeur de référence au rattachement (dernier relevé ; sinon une collecte est provoquée — qui peut coûter). `apply_routine_improvement` REFIGE la référence des KPI rattachés. | Prévenir avant chaque rattachement ; pour repartir d'une nouvelle référence : `detach` puis `attach`. |
| Verdicts | Boucle : improving / flat / degrading — ou `not_enough_data` tant que < 3 exécutions ET < 14 jours. Routine : effective / needs_improvement / no_measured_effect / failing / not_enough_data. | **Aucun effet annoncé sur `not_enough_data`** ; le hook verite-des-donnees le rappelle. |
| `throttled` | `refresh_kpi` trop rapproché renvoie l'instantané existant avec `throttled: true` et son âge en minutes. | Dire « valeur pas fraîche, relevée il y a N minutes », jamais « relevé du moment ». |
| Estimations | `estimate_routine_cost` donne sa base : `measured` (90 jours réels), `flat_price` ou `default`. | flat_price/default ne se présentent JAMAIS comme une mesure. |
| Propositions | `propose_routine` ENREGISTRE sans créer ; une proposition identique en attente est renvoyée telle quelle ; une proposition REFUSÉE n'est jamais reproposée à l'identique — changer l'horaire ne suffit pas. `propose_routine_improvement` : un seul changement, la dernière proposition remplace la précédente. | `list_pending_routine_actions` en début de séance pour ne rien reproposer ; accept/apply seulement sur l'accord explicite portant sur CETTE proposition. |
| Pause | On ne met JAMAIS une routine en pause de sa propre initiative, même en échec ou coûteuse (règle du serveur sur `pause_routine`). | Proposer d'abord une amélioration ; pause sur demande explicite seulement. |
| `resume_routine` | Refusé si un connecteur de la routine est débranché ; remet le compteur d'échecs à zéro et la consommation reprend. | Vérifier `list_mcp_servers` avant, annoncer le coût. |
| Calendrier | `get_calendar` : 62 jours au plus par appel ; un état autre que `done` ne veut JAMAIS dire « exécuté » ; les routines événementielles sont à part (`event_routines`, sans horaire). | Plages ≤ 62 j ; chevauchements vérifiés avant de proposer un horaire. |
| `select_routine_tools` | Passe par un modèle : jusqu'à TROIS MINUTES. | Prévenir l'utilisateur avant l'appel. |
| `add_mcp_server` | Enregistre l'URL mais NE CONNECTE RIEN (l'authentification se fait dans l'app) ; URL déjà connue = renvoie l'existant. Catalogue public et connecteur natif Plan'It : jamais supprimables. | Renvoyer vers l'écran Connecteurs après l'ajout ; `remove_mcp_server` réservé aux connecteurs ajoutés par l'utilisateur. |
| Connecteurs réels (relevé 2026-10-25) | Connectés : Gmail (62 outils), Plan'It natif (63), RapidoCMS (45), RapidoRH (22). **FoodEatUp en erreur** (« token expired », dernier succès 2026-07-10). **RapidoCRM déconnecté** (depuis le 2026-06-26). | Toute routine s'appuyant sur un connecteur en erreur/déconnecté sera refusée : relire `list_mcp_servers` du jour, et renvoyer vers l'app pour reconnecter. |
| Promotions | `list_promotions` fait foi (titre, cible, crédits offerts, fin). | Jamais une promotion hors liste, jamais un bonus déjà consommé promis. |
| Vidéo | `compose_video` : 1 crédit par tranche de 2 s, 5 minimum (10-60 s). | crédits = max(5, ⌈durée/2⌉) — calcul par script, coût annoncé avant. |
| Événements | `list_event_sources` ne montre que les connecteurs Composio RÉELLEMENT connectés ; `subscribe_event` en `auto` est refusé si la routine contient un outil destructif. | Gouvernance `validation` par défaut ; connecteur absent → proposer de le connecter. |
| Alertes | `decide_kpi_alert` refuse une alerte déjà traitée. | L'accord explicite de l'utilisateur AVANT de trancher, à chaque fois. |
