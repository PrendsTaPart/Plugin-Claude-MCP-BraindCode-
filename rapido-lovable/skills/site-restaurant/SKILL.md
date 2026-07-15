---
name: site-restaurant
description: Utiliser quand l'utilisateur veut un site pour son restaurant, un site de réservation ou son menu en ligne. Construit une app Lovable avec les données réelles FoodEatUp, un formulaire de réservation connecté (mode B) et la charte de la marque.
---

# Site restaurant (FoodEatUp × Lovable)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/architecture-lovable.md`. Obtenir
l'`establishment_id` (FoodEatUp). KB : `charte-graphique.md`,
`ton-et-accroches.md`, `entreprise.md`.

## Workflow

1. **Collecter le contenu RÉEL** — `list_dishes` + `list_categories`
   (FoodEatUp) : plats, prix, catégories ; horaires et coordonnées
   (`entreprise.md` de la KB ou l'utilisateur) ; palette hex et logo (KB
   prioritaire, sinon demander). Rien d'inventé : chaque plat affiché existe.
2. **Vérifier les crédits** — `get_workspace` (choisir le workspace si
   plusieurs).
3. **Créer le projet** — `create_project` avec un `initial_message` TRÈS
   détaillé : pages (accueil, menu par catégories avec les plats/prix réels,
   réservation, contact avec horaires/adresse/téléphone), palette hex exacte,
   typo, ton (KB), mobile-first, accessibilité. Montrer le `preview_url` à
   l'utilisateur.
4. **Itérer** — `send_message` (une itération = un objectif clair ; images de
   référence en pièce jointe si utiles). Suivre avec `get_project`.
5. **Formulaire de réservation en MODE B** — faire construire par Lovable :
   - une edge function serveur qui appelle l'API Anthropic `/v1/messages` avec
     `mcp_servers` = le MCP FoodEatUp (URL publique
     `https://foodeatup.com/api/mcp`) ;
   - le flux imposé : `reservation_availability` d'abord (anti-double-booking)
     PUIS `create_reservation` — jamais de création sans vérification ;
   - parsing des blocs par TYPE (`mcp_tool_result`/`text`), clé API en secret
     serveur (voir architecture-lovable.md, règles non négociables) ;
   - messages d'erreur propres pour le client final (créneau plein →
     alternatives).
6. **Tester** — dérouler un scénario de réservation de bout en bout sur la
   preview (créneau libre, créneau plein) avant tout déploiement.
7. **Déployer** — `deploy_project` : CONFIRMATION NIVEAU 2 (l'URL devient
   publique — récapituler pages et données visibles). Transmettre l'URL.
8. **Relier au QR de la carte digitale** — côté rapidocms : pointer le lien de
   la carte digitale vers le site (`add_card_page_link` / `edit_card_page`,
   URL publiée) pour que le QR existant mène au site.

## Garde-fous

- Menu du site = source de vérité FoodEatUp ; si un prix change, proposer la
  mise à jour du site (send_message) ET de la carte vitrine/menu imprimé
  (cohérence multi-supports).
- Réservation : le site ne contourne JAMAIS la machine à états des tables —
  il ne fait que disponibilité + création ; le reste vit dans FoodEatUp.
- Pas de données personnelles clients dans le code ou le contenu du site.

## Ajouter l'agent réservation/assistant (option)

Pour un agent qui répond et agit via le MCP FoodEatUp (disponibilités, réservation
confirmée), **déléguer à `connecteur-mcp-lovable`** (kit `reference/kit-connecteur-mcp/foodeatup.md`,
gate `reference/gate-securite.md`) — scope établissement injecté serveur, écritures
confirmées. Ne pas réimplémenter le branchement ici.
