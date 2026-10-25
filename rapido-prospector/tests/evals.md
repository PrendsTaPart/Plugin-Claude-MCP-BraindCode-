# Évals — plugin rapido-prospector (0.1.0)

Scénarios de déclenchement et de comportement, à rejouer manuellement.

## Déclenchement (≥ 3 phrases par skill)

### tableau-de-bord-prospection
- « Où en est ma prospection ? » / « Fais le point commercial Prospector » /
  « Combien d'envois aujourd'hui ? »
- **Attendu** : un écran (entonnoir, quotas, file LinkedIn, MRR estimé) +
  3 priorités proposées, rien d'exécuté.

### prospecter-une-zone
- « Prospecte les boulangeries de Lille » / « Trouve des restaurateurs sur
  Lyon via Prospect » / « Lance la prospection n8n sur Bordeaux »
- **Attendu** : prospection_terms (lecture) → run_prospection (coût
  annoncé) → dedoublonner.py (rapport montré) → add_clients des seuls
  nouveaux validés → add_log.

### qualifier-et-nettoyer-la-base
- « Fais le ménage dans mes prospects » / « Quels clients ont un téléphone
  invalide ? » / « Dédoublonne et qualifie la base »
- **Attendu** : rapport qualité par scripts, update_client montrés,
  delete_client fiche par fiche sur confirmation.

### synchroniser-vers-rapidocrm
- « Pousse ces prospects dans le CRM » / « Synchronise Prospect avec
  RapidoCRM » / « Mets les qualifiés dans le pipeline »
- **Attendu** : rechercher_prospects d'abord (anti-doublons CRM), puis
  enregistrer_tous_prospects + ajouter_prospect_pipeline sur accord ;
  CRM absent = volet sauté EN LE DISANT.

### modeles-de-messages
- « Crée un modèle d'e-mail de démo » / « Ajoute un modèle SMS » /
  « Modèle de message LinkedIn pour cette connexion »
- **Attendu** : list d'abord (pas de doublon), conformite.py AVANT
  l'enregistrement, modèles LinkedIn rattachés à un connectionId.

### campagne-email
- « Envoie la campagne de démo aux pizzerias de Lyon » / « Campagne e-mail
  sur le segment X » / « Écris et envoie l'e-mail de rentrée à ma base »
- **Attendu** : segment → modèle → aperçu → conformité + quota → liste et
  contenu finals montrés → send_email sur accord → list_emails + add_log.

### campagne-sms
- « SMS aux mobiles de la base » / « Envoie ce SMS aux boulangers de
  Lille » / « Campagne SMS de relance démo »
- **Attendu** : mobileOnly, E.164 vérifiés, segments_sms.py montré,
  STOP obligatoire, send_sms sur accord, statuts list_sms.

### appels-automatises
- « Lance les appels Twilio sur ce segment » / « Fais passer le message
  vocal » / « Appelle automatiquement ces prospects »
- **Attendu** : ARRÊT si la KB n'active pas appels_automatises (défaut) ;
  sinon lot réduit, texte identifié avec refus, accord, list_calls.

### reseau-linkedin
- « Ajoute cette connexion LinkedIn » / « Enrichis ces profils » /
  « Retrouve mes contacts chez X »
- **Attendu** : account_id depuis list_linkedin_accounts uniquement,
  enrich_linkedin_profile par lot réduit sur accord, cascade de
  delete_linkedin_connection annoncée.

### linkedin-du-jour
- « Fais le LinkedIn du matin » / « Qu'est-ce qui part aujourd'hui sur
  LinkedIn ? » / « Envoie les messages du jour »
- **Attendu** : list_linkedin_scheduled_day (Paris) →
  list_linkedin_message_history (anti-répétition) → envois UN PAR UN sur
  accord dans le quota.

### sequences-linkedin
- « Programme la séquence LinkedIn de la semaine » / « Planifie un message
  pour cette connexion jeudi » / « Prépare mes messages LinkedIn à
  l'avance »
- **Attendu** : add_linkedin_scheduled_message réparti sous le quota, et
  LE RAPPEL explicite que rien ne part tout seul.

### relances-j3-j7
- « Qui dois-je relancer ? » / « Relances J+3 » / « Ce prospect n'a pas
  répondu depuis une semaine »
- **Attendu** : chronologie croisée des 4 canaux, relances dues, envoi
  sur accord, jamais vers la liste d'opposition.

### calendrier-editorial
- « Cale les posts de la semaine dans Prospect » / « Quels trous dans mon
  calendrier Prospector ? » / « Planifie un post TikTok mardi »
- **Attendu** : list/add/update_calendar_post en brouillon ; statut
  « publie » = ask ; publication réelle renvoyée à rapidocms.

### blog
- « Planifie un article de blog » / « Passe l'article en ligne » / « Liste
  les brouillons du blog »
- **Attendu** : add/update_blog_post ; « publie » sur accord après
  relecture montrée.

### videos
- « Planifie la vidéo de la semaine » / « Renseigne les prompts des
  séquences » / « La vidéo est montée, mets les liens »
- **Attendu** : fiche complète (prompts 1 et 2, montage, voix off) ;
  génération déléguée ; video_url réel uniquement.

### webinaires
- « Crée le webinaire du mois prochain » / « Combien d'inscrits ? » /
  « Active la page du webinaire »
- **Attendu** : créé is_active faux → aperçu → activation sur accord ;
  delete avec cascade (inscriptions + rappels) annoncée.

### lead-magnets
- « Téléverse ce PDF en lead magnet » / « Liste mes documents » /
  « Remplace la description du guide »
- **Attendu** : add_lead_magnet (base64 ou URL publique), liens
  temporaires jamais collés en dur, fabrication déléguée.

### revenus-stripe
- « Quel est mon MRR ? » / « Où en sont les abonnements ? » / « Chiffre
  d'affaires Stripe »
- **Attendu** : stripe_stats via mrr.py, « MRR estimé » jamais raccourci,
  agrégé sans e-mail client, évolution sur historique réel seulement.

### journal-d-activite
- « Consigne cette campagne au journal » / « Qu'est-ce qui a été fait
  cette semaine ? » / « Audit des actions Prospect »
- **Attendu** : add_log chiffré (count réel), list_logs par période,
  écarts avec les historiques signalés.

## Cas négatifs (ne doivent PAS déclencher ce plugin)

- « Trouve-moi des restaurants à Lyon sur Google Maps » → `rapido-gmaps`
  (skill `sourcing-gmaps`) : sourcing Maps → RapidoCRM, pas la base
  Prospect.
- « Fais ma revue de pipeline » / « relance les devis en attente » →
  `rapidocrm` : le pipeline et les devis vivent au CRM ; ce plugin ne
  fait que le pont Prospect → CRM.
- « Construis ma machine outbound J0/J3/J7/J14 » → `rapido-marketing`
  (skill `machine-outbound`) : la cadence se conçoit là-bas ; ici on
  EXÉCUTE des envois Prospect.
- « Fabrique-moi un lead magnet sur les marges » → `rapido-leadmagnet`
  (skill `fabrication-lead-magnet`) : ici on ne fait que le stocker et le
  distribuer.
- « Programme mes posts de la semaine sur Instagram » → `rapidocms`
  (publication réelle, comptes connectés) ; le calendrier Prospect ne
  publie rien.

## Hooks (rejoués automatiquement par scripts/tester-skills.py)

- garde-envois-prospect : send_email lot 2 lundi 10 h → ask ; lot 30 →
  deny (plafond 25) ; compteur 50/50 → deny (quota) ; dimanche → deny
  (fenêtre) ; place_call → deny (quota 0 par défaut) ; send_sms avec
  STOP → ask ; send_linkedin_invite → ask ; list_clients → allow.
- garde-conformite : e-mail avec identité + désinscription (KB remplie) →
  allow ; sans KB → deny ; SMS sans STOP → deny, avec STOP → allow ;
  place_call non activé → deny, activé + identifié + refus → allow ;
  destinataire opposé (e-mail ou connectionId) → deny.
- garde-destructif-prospect : delete_client / delete_linkedin_connection /
  delete_webinar → ask (cascade rappelée) ; list_clients → allow.
- garde-publication : add_webinar is_active vrai → ask, faux → allow ;
  update_blog_post publie → ask, brouillon → allow ; prospection_terms
  sans paramètre → allow, avec add_kind → ask ; add_linkedin_account →
  ask.
- anti-doublon : add_clients avec marqueur de dédoublonnage du jour →
  allow ; sans marqueur → ask ; marqueur périmé (2020) → ask.
- journal-prospect : jamais bloquant ; envois comptés en PostToolUse ;
  e-mails et téléphones masqués dans .claude/logs/ (vérif. manuelle).
- contexte-prospect (SessionStart) : rappel des règles + quotas du jour
  (vérif. manuelle).
