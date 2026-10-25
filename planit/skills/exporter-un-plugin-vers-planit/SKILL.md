---
name: exporter-un-plugin-vers-planit
description: Utiliser quand l'utilisateur demande EXPLICITEMENT un export, dit « exporte le plugin rapidocrm vers Plan'It », « transpose foodeatup-boucles dans mon catalogue privé », « mets ce plugin de la marketplace dans Plan'It ». Lit le plugin du dépôt et le transpose en plugin privé + consignes — écarts d'outils signalés, jamais inventés.
disable-model-invocation: true
---

# Exporter un plugin vers Plan'It (la marketplace → le catalogue privé)

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.
2. Demande explicite seulement (frontmatter `disable-model-invocation`).
3. Lire le plugin source dans CE dépôt : `.claude-plugin/plugin.json`,
   `.mcp.json`, chaque `skills/*/SKILL.md`.

## Workflow

1. **Correspondance des connecteurs** : chaque serveur du `.mcp.json` du
   plugin source se traduit en CLÉ Plan'It via `list_mcp_servers` (ex.
   rapidocrm → `rapidocrm`, foodeatup → `foodeatup`, gmail → `cmp_gmail`).
   Un serveur sans équivalent Plan'It se SIGNALE — jamais une clé inventée.
   L'état de connexion se dit (un connecteur en erreur fonctionnera quand
   il sera ré-authentifié dans l'app).
2. **`create_private_plugin`** — slug = nom du plugin source, nom,
   description, et les clés de connecteurs correspondantes
   (required_mcp_keys). Idempotent : relancer met à jour.
3. **Chaque SKILL.md → `create_private_skill`** : slug du skill, le corps
   (quand l'utiliser, outils dans l'ordre, confirmations, pièges — repris du
   SKILL.md, condensé), et `required_tools` VÉRIFIÉS un par un sur
   **`get_mcp_server_tools`** du connecteur : un outil cité par le skill qui
   n'existe pas côté Plan'It est RETIRÉ de required_tools et listé dans le
   rapport d'écart — jamais inventé, jamais « probablement là ».
4. **Le rapport d'export** : plugins/consignes créés ou mis à jour, écarts
   d'outils par skill, connecteurs à authentifier. L'utilisateur vérifie
   dans l'app (`list_my_private_catalog` pour contrôle).

## Garde-fous

- Les hooks et scripts du plugin source NE S'EXPORTENT PAS (Plan'It n'exécute
  pas de hooks de ce dépôt) : le dire — les garde-fous deviennent des
  consignes écrites dans la skill privée.
- Jamais de secret dans un corps de consigne ; la KB client reste chez le
  client.
- Export = geste volumineux : annoncer le plan (N skills) avant d'écrire.
