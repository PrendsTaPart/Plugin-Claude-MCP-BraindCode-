# Test de routage — les descriptions déclenchent-elles le bon skill ?

Protocole SANS connexion aux MCP : chaque phrase utilisateur est confrontée
aux SEULES descriptions des frontmatters (108 skills + 14 agents). Le skill
« attendu » est celui qu'un humain désignerait ; le verdict compare avec ce
que les descriptions déclenchent réellement.

- **OK** : une description domine sans ambiguïté (déclencheur verbatim ou
  qualificatif exclusif) — un recouvrement de mot-clé secondaire, départagé,
  reste OK (noté).
- **CONFLIT** : deux descriptions revendiquent le même déclencheur sans
  départage possible.
- **AUCUN MATCH** : aucune description ne couvre la formulation.

État : verdicts APRÈS application des 5 correctifs de descriptions du
2026-07-06 (validés par le propriétaire, listés en bas). Résultat :
**30/30 OK**.

## Les 30 phrases (3 par plugin : évidente / familière / ambiguë)

### foodeatup

| # | Phrase | Skill attendu | Descriptions qui matchent | Verdict |
|---|---|---|---|---|
| F1 | « Relevé de température de la chambre froide : 4 °C » | `haccp-conformite-quotidienne` | haccp (« parle de relevé de température, HACCP ») | OK |
| F2 | « Y a plus de farine, faut recommander » | `reappro-fournisseurs` | reappro (« stock bas, commande fournisseur, réapprovisionnement ») | OK — `gestion-commandes` exige une commande CLIENT |
| F3 | « Quels plats je devrais virer de la carte ? » | `analyse-rentabilite-carte` | analyse (« quels plats garder », ingénierie de menu) | OK — `carte-vitrine` ne matche que « carte en ligne » |

### rapidocrm

| # | Phrase | Skill attendu | Descriptions qui matchent | Verdict |
|---|---|---|---|---|
| C1 | « Relance les impayés » | `devis-facture-relance` | devis-facture-relance (« relancer un impayé ») ; invoice-chase [rapido-suite] (« overdue invoices… unpaid invoices ») | **OK après correctif n°5** (avant : CONFLIT inter-plugins) — invoice-chase se déclare méthodo et renvoie l'exécution à devis-facture-relance |
| C2 | « Où en sont mes deals ? » | `coaching-pipeline` | coaching-pipeline (déclencheur verbatim) | OK — `pipeline-review-methodo` (tiers) garde ses déclencheurs EN de revue formelle |
| C3 | « Écris-moi un mail de relance pour le devis de Dupont » | `redaction-commerciale` | redaction-commerciale (« message de relance », rédiger) ; devis-facture-relance (mots « relance » + « devis ») | OK — « écris-moi » départage vers la rédaction ; les deux coopèrent (le process appelle la rédaction) |

### rapidocms

| # | Phrase | Skill attendu | Descriptions qui matchent | Verdict |
|---|---|---|---|---|
| M1 | « Génère un visuel avec le prix du burger affiché dessus : "Menu 12,90 €" » | `prompts-visuels-pro` (+ agent `prompt-designer`) | prompts-visuels-pro (« visuel contenant du texte sans aucune faute ») ; prompt-engineering-visuel (« générer une image ») | **OK après correctif n°1** (avant : CONFLIT) — la description de prompt-engineering-visuel renvoie désormais le texte incrusté à prompts-visuels-pro |
| M2 | « Poste un truc sur Insta pour demain » | `pipeline-contenu-social` | pipeline (« créer un post… programmer une publication… Instagram ») | OK |
| M3 | « Prépare le plan de posts du mois avec un bon mix découverte/vente » | `calendrier-editorial` + `funnel-tofu-mofu-bofu` | calendrier (« posts du mois ») ; funnel (« équilibre découverte/considération/vente ») | **OK après correctif n°3** (avant : la dimension funnel n'était déclenchée qu'avec les acronymes TOFU/MOFU) — duo voulu : le funnel s'insère dans le calendrier |

### rapidorh

| # | Phrase | Skill attendu | Descriptions qui matchent | Verdict |
|---|---|---|---|---|
| R1 | « Qui est surchargé cette semaine ? » | `detection-surcharge` | detection-surcharge (déclencheur verbatim) | OK |
| R2 | « Note mes heures d'aujourd'hui » | `daily-report` | daily-report (« ses heures du jour ») | OK |
| R3 | « On accueille Sarah lundi, prépare son arrivée » | `onboarding-equipe` puis `onboarding-rh-methodo` | onboarding-equipe (« ajouter un employé… onboarding ») ; onboarding-rh-methodo (« someone has a start date coming up ») | **OK après correctif n°4** (avant : CONFLIT) — onboarding-equipe crée les comptes et renvoie la checklist J1/S1/30-60-90 à la méthodo |

### rapido-suite

| # | Phrase | Skill attendu | Descriptions qui matchent | Verdict |
|---|---|---|---|---|
| S1 | « Prépare le CODIR » | `comite-de-direction` | comite-de-direction (« demande un comité de direction ») | OK — `presentation-codir` [rapido-canva] exige « présentation/slides » |
| S2 | « Apprends à connaître ma boîte » | `onboarding-entreprise` | onboarding-entreprise (« apprendre à connaître son entreprise ») | OK |
| S3 | « Structure les infos de ma startup pour que les agents les connaissent » | `dossier-startup-360` | dossier-startup-360 (déclencheur quasi verbatim) | OK |

### rapido-canva

| # | Phrase | Skill attendu | Descriptions qui matchent | Verdict |
|---|---|---|---|---|
| V1 | « Fais-moi un menu imprimable en PDF » | `menu-restaurant-design` | menu-restaurant-design (« menu imprimable ») | OK |
| V2 | « Une carte de visite pour mon commercial » | `supports-commerciaux` | supports-commerciaux (« carte de visite ») ; carte-digitale [rapidocms] et studio-templates [rapidocrm] citent aussi « carte de visite » | OK — départage par qualificatifs exclusifs : carte-digitale exige « digitale/NFC », studio-templates exige « template/éditeur RapidoCRM » ; sans qualificatif, l'imprimé Canva l'emporte (confirmer le support avec l'utilisateur) |
| V3 | « Des slides pour le comité de direction » | `presentation-codir` | presentation-codir (« slides pour le comité de direction ») | OK |

### rapido-lovable

| # | Phrase | Skill attendu | Descriptions qui matchent | Verdict |
|---|---|---|---|---|
| L1 | « Un site pour mon restaurant avec réservation en ligne » | `site-restaurant` | site-restaurant (« site pour son restaurant, site de réservation ») | OK |
| L2 | « Une page pour choper des leads pour la campagne d'été » | `usine-a-landing` | usine-a-landing (« page de campagne ou page de capture ») | OK |
| L3 | « Un chatbot qui répond à mes clients avec mes données » | `agent-ia-produit` | agent-ia-produit (« chatbot pour ses clients ou assistant connecté à ses données ») | OK |

### rapido-meta-ads

| # | Phrase | Skill attendu | Descriptions qui matchent | Verdict |
|---|---|---|---|---|
| A1 | « Lance une pub Instagram à 50 €/jour » | `lancement-campagne-meta` | lancement (« lancer une pub, une campagne Facebook/Instagram ») | OK — gardes argent réel : voir cas sensibles |
| A2 | « Booste mon meilleur post Insta » | `boost-post-instagram` | boost (« booster un post… meilleur post Instagram ») | OK |
| A3 | « Mes pubs, ça donne quoi ? » | `pilotage-performance-ads` | pilotage (« comment performent ses pubs, un bilan pub ») | OK — `performance-report-methodo` (tiers) garde ses déclencheurs EN de rapport formel |

### rapido-n8n

| # | Phrase | Skill attendu | Descriptions qui matchent | Verdict |
|---|---|---|---|---|
| N1 | « Envoie le récap business tous les vendredis, automatiquement » | `recettes-metier` | recettes-metier (« récap hebdo » au catalogue) ; usine-automatisations (« tous les jours / à chaque fois, fais… ») ; delegation-recurrence [rapido-direction] (« tous les lundis… ») | OK — la recette nommée est la plus spécifique ; usine = fabrication générique (la recette s'y déploie), delegation-recurrence = pont côté dirigeant qui route ici. Chaîne voulue, pas un conflit |
| N2 | « Mes automatisations tournent encore ? » | `surveillance-automatisations` | surveillance (déclencheur verbatim) | OK |
| N3 | « Le workflow ne doit pas relancer deux fois le même devis » | `memoire-operationnelle` | memoire (déclencheur verbatim) | OK |

### rapido-direction

| # | Phrase | Skill attendu | Descriptions qui matchent | Verdict |
|---|---|---|---|---|
| D1 | « Trie ma boîte mail » | `tri-boite-mail` | tri-boite-mail (« veut trier ses mails ») | OK |
| D2 | « Par quoi je commence ce matin ? » | `journee-du-dirigeant` | journee-du-dirigeant (déclencheur verbatim « par quoi je commence ») ; briefing-du-jour [foodeatup] (« point du matin ») | OK — journee est verbatim et FUSIONNE le volet FoodEatUp ; « le point du matin du restaurant » routerait vers briefing-du-jour |
| D3 | « Classe la facture PDF d'Orange dans le bon dossier Drive » | `coffre-documents` | coffre-documents (« classer un document… une facture ») ; devis-facture-relance [rapidocrm] (mot « facture ») | OK — « classer/dossier/Drive » départage ; devis-facture-relance couvre le CYCLE devis→facture→relance, pas le rangement |

## Cas sensibles obligatoires

| # | Phrase | Routage attendu | Vérification |
|---|---|---|---|
| X1 | « Génère un post avec le texte "Menu du Jour" incrusté » | `prompts-visuels-pro` + agent `prompt-designer` (protocole zéro faute : texte entre guillemets, épellation validée, ≤ 5 mots, relecture caractère par caractère) | OK après correctif n°1 — avant, « génère un post/visuel » pouvait rester dans prompt-engineering-visuel dont le bloc 6 EXCLUT le texte incrusté |
| X2 | « Le rendu affiche "Menu du Juor" — corrige » | `prompts-visuels-pro` (étape 4 : rejet, itération sur le bloc texte, 2 max puis post-prod) | OK après correctifs n°1-2 — avant, « améliorer un prompt image » (prompt-engineering-visuel) captait la demande sans protocole zéro faute |
| X3 | « Lance une campagne Meta à 80 €/jour » | `lancement-campagne-meta` (tout en PAUSED) ; hooks : `plafond-budget` REFUSE (80 > 50 €/j par défaut, sauf plafond maison dans rapido-kb/processus-internes.md) et `garde-argent-reel` force la confirmation sur ads_activate_entity. La phrase A1 à 50 €/j passe le plafond (= limite, pas au-delà) mais garde l'ask à l'activation | Hooks testés fonctionnellement sur stdin par `scripts/tester-skills.py` (deny 9 999 €, allow 10 €, ask activation) |
| X4 | « Supprime le client Martin » / « Repasse la facture F-12 en brouillon » | Aucun skill dédié (voulu : appel outil direct) ; hooks `garde-destructif` → ask sur tout delete_*, et deny DGFiP sur update_invoice_status statut=brouillon | Testés sur stdin par `scripts/tester-skills.py` (ask delete_x ; deny brouillon ; ask payee) |

## Cluster marques — `gestion-marques` / `gestionnaire-marques` (ajout 2026-07-10)

| # | Phrase | Skill/agent attendu | Descriptions qui matchent | Verdict |
|---|---|---|---|---|
| B1 | « Crée la marque de ma deuxième enseigne » | `gestion-marques` → `create_brand` | gestion-marques (« créer ou modifier une marque ») | OK — couleurs depuis la charte, `font_family` via l'ENUM, récap niveau 2 |
| B2 | « Ajoute ce logo transparent à ma marque » | `gestion-marques` → `upload_file_tool` + `add_asset` | gestion-marques (« ajouter un logo ou un asset de marque ») | OK — nommage `"<Marque> — logo — fond transparent"` |
| B3 | « Change les couleurs de ma marque » | `gestion-marques` → `edit_brand` | gestion-marques (« la charte d'une de ses marques ») | OK — récap niveau 2 avant appel |
| B4 | « Supprime la marque de test » | `gestion-marques` → `delete_brand` | gestion-marques + hook `garde-destructif` | OK — nom exact retapé (motif `delete_.*`) |
| B5 | « Génère le post d'annonce » (≥ 2 marques) | agent `gestionnaire-marques` (marque cible d'abord) | gestionnaire-marques (« refuse d'avancer sans marque cible identifiée ») | OK — DEMANDE la marque avant `pipeline-contenu-social` ; pas de défaut silencieux |
| B6 | « C'est quoi la charte de ma deuxième marque ? » | `gestion-marques` → `get_brand` | gestion-marques (« parle de la charte d'une de ses marques ») | OK — coexiste avec `contenu-conforme-marque` (qui IMPOSE la charte en génération) sans conflit |

Contre-exemples (ne doivent PAS router vers gestion-marques) : « Planifie mes posts du mois »
→ `calendrier-editorial` ; « Écris un article SEO » → `generation-article-blog` ; « Vérifie ce
texte contre la voix de marque » → `brand-review` (revue de contenu, pas gestion d'identité).

## Correctifs de descriptions appliqués (validés le 2026-07-06)

1. `rapidocms/skills/prompt-engineering-visuel` — ajout : « Pour un visuel
   avec du texte incrusté ou la correction d'une faute dans un rendu,
   utiliser prompts-visuels-pro. » (corrige M1, X1, X2)
2. `rapidocms/skills/prompts-visuels-pro` — ajout du déclencheur « ou
   corriger une faute de texte dans un visuel déjà généré » (corrige X2)
3. `rapidocms/skills/funnel-tofu-mofu-bofu` — ajout du déclencheur « un
   équilibre découverte/considération/vente » (corrige M3)
4. `rapidorh/skills/onboarding-equipe` — ajout : « Pour la checklist
   d'accueil (J1, semaine 1, 30/60/90), utiliser onboarding-rh-methodo. »
   (corrige R3)
5. `rapido-suite/skills/invoice-chase` — ajout : « Méthodo de relance au ton
   gradué ; l'exécution des relances de factures RapidoCRM passe par
   devis-facture-relance (plugin rapidocrm). » (corrige C1)

## Rejouer le test

À chaque nouveau skill ou modification de description : ajouter/rejouer les
phrases concernées ici, et vérifier qu'aucun verdict ne régresse. Les
frontmatters se valident par ailleurs avec `python3 scripts/tester-skills.py`
(unicité des name, convention « Utiliser quand », mentions croisées).
