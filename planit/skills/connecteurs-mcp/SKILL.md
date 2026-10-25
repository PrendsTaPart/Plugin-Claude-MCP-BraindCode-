---
name: connecteurs-mcp
description: Utiliser quand les connecteurs Plan'It se gèrent, que l'utilisateur dit « quels connecteurs sont branchés », « pourquoi FoodEatUp est en erreur », « ajoute ce serveur MCP à Plan'It », « teste le connecteur CRM ». Lit l'état réel, distingue connecteur cassé et erreur d'usage, enregistre une URL — l'authentification reste dans l'app.
---

# Connecteurs MCP (l'état réel, jamais promis)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.

## Workflow

1. **`list_mcp_servers`** — pour chaque connecteur : clé, libellé, natif ou
   ajouté, état RÉEL (connecté, erreur, jamais branché), nombre d'outils,
   dernier succès, message d'erreur. C'est l'état du jour qui fait foi, pas
   un souvenir (relevé du 2026-10-25 : FoodEatUp « token expired »,
   RapidoCRM déconnecté — à re-relever à chaque séance).
2. **`get_mcp_server_tools`** — ce qu'un connecteur sait faire : outils,
   schémas, drapeau destructif.
3. **Une action a échoué** : **`test_mcp_server`** — le connecteur répond-il
   avec les identifiants de l'utilisateur ? Cassé (erreur, jeton expiré) →
   renvoyer vers l'écran Connecteurs de l'app pour ré-authentifier ; il
   répond → l'erreur est un usage (mauvais paramètre, outil absent), à
   corriger côté appel.
4. **Ajouter** : **`add_mcp_server`** avec l'URL — RAPPELER qu'il
   n'authentifie RIEN : l'OAuth ou la clé se fait ensuite dans l'écran
   Connecteurs de l'application. URL déjà connue = le connecteur existant
   est renvoyé, pas de doublon.
5. **Retirer** : **`remove_mcp_server`** — sur confirmation, et SEULEMENT
   pour un connecteur ajouté par l'utilisateur : le catalogue public et le
   connecteur natif Plan'It ne sont jamais supprimables (le serveur
   refuserait ; ne pas essayer).

## Garde-fous

- Jamais « c'est branché » sans l'avoir lu dans list_mcp_servers du jour.
- Une URL de connecteur ne s'invente pas ; un jeton ne se colle jamais dans
  la conversation (il vit dans l'app).
