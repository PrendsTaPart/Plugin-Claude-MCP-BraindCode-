# Directives communes d'utilisation des outils (rapido-suite)

Règles applicables à TOUTE exécution de skill de ce plugin, qui orchestre
4 serveurs MCP : rapidocrm, rapidocms, rapidorh, foodeatup.
Au moindre doute sur un outil (paramètres pièges, formats, enums), consulter
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-outils.md`.

## 1. Résolution d'ID d'abord

- Ne JAMAIS deviner un ID, quel que soit le serveur : `entreprise_id` (CRM),
  `account_id`/`campagne_id`/`card_id` (CMS), IDs utilisateurs/projets/tâches
  (RH), `establishment_id` (FoodEatUp).
- Récupérer chaque ID via l'outil de liste/recherche du serveur concerné ou le
  demander à l'utilisateur, AVANT d'agir.
- La plupart des outils Rapido déduisent `company_id`/`user_id` de la session
  authentifiée ; FoodEatUp exige souvent un `establishment_id` EXPLICITE — le
  demander avant tout appel FoodEatUp.
- Réutiliser les identifiants d'un serveur à l'autre (ex. le nom client du CRM
  pour nommer le projet RH) — ne pas redemander ce qui est déjà connu.

## 1 bis. Base de connaissance entreprise (./rapido-kb/)

- Si le répertoire de travail contient `./rapido-kb/` (signalé par le hook de
  session), charger le(s) fichier(s) pertinent(s) AVANT de produire du contenu
  ou des recommandations : `entreprise.md`, `produits-services.md`,
  `propositions-valeur.md`, `cibles-personas.md`, `charte-graphique.md`,
  `ton-et-accroches.md`, `processus-internes.md`, `concurrents.md`.
- Priorité des sources : données MCP live > KB > références génériques du
  plugin. Un `### À COMPLÉTER` dans la KB = donnée manquante, à demander.
- La KB ne se modifie que via le skill `mise-a-jour-kb` ou par l'utilisateur ;
  si elle est absente, proposer le skill `onboarding-entreprise`.

## 2. Confirmation avant action destructrice ou irréversible

- Tout `delete_*`, tout envoi (email, SMS, publication), tout changement de
  statut légal de facture, toute suppression de pages/tâches : récapituler et
  obtenir un accord explicite.
- Règle transverse propre à ce plugin : une confirmation PAR SYSTÈME avant
  d'écrire dans un nouveau serveur — jamais deux serveurs modifiés sur une seule
  validation globale.

## 3. Ne jamais inventer de données

Montants, budgets, dates, températures, quantités : toujours fournis par
l'utilisateur ou lus via l'API du serveur concerné.

## 4. Locale et formats

- Monnaie : euros. Dates ISO `YYYY-MM-DD`, heures `HH:MM`.
- Respecter les formats stricts propres à chaque serveur : CMS
  `post_date` = `Y-m-d` / `post_heure` = `H-i-s` ; CRM envois planifiés
  `YYYY-MM-DD HH:MM:SS`.
- TVA : appliquer les règles du serveur concerné (restauration côté FoodEatUp,
  facturation côté CRM).
- Comparaisons multi-serveurs : toujours la MÊME période partout.

## 5. Gestion d'erreur

Si un outil échoue : expliquer clairement, ne PAS boucler. Dans un workflow
transverse, s'ARRÊTER à l'étape en échec, lister ce qui a déjà été créé dans les
serveurs précédents (pas de retour arrière silencieux), proposer l'alternative
manuelle.

## 6. Récapitulatif de fin de séquence

Terminer par un récapitulatif PAR SERVEUR des objets créés/modifiés avec leurs
IDs (CRM / CMS / RH / FoodEatUp), en mentionnant ce qui a été volontairement
sauté et pourquoi.
