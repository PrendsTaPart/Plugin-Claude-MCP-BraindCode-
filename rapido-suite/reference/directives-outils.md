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

Si `./rapido-kb/` existe dans le répertoire de travail (signalé par le hook de
session), charger les fichiers pertinents AVANT de produire :
- contenu marketing/social → `ton-et-accroches.md` + `charte-graphique.md` +
  `propositions-valeur.md` + `cibles-personas.md` ;
- emails commerciaux / devis → `propositions-valeur.md` + `cibles-personas.md` +
  `processus-internes.md` (politique de remise, cadences) ;
- analyses financières / carte → `processus-internes.md` (seuils maison
  prioritaires sur les standards du secteur) ;
- toute comparaison marché → `concurrents.md`.
La KB PRIME sur les valeurs par défaut des skills. Si la KB est absente,
utiliser les standards du secteur ET le signaler (« valeur par défaut — lancez
l'onboarding pour personnaliser »), et proposer le skill `onboarding-entreprise`.

Priorité des sources : données OPÉRATIONNELLES (prix, stocks, stats, pipeline)
= MCP live d'abord ; identité de MARQUE (charte, ton, arguments) = KB d'abord
(complétée et validée par le client), l'API servant de vérification — signaler
tout écart. Un `### À COMPLÉTER` dans la KB = donnée manquante, à demander.
La KB ne se modifie que via le skill `mise-a-jour-kb` ou par l'utilisateur.

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
