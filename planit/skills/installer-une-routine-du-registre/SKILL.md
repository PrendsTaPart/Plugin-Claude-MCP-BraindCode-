---
name: installer-une-routine-du-registre
description: Utiliser quand une routine du registre de la marketplace s'installe dans Plan'It, que l'utilisateur dit « installe FIN-CFO-HEBDO dans Plan'It », « mets la routine MKT-HEBDO en place », « traduis cette routine du registre ». Traduit l'entrée de reference/registre-routines.md en proposition Plan'It — outils via la sélection, KPI du catalogue Plan'It, écarts dits.
---

# Installer une routine du registre (du dépôt vers Plan'It)

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.
2. Lire l'entrée du registre dans `reference/registre-routines.md` du DÉPÔT
   (identifiant canonique ou alias) : objectif, cadence, plugin
   propriétaire, KPI attendus.

## Workflow

1. **Qualifier** : l'entrée du registre devient une consigne Plan'It en une
   phrase (quoi, sur quels connecteurs, à quelle cadence, pour quel objectif
   chiffré — chiffré depuis le registre ou `./rapido-kb/`).
2. **`list_mcp_servers` (connected_only)** puis **`select_routine_tools`**
   sur la consigne (jusqu'à trois minutes — prévenir) : les outils viennent
   de la sélection, jamais recopiés du registre de tête.
3. **Le KPI** : **`list_kpi_catalog`** — si le KPI du registre N'EXISTE PAS
   dans le catalogue Plan'It, LE DIRE (la routine s'installe sans boucle, ou
   avec le KPI catalogue le plus proche, au choix de l'utilisateur) — jamais
   un KPI inventé.
4. **`estimate_routine_cost`** sur le brouillon, puis **`propose_routine`**
   (raison : « registre <ID> », fuseau Europe/Paris) — proposition
   enregistrée, acceptation seulement sur accord explicite (chaîne du skill
   `creer-une-routine`).
5. Consigner dans la conversation l'écart éventuel entre le registre et ce
   que Plan'It permet (outil manquant, KPI absent, cadence refusée).

## Garde-fous

- Le registre du dépôt fait foi pour l'INTENTION ; Plan'It fait foi pour les
  OUTILS et les KPI — aucun des deux ne se force.
- Une entrée du registre dont le plugin propriétaire n'est pas installé côté
  Claude Code se signale : la routine Plan'It n'en remplace pas les skills.
