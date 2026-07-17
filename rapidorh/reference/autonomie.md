# Niveaux d'autonomie (rapidorh)

> **Source de vérité** : `rapido-startup:reference/autonomie.md` + le registre
> `reference/registre-routines.md` (racine). Ce fichier en est le **rappel local**
> pour que les skills de `rapidorh` (dont `tournee-des-agents`) raisonnent sans
> dépendre d'un autre plugin. En cas de divergence, la version rapido-startup fait foi.

## Les 4 niveaux

- **Niveau 0 — Lecture seule** : appels MCP de lecture, calculs par script,
  écriture de journaux dans `./rapido-kb/` uniquement. Aucune confirmation requise.
- **Niveau 1 — Préparation** : brouillons et plans (tâche proposée, message non
  envoyé, plan) — présentés, jamais exécutés seuls.
- **Niveau 2 — Écriture confirmée** : création/modification dans les systèmes
  (tâches RapidoRh, dailies, rôles, utilisateurs…) — **une confirmation par
  système**, récapitulatif des IDs exigé (hook Stop récap).
- **Niveau 3 — Externe (JAMAIS automatique)** : tout ce qui sort de l'entreprise
  ou engage de l'argent/une personne — envoi d'email d'invitation
  (`create-user-tool`), suppression (`delete-user-tool`), publication externe.
  Demande explicite de l'utilisateur au moment T, confirmation dédiée.

## En tournée des agents (`tournee-des-agents`)

Ce que la tournée peut faire **seule**, par niveau de la tâche relayée :

| Niveau de la tâche | Comportement en tournée | Colonne de sortie |
|---|---|---|
| **0** lecture | exécuter, consigner le résultat | **Fait** |
| **1** préparation | produire le livrable préparé (brouillon/plan), consigner | **Fait** |
| **2** écriture confirmée | **préparer** l'écriture, **ne pas écrire sans confirmation** | **Validation** (attend le OK humain) |
| **3** externe | **JAMAIS en tournée** : préparer et **signaler**, aucune exécution | **Validation** + mention explicite au récap |

> Règle absolue : **niveau 3 n'est jamais exécuté en tournée.** Une tâche sans
> niveau d'autonomie lisible dans son relais est traitée comme **bloquée**
> (cf. `relais-par-tache.md`), jamais exécutée sur interprétation.
