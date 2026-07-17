# Outils MCP manquants — specs pour le backend (Tunis)

> Registre des capacités MCP nécessaires aux skills mais **non exposées
> aujourd'hui** par les serveurs Rapido. Chaque entrée = spec courte (endpoint
> souhaité, champs, cas d'usage, priorité) pour l'équipe backend. Vérifié contre
> l'audit M0 (`docs/MATRICE-COUVERTURE.md`) et les schémas live. Aucune donnée
> inventée : tant qu'un outil n'existe pas, le skill fonctionne en **mode
> dégradé** documenté.

## 1. Télémétrie de délivrabilité (bounces / plaintes / échecs par destinataire)
- **Constat (live, audit M0)** : `get_stats_campagne` renvoie
  `{success, total, par_statut[]}` — des totaux par statut, **pas** de taux de
  bounce/plainte ni de motif d'échec par destinataire exploitable pour la
  délivrabilité.
- **Cas d'usage** : suivi post-envoi et runbook incident de `delivrabilite-email`
  (détecter un pic d'échecs, purger les invalides, décider une pause).
- **Endpoint souhaité** : `get_delivrabilite_campagne(campagne_id, periode)` →
  `{envoyes, delivres, bounces_hard, bounces_soft, plaintes, desabonnements,
  taux_bounce, taux_plainte, echecs: [{email_hash, motif, date}]}`.
- **Priorité** : haute (garde-fou d'envoi).

## 2. Infra warmup / rotation de boîtes / mesure de placement inbox
- **Constat** : aucun outil Rapido de warmup, de rotation de domaines/boîtes, ou
  de mesure de placement inbox↔spam (équivalents Smartlead/Instantly).
- **Cas d'usage** : montée en charge d'un domaine neuf ; envois froids à volume.
- **Souhait** : un MCP infra email dédié, ou une intégration externe documentée.
- **Priorité** : moyenne (contournable par la méthode + un outil externe en
  attendant ; la partie audit/méthode/garde-fous reste applicable).

## 3. Annulation d'un envoi planifié
- **Constat** : `schedule_email` / `schedule_sms` existent, mais **aucun outil
  d'annulation** d'un envoi déjà planifié n'est exposé côté CRM (RapidoCMS a son
  équivalent pour les posts).
- **Cas d'usage** : étape PAUSE du runbook incident (annuler les lots restants).
- **Endpoint souhaité** : `cancel_scheduled_email(id)` (analogue au tool
  d'annulation de posts planifiés de RapidoCMS).
- **Priorité** : haute (sécurité d'envoi).

## 4. Données d'intent tierces (enrichissement compte)
- **Constat** : pas de provider d'intent externe (ZoomInfo / Bombora / 6sense —
  techno installée, intent tiers, signaux d'achat marché) exposé côté Rapido.
- **Cas d'usage** : enrichir l'axe **intention** du skill `lead-scoring` au-delà
  des signaux first-party + actualité `account-research`.
- **Souhait** : un MCP d'enrichissement compte, ou une intégration documentée.
- **Priorité** : basse (les signaux first-party + `account-research` couvrent le
  besoin courant ; l'intent tiers est un bonus).

## 5. Clé de ré-scrape stable sur une fiche (place_id / cid Google Maps)
- **Constat** : aucun champ CRM dédié pour stocker `place_id` / `cid` / `data_id`
  d'une fiche Google Maps (identifiants stables d'un établissement).
- **Cas d'usage** : `rapido-gmaps:enrichissement-fiches` — re-scraper une fiche
  existante par son `place_id` pour compléter/rafraîchir ses coordonnées, sans
  re-chercher par nom (ambigu).
- **Endpoint souhaité** : champ `place_id` (+ `cid`) sur l'entreprise, ou
  `set_external_ref(entreprise_id, source, ref)` / `get_by_external_ref(source, ref)`.
- **Contournement actuel** : stocké en note `log_activity` + tag (non requêtable).
- **Priorité** : moyenne (débloque l'enrichissement fiable ; contourné en note).

## 6. Score de priorité prospect structuré
- **Constat** : pas de champ « score » structuré sur une fiche prospect ; le
  score `rating × log(review_count+1) × signal_opportunite` de `rapido-gmaps` ne
  peut être ni stocké ni filtré côté CRM.
- **Cas d'usage** : trier/segmenter les leads sourcés par score ; entraîner
  `rapido-marketing:icp-generator` sur « quels scores convertissent ».
- **Endpoint souhaité** : champ numérique `score` (ou `set_lead_score(id, valeur,
  source)`), filtrable par `rechercher_prospects`.
- **Contournement actuel** : note + tag de priorité (non requêtable finement).
- **Priorité** : moyenne.

## 7. Attributs structurés de fiche (popular_times / horaires / répartition avis)
- **Constat** : pas de réceptacle structuré pour `popular_times`,
  `reviews_per_rating`, `open_hours`, `about[]` d'une fiche Google Maps.
- **Cas d'usage** : recommander la **fenêtre d'appel** optimale (affluence),
  croiser avec `foodeatup:reservation_availability`.
- **Endpoint souhaité** : bloc `attributs` JSON sur l'entreprise, ou
  `set_entreprise_attributs(id, {...})`.
- **Contournement actuel** : note `log_activity` (lecture humaine seulement).
- **Priorité** : basse (la note libre suffit au premier usage).

## 8. Création de formulaire de capture (RapidoCRM)
- **Constat (live, LM0)** : côté formulaires, seuls `list_formulaires` et
  `get_formulaire_soumissions` sont exposés (**lecture**) ; **aucun `create_formulaire`**.
  `list_formulaires` → 0 formulaire.
- **Cas d'usage** : `rapido-leadmagnet:page-et-capture` — créer le formulaire de capture
  d'un lead magnet et câbler la soumission au pipeline, sans passer par Lovable.
- **Endpoint souhaité** : `create_formulaire(nom, champs[], consentement_rgpd:bool
  (checkbox non pré-cochée), redirect_url, webhook)` → à la soumission, déclenche
  `enregistrer_prospect` + tag + segment.
- **Contournement actuel** : **Lovable mode B** (`usine-a-landing` → `enregistrer_prospect`)
  ou formulaire intégré d'une landing `create_editor_template` (câblage à confirmer).
- **Priorité** : haute (débloque la capture native CRM de bout en bout).

## 9. Création de CTA tracké (RapidoCRM)
- **Constat (live, LM0)** : `list_cta` expose le **suivi** de clics (lecture) ; **aucun
  `create_cta`**. `list_cta` → 0.
- **Cas d'usage** : CTA « Télécharger le guide » tracké sur la landing du lead magnet.
- **Endpoint souhaité** : `create_cta(libelle, url_cible, campagne_id?)` → id trackable
  par `list_cta`.
- **Contournement actuel** : CTA en dur dans le HTML de la landing (tracking via
  paramètres UTM + soumission formulaire) ; pas de compteur natif tant que la création
  n'existe pas.
- **Priorité** : moyenne.

## 10. Câblage formulaire intégré → prospect d'une landing `create_editor_template`
- **Constat (live, LM0)** : `create_editor_template` crée une `landing_page` depuis du
  HTML (formulaire intégré prouvé en prod, ex. template id=7), mais le **câblage
  automatique soumission → prospect** n'est pas garanti sans `create_formulaire`/webhook.
- **Cas d'usage** : Route A 100 % native (landing CRM + capture) sans Lovable.
- **Souhait** : confirmer/documenter le mécanisme de capture d'un formulaire intégré
  publié dans l'éditeur CRM (ou exposer un webhook de soumission).
- **Priorité** : haute (débloque la Route A totalement native).

## 11. Auth multi-tenant des MCP Rapido (PRÉREQUIS PRODUIT — priorité absolue)
- **Constat (live, LV0)** : le pattern MCP de production (`academyrapido:execute-prompt`)
  appelle les URLs MCP **globales** (`crm/cms/rh.rapidosoftware`, `foodeatup.com/api/mcp`)
  avec `mcp_servers:[{type:url,url,name}]` **sans token ni scope par client**, et une
  **clé Anthropic plateforme partagée** (`settings.ANTHROPIC_API_KEY`). En session Claude
  Code, l'accès MCP passe par un **OAuth interactif par utilisateur** — inexploitable par
  un edge function serveur-à-serveur d'un site client.
- **Cas d'usage** : livrer à **chaque client** (restaurateur, commerçant) un **site
  agentique scopé sur SON établissement**, avec SES identifiants — sans qu'aucune clé
  BraindCode ni donnée d'un autre tenant ne fuite.
- **Souhait** : un mécanisme d'**auth MCP par tenant** :
  - **token par établissement/compte** (ex. header `Authorization: Bearer <token_tenant>`
    ou clé d'API scopée sur `foodeatup.com/api/mcp`) ;
  - **scope serveur non contournable** (`establishment_id`/`company_id` lié au token,
    jamais un paramètre que le front peut manipuler) ;
  - **rotation** et révocation des tokens ; journal d'accès par tenant.
- **Contournement actuel** : scope injecté **côté serveur** par l'edge function depuis
  l'env (jamais depuis le front) + clé du **client** en secret Lovable — mais tant que le
  serveur MCP n'isole pas par token, l'isolation reste imparfaite.
- **Priorité** : **absolue** — c'est le prérequis qui transforme le kit connecteur en
  **produit vendable** (chaque client son site agentique), pas juste un outil interne.

## 12. Police custom dans la charte CMS (au-delà des 9 web-safe)
- **Constat (live, D0)** : `edit_brand.font_family` est une **liste FERMÉE de 9 polices
  web-safe** (Arial, Verdana, Tahoma, Trebuchet MS, Georgia, Times New Roman, Garamond,
  Courier New, Lucida Console). Impossible de stocker une police riche (Google Font,
  fonderie) comme identité de marque.
- **Cas d'usage** : `rapido-design` — la direction artistique choisit souvent une police
  distinctive ; le CMS (source de vérité) ne peut pas la porter → divergence potentielle
  entre le DS Figma/Lovable (vraie police) et la charte CMS (approximation).
- **Souhait** : `font_family` en **texte libre** (nom de police + fallback) ou champ
  `font_url` (WOFF2/Google Fonts) sur la marque.
- **Contournement actuel** : la vraie police vit dans le **DS Figma/Lovable** ; le CMS
  stocke la **plus proche des 9** (documenté dans la charte KB). Le fil rouge couleurs
  reste intact ; seule la typo est approximée côté CMS.
- **Priorité** : moyenne (contourné ; gêne la fidélité typographique de marque).

## 13. Historisation des stocks bas (FoodEatUp) — pour la boucle d'amélioration n°14
- **Constat (inventaire, 164 outils)** : `list_low_stocks` renvoie un **instantané** des
  stocks sous seuil au moment de l'appel ; `list_stocks` / `adjust_stock` gèrent l'état
  courant. **Aucun outil ne renvoie une série temporelle** des ruptures/alertes de stock
  (historique daté sur 30 j).
- **Cas d'usage** : boucle d'amélioration **n°14** (« La commande fournisseur ni trop ni
  trop peu ») veut mesurer *ruptures évitées = alertes suivies d'une commande ≤ 24 h ÷
  alertes* sur 30 j — impossible sans historique des alertes de stock.
- **Souhait** : un outil `list_stock_alerts_history` (ou paramètre `since`/`from`/`to` sur
  `list_low_stocks`) renvoyant les alertes datées sur une fenêtre.
- **Contournement actuel** : la boucle **ANNONCE le proxy** (« lignes commandées non
  consommées à J+14 » comme proxy de sur-stock) et journalise elle-même les snapshots
  quotidiens dans `./rapido-kb/` pour reconstituer un historique — **jamais de proxy
  silencieux** (protocole `boucle-amelioration.md`).
- **Priorité** : moyenne (contourné par journalisation locale ; natif = mesure fiable).
