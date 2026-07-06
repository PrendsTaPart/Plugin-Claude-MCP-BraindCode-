---
name: revue-projet-hebdo
description: Utiliser quand l'utilisateur demande où en est le projet, une revue hebdo projet ou l'avancement. Mesure l'avancement par colonne, détecte blocages et retards, lit les dailies de la semaine et livre 3 actions.
---

# Revue projet hebdo

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).

## Workflow (lecture seule jusqu'aux actions validées)

1. **Identifier le projet** — `get-projects-list-tool` (`search` par nom) si le
   `project_id` n'est pas connu ; noter son statut (0 en cours / 1 terminé /
   2 archivé).
2. **Avancement par colonne** — `get-task-lists-tool` (IDs des colonnes) puis
   `get-project-tasks-tool` (`project_id`, par `tasklist_id`) :
   - % d'avancement = tâches en Done / total des tâches (préciser le mode de
     calcul ; pondérer seulement si l'utilisateur le demande) ;
   - répartition Todo / Doing / Done (+ colonnes personnalisées).
3. **Tâches bloquées** — en Doing depuis trop longtemps (défaut : > 5 jours
   ouvrés ; demander le seuil de l'équipe si différent). Si l'API n'expose pas
   la date d'entrée en colonne, croiser avec les dailies (une tâche en Doing
   sans aucune heure déclarée dessus cette semaine = suspecte) et le dire.
4. **Tâches en retard** — `due_date` dépassée et pas en Done : lister avec
   assigné et retard en jours.
5. **Dailies de la semaine** — `get-dailies-tool` (par `date`, boucler sur la
   semaine ; vue owner pour toute l'équipe) : qui a rempli, heures par
   personne, membres sans daily plusieurs jours de suite.
6. **Synthèse** :
   ```
   📊 REVUE PROJET — {projet} — semaine {n}
   Avancement : X % (Done a/b) | Todo n | Doing n | Done n
   🚧 Bloquées (> 5 j en Doing) : tâche | assigné | piste
   ⏰ En retard : tâche | assigné | échéance | retard
   📝 Dailies : remplis x/y — absents : …
   ✅ 3 ACTIONS (assignées, datées)
   ```
7. **3 actions maximum** — chacune : quoi + qui + pour quand, adossée à l'outil
   ou au skill concerné (`move-task-tool` pour débloquer, `create-task-tool`
   pour découper une tâche trop grosse, `detection-surcharge` si la cause est
   une personne débordée). Exécution APRÈS validation de l'utilisateur.

## Garde-fous

- Les blocages se formulent en termes de tâches et d'obstacles, pas de
  personnes (« la tâche X attend Y » et non « Untel traîne »).
- Ne pas conclure « bloqué » sur un seul signal : croiser colonne + dailies +
  échéance avant d'alerter.
- Membre vs owner : `get-project-tasks-tool` et `get-dailies-tool` ne renvoient
  la vue complète qu'à un owner — signaler si la revue est partielle.
