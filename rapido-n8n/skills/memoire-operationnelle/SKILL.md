---
name: memoire-operationnelle
description: Utiliser quand un workflow a besoin d'une mémoire entre exécutions — ne pas relancer deux fois le même devis, se souvenir de ce qui a été traité. Gère les tables de données n8n comme mémoire tampon, une table par usage documenté.
---

# Mémoire opérationnelle (tables de données n8n)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-n8n.md`.

## Principe

Les tables de données n8n servent de MÉMOIRE TAMPON entre exécutions de
workflows — l'exemple canonique : une table `relances_envoyees`
(devis_id, palier, date) pour ne JAMAIS relancer deux fois le même devis au
même palier.

RÈGLE : **une table = un usage**, documenté dans le registre des
automatisations (`rapido-kb/processus-internes.md`) : nom de la table, quel
workflow écrit, quel workflow lit, quelles colonnes, politique de purge.
Pas de table fourre-tout « data ».

## Workflow

1. **Vérifier l'existant** — `search_data_tables` : une table pour cet usage
   existe peut-être déjà (le registre fait foi). Réutiliser plutôt que
   dupliquer.
2. **Créer** — `create_data_table` : nom explicite en snake_case
   (`relances_envoyees`, `stocks_alertes_envoyees`), colonnes minimales
   (identifiant métier, état, date) — `add_data_table_column` pour étendre
   plus tard, `rename_data_table`/`rename_data_table_column` pour corriger.
3. **Brancher dans le workflow** — le nœud data table (découvert via
   `search_nodes` + `get_node_types`, comme tout nœud) : LIRE avant d'agir
   (le devis est-il déjà dans la table ?), ÉCRIRE après avoir agi
   (`add_data_table_rows` côté workflow). Le pattern anti-doublon :
   lecture → filtre (If) → action → écriture.
4. **Peupler/corriger à la main si besoin** — `add_data_table_rows` via MCP
   (ex. initialiser avec les relances déjà faites manuellement pour éviter
   les doublons au premier run).
5. **Documenter** — inscrire la table au registre (usage, workflows liés,
   purge : ex. lignes de plus de 6 mois supprimables).

## Garde-fous

- Pas de PII au-delà du nécessaire dans les tables (des IDs métier, pas des
  emails en clair si l'ID suffit).
- Suppression de colonnes (`delete_data_table_column`) : confirmation — des
  workflows en dépendent peut-être (vérifier via le registre).
- Une table jamais lue par personne = à archiver (la signaler lors des
  passages de `surveillance-automatisations`).
