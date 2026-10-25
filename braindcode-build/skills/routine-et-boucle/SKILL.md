---
name: routine-et-boucle
description: Utiliser quand l'extension devient une routine mesurée — « écris la routine de mon extension », « audite le prompt de routine », « rattache la boucle KPI du projet ». Plan de routine Build, audit six blocs, coût Plan'It annoncé, rattachement, proposition sans acceptation d'office.
---

# Routine et boucle KPI (critère n° 5 : l'extension ne vaut que par sa routine)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/methode-build.md` (étape 10).

## Démarche
1. **Le plan de routine** : `get_project_routine_plan` — objectif chiffré,
   déclencheur, outils autorisés, garde-fous, point d'arrêt humain,
   mesure : les SIX blocs attendus.
2. **Audit du prompt** : par l'outil d'audit de la marketplace
   (`auditer_routines`, plugin.braindcode.com) s'il répond, sinon par
   `check_routine_prompt` de l'Academy — un bloc manquant = routine
   incomplète, on corrige avant de continuer.
3. **Côté Plan'It** : `select_routine_tools` (la sélection prend ~3 min :
   prévenir), puis `estimate_routine_cost` — le coût s'ANNONCE avant
   toute proposition.
4. **Rattacher côté Build** : `attach_project_routine` — routine, boucle,
   KPI (source réelle, cible, alerte), nom du plugin, URL du dépôt.
5. **Proposer côté Plan'It** : `propose_routine` — une PROPOSITION,
   enregistrée sans création ; l'acceptation n'arrive qu'après l'accord
   explicite sur CE coût annoncé. Jamais d'acceptation d'office.

## Délégation
L'exécution, la mesure des boucles et les améliorations vivent dans le
plugin planit s'il est installé — ici on CONÇOIT et on rattache.

## Pièges
- Un KPI sans source réelle (quel outil le mesure ?) ne se rattache pas :
  la mesure de la démo (skill `mesurer-la-demo`) peut servir de source.
- L'objectif « améliorer » n'est pas chiffré : un nombre, une unité, une
  échéance.

## Dégradation propre
Audit en échec des deux côtés (marketplace et Academy absents) : audit
maison sur les six blocs, marqué comme tel, et proposition retardée si un
bloc manque.
