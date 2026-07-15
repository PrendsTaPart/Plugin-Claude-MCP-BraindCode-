---
name: connecteur-mcp-lovable
description: Utiliser quand l'utilisateur veut brancher un serveur MCP Rapido (FoodEatUp, CRM, CMS, RH) sur un site Lovable via un agent embarqué — « connecte le MCP FoodEatUp au site », « prompts Lovable pour brancher le CRM », « ajoute l'agent IA au site du client », « connecteur MCP sur Lovable ». Génère les prompts Lovable étagés depuis le kit canonique, avec sécurité et scope verrouillés. À NE PAS utiliser pour un MVP multi-pages complet (mvp-lovable) ni un brief one-shot (prompt-lovable).
---

# Connecteur MCP → site Lovable

Produit **toujours les mêmes prompts** pour câbler un MCP Rapido sur un site Lovable :
même méthode, même sécurité, même scope. Fondé sur `reference/kit-connecteur-mcp/`.

## Étape 0 — charger le kit

Lire la **fiche du MCP demandé** (`reference/kit-connecteur-mcp/{foodeatup|crm|cms|rh}.md`),
`reference/kit-connecteur-mcp/_commun.md`, `reference/gate-securite.md`,
`reference/regles-stack-lovable.md`. Contexte projet : si projet existant, `get_project` +
`list_files` (repérer `supabase/functions/`, la stack) ; sinon, prévoir la création.

## 1. Qualification courte

- **Quel(s) MCP** (foodeatup / crm / cms / rh — un ou plusieurs) ?
- **Projet neuf ou existant** ?
- **Périmètre de l'agent** : lecture seule, ou lecture + **écritures confirmées** (selon
  les familles autorisées de la fiche) ?
- **Credentials du CLIENT** disponibles (sa clé Anthropic, son token/établissement) ?
  **Jamais les clés BraindCode** : si on demande d'utiliser une clé maîtresse BraindCode,
  **refus écrit** (chaque site porte les identifiants de SON client).

## 2. Générer les PROMPTS LOVABLE ÉTAGÉS (prêts à coller)

Chaque prompt inclut ses **critères de done** et rappelle les **interdits** (pas de clé en
dur, pas d'appel client-side). Noms d'env **immuables** repris de la fiche.

- **P1 — Secrets & env** : lister les secrets à créer dans l'UI Lovable/Supabase (noms
  standardisés : `ANTHROPIC_API_KEY`, `<MCP>_MCP_URL`, `<MCP>_MCP_TOKEN`, `<MCP>_SCOPE_ID`).
  **Les valeurs sont saisies par l'utilisateur dans l'UI, JAMAIS écrites dans le prompt.**
- **P2 — Edge function `agent-{mcp}`** : le template de `_commun.md` (appel Anthropic +
  `mcp_servers` type url, parsing par type, rate-limits, filtre injection, **scope injecté
  serveur** depuis l'env). Aucune clé dans le code.
- **P3 — Composant chat UI** : la spec du kit (fil, indicateur d'outil, **carte de
  confirmation avant écriture**, journal), charte via `sync-marque-lovable` / `get_brand`.
- **P4 — System prompt + knowledge du projet** : le bloc de la fiche MCP (familles
  d'outils, scope verrouillé, confirmation, langue) → poussé en `set_project_knowledge`
  (contexte client) ; pas de secret dans le knowledge.
- **P5 — Tests d'acceptation** : les 5 critères du kit (secrets hors bundle, appels
  serveur only, écriture bloquée sans confirmation, scope non contournable, injection
  filtrée) — à exécuter et rapporter.

## 3. Exécution assistée (optionnelle, confirmée)

Si l'utilisateur le souhaite : envoyer les prompts **un par un** via `send_message`
(consomme des crédits Lovable — cadrer avant), **vérifier entre chaque étape**
(`get_message`, `read_file` ciblé sur l'edge function / le composant), passer le **gate
sécurité** en fin, puis une **recette** avec un **compte de démo** (jamais la prod).
Jamais deux étapes sans contrôle ; déploiement/publication uniquement sur confirmation.

## 4. Livraison

- **Doc client courte** : ce que l'agent sait faire, ce qu'il demande en confirmation, où
  sont les clés (env Lovable), rappel scope.
- Entrée `rapido-kb/lovable/connecteurs-installes.md` : projet, MCP, **version du kit**,
  date.

## Interdits (non négociables)

- **Jamais de clé BraindCode** chez un client (refus écrit) ; jamais de valeur de secret
  dans un prompt.
- **Jamais d'appel client-side** vers Anthropic ou un MCP ; tout en edge function.
- **Jamais d'écriture sans confirmation UI** ; **jamais** de scope depuis le front.
- Ne rien promettre sur l'**isolation multi-tenant** tant que le token par établissement
  n'est pas livré côté serveur (`docs/OUTILS-MCP-MANQUANTS.md` §11).

## Passerelles

MVP multi-pages complet → `mvp-lovable`. Brief one-shot (landing simple) →
`rapido-prompteur:prompt-lovable`. Marque/kit en workspace → `sync-marque-lovable` (LV4).
