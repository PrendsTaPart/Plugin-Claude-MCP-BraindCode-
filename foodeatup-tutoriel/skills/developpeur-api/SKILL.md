---
name: developpeur-api
description: Utiliser quand la question est technique, que l'utilisateur dit « comment marche l'API FoodEatUp », « créer une clé API », « brancher n8n ou Make », « c'est quoi le JSON-RPC du MCP », « montre-moi un appel cURL ». Explique l'authentification, le point d'entrée JSON-RPC, les jetons, les erreurs et les limites — depuis la documentation servie, jamais un endpoint inventé.
---

# Développeur API (la porte technique, documentée)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.

## Workflow

1. **`documentation_api_foodeatup`** — cibler la `section` utile plutôt que
   tout : `authentification` (clé client_id/client_secret, jeton Bearer
   24 h), `jsonrpc` (POST unique, tools/list et tools/call, exemples cURL),
   `jetons` (clé d'établissement, jeton employé, OAuth), `erreurs`,
   `limites`, `cas_usage`, `exemple_predibot` (agent WhatsApp n8n), `faq`.
2. **Restituer sans invention** : endpoints, codes d'erreur, limites d'appel
   et exemples se citent TELS QUE RENVOYÉS. La doc officielle en ligne est
   celle que la réponse référence — pointer ses pages plutôt que
   paraphraser de mémoire.
3. **Cas n8n/Make/Zapier** : section `exemple_predibot` — bien relayer son
   avertissement : les adresses de connecteur de l'exemple sont FICTIVES,
   chaque utilisateur expose sa propre console ; et le point de vigilance :
   un connecteur MCP sans jeton est ouvert à quiconque a l'adresse (en-tête
   Authorization avant tout déploiement).
4. **Leçons vidéo associées** : module `api-developpeurs` du catalogue —
   vérifier `videosEnLigne` avant de promettre quoi que ce soit (relevé du
   2026-10-25 : 0 vidéo en ligne, 4 prévues).
5. L'utilisateur veut brancher Claude à SON restaurant (pas coder) → skill
   `passer-a-l-action`.

## Garde-fous

- **Jamais d'endpoint, de paramètre ou de code d'erreur inventé** : la
  réponse de `documentation_api_foodeatup` est la source unique.
- `client_secret` et jetons sont des secrets : jamais collés dans la
  conversation, jamais stockés en dur (règle de la doc elle-même : le jeton
  expire en 24 h, on le redemande).
- Les comptages d'outils de l'API se citent avec leur source et leur date
  (piège vérifié : deux outils du serveur peuvent annoncer deux totaux
  relevés à des dates différentes).
