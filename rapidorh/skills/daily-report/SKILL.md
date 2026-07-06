---
name: daily-report
description: Utiliser quand l'utilisateur parle de daily, de rapport journalier ou de ses heures du jour dans RapidoRh. Crée le daily du jour avec les tâches travaillées et les heures, en appliquant les règles strictes du serveur.
---

# Daily report

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).

## Règles STRICTES (refus du serveur sinon)

- **Un seul daily par jour par utilisateur** : vérifier AVANT de créer.
- **Heures entre 0,5 et 24 par tâche** : refuser toute valeur hors bornes.
- **Réservé aux membres** : les owners ne créent PAS de dailies (ils les
  consultent). Si l'utilisateur est owner, le lui rappeler au lieu d'appeler
  l'outil.

## Workflow

1. **Vérifier qu'aucun daily n'existe aujourd'hui** — `get-dailies-tool`
   (`date` = date du jour YYYY-MM-DD). S'il en existe déjà un : STOP, informer
   l'utilisateur (pas de doublon possible) et proposer de lister son contenu.
2. **Récupérer des task_id valides** — `get-project-tasks-tool` (`project_id`,
   via `get-projects-list-tool` si besoin) : le daily ne peut référencer que des
   tâches existantes, assignées à l'utilisateur. Ne JAMAIS inventer un `task_id`.
3. **Collecter les heures** — pour chaque tâche travaillée : heures (0,5 à 24) et
   description facultative du travail effectué. Si l'utilisateur donne un total
   sans détail, demander la répartition par tâche.
4. **Créer le daily** — `create-daily-tool` (`tasks` = liste
   `{task_id, hours, description}`). Le daily est daté d'aujourd'hui
   automatiquement (pas de date rétroactive possible via cet outil).
5. **Confirmer** — récapituler : tâches, heures par tâche, total du jour. Si le
   total dépasse 12 h, le signaler (probable erreur de saisie).

## Garde-fous

- En cas d'erreur du serveur « daily déjà existant », ne PAS réessayer : expliquer
  la règle un-par-jour.
- Heures invalides (0, négatives, > 24 ou < 0,5) : demander correction avant tout
  appel.
- Consultation : `get-dailies-tool` (owner : filtres `user_id`, `search` ;
  membre : ses propres dailies uniquement).
