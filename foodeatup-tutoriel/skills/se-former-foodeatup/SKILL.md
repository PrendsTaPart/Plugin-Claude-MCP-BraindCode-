---
name: se-former-foodeatup
description: Utiliser quand l'utilisateur veut se former sur FoodEatUp ou suivre sa formation — « apprends-moi à utiliser la caisse », « quel tutoriel pour le HACCP », « où j'en suis dans ma formation », « marque ce cours comme terminé », « mes prochaines sessions de formation ». Parcours apprenant de l'Académie, relié aux vrais besoins du restaurant.
---

# Se former sur FoodEatUp (parcours apprenant)

## Le principe : la formation part du besoin réel

Ne jamais dérouler un catalogue à l'aveugle. D'abord identifier CE QUI COINCE
dans l'exploitation (une question posée, une erreur répétée, un module jamais
utilisé — les plugins foodeatup le montrent), puis chercher le cours qui y
répond.

## Enchaînement d'outils MCP

1. **Trouver** : `academy_search` (mots-clés du besoin : « HACCP », « caisse »,
   « campagne ») ; `academy_list_parcours` pour la vue d'ensemble des parcours.
2. **Choisir** : `academy_get_parcours` (contenu, prérequis, durée) puis
   `academy_get_cours` pour le détail d'un cours. Croiser avec `me_mes_achats`
   (ce qui est déjà acquis) — ne jamais recommander d'acheter un contenu déjà
   possédé.
3. **Suivre** : `me_progression` (où en est l'apprenant, cours par cours) ;
   `me_reservations_upcoming` (sessions à venir — les rappeler la veille si on
   fait un point).
4. **Valider** : `me_mark_cours_complete` UNIQUEMENT quand l'utilisateur dit
   avoir terminé le cours — jamais pour « faire avancer la barre ».
5. **Organiser** : `me_favorites_add` / `me_favorites_remove` pour la liste
   « à suivre » ; `academy_get_public_link` / `academy_list_public_links` pour
   partager un contenu public à un collègue.

## Règles

- La progression affichée vient de `me_progression`, jamais estimée.
- Un cours marqué complet est un acte de l'utilisateur, pas une initiative.
- Recommandation = 1 à 3 cours maximum, chacun avec SA raison (« parce que tu
  as bloqué sur la clôture de caisse hier ») — pas une liste de catalogue.

## Ce que ce skill NE fait PAS

- Suivre ses apprenants en tant que formateur → skill `enseigner-foodeatup`.
- Créer un cours → skill `fabriquer-des-cours`.
- Exécuter l'opération du restaurant elle-même → plugins foodeatup (faire)
  vs ce plugin (apprendre à faire).
