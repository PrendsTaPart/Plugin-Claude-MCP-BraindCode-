---
name: boucle-du-vendredi
description: Utiliser quand la semaine se juge, que l'utilisateur dit « fais ta boucle du vendredi », « conclus les expériences et pose les verdicts », « prépare la revue hebdo de l'employé ». Conclut les expériences échues, en lance une par routine qui stagne (une variable), pose les verdicts, enregistre les KPI et la rétrospective, puis monte le rapport du vendredi sur son gabarit.
---

# Boucle du vendredi (mesurer, trancher, retenir)

Famille engagée : **configurer** (Confirmé — écritures Academy avec aperçu
serveur ; le rapport sortant suit le skill `rapport-de-fin-de-journee`).

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.
2. Les KPI de la semaine sont relevés (skill `point-du-matin` du jour fait).

## Workflow

1. **`get_improvement_review`** — l'état de la boucle : expériences échues,
   routines qui stagnent, leçons en attente.
2. **Conclure** : `conclude_experiment` sur chaque expérience échue — le
   résultat DIT par les chiffres (gagné/neutre/perdu), jamais au ressenti.
3. **Lancer** : `start_experiment` sur UNE SEULE variable par routine qui
   stagne — trois expériences actives au plus, et jamais deux variables sur
   la même routine.
4. **Trancher** : `set_routine_verdict` par routine due — gardée, ajustée ou
   arrêtée, avec la raison chiffrée. V0→V1 exige 3 exécutions au journal ;
   V1→V2 un KPI mesuré sur 14 jours — pas de promotion « à l'ancienneté ».
5. **Enregistrer** : `record_kpi` (mesures du vendredi, avec source) puis
   **`record_retrospective`** — ce qui a marché, raté, appris. Les leçons
   entrent dans la mémoire (`remember`, type méthode) et se relisent dans
   `get_claude_brief`.
6. **Le rapport du vendredi** : **`get_report_brief`** — son gabarit HTML
   fait le `tableau-de-bord-kpi` (widget, via
   `${CLAUDE_PLUGIN_ROOT}/scripts/render_widget.py`) ; remise au responsable
   via le skill `rapport-de-fin-de-journee` (email_report ou brouillon).

KPI : tous ceux des routines ; `routines-en-service`, `objectifs-atteints`.
Formations : `reporting` (8 missions), `rituels`, `orchestration`.

## Garde-fous

- Pas de verdict sans mesures : une routine sans journal cette semaine se
  constate (« non exécutée ») — elle ne se « garde » pas par défaut.
- Une variable à la fois : c'est la condition pour savoir ce qui a agi.
- La rétrospective nomme aussi les échecs — un vendredi sans rien d'appris
  est un vendredi raté.
