---
name: tester-et-rapporter
description: Utiliser quand l'extension se teste — « fais la recette de l'app », « écris le rapport de test », « teste les cas d'erreur MCP ». Parcours manuel décrit, scénarios automatisés (jeton expiré, outil absent, entrée invalide, quota), rapport obligatoire.
---

# Tester et rapporter (critère n° 4 : le rapport est obligatoire)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/methode-build.md` (étape 07) ;
- les critères de recette TESTABLES du cahier des charges.

## Démarche
1. **Parcours manuel complet** sur le preview_url (`get_project`) : écran
   par écran, action par action, résultat CONSTATÉ (pas attendu) — y
   compris les trois états (vide, chargement, erreur).
2. **Scénarios automatisés des appels MCP** (via prompts Lovable de
   tests) : jeton expiré, outil absent du serveur, entrée invalide,
   quota atteint — chaque cas d'erreur a un comportement défini, pas une
   page blanche.
3. **Le rapport** : markdown structuré (périmètre testé, parcours, cas
   d'erreur, constats, écarts, verdict par critère de recette) — dans le
   docs/ du projet Lovable ou en lien ; widget rapport-de-test sur
   demande. Un écart constaté s'écrit tel quel : un rapport complaisant
   ne vaut rien.
4. **Enregistrer** : `save_project_progress` avec test_report_url ; carte
   de tests close par `complete_prompt_step` (needs_review si des écarts
   restent).
5. **Academy** : si le connecteur est branché, la mise en pratique des
   formations « recette » s'applique (exercices et preuves côté Academy).

## Pièges
- Tester seulement le chemin heureux : les quatre cas d'erreur MCP sont
  EXIGÉS par la méthode.
- Un rapport sans date ni commit/état de l'app ne permet pas de rejouer :
  horodater et lier l'état exact.

## Dégradation propre
Preview indisponible : `report_blocker`, et les scénarios s'écrivent quand
même (prêts à rejouer) — le rapport dit ce qui n'a pas pu être constaté.
