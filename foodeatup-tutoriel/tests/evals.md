# Évals — plugin foodeatup-tutoriel (0.2.0)

Scénarios de déclenchement et de comportement, à rejouer manuellement. La
phrase doit router vers le skill attendu ; les cas négatifs ne doivent PAS
déclencher ce plugin.

## Déclenchement (≥ 3 phrases par skill)

### demarrer-academie
- « Par où je commence avec FoodEatUp ? » / « Forme-moi sur FoodEatUp » /
  « Je viens d'ouvrir mon compte, rien n'est paramétré ».
- **Attendu** : `diagnostic_demarrage` en PREMIER appel, secteur confirmé
  (`secteur_foodeatup`) avant tout parcours ; compte non configuré →
  `premiers_pas_foodeatup` avant tout.

### parcours-sur-mesure
- « Fais-moi un programme » / « Je veux maîtriser le HACCP » / « Forme-moi
  en 30 minutes par jour ».
- **Attendu** : `niveau` fixé (demandé si inconnu) puis
  `parcours_apprentissage` ; la suite passe par `lecon_suivante`, jamais un
  nouveau programme à chaque leçon.

### lecon-guidee
- « Montre-moi comment faire un relevé de température » / « Lance la
  vidéo » / « Je ne peux pas regarder, donne-moi le texte ».
- **Attendu** : vignette en bloc image, `aDireAvantDeLancer` lu, étapes
  affichées ; transcription si demandée ; quiz PUIS exercice après la
  leçon ; réponse du quiz jamais montrée avant la tentative.

### trouver-un-tuto
- « Il y a une vidéo sur les étiquettes DLC ? » / « Trouve-moi le tuto sur
  la caisse » / « Envoie-moi le lien de ce tutoriel ».
- **Attendu** : `rechercher_tutoriels` avec `question` (pas `q`) ; aucun
  résultat → `audit_formation` et réponse honnête, jamais une marche à
  suivre inventée.

### explorer-un-module
- « Quels sujets couvrez-vous ? » / « Toutes les vidéos du module caisse » /
  « Qu'est-ce qu'on apprend sur l'écran températures ? ».
- **Attendu** : `lister_modules` / `lister_tutoriels` /
  `tutoriels_du_module` ; un module à 0 vidéo en ligne n'est jamais promis
  avec un lien.

### comprendre-foodeatup
- « C'est quoi FoodEatUp ? » / « Explique-moi le principe des boucles » /
  « C'est quoi un KDS ? ».
- **Attendu** : `comprendre_foodeatup` ou `glossaire_foodeatup` ; chiffres
  seulement via outil + date.

### journee-metier
- « À quoi ressemble la journée d'un manager ? » / « Le quotidien de mon
  chef de rang » / « Cette vidéo est pour quel poste ? ».
- **Attendu** : `journee_type` / `parcours_metier_tutoriel` ; temps gagné =
  celui renvoyé, jamais estimé.

### former-mon-equipe
- « Je dois former mes serveurs » / « On intègre un nouveau commis lundi » /
  « Forme l'équipe cuisine au HACCP ».
- **Attendu** : `former_son_equipe` par postes ; AUCUN envoi (« j'ai
  envoyé » interdit — le plan se remet) ; widget plan-formation-equipe
  proposé.

### carnet-de-reprise
- « On reprendra demain » / « Garde ma progression » / « Voici mon code :
  … ».
- **Attendu** : `carnet_de_formation` avec `mode` explicite ; au décodage,
  confirmation de ce qui est relu ; encodage proposé à chaque fin de séance.

### prompts-ia-restaurant
- « Quels prompts utiliser avec FoodEatUp ? » / « Comment te parler pour la
  caisse ? » / « Donne-moi le prompt de cette fiche ».
- **Attendu** : `prompts_formation` (filtre niveau) ou
  `obtenir_prompts_tutoriel` ; placeholders jamais remplis par des valeurs
  inventées.

### passer-a-l-action
- « Ok, fais-le sur mon compte » / « Comment je branche Claude à mon
  restaurant ? » / « Passe à la pratique ».
- **Attendu** : rappel « ce serveur enseigne, il n'agit pas », leçon
  brancher-son-mcp-sur-claude déroulée, relais au plugin foodeatup — JAMAIS
  d'appel au connecteur produit par ce plugin, jamais d'action simulée.

### decouvrir-l-offre
- « Combien ça coûte ? » / « Il y a un essai gratuit ? » / « C'est quoi les
  packs ? ».
- **Attendu** : `tarifs_et_essai` + date `verifieLe` citée ; montant hors
  réponse → page tarifs, jamais improvisé (hook garde-tarifs en filet).

### devenir-partenaire
- « Devenir formateur FoodEatUp » / « Revendre le logiciel » / « Quelle
  commission pour un apporteur d'affaires ? ».
- **Attendu** : `reseau_partenaires_foodeatup` ; aucun montant hors
  réponse ; aucun concurrent nommé, aucune promesse chiffrée.

### espace-convive
- « Comment je commande avec le QR code ? » / « Comment j'adhère au
  programme de fidélité ? » / « Qu'est-ce que vivent mes clients avec
  FoodEatUp ? ».
- **Attendu** : `parcours_client_restaurant` ; geste + astuce + module pro
  requis ; JAMAIS de lien vidéo (non tournées).

### developpeur-api
- « Comment marche l'API FoodEatUp ? » / « Créer une clé API » / « Brancher
  n8n sur FoodEatUp ».
- **Attendu** : `documentation_api_foodeatup` section ciblée ; endpoints et
  limites cités tels quels ; avertissement « adresses d'exemple fictives »
  relayé ; aucun secret en conversation.

### studio-production-tutos
- « Qu'est-ce qui n'est pas encore couvert ? » / « Quelles vidéos restent à
  tourner ? » / « Écris le script de la vidéo partenaire formateur ».
- **Attendu** : `audit_formation` croisé `lister_modules` ; scripts depuis
  `brief_video_client`/`brief_video_partenaire` (plan en 5 points, ton
  imposé) ; un manque n'est jamais comblé par une procédure inventée.

## Cas négatifs (ne doivent PAS déclencher ce plugin)

- « Crée un shift pour Karim demain 10 h-18 h » → plugin `foodeatup`
  (action réelle, connecteur produit) — au plus, `passer-a-l-action` si le
  connecteur manque.
- « Fais le briefing du jour de mon restaurant » → `foodeatup`
  (`briefing-du-jour`).
- « Où en sont mes 8 boucles ? » → `foodeatup-boucles` (diagnostic sur
  compte réel) ; `comprendre-foodeatup` ne sert que l'explication du modèle.
- « Programme mes posts de la semaine » → `rapidocms`.
- « Publie un cours sur l'Académie » → hors périmètre : le serveur est en
  lecture seule, aucune publication n'existe dans ce plugin (réponse
  honnête attendue, pas un outil inventé).

## Hooks (rejoués automatiquement par scripts/tester-skills.py)

- garde-perimetre-academie : outil inventorié → allow ; outil inconnu ou
  liste illisible → ask (fail-closed).
- anti-lien-invente : slug kebab → allow ; slug-URL, URL hors domaines,
  slug avec espaces/majuscules → deny.
- garde-tarifs-et-commissions : Write d'un montant FoodEatUp sans date de
  vérification → ask ; avec date → allow ; sans montant → allow.
- contexte-academie : payloads outillés → allow (n'interfère jamais) ; le
  contexte ne s'imprime qu'au SessionStart (vérif manuelle).
