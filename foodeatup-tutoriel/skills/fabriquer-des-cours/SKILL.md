---
name: fabriquer-des-cours
description: Utiliser quand un administrateur de l'Académie FoodEatUp crée ou gère des contenus de formation — « crée un cours sur la clôture de caisse », « monte un parcours onboarding serveur », « publie ce cours », « change le rôle de cet utilisateur », « où en sont les candidatures et paiements ». Création en BROUILLON uniquement : un humain publie.
---

# Fabriquer des cours (administration de l'Académie)

## La règle du serveur, non négociable

**Tout contenu créé par l'IA reste en brouillon (`published=false`).** C'est
une règle du serveur Academy FoodEatUp, pas une politesse : un humain valide
dans `/admin/contenu-cours`. Toutes les actions sont journalisées côté serveur
(`admin_mcp_audit_tail` pour relire la piste).

## Enchaînement d'outils MCP

1. **Ne pas créer de doublon** : `academy_search` + `academy_list_parcours`
   AVANT toute création — un cours existant s'améliore, il ne se duplique pas.
2. **Créer (brouillons)** :
   - `admin_cours_create` : un cours = un geste métier précis (« clôturer la
     caisse »), adossé aux VRAIS outils du restaurant (citer les skills des
     plugins foodeatup comme travaux pratiques) ;
   - `admin_parcours_create` : un parcours = une progression de rôle
     (serveur, cuisinier, gérant), cours ordonnés du simple au composé ;
   - `admin_prompt_create` : les prompts d'accompagnement du marketplace.
3. **Publier — acte humain** : `admin_publish_toggle` passe par le garde-fou
   du plugin (confirmation) ; récapituler le contenu avant (titre, parcours,
   public visé). Jamais de publication en lot.
4. **Gérer** : `admin_users_search` (retrouver un compte),
   `admin_user_role_set` (changement de rôle = acte de gouvernance →
   confirmation, et jamais d'auto-promotion), `admin_candidatures_list`
   (candidatures formateurs à traiter), `admin_paiements_summary`
   (synthèse des paiements — chiffres lus, pas calculés de tête).
5. **Auditer** : `admin_mcp_audit_tail` — relire ce que l'IA a fait côté
   Académie, c'est le journal de confiance.

## Qualité d'un cours (avant de créer)

- Un objectif observable (« à la fin, l'apprenant clôture une caisse seul »),
  pas un thème vague.
- Les étapes s'appuient sur les écrans et outils réels de FoodEatUp — pas de
  capture inventée, pas de fonctionnalité supposée : vérifier contre la liste
  live des outils (docs/inventaires/foodeatup-tools-live.txt).
- Chaque cours se termine par un exercice faisable dans l'établissement de
  l'apprenant.

## Ce que ce skill NE fait PAS

- Suivre sa formation → skill `se-former-foodeatup` ; activité formateur →
  skill `enseigner-foodeatup`.
- Les tutoriels vidéo (storyboards, rendus) → plugin RapidoTuto, hors
  périmètre de ce plugin.
