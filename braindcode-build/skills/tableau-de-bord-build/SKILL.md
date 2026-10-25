---
name: tableau-de-bord-build
description: Utiliser quand l'utilisateur demande « où en sont mes projets Build ? », « fais le point BraindCode Build », « qu'est-ce qui manque pour publier ? ». Un écran - projets, readiness, validations en attente, kanban du projet actif, idées proposées.
---

# Tableau de bord Build

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/methode-build.md` (les cinq critères) ;
- `${CLAUDE_PLUGIN_ROOT}/reference/carte-des-interconnexions.md`.

## Démarche
1. **Mes projets** : `list_my_projects` — statut, mode (ia/hybride),
   dernière progression.
2. **Readiness** : `check_project_readiness` sur CHACUN — la liste exacte
   de ce qui manque pour publier (démo, tutoriel, fonctionnement, modèle
   économique, images, liens). Rien n'est « presque prêt » : on liste.
3. **Validations en attente** : `get_pending_validations` — OAuth, clés,
   paiements, mises en ligne qui attendent l'humain.
4. **Kanban du projet actif** : `get_board` — cartes en cours, bloquées,
   à valider.
5. **Mes idées** : `list_my_ideas` — propositions et leur statut.
6. **Restitution en un écran** (widget tableau-de-bord-build sur demande) :
   par projet, ce qui manque et la PROCHAINE action ; les validations en
   attente en tête. Rien n'est exécuté d'office.

## Pièges
- Les éléments manquants viennent de `check_project_readiness`, jamais
  d'une impression : au relevé du 2026-10-25, les 20 vitrines publiées
  n'ont pas de tutoriel — voir skill `completer-les-vitrines`.
- Une validation en attente ne se « relance » pas en la recréant : on la
  montre à l'humain.

## Dégradation propre
Serveur Build non connecté (OAuth au premier appel) : le dire et proposer
la connexion ; aucun état inventé.
