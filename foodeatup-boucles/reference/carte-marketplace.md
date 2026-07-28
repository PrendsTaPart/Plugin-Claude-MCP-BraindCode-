# Carte de la marketplace `rapido` — générée, ne pas éditer à la main

> Régénérer avec : `python3 scripts/generer-carte-boucles.py` (depuis la
> racine du dépôt de la marketplace). Source : les plugin.json réels.

## Restaurant (FoodEatUp)

| Plugin | Version | Skills | Description |
|---|---|---|---|
| `foodeatup` | 1.9.0 | 22 | Gestion restaurant FoodEatUp : HACCP, service en salle, coordination cuisine (KDS), recettes & marges, production, réapprovisionnement — … |
| `foodeatup-boucles` | 0.2.0 | 10 | Pilotage FoodEatUp par les 8 boucles du livre blanc (configuration, équipe, stock/production, HACCP, e-commerce, communication, fidélité,… |

Phrases qui déclenchent le bon skill :
- « fais le briefing du jour de mon restaurant »
- « où en sont mes 8 boucles ? »
- « détecte les incohérences entre ma com et mon stock »

## Ventes & CRM

| Plugin | Version | Skills | Description |
|---|---|---|---|
| `rapidocrm` | 1.8.0 | 31 | RapidoCRM : prospection, pipeline, campagnes marketing, devis/factures, communication client, performance commerciale — avec agents direc… |
| `rapido-relation-client` | 0.2.0 | 6 | (bêta) Service client, fidélité et santé client en boucle : SLA, CSAT/NPS, health score, sauvetages et 100 premiers jours — orchestré sur… |
| `rapido-gmaps` | 0.5.0 | 4 | Sourcing de leads Google Maps → pipeline RapidoCRM : scraping géo-ciblé (gosom/google-maps-scraper, MIT — Docker local ou API SaaS auto-h… |

Phrases qui déclenchent le bon skill :
- « fais ma revue de pipeline »
- « relance les devis en attente »
- « trouve-moi des prospects restaurateurs à Lyon »

## Contenu & réseaux sociaux

| Plugin | Version | Skills | Description |
|---|---|---|---|
| `rapidocms` | 1.11.8 | 22 | RapidoCMS : contenu réseaux sociaux (Facebook, Instagram, LinkedIn, TikTok), campagnes de posts, cartes digitales, gestion des marques mu… |
| `rapido-copywriter` | 0.6.0 | 4 | Le copywriter LinkedIn · Facebook · Instagram · TikTok : grammaires natives par réseau (datées, révisées trimestriellement), banque de ho… |
| `rapido-canva` | 1.0.2 | 7 | Design Canva alimenté par les données Rapido : menus restaurant (FoodEatUp), visuels sociaux (RapidoCMS), supports commerciaux (RapidoCRM… |
| `rapido-design` | 0.5.0 | 4 | Le studio UX/UI : orchestre la chaîne charte CMS → direction artistique → sitemap/flows → maquettes hi-fi Figma → design system → MVP Lov… |
| `rapido-prompteur` | 1.0.0 | 4 | Directeur de prompts : l'agent directeur-prompts orchestre la conception de prompts (image, vidéo, web, audio) pour Higgsfield, RapidoCMS… |

Phrases qui déclenchent le bon skill :
- « programme mes posts de la semaine »
- « écris la copy de ce lancement »
- « décline ce visuel aux couleurs de ma marque »

## Publicité & acquisition

| Plugin | Version | Skills | Description |
|---|---|---|---|
| `rapido-marketing` | 0.18.3 | 17 | Marketing & acquisition Rapido-first : génération de leads, tunnel de conversion, nurturing, publicité, sales intelligence (transcripts R… |
| `rapido-meta-ads` | 1.0.5 | 13 | Publicité Meta (Facebook/Instagram) pilotée par les données Rapido : lancement de campagnes, boost de posts, audiences CRM, créatifs, pix… |
| `rapido-google-ads` | 0.1.0 | 4 | (bêta) SEA Google Ads en LECTURE SEULE (MCP officiel read-only) : pilotage de performance, audit de compte, mots-clés payants, synergie S… |
| `rapido-tiktok-ads` | 0.1.0 | 3 | (bêta) TikTok Ads VERROUILLÉ — argent réel (MCP officiel lecture/écriture). Pilotage de performance, lancement de campagne 100 % en état … |
| `rapido-leadmagnet` | 0.5.0 | 4 | L'usine à lead magnets de bout en bout : fabrication (contenu + PDF brandé → bibliothèque CMS), page de capture (landing + formulaire Lov… |
| `rapido-seo` | 0.1.0 | 6 | (bêta) SEO & acquisition organique pilotés par les données : audit technique, recherche de mots-clés, netlinking, Search Console, GA4, te… |

Phrases qui déclenchent le bon skill :
- « monte une campagne Meta sur mon audience CRM »
- « construis-moi un lead magnet »
- « audite le SEO de mon site »

## Vidéo & médias IA

| Plugin | Version | Skills | Description |
|---|---|---|---|
| `rapido-video` | 1.0.1 | 2 | Montage vidéo 100 % libre (ffmpeg + Whisper) : concat, coupes, transitions, reframe 9:16/1:1/16:9, overlay logo, sous-titres burn-in, sup… |
| `rapido-higgsfield` | 1.0.4 | 9 | Usine média IA (Higgsfield) branchée sur l'écosystème Rapido : images 4K/packshots, vidéos génératives et pubs, personnages cohérents (So… |
| `rapido-elevenlabs` | 0.1.1 | 0 | Préversion — en attente de la connexion locale ElevenLabs. La voix de l'écosystème (MCP officiel ElevenLabs) : voix off & narration, tran… |

Phrases qui déclenchent le bon skill :
- « fais une vidéo de 30 s pour ce plat »
- « génère un packshot 4K de ce produit »
- « double cette vidéo en anglais »

## Équipe & projets

| Plugin | Version | Skills | Description |
|---|---|---|---|
| `rapidorh` | 1.1.0 | 12 | RapidoRh : projets, Kanban, dailies (rapports journaliers), onboarding des employés et rôles — avec agents chef-de-projet et responsable-rh |

Phrases qui déclenchent le bon skill :
- « fais la tournée des dailies »
- « crée le projet d'onboarding du nouveau »
- « où en est le Kanban ? »

## Direction & finance

| Plugin | Version | Skills | Description |
|---|---|---|---|
| `rapido-direction` | 1.1.0 | 5 | Chef de cabinet du dirigeant : Gmail, Google Calendar et Google Drive (compte connecté de chacun) unifiés avec CRM, FoodEatUp et n8n — jo… |
| `rapido-startup` | 1.10.0 | 6 | Finance & création de startup : interview business plan en 9 phases avec le coach-startup, Stripe (lecture d'abord) croisé avec les 4 ser… |
| `rapido-suite` | 1.4.2 | 13 | Orchestration transverse des 4 serveurs MCP Rapido : onboarding client 360°, revue business, comité de direction et base de connaissance … |

Phrases qui déclenchent le bon skill :
- « prépare mon comité de direction »
- « où en est ma trésorerie ? »
- « pilote la boîte : sense, plan, act »

## Sites & apps

| Plugin | Version | Skills | Description |
|---|---|---|---|
| `rapido-lovable` | 1.5.2 | 10 | Apps et agents IA Lovable alimentés par les données Rapido : site restaurant (FoodEatUp), usine à landing pages (CRM), agent IA produit c… |
| `rapido-n8n` | 1.6.2 | 4 | Automatisations n8n sur l'instance du client : usine à workflows (cycle SDK complet), recettes métier Rapido prêtes à déployer, surveilla… |

Phrases qui déclenchent le bon skill :
- « construis un MVP multi-pages »
- « automatise ce process dans n8n »
- « branche mon app sur les données Rapido »

## Formation & incubation

| Plugin | Version | Skills | Description |
|---|---|---|---|
| `rapido-forge` | 1.1.3 | 181 | StartupsForge (PrendsTaPart) : 180 exercices d'incubateur en 3 parcours — bootcamp 5 jours, roadmap idéation, roadmap scale — pilotés par… |

Phrases qui déclenchent le bon skill :
- « démarre le bootcamp 5 jours »
- « aide-moi à valider mon idée »
- « passe-moi en mode mentor scale »

## Ce que la marketplace ne peut PAS faire (limites connues)

- Créer/activer une **roue cadeaux** ou un **sondage** FoodEatUp : lecture
  seule côté MCP, la création se fait en back-office
  (docs/couverture-fidelite-jeux.md).
- Encaisser, lancer une campagne, publier un site **sans confirmation
  humaine** : les garde-fous PreToolUse l'empêchent volontairement.
- Les paiements de la marketplace elle-même : il n'y a pas de rail de
  paiement dans le système de plugins Claude Code.
- Toute donnée non exposée par les serveurs MCP connectés : rien n'est
  estimé à la place d'un outil manquant.

