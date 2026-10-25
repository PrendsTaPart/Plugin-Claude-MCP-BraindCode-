---
name: mon-equipe-d-agents
description: Utiliser quand l'équipe d'agents IA se construit ou se règle, que l'utilisateur dit « configure l'agent relances », « prépare la routine de l'agent accueil », « passe l'agent veille en service ». Lit les agents préparés dans l'Academy, écrit leurs routines aux six blocs, les rattache, et ne met en service qu'une routine V1 avec un KPI et un point d'arrêt.
---

# Mon équipe d'agents (six agents, des routines au contrat)

Famille engagée : **configurer** (Confirmé au cadre actuel — écritures
Academy avec aperçu serveur). `set_agent_state` vers « en service » a ses
conditions ; `set_agent_policy` est INTERDIT (gouvernance du responsable).

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow

1. **`list_agents`** — les six agents préparés dans l'Academy (Accueil des
   demandes, Relance et devis, Prescripteurs, Contenus, Veille, Pilotage) :
   rôle, état, routines rattachées.
2. **`get_agent_brief`** sur l'agent travaillé — son brief pour Plan'It
   (prompt système, connecteurs, limites). Le brief du serveur FAIT FOI :
   les fichiers agents de ce plugin ne fixent que le rôle, le périmètre
   d'outils et les garde-fous.
3. **La routine de l'agent** : écrire le prompt aux SIX BLOCS — objectif
   (chiffré), sources, limite, rendu, critère d'arrêt, accord humain — puis
   **`check_routine_prompt`** jusqu'à zéro manque, et **`configure_routine`**
   (aperçu → accord → confirm). **`attach_routine_to_agent`** pour le
   rattachement.
4. **Côté Plan'It** (si branché) : la routine planifiée s'enregistre là-bas
   (`create_routine` Plan'It / `propose_routine`) avec les mêmes six blocs ;
   `estimate_routine_cost` avant toute cadence serrée.
5. **Mise en service** : `set_agent_state` « en service » SEULEMENT si la
   routine est V1 (3 exécutions journalisées), avec un KPI rattaché et un
   point d'arrêt humain écrit. Sinon : l'agent reste en préparation et on le
   dit.
6. Le suivi vit dans les skills `executer-mes-routines` et
   `boucle-du-vendredi`.

KPI : `routines-en-service`.
Formations : `orchestration` (4 missions), `rituels`, `planit`.

## Garde-fous

- `set_agent_policy`, et toute validation de son propre cadre : deny absolu
  (hook garde-auto-gouvernance) — le responsable gouverne, l'employé
  configure.
- Pas de routine sans objectif chiffré ni garde-fou : `check_routine_prompt`
  est un passage obligé, pas une suggestion.
- Une routine par changement, un changement par semaine.
