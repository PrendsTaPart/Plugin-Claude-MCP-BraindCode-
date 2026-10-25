---
name: completer-les-vitrines
description: Utiliser quand les vitrines publiées se rattrapent une à une — « complète les tutoriels manquants des 20 vitrines », « rattrape la vitrine RapidoRH Ascend », « finis Daily Brief ». Projet par projet - retrouver le code Lovable, rédiger depuis le réel, republier sur accord.
---

# Compléter les vitrines publiées (le rattrapage)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md` — état au
  2026-10-25 : 20 vitrines « lauréat » sans tutoriel ; RapidoRH Ascend et
  PodForge Collective sans démo ; Daily Brief en brouillon (démo,
  tutoriel, fonctionnement, modèle économique manquants).

## Démarche — PROJET PAR PROJET, jamais en lot aveugle
1. **L'état réel** : `list_my_projects` + `check_project_readiness` du
   projet — ce qui manque AUJOURD'HUI (pas la liste d'hier).
2. **Retrouver le code** : `list_projects` Lovable avec query sur le nom,
   puis `get_project` (preview_url) et `read_file` sur les écrans clés.
3. **Rédiger depuis le réel** : le tutoriel suit le parcours CONSTATÉ
   (préview ouverte, étapes vérifiées) ; how_it_works décrit données,
   outils MCP et sécurité tels qu'ils sont dans le code.
4. **Ce qui exige l'humain** : démo manquante → deploy_project après
   validation mise_en_ligne ; business_model → sur indication seulement.
5. **Republier SUR ACCORD** : `publish_project` (hook garde-build), un
   projet à la fois, avec le diff de la vitrine montré avant.
6. **Consigner** : `save_project_progress` par projet complété.

## Pièges
- Vingt tutoriels « à la chaîne » sans ouvrir les apps = vingt tutoriels
  faux : chaque rédaction passe par le code et la préview DU projet.
- Daily Brief est en BROUILLON : le compléter ne le publie pas — la
  publication est une décision à part.

## Dégradation propre
Projet Lovable introuvable pour une vitrine : le dire, demander le lien,
et passer au suivant — pas de tutoriel écrit à l'aveugle.
