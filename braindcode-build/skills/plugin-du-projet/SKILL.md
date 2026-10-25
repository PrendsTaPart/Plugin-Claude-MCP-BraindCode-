---
name: plugin-du-projet
description: Utiliser quand l'extension publie son plugin Claude Code — « génère le plugin du projet », « mets le scaffold aux normes du dépôt », « ouvre la PR du plugin ». generate_plugin_scaffold, normes marketplace, validateurs, PR, enregistrement Build.
---

# Le plugin Claude Code du projet (critère n° 2)

## Étape 0
- CONTRIBUTING.md et docs/POLITIQUE-VERSIONS.md de CE dépôt ;
- `${CLAUDE_PLUGIN_ROOT}/reference/methode-build.md`.

## Démarche
1. **Le scaffold** : `generate_plugin_scaffold` avec le slug du projet —
   chemin et contenu EXACTS de chaque fichier, prêts pour ce dépôt.
2. **Écrire** les fichiers sur la branche du projet (jamais main), puis
   les mettre AUX NORMES de la marketplace : description « Utiliser
   quand… », étape 0 reference/, hooks fail-closed testés, inventaire
   d'outils versionné, CHANGELOG daté, tests/evals.md, entrée
   marketplace.json synchronisée, table du README régénérée PAR LE SCRIPT.
3. **Compléter** : si la CI réclame un fichier absent du scaffold, le
   gabarit `get_plugin_kit` de l'Academy sert de référence (plugin.json,
   SKILL.md, hooks.json, script de hook).
4. **Valider** : python3 scripts/valider-plugins.py et
   python3 scripts/tester-skills.py jusqu'à ZÉRO erreur.
5. **Ouvrir la pull request** (draft) avec le récapitulatif.
6. **Enregistrer côté Build** : `attach_project_routine` reçoit
   plugin_name et plugin_repo_url ; `save_project_progress`.

## Pièges
- Un scaffold collé tel quel ne passe pas la CI du dépôt : les normes
  maison (étape 0, hooks testés, inventaires) s'ajoutent TOUJOURS.
- La table du README ne s'édite jamais à la main.

## Dégradation propre
Scaffold incomplet côté serveur : le dire, générer le manquant depuis
get_plugin_kit, et consigner l'écart (report_blocker si c'est un bug
Build).
