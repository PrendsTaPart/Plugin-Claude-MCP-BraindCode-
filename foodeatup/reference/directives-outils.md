# Directives communes d'utilisation des outils (foodeatup)

Règles applicables à TOUTE exécution de skill de ce plugin.
Au moindre doute sur un outil (paramètres pièges, formats, enums), consulter
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-outils.md`.

## 1. Résolution d'ID d'abord

- Ne JAMAIS deviner un ID : `establishment_id`, IDs d'équipements, de tables, de
  réservations, de recettes, de plans de production, de produits, de fournisseurs…
- Récupérer chaque ID via l'outil de liste/recherche correspondant (`list_*`,
  `get_*`) ou le demander à l'utilisateur, AVANT d'agir.
- FoodEatUp exige un `establishment_id` explicite sur la quasi-totalité des
  outils : c'est l'« Étape 0 » de chaque skill. S'il est inconnu, le demander en
  premier — aucun autre appel avant.

## 1 ter. Résolution des noms (search_entities)

Tout skill qui reçoit un nom parlé ou écrit — produit, ingrédient, plat,
équipement, table, recette — le résout via `search_entities`
(`establishment_id` + `query` + `types` ciblés, ex. `["dish"]`,
`["equipment"]`) AVANT tout autre appel utilisant cet ID.
- Le serveur gère le fuzzy français (accents, pluriels) : passer le nom tel
  que dicté (« tomates », « frigo 3 »), ne pas le « corriger » soi-même.
- Si la réponse contient `ambiguous=true` : présenter les candidats à
  l'utilisateur et DEMANDER confirmation avant d'agir — jamais de choix
  silencieux.
- INTERDICTION de deviner un ID (cf. règle 1) : `search_entities` est le
  chemin nominal du nom vers l'ID ; les `list_*` restent le repli quand on
  veut un inventaire complet plutôt qu'une résolution.

## 1 bis. Base de connaissance entreprise (./rapido-kb/)

Si `./rapido-kb/` existe dans le répertoire de travail, charger les fichiers
pertinents AVANT de produire :
- contenu marketing/social → `ton-et-accroches.md` + `charte-graphique.md` +
  `propositions-valeur.md` + `cibles-personas.md` ;
- emails commerciaux / devis → `propositions-valeur.md` + `cibles-personas.md` +
  `processus-internes.md` (politique de remise, cadences) ;
- analyses financières / carte → `processus-internes.md` (seuils maison
  prioritaires sur les standards du secteur) ;
- toute comparaison marché → `concurrents.md`.
La KB PRIME sur les valeurs par défaut des skills. Si la KB est absente,
utiliser les standards du secteur ET le signaler (« valeur par défaut — lancez
l'onboarding rapido-suite pour personnaliser »).

## 2. Confirmation avant action destructrice ou irréversible

Récapituler l'action et obtenir un accord explicite de l'utilisateur avant :
- toute suppression (`delete_dish`, `delete_recipe`, `delete_ingredient`,
  `delete_client`, `delete_employee`, `delete_product`, `delete_category`…) ;
- `cancel_reservation`, `no_show_reservation` ;
- toute commande fournisseur (`create_supplier_order`) — elle engage un achat ;
- `adjust_stock` en mode `set` (écrase la valeur existante).
Une confirmation PAR action ; un accord donné pour une action ne vaut pas pour la
suivante.

## 3. Ne jamais inventer de données

Températures, quantités, montants, prix d'ingrédients, dates, réponses de
checklists : toujours fournis par l'utilisateur ou lus via l'API. Valeur
manquante → la demander, ne pas supposer.

## 4. Locale et formats

- Langue : français par défaut. Devise : celle du client — lue dans
  `./rapido-kb/entreprise.md` si renseignée (défaut : euros, en le signalant).
  Dates ISO `YYYY-MM-DD`, heures `HH:MM`.
- TVA restauration (règles FRANCE, défaut produit — si la KB définit une
  autre juridiction, elle prime) : `immediate` = 10 % (consommation
  immédiate) ; `conservable` = 10 % sur place / 5,5 % à emporter (demander le
  canal si ambigu) ; `alcohol` = 20 %.
- Quantités de recettes en poids BRUT.

## 5. Gestion d'erreur

Si un outil échoue : expliquer clairement la cause probable, ne PAS boucler ni
réessayer aveuglément (un seul retry si erreur transitoire évidente), proposer
l'alternative manuelle (ex. saisie dans l'interface FoodEatUp).

## 6. Récapitulatif de fin de séquence

Terminer chaque séquence par la liste des objets créés/modifiés avec leurs IDs
(relevés, réceptions, étiquettes, réservations, recettes, productions,
commandes), plus les non-conformités ou alertes détectées.
