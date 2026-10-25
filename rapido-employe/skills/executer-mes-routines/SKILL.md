---
name: executer-mes-routines
description: Utiliser quand l'employé déroule ses routines du registre, que l'utilisateur dit « exécute tes routines », « fais tourner les routines dues », « quelles routines aujourd'hui ». Liste les routines de l'Academy, exécute celles qui sont dues dans leur niveau d'autonomie et leurs quotas, et journalise chaque exécution.
---

# Exécuter mes routines (le registre fait foi)

Familles engagées : selon la routine (sa famille est celle de ses actions) ;
le journal (`log_routine_run`) est en **configurer**.

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.
2. Cadre du jour absent ou périmé → skill `prise-de-poste` d'abord.

## Workflow

1. **`list_routines`** (Academy) — nom, cadence, KPI, étape (V0/V1/V2),
   autonomie, verdict. Retenir celles DUES aujourd'hui (cadence + dernier
   passage au journal).
2. Pour chaque routine due : **`get_routine`** — son prompt (6 blocs :
   objectif, sources, limite, rendu, critère d'arrêt, accord humain), son
   journal, son historique.
3. **Exécuter dans le niveau de SA famille** et les quotas du jour :
   - une routine en Aperçu (toutes les 20 du registre actuel sont en V0
     Aperçu) MONTRE ce qu'elle ferait et attend l'accord ;
   - le critère d'arrêt du prompt s'applique à la lettre ;
   - les actions passent par les skills métier correspondants
     (`relancer-j3-j7`, `communication-de-la-semaine`…), jamais en direct.
4. **`log_routine_run`** après chaque exécution : fait, résultat, incident —
   c'est ce journal qui fait passer V0 → V1 (3 exécutions).
5. Récapituler : routines exécutées / sautées (et pourquoi), quotas
   consommés, ce qui attend un accord.

KPI : `routines-en-service`, plus ceux de chaque routine.
Formations : `rituels`, `orchestration`, `prospector-hub` (PH8).

## Garde-fous

- La source de vérité des routines est l'Academy (et Plan'It pour les
  planifiées) — le plugin n'en invente aucune ; le registre du dépôt
  (`reference/registre-routines.md`) n'est qu'un renvoi.
- Jamais deux variables changées sur une routine la même semaine ; le
  verdict appartient au vendredi (skill `boucle-du-vendredi`).
- Une routine dont le prompt échoue au contrat des 6 blocs se corrige avec
  `check_routine_prompt` AVANT d'être exécutée.
