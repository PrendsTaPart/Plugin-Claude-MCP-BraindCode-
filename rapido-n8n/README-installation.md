# Installation du plugin rapido-n8n

Ce plugin est GÉNÉRALISTE : chaque client connecte SA PROPRE instance n8n
(n8n Cloud ou auto-hébergée). Aucune URL d'instance n'est codée en dur — la
connexion passe par la variable d'environnement `N8N_MCP_URL`.

## 1. Trouver l'URL MCP de votre instance n8n

- **n8n Cloud** : dans votre instance, Settings → MCP (ou la section
  « MCP Server » de la documentation n8n) — l'URL a la forme
  `https://<votre-instance>.app.n8n.cloud/mcp-server/http`.
- **Self-hosted** : activez le serveur MCP de votre instance (voir la
  documentation n8n de votre version), l'URL a la forme
  `https://<votre-domaine-n8n>/mcp-server/http`.
- L'authentification (token/header) se configure selon votre instance —
  suivez la documentation n8n correspondante.

## 2. Définir la variable d'environnement AVANT de lancer Claude Code

```bash
export N8N_MCP_URL=https://<votre-instance>/mcp-server/http
claude
```

ou de façon persistante dans le fichier d'environnement de votre projet
(`.env` chargé par votre shell, `direnv`, profil…). Sans cette variable, le
serveur n8n du plugin ne démarre pas.

## 3. Vérification

Dans une session Claude Code, demandez : « liste mes workflows n8n » —
l'outil `search_workflows` doit répondre.

- ✅ Réponse (même vide) : la connexion fonctionne.
- ❌ Outils n8n absents : les skills du plugin l'expliquent et vous renvoient
  vers ce README au lieu d'échouer — vérifiez dans l'ordre :
  1. `N8N_MCP_URL` est bien exportée dans le shell qui a lancé Claude Code ;
  2. l'URL répond (instance démarrée, MCP activé) ;
  3. l'authentification de l'instance est configurée.

Le hook de session du plugin vérifie la variable au démarrage et affiche un
message guidé si elle manque.

## Rappels

- Les CREDENTIALS des workflows (Gmail, HTTP vers les API Rapido…) se
  configurent dans l'UI de VOTRE instance n8n — jamais via le plugin.
- Rôle du plugin : Claude CONSTRUIT des automatisations qui tournent ensuite
  SANS lui. Tâche ponctuelle → Claude l'exécute via les MCP ; tâche
  récurrente → workflow n8n.
