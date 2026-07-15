---
name: sales-intelligence-fireflies
description: Utiliser quand l'utilisateur veut « analyser mes calls », savoir « quelles objections reviennent », capter la « voix du client », « miner mes transcripts » ou comprendre « ce que disent les prospects en RDV ». Transforme les transcripts de RDV réels (MCP Fireflies) en playbook d'objections chiffré et en hooks de copy, avec verbatims anonymisés.
---

# Sales intelligence — miner les RDV réels (Fireflies)

Ce skill est la **SOURCE DE DONNÉES** de la voix du client : il extrait des
**transcripts d'appels réels** (MCP Fireflies) les objections récurrentes, les
questions qui reviennent et les patterns gagné/perdu, puis les réinjecte dans la
copy et la qualification. **Ce n'est pas un doublon** des skills d'objections.

Adapté de la fiche `docs/methodo/ops/sales-intelligence.md` (distillation
gtm-flywheel, MIT © 2026 ColdIQ — voir `docs/methodo/ops/NOTICE.md`), branchée
sur NOS données.

## Articulation (à dire en tête d'exécution)
- `rapido-forge:scale-objections-playbook` = **FORMAT du livrable** (objection →
  réponse structurée LAER + preuve). Ce skill le **remplit avec des données
  réelles**, il ne le réécrit pas.
- `rapidocrm:mom-test` = **grille de lecture des verbatims** : ne retenir que le
  **passé** et le **concret** (« la dernière fois que… », un budget déjà dépensé,
  un outil déjà en place) — **jamais une intention** (« je paierais », « ce
  serait bien »), qui ne prédit rien.
- Ce skill **alimente** `rapidocrm:redaction-commerciale` et `machine-outbound`
  (hooks de copy), il ne rédige pas les messages lui-même.

## Étape 0 — Charger (obligatoire)
- `${CLAUDE_PLUGIN_ROOT}/reference/garde-fous-marketing.md` — **§b (données
  personnelles / RGPD)** s'applique en plein : un transcript est une **donnée
  personnelle**.
- `${CLAUDE_PLUGIN_ROOT}/reference/priorite-mcp.md` (ordre des serveurs, mode dégradé).
- `./rapido-kb/marketing/icp.md` (cible : à qui rattacher les objections) et
  `./rapido-kb/marketing/apprentissages.md` (leçons passées — elles **priment**).
  Fichiers absents → créés depuis `${CLAUDE_PLUGIN_ROOT}/reference/kb-templates/`
  (voir `reference/memoire.md`).

## Garde-fous (non négociables)
- **Périmètre confirmé AVANT toute lecture** : jamais de `fireflies_get_transcripts`
  sur « tous mes appels » sans cadrage (période, type de calls, participants).
  Un périmètre trop large ou non confirmé = **on demande le cadrage, on ne lit pas**.
- **Transcripts = données personnelles** → usage **interne KB uniquement**.
- **Aucun nom de client** dans un livrable publiable **sans accord écrit** : les
  verbatims sortent **anonymisés** (le script s'en charge) ; toute réutilisation
  nominative (témoignage, étude de cas) est proposée, jamais faite d'office.

## Pipeline

### 1. Cadrage & sélection (confirmé)
- Faire préciser : **période** (du/au), **type de calls** (découverte, démo,
  closing…), **participants** (emails), objectif d'analyse.
- Puis **`fireflies_get_transcripts`** filtré (`fromDate`/`toDate`, `participants`,
  `keyword`, `limit` ≤ 50) → liste de RDV. Recherche fine possible via
  **`fireflies_search`** (grammaire `keyword:"…" scope:sentences from:… to:…`).
- Présenter la liste retenue (titre, date, participants) et **faire valider** avant
  d'aller au détail.

### 2. Récupération du détail
- Par call retenu : **`fireflies_get_summary`** (aperçu, action items, mots-clés)
  puis **`fireflies_get_transcript`** (phrases + speakers horodatés) pour le
  contenu à miner. `fireflies_get_transcripts` ne renvoie **pas** le détail —
  toujours passer par ces deux appels par ID.

### 3. Mining (par script — jamais de comptage de tête)
- Construire l'entrée JSON depuis les transcripts : pour chaque call, `id`, `date`,
  `issue` (voir étape 4), `masquer` (noms + emails + enseignes des participants
  externes), et `phrases` avec `role` (`externe` = prospect / `interne` =
  commercial), `time`, `texte`.
- Lancer :
  `python3 "${CLAUDE_PLUGIN_ROOT}/skills/sales-intelligence-fireflies/scripts/mine_transcripts.py" entree.json`
- Le script sort, **avec formule affichée** : fréquence des objections par catégorie
  (**prix, timing, concurrent, confiance, technique, autorité**), leur **part**,
  les **questions récurrentes** (≥ 2 occurrences), et des **verbatims horodatés
  ANONYMISÉS** (emails/téléphones/noms remplacés par jetons — fonction
  `anonymiser` du script). Grille `mom-test` : ne garder que passé/concret.

### 4. Croisement CRM (issue des deals)
- Rattacher chaque call à son entreprise : **`rechercher_prospects`** puis
  **`get_entreprise`** (rapidocrm) pour lire l'issue (gagné / perdu / en cours).
- Renseigner `issue` dans l'entrée du script → sortie **patterns gagné vs perdu**
  (quelles objections dominent les deals perdus). Issue inconnue = `null`, jamais
  inventée.

## Livrables données
- **`./rapido-kb/marketing/objections.md`** au **format
  `rapido-forge:scale-objections-playbook`** : par objection →
  **fréquence chiffrée** (du script) → **réponse recommandée** (LAER) →
  **preuve/verbatim anonymisé horodaté**. Trié par part décroissante.
- **Hooks de copy** proposés à `rapidocrm:redaction-commerciale` et à
  `machine-outbound` (accroches qui répondent aux objections dominantes) — proposés,
  jamais envoyés.
- **Mise à jour `benchmarks.md`** (part des catégories = référence) et
  **`apprentissages.md`** : **1 à 3 leçons datées**, chacune adossée à **≥ 2
  occurrences chiffrées** (format `date | contexte | leçon | preuve | skill
  source`). **Aucune leçon sur un cas unique.**

## Write-backs CRM/Fireflies — OPTIONNELS et confirmés un par un
- **`log_activity`** (rapidocrm) sur les fiches entreprises concernées (synthèse
  des objections du RDV) — proposé fiche par fiche, jamais en masse.
- **`fireflies_create_soundbite`** (`transcriptId`, `startTime`/`endTime` en
  secondes) pour capturer les **meilleurs moments** d'enablement — un extrait à la
  fois, après accord ; `privacies` par défaut `team`.

## Mode dégradé
- **MCP Fireflies indisponible** (non connecté / `${FIREFLIES_MCP_URL}` absent) :
  ne rien inventer — signaler que la source de transcripts manque, proposer
  l'import manuel d'un export (coller le texte → même entrée JSON du script) et
  **flaguer au backend (Tunis)** le besoin de connecter Fireflies.
- **CRM absent** : mining possible sans l'issue (patterns gagné/perdu omis, dit
  explicitement).

## Capitalisation automatique (obligatoire)
À chaque analyse close : 1-3 leçons datées et **sourcées** (chiffre du script)
dans `apprentissages.md`, `benchmarks.md` mis à jour si une part de catégorie
devient une référence — via `mise-a-jour-kb`. Pas de leçon sans preuve chiffrée.

## Cas d'usage croisés
- Format & traitement des objections → `rapido-forge:scale-objections-playbook`.
- Lecture des verbatims (passé/concret) → `rapidocrm:mom-test`.
- Rédaction des messages nourris par ces objections → `rapidocrm:redaction-commerciale`.
- Réinjection en séquences → `machine-outbound`.

## Garde-fous (rappel)
Périmètre **confirmé avant lecture** ; transcripts = **données personnelles**
(KB interne) ; verbatims **anonymisés**, aucun nom publiable sans accord écrit ;
fréquences **par script** (jamais de tête) ; write-backs confirmés un par un ;
issue jamais inventée.
