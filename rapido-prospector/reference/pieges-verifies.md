# Pièges vérifiés — serveur Prospect (relevé du 2026-10-25)

Constats faits sur le serveur réel (sonde HTTP + manifeste MCP du projet,
commit 6ad9af2). À relire avant d'écrire ou de corriger un skill.

| Piège | Constat vérifié | Parade |
|---|---|---|
| Croire la prospection enregistrée | `run_prospection` renvoie les prospects trouvés mais ne les sauvegarde pas | enchaîner dédoublonnage → accord → `add_clients` (city + speciality) → `add_log` |
| Envoyer sur LinkedIn sans enrichir | `send_linkedin_invite` et `send_linkedin_message` exigent un provider_id que seul `enrich_linkedin_profile` pose (avec un `account_id` de `list_linkedin_accounts`) | enrichir d'abord, par lot réduit et sur accord ; `enrichedOnly: true` pour lister les profils prêts |
| Croire le calendrier LinkedIn autonome | `add_linkedin_scheduled_message` « enregistrement uniquement, pas d'envoi automatique » (description serveur) | le rituel /linkedin-du-jour envoie un par un, sur accord |
| Écrire deux fois à la même personne | l'historique complet vit dans `list_linkedin_message_history` | le lire AVANT toute rédaction ; filtrer par connectionId |
| SMS vers des fixes ou des formats locaux | `send_sms` exige E.164 ; `list_clients` avec `mobileOnly: true` ne garde que les mobiles français | normaliser_telephone.py avant toute campagne ; jamais de numéro deviné |
| Dépasser les plafonds du serveur | SMS : 200 cibles et 1 600 caractères ; appels : 100 cibles, synthèse vocale française | segments_sms.py + quotas.py ; les plafonds de la KB sont plus bas |
| Coller un lien de lead magnet dans un contenu durable | `list_lead_magnets` renvoie des liens de téléchargement TEMPORAIRES | dans un e-mail ou une page : pointer vers la page de capture, pas vers le lien signé |
| Publier le lien d'un webinaire | le lien de connexion n'est visible que des inscrits | la communication renvoie vers la page d'inscription |
| Prendre le MRR Stripe pour un chiffre comptable | `stripe_stats` renvoie un « MRR estimé » | toujours le présenter comme estimation, agrégé, sans e-mail client |
| Sous-estimer une suppression | cascades : connexion → modèles + historique + messages programmés ; webinaire → inscriptions + rappels ; lead magnet → fichier stocké ; client → définitif | reference/outils-sensibles.json fait foi ; la cascade est rappelée dans l'ask |
| Compter un SMS = un message | GSM-7 : 160 caractères puis 153/segment ; hors GSM-7 (emoji, caractères spéciaux) : 70 puis 67 | segments_sms.py affiche segments et coût relatif avant l'accord |
| Croire le serveur ouvert | le point d'entrée répond 401 avec `WWW-Authenticate: Bearer` et `.well-known/oauth-protected-resource` (OAuth Supabase, audience authenticated) | l'authentification est l'OAuth du premier appel ; aucun jeton dans le dépôt ; sans session connectée, aucune recette live |
| Modèles LinkedIn « globaux » | les modèles LinkedIn sont rattachés à UNE connexion (`connectionId` requis, même pour `list_linkedin_templates`) | les modèles réutilisables vivent côté e-mail (`add_email_template`) et SMS/appel (`add_message_template`) |
| `prospection_terms` qui écrit sans le dire | le même outil liste ET ajoute (`add_kind`/`add_value`) | sans paramètre = lecture ; tout ajout de terme passe par un accord (hook de configuration) |
