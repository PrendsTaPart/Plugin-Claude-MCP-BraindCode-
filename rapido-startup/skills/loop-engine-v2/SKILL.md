---
name: loop-engine-v2
description: Utiliser quand l'utilisateur dit « lance R4/R5/R6/R7/R8/R9 », « routine du lundi », « board mensuel », « sentinelle cash », « épisode du jour », ou veut installer/planifier ses routines. Moteur des routines Loop Engine - Sense → Plan → Act → Feed → Report, calculs délégués à catalogue-kpi, autonomie gouvernée.
---

# Loop Engine v2 — le moteur des routines R4-R9

Chaque routine est un fichier autonome dans `references/routines/`, avec un
**bloc CONFIG interchangeable en tête** (pattern client-resellable : le même
fichier sert tous les clients, seule la CONFIG et la KB changent).

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et SURTOUT
`${CLAUDE_PLUGIN_ROOT}/reference/autonomie.md` (la gouvernance : ce qu'une
routine a le droit de faire seule). Seuils : `./rapido-kb/` prime.

## Workflow

1. **Identifier la routine** demandée :
   - « R4 », « routine du lundi », « revue finance » → `R4-CFO-WEEKLY.md`
   - « R5 », « avancement startup », « delta d'exécution » → `R5-STARTUP-BUILDER.md`
   - « R6 », « boucle growth », « expérience de la semaine » → `R6-GROWTH-LOOP.md`
   - « R7 », « sentinelle cash », « surveille ma trésorerie » → `R7-CASH-SENTINEL.md`
   - « R8 », « board mensuel », « pack investisseurs » → `R8-MONTHLY-BOARD.md`
   - « R9 », « épisode du jour », « vidéo du jour », « video factory » →
     `R9-VIDEO-FACTORY.md`
   Ambigu → demander laquelle (ou proposer la séquence hebdo R4→R5→R6).
2. **Charger le fichier de routine** et appliquer sa CONFIG : les valeurs de
   `./rapido-kb/` (fuseau, seuils, canaux) écrasent les défauts du bloc.
3. **Exécuter les 5 phases** du fichier, dans l'ordre :
   **Sense** (collecter — lecture seule) → **Plan** (analyser, prioriser) →
   **Act** (préparer/exécuter selon le niveau d'autonomie de
   `reference/autonomie.md` — confirmations sur tout envoi/écriture) →
   **Feed** (mettre à jour la mémoire : journaux `./rapido-kb/startup/`) →
   **Report** (restitution au format de la routine + récap des IDs).
4. **Tous les calculs chiffrés passent par le skill `catalogue-kpi`**
   (scripts/calcul_kpi.py — formule affichée, hook « KPI sans script »
   actif). Une routine ne calcule JAMAIS de tête.
5. **Installer/planifier les routines** (« installe mes routines ») :
   proposer le calendrier (R7 quotidien ou 2×/sem, R4-R6 hebdo, R8 mensuel),
   créer les événements récurrents Google Calendar (si connecté) après
   accord, et noter le planning dans `./rapido-kb/startup/routines.md`.
   Pour qu'une routine tourne SANS Claude : skill `usine-automatisations`
   (plugin rapido-n8n) — voir le `TODO` R7 au CHANGELOG.

## Garde-fous

- `reference/autonomie.md` fait LOI : lecture seule par défaut ; écritures
  par système après confirmation ; envois externes jamais automatiques ;
  écriture Stripe INTERDITE en routine (hook garde-stripe-write en filet).
- L'agent `cfo-virtuel` porte les routines financières (R4, R7, R8).
- Une routine qui ne trouve pas ses données le DIT (« pas de visibilité
  sur X ») — elle n'estime pas, elle n'invente pas.
- Chaque exécution laisse une trace datée dans
  `./rapido-kb/startup/routines-journal.md` (phase Feed).
