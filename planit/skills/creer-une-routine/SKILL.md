---
name: creer-une-routine
description: Utiliser quand une routine se conçoit, que l'utilisateur dit « mets en place une routine qui… », « automatise ce geste chaque semaine », « crée une routine avec objectif chiffré ». Déroule la chaîne de l'Architecte — connecteurs, sélection d'outils, destructifs, KPI, coût, proposition — et n'accepte qu'après l'accord explicite sur CETTE proposition.
---

# Créer une routine (la chaîne de l'Architecte)

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
   `${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.
2. Si `./rapido-kb/` existe : y lire objectifs et seuils pour CHIFFRER
   l'objectif de la routine (jamais un objectif inventé).
3. Une routine refuse `once` et `custom` ; sans objectif chiffré, elle est
   incomplète — on ne la propose pas.

## Workflow

1. **`list_mcp_servers` avec `connected_only: true`** — la routine ne
   s'appuie QUE sur des connecteurs réellement connectés (relevé du
   2026-10-25 : FoodEatUp en erreur de jeton et RapidoCRM déconnecté
   seraient refusés par le serveur — le dire et renvoyer vers l'app).
2. **`select_routine_tools`** sur la consigne — PRÉVENIR : jusqu'à trois
   minutes. Le sous-ensemble scoré remplace toute devinette d'outils.
3. **`list_destructive_tools`** sur les connecteurs retenus — chaque étape
   destructive se nomme : elle forcera le niveau confirm.
4. **`list_kpi_catalog`** — le KPI de la boucle (target ou watch), son coût
   de collecte annoncé.
5. **`estimate_routine_cost`** sur le brouillon (frequency + scheduled_at) —
   le coût mensuel s'annonce AVANT la proposition ; base flat_price/default
   dite comme telle.
6. **`propose_routine`** — objectif chiffré, raison, outils sélectionnés,
   KPI (rôle, valeur cible, widget éventuel), fuseau **Europe/Paris**,
   niveau d'autonomie (auto = décision de l'utilisateur, jamais un défaut).
   La proposition est ENREGISTRÉE, pas créée.
7. **Présenter** : la proposition, son diff de coût mensuel, le créneau sans
   chevauchement (skill `agenda-des-routines`). Puis, et seulement sur
   l'accord explicite portant sur CETTE proposition :
   **`accept_routine_proposal`**.

## Variante directe (réservée à la demande EXPRESSE de l'utilisateur)

`create_task` avec `is_routine`, puis `attach_kpi_to_routine` (la référence
se FIGE maintenant — le dire), puis `add_kpi_widget` avec source
`suggested_by_routine` et le `task_id`. Même règle de coût annoncé.

## Garde-fous

- Une proposition refusée est définitive à l'identique — changer l'horaire
  ne suffit pas ; on repart de la conception.
- Jamais d'accept dans la foulée du propose : deux temps, deux accords.
- Les hooks garde-cout-annonce et garde-autonomie verrouillent en filet.
