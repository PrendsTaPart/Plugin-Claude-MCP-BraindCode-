# Directives d'usage des 66 outils du serveur Prospect (« Prospector Hub »)

Relevé du 2026-10-25 depuis le manifeste MCP publié du projet (commit
6ad9af2). Point d'entrée : https://prospect-pebble.lovable.app/mcp —
ressource OAuth (Supabase) : l'authentification se fait au premier appel,
aucun jeton n'est stocké dans le dépôt. À relire au début de chaque skill.

## Les cinq lois du plugin

1. **run_prospection ne sauvegarde rien** : il renvoie des prospects.
   Seul `add_clients` enregistre, avec `city` et `speciality`.
2. **Tout envoi réel passe par un humain** : les 5 outils d'envoi
   (`send_email`, `send_sms`, `place_call`, `send_linkedin_invite`,
   `send_linkedin_message`) déclenchent un ask systématique, des quotas et
   des contrôles de conformité (hooks). Les champs posés par le modèle ne
   valent jamais confirmation humaine.
3. **LinkedIn exige un provider_id** : `enrich_linkedin_profile` (avec un
   `account_id` pris dans `list_linkedin_accounts`) AVANT tout
   `send_linkedin_invite` / `send_linkedin_message`. Le calendrier
   (`add_linkedin_scheduled_message`) n'envoie JAMAIS tout seul.
4. **12 suppressions définitives**, avec cascades (connexion → modèles +
   historique + messages programmés ; webinaire → inscriptions + rappels ;
   lead magnet → fichier stocké) : confirmation fiche par fiche.
5. **Aucune donnée embellie** : MRR Stripe = estimation, liens de lead
   magnets = temporaires (jamais collés dans un contenu durable), lien de
   webinaire visible des seuls inscrits.

## Prospection et base clients

| Outil | Rôle | À savoir avant d'appeler |
|---|---|---|
| `prospection_terms` | régions et spécialités connues | sans paramètre = lecture ; `add_kind`+`add_value` = écriture de configuration (accord requis) |
| `run_prospection` | lance la prospection n8n (city, speciality) | coût externe (webhook) ; ne sauvegarde PAS les prospects |
| `prospection_history` | historique des prospections | sert au tableau de bord et à éviter de refaire une zone |
| `add_clients` | enregistre des clients (lot) | APRÈS dédoublonnage (scripts/dedoublonner.py) et accord ; porter city + speciality |
| `list_clients` | recherche et filtres (search, city, speciality, mobileOnly) | `mobileOnly` = mobiles français seulement → base des SMS |
| `update_client` | corrige une fiche (contact, statut) | statut de prospection tenu ici |
| `delete_client` | suppression DÉFINITIVE | fiche par fiche, sur confirmation |

## Envois : e-mail, SMS, appels

| Outil | Rôle | À savoir |
|---|---|---|
| `send_email` | envoi via le webhook n8n d'e-mailing | identité d'expéditeur + phrase de désinscription obligatoires ; vérifier ensuite dans `list_emails` |
| `send_sms` | SMS Twilio | numéros E.164, 200 cibles max, 1 600 caractères max, mention STOP obligatoire ; statuts dans `list_sms` |
| `place_call` | appel automatisé Twilio, texte lu en synthèse vocale française | 100 cibles max ; DÉSACTIVÉ par défaut (./rapido-kb/prospection.md) ; le texte identifie l'expéditeur et offre un refus |
| `list_emails` / `list_sms` / `list_calls` | historiques d'envoi | preuve de ce qui est parti ; base des relances J+3/J+7 |

## Modèles de messages

| Outil | Rôle |
|---|---|
| `list_email_templates` / `add_email_template` / `update_email_template` / `delete_email_template` | modèles d'e-mail HTML avec objet |
| `list_message_templates` / `add_message_template` / `update_message_template` / `delete_message_template` | modèles `kind` sms ou call (texte lu) |
| `list_linkedin_templates` / `add_linkedin_template` / `update_linkedin_template` / `delete_linkedin_template` | modèles PAR CONNEXION LinkedIn (`connectionId` requis) |

Chaque modèle passe par scripts/conformite.py avant enregistrement.

## LinkedIn

| Outil | Rôle | À savoir |
|---|---|---|
| `list_linkedin_accounts` | comptes d'envoi (nom, account_id) | source UNIQUE des `account_id` ; n'en invente jamais |
| `add_linkedin_account` / `update_linkedin_account` / `delete_linkedin_account` | configuration des comptes | écriture de configuration : accord requis |
| `list_linkedin_connections` | recherche (search, company, enrichedOnly) + pagination | `enrichedOnly` = profils avec provider_id |
| `get_linkedin_connection` / `add_linkedin_connection` / `update_linkedin_connection` | fiche connexion | `delete_linkedin_connection` = cascade complète |
| `enrich_linkedin_profile` | webhook : provider_id, headline, contacts | coût externe ; par lot réduit, sur accord ; prérequis des envois |
| `send_linkedin_invite` / `send_linkedin_message` | envois via webhooks | provider_id requis (enrichir d'abord) ; un par un, sur accord |
| `add_linkedin_scheduled_message` / `update_linkedin_scheduled_message` / `delete_linkedin_scheduled_message` / `list_linkedin_scheduled_messages` | calendrier LinkedIn | inscription seulement : RIEN ne part automatiquement |
| `list_linkedin_scheduled_day` | la file d'un jour (heure de Paris) | point d'entrée du rituel « LinkedIn du jour » |
| `list_linkedin_message_history` | tout ce qui a été écrit à qui | à lire AVANT d'écrire : jamais deux fois le même message à la même personne |

## Contenus : calendrier, blog, vidéos, webinaires, lead magnets

| Outil | Rôle | À savoir |
|---|---|---|
| `list_calendar_posts` / `add_calendar_post` / `update_calendar_post` / `delete_calendar_post` | calendrier éditorial (networks, format, subject, visual) | statut « publie » = publication visible → ask ; la publication réelle passe par le plugin rapidocms |
| `list_blog_posts` / `add_blog_post` / `update_blog_post` / `delete_blog_post` | articles de blog planifiés | passage au statut « publie » sur accord |
| `list_video_posts` / `add_video_post` / `update_video_post` / `delete_video_post` | vidéos (prompts séquences 1 et 2, montage, voix off, miniature) | la génération est déléguée (rapido-higgsfield / rapido-video) ; on renseigne ensuite video_url et thumbnail_url |
| `list_webinars` / `add_webinar` / `update_webinar` / `delete_webinar` | webinaires + nombre d'inscrits | créer avec `is_active: false`, activer sur accord ; le lien de connexion n'est visible que des inscrits ; delete = cascade inscriptions + rappels |
| `list_lead_magnets` / `add_lead_magnet` / `update_lead_magnet` / `delete_lead_magnet` | documents (base64 ou URL publique) | liens de téléchargement TEMPORAIRES ; la fabrication est déléguée à rapido-leadmagnet ; delete efface le fichier |

## Mesure et journal

| Outil | Rôle | À savoir |
|---|---|---|
| `stripe_stats` | clients, paiements, abonnements actifs, CA, MRR | le MRR est une ESTIMATION et se présente comme telle |
| `add_log` | journalise une action (action, message, count) | après chaque prospection, campagne ou série d'envois |
| `list_logs` | audit des tâches journalisées | tableau de bord et traçabilité |

## Serveur optionnel : RapidoCRM

Déclaré dans .mcp.json pour la synchronisation des prospects qualifiés
(`rechercher_prospects` contre les doublons, puis
`enregistrer_tous_prospects` et `ajouter_prospect_pipeline`). S'il n'est pas
branché dans la session, le volet est sauté EN LE DISANT.
