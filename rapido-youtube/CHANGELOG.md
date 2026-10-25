# Changelog — plugin rapido-youtube

## 0.1.0 — 2026-10-25 — YouTube Publisher Bot de bout en bout

Première version, bâtie sur le serveur MCP Rapido YouTube (« YouTube
Publisher Bot », https://youtube.rapidocms.com/mcp — ressource OAuth
Supabase vérifiée par sonde, authentification au premier appel, aucun
jeton dans le dépôt). Inventaire : **86 outils OFFICIELS yt_**
(docs/inventaires/rapido-youtube-tools-live.txt) relevés au manifeste MCP
publié du projet (serveur youtube-publisher-bot 0.4.0), qui expose AUSSI
**86 alias dépréciés** sans préfixe (retrait le 2026-12-31) :
- contrôle CI dédié ALIAS-YT (vérifié par appât) : toute citation d'un
  alias dans le plugin fait échouer le build ;
- hook alias-deprecies : deny à l'exécution, avec le nom yt_ à utiliser.

Sept serveurs optionnels déclarés (tutoriel FoodEatUp, Academy, RapidoCMS,
académies RapidoCMS/RapidoRH tuto et Plan'it tutoriel en variables
d'environnement, Plan'It) — absents, le volet est sauté en le disant.

- **20 skills** : tableau-de-bord-youtube, choisir-la-chaine,
  veille-et-outliers, recherche-de-mots-cles, titre-description-seo,
  atelier-miniatures, publier-une-video, planifier-et-grille, autopilote,
  shorts-depuis-une-video-longue, distribution-multi-plateformes,
  tests-ab-miniatures, analytics-et-rapports,
  audit-et-corrections-en-lot, commentaires, reprise-des-echecs,
  bibliotheque-de-prompts, serie-tutoriels-foodeatup,
  academies-et-formations, routines-youtube.
- **6 agents** : stratege-de-chaine, directeur-artistique-youtube,
  programmateur-youtube, monteur-shorts-distribution,
  community-manager-youtube, analyste-youtube.
- **17 commandes** : /youtube, /chaine, /veille, /idees, /miniature,
  /publier, /planning, /autopilote, /shorts, /distribuer, /ab-test,
  /stats, /audit, /commentaires, /reprise, /quota, /tutos-foodeatup.
- **9 widgets HTML** avec en-tête aux couleurs du KIT DE MARQUE de la
  chaîne (lu sur yt_list_brand_kits ; thème neutre signalé sans kit) +
  scripts/render_widget.py — sortie gitignorée, liens signés temporaires
  jamais recopiés.
- **5 scripts stdlib testés** (formules affichées) : quota.py (la
  campagne tient-elle dans le DISPONIBLE RÉEL ?), credits.py (barème LU,
  rien en dur), chapitres.py (0:00, ≥ 3, ≥ 10 s), seo_checklist.py,
  grille.py (chevauchements entre chaînes).
- **11 hooks fail-closed — 36 cas CI** : alias-deprecies (deny + bon
  nom), garde-chaine (channel_id explicite, bascules sur accord),
  garde-quota (deny sans lecture < 30 min ou sur will_fail, ask sur
  tight), garde-credits (variations > 1, seuil de session KB),
  garde-public (privacy public, vidéo en ligne, A/B, réponse, cross-post,
  rapport, prompt public), garde-lot (preview_only/dry_run obligatoires,
  même opération), garde-grille (grille lue, liste vide = effacement
  explicite), garde-visage (modèles de l'utilisateur seulement),
  garde-destructif-youtube (yt_delete_video laisse la vidéo EN LIGNE sur
  YouTube — rappelé), SessionStart, journal masqué. Les champs confirm et
  dry_run posés par le modèle ne valent jamais confirmation humaine.
- **Référence** : directives-outils.md (règle n° 1 des noms, 11 lois du
  serveur, chaînes de travail), pieges-verifies.md (will_fail du relevé,
  pas de chaîne RapidoRH, aucun compte de distribution…),
  quota-et-credits.md, chaines.md (4 chaînes, rien codé en dur), gabarit
  des miniatures tutos FoodEatUp, outils-sensibles.json (7 familles).
- **KB** : gabarit rapido-kb-template/youtube.md (seuil de crédits par
  session, variations max, fenêtre de publication).
- CI : catalogue fail-closed rapido-youtube (86, min 80) + inventaires
  des académies tuto (rapidocms-tuto, rapidorh-tuto, planit-tutoriel)
  relevés en session + périmètre OUTILS strict + contrôle ALIAS-YT.
