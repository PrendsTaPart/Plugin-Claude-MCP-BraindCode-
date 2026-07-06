# Directives communes d'utilisation des outils (rapido-canva)

Règles applicables à TOUTE exécution de skill de ce plugin, qui croise le
serveur Canva avec les 4 serveurs Rapido.
OBLIGATOIRE avant tout appel Canva : charger
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-canva.md` (flux présentations, exports,
transactions d'édition, candidats, brand kits) et
`${CLAUDE_PLUGIN_ROOT}/reference/CONFORMITE.md` (données personnelles,
traçabilité des chiffres).

## 1. Résolution d'ID d'abord

- Côté Rapido : mêmes règles que les autres plugins — jamais d'ID deviné,
  `establishment_id` explicite pour FoodEatUp, `company_id`/`user_id` déduits
  de la session pour CRM/CMS/RH.
- Côté Canva : `design_id` (11 caractères, « D... ») vient de
  `create-design-from-candidate` ou `get-design` ; `job_id`/`candidate_id` de
  `generate-design` ; `brand_template_id` (« BTM... ») de
  `search-brand-templates`. Les IDs dans les URLs de candidats ne sont PAS des
  design IDs.

## 1 bis. Base de connaissance entreprise (./rapido-kb/)

Si `./rapido-kb/` existe dans le répertoire de travail, charger les fichiers
pertinents AVANT de produire : `charte-graphique.md` et `ton-et-accroches.md`
pour tout design, `propositions-valeur.md` + `concurrents.md` pour les
supports commerciaux, `processus-internes.md` pour les seuils cités dans les
slides. La KB PRIME sur les valeurs par défaut ; sans KB, standards du secteur
en le signalant (« valeur par défaut — lancez l'onboarding pour
personnaliser »).

## 2. Confirmation avant action irréversible

- `commit-editing-transaction` : TOUJOURS preview + accord explicite avant.
- Tout envoi (ex. `send_email` avec un document) : récapitulatif
  destinataire + pièce avant envoi.
- Publication d'un visuel généré (CMS) : validation du design exporté avant
  `schedule_draft_tool`.

## 3. Ne jamais inventer de données

Prix, plats, stats, preuves chiffrées : toujours issus des outils Rapido, de
la KB ou de l'utilisateur — chiffre sans source = pas de design (CONFORMITE.md).

## 4. Gestion d'erreur

Un appel Canva qui échoue : lire le message (« Common queries will not be
generated » = query trop vague ; « Missing scopes » = reconnecter le
connecteur), expliquer, ne pas boucler. Une transaction d'édition en échec au
commit = modifications perdues : le dire et proposer de recommencer.

## 4 bis. Dégradation propre

Si les outils Canva sont ABSENTS de la session (connecteur non activé) :
le dire en une phrase, indiquer la marche à suivre (activer le connecteur
Canva dans les paramètres / vérifier l'authentification via `/mcp`), et
faire ce qui reste possible avec les serveurs Rapido (préparer le contenu,
les textes, la structure — prêt à générer une fois Canva connecté). Jamais
d'erreur brute.

## 5. Récapitulatif de fin de séquence

Designs créés (IDs + liens), exports (URLs de téléchargement), objets Rapido
créés/modifiés (IDs par serveur), et sources des chiffres utilisés.
