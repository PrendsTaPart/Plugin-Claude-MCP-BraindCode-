# Évals — plugin rapido-youtube (0.1.0)

Scénarios de déclenchement et de comportement, à rejouer manuellement.

## Déclenchement (≥ 3 phrases par skill)

### tableau-de-bord-youtube
- « Où en sont mes chaînes YouTube ? » / « Fais le point YouTube » /
  « Quota et planning du jour »
- **Attendu** : un écran (chaîne, quota + risque, crédits, planning 7 j,
  échecs, santé, commentaires, comptes) + 3 priorités ; will_fail ⇒ la
  priorité n° 1 est la revue du planning sous 24 h.

### choisir-la-chaine
- « Passe sur la chaîne RapidoCMS » / « Quelle chaîne est active ? » /
  « Mets Formation Braindcode en favorite »
- **Attendu** : lecture d'abord, bascule sur accord, règle du channel_id
  explicite rappelée ; pas de chaîne RapidoRH.

### veille-et-outliers
- « Trouve les outliers de la semaine » / « Quelles vidéos surperforment
  dans ma niche ? » / « Idées du jour »
- **Attendu** : panel réel, filtres (fenêtre, format, score, taille de
  chaîne), motifs analysés — adaptation, jamais de copie.

### recherche-de-mots-cles
- « Quels mots-clés pour cette vidéo ? » / « Recherche de requêtes en
  français » / « La concurrence sur ce sujet »
- **Attendu** : français/France ; with_competition = quota, sur accord.

### titre-description-seo
- « Propose des titres » / « Écris la description chaptée » / « Note le
  SEO avant publication »
- **Attendu** : scores = estimations, choix humain, chapitres depuis la
  transcription (script), yt_score_video_seo avant publication.

### atelier-miniatures
- « Génère la miniature » / « Analyse cette vignette » / « Applique le
  style de la chaîne »
- **Attendu** : kits/styles/visages lus, coût annoncé, 1 variation puis
  analyse gratuite, liens d'aperçu jamais en dur.

### publier-une-video
- « Publie cette vidéo » / « Envoie le fichier sur la chaîne » /
  « Mets-la en ligne en non répertorié »
- **Attendu** : quota → chaîne → SEO → miniature → privacy prudente →
  client_request_id → statut constaté.

### planifier-et-grille
- « Planifie la vidéo mardi 18 h » / « Propose mes créneaux » / « Refais
  la grille de la chaîne »
- **Attendu** : créneaux de l'historique réel, grille LUE avant
  remplacement, lots de 10 max, chevauchements scriptés.

### autopilote
- « Active l'autopilote » / « Mets la file en automatique » / « Pause
  l'autopilote pendant les vacances »
- **Attendu** : Europe/Paris, exclusions, espacement, pause motivée —
  sur accord, coût quota des envois rappelé.

### shorts-depuis-une-video-longue
- « Découpe cette vidéo en Shorts » / « Quels clips dans ce tuto ? » /
  « Publie les 3 meilleurs clips »
- **Attendu** : asynchrone suivi, choix humain, rendu dans l'app
  vérifié, scores = estimations éditoriales.

### distribution-multi-plateformes
- « Poste ce clip sur TikTok et Instagram » / « Programme la
  distribution » / « Où en sont mes cross-posts ? »
- **Attendu** : comptes vérifiés (aucun au relevé → page Distribution ou
  rapidocms), 6 posts max, légendes par plateforme.

### tests-ab-miniatures
- « Lance un A/B sur cette vidéo » / « Quelle miniature gagne ? » /
  « Résultat du test »
- **Attendu** : comparaison d'abord, lancement sur accord, verdict
  restitué tel quel (95 % / 100 impressions, sinon non concluant).

### analytics-et-rapports
- « Les stats de la chaîne » / « Compare ces deux vidéos » / « Génère le
  rapport du mois »
- **Attendu** : refresh sur accord, « Analytics coupée » = reconnecter,
  rapport partageable sur accord avec durée de vie.

### audit-et-corrections-en-lot
- « Audite la chaîne » / « Corrige les descriptions des 200 vidéos » /
  « Remplace l'ancien lien partout »
- **Attendu** : aperçu preview_only MONTRÉ puis job réel sur accord ;
  chercher-remplacer en dry_run d'abord.

### commentaires
- « Réponds aux commentaires sans réponse » / « Quelles questions en
  attente ? » / « Gère les négatifs »
- **Attendu** : brouillons relus, réponses une à une (50 unités), jamais
  d'automatique sur négatif ou spam.

### reprise-des-echecs
- « Pourquoi cette vidéo est en erreur ? » / « Relance les envois
  échoués » / « C'est quoi uploadLimitExceeded ? »
- **Attendu** : erreurs expliquées, reprises dans le quota, heure de
  réarmement respectée et transmise.

### bibliotheque-de-prompts
- « Sauvegarde ce prompt de miniature » / « Retrouve mon prompt de
  titre » / « Rends ce prompt public »
- **Attendu** : privé par défaut, aucun secret, texte rendu montré,
  is_public et suppression sur accord.

### serie-tutoriels-foodeatup
- « Mets les tutoriels du module caisse sur la chaîne » / « Prépare la
  série FoodEatUp » / « Quelles vidéos tuto manquent sur YouTube ? »
- **Attendu** : fiches/transcriptions/vignettes lues au serveur
  tutoriel, gabarit de miniature appliqué, liens YouTube rendus en
  TABLEAU (serveur tutoriel en lecture seule).

### academies-et-formations
- « Publie les tutos RapidoCMS et enregistre les liens » / « Quelles
  vidéos Plan'It manquent ? » / « Transforme les BD de l'Academy en
  Shorts »
- **Attendu** : enregistrement en retour sur accord après publication
  constatée ; Shorts Academy sur Formation Braindcode ; chaîne RapidoRH
  inexistante → destination demandée.

### routines-youtube
- « Propose la routine de veille hebdo » / « Automatise le momentum
  quotidien » / « La routine commentaires chaque matin »
- **Attendu** : 5 routines types avec leur KPI, proposées via planit
  (coût annoncé), jamais acceptées sans accord.

## Cas négatifs (ne doivent PAS déclencher ce plugin)

- « Programme mes posts Instagram de la semaine » → `rapidocms` : la
  publication sociale générale n'est pas la distribution d'un Short.
- « Monte cette vidéo, coupe les silences, ajoute les sous-titres » →
  `rapido-video` (ffmpeg/Whisper) : ici on détecte et publie, on ne
  monte pas.
- « Génère un packshot 4K du plat » → `rapido-higgsfield` : la
  génération média lourde n'est pas l'atelier de miniatures.
- « Écris la copy LinkedIn de ce lancement » → `rapido-copywriter` : la
  copy multi-réseaux se délègue (les légendes de cross-post la
  consomment, sans la réécrire).

## Hooks (rejoués automatiquement par scripts/tester-skills.py)

- alias-deprecies : l'appel d'un outil du serveur sous son ANCIEN nom
  sans préfixe (ex. publish_video, get_channel_status — écrits ici sans
  accents graves exprès) → deny avec le nom yt_ à utiliser ; le nom
  officiel → allow.
- garde-chaine : envoi sans channel_id → ask (cible par défaut nommée) ;
  avec channel_id → allow ; bascules active/favorite → ask ; lecture →
  allow.
- garde-quota : envoi sans lecture → deny ; lecture de 60 min → deny ;
  risque will_fail → deny ; tight → ask ; ok et frais → allow ; outil
  gratuit → allow.
- garde-credits : variations 3 → ask ; cumul de session 30 ≥ seuil 25 →
  ask ; cumul 3 → allow ; analyse gratuite → allow.
- garde-public : privacy public → ask, private → allow ; métadonnées
  d'une vidéo / réponse à un commentaire / A/B / prompt is_public → ask ;
  prompt privé → allow.
- garde-lot : preview_only / dry_run → allow ; job ou remplacement RÉEL
  sans aperçu identique en session → deny.
- garde-grille : liste vide → ask (effacement explicite) ; grille non
  lue → ask ; lue → ask avec grille montrée.
- garde-visage : échange sans relevé des modèles → deny ; modèle hors
  liste → deny ; modèle de l'utilisateur listé → ask ; génération sans
  visage → allow.
- garde-destructif-youtube : suppression de vidéo (avec confirm posé par
  le modèle) → ask quand même (la vidéo RESTE sur YouTube, rappelé) ;
  annulations → ask ; lectures → allow.
- journal-youtube : jamais bloquant ; quota/grille/visages/aperçus posés
  en état de session (vérif. manuelle) ; liens signés masqués.
- contexte-youtube (SessionStart) : chaîne ciblée + lecture du quota
  rappelées (vérif. manuelle).
