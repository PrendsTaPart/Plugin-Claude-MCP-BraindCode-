# Les règles Lovable — à respecter dans CHAQUE prompt envoyé

À relire avant tout `create_project`, `send_message` ou
`set_project_knowledge`. Elles s'écrivent aussi dans le knowledge du
projet pour que l'agent Lovable les garde.

## Dans l'application construite

1. **IA intégrée de Lovable (Lovable AI)** : aucune clé Anthropic, aucun
   paramètre `mcp_servers` dans l'application.
2. **E-mails par le système intégré de Lovable** — pas Resend, pas un
   autre fournisseur.
3. **MCP produit côté serveur UNIQUEMENT** : edge function ou connecteur
   Lovable. Aucun appel MCP depuis le front, aucune URL MCP accompagnée
   d'un jeton, aucune variable d'environnement exposée au navigateur qui
   porte une clé (le hook audit-credentials-front le signale).
4. **Charte** : projet FoodEatUp → charte complète lue par
   `get_brand_guidelines` avec `product: foodeatup` (palette hexadécimale,
   typographie, règles du logo, motif) + CTA « Demander un devis » vers
   https://site.foodeatup.com/creer-mon-devis. Autre produit → la charte de
   ce produit ; sans produit → la charte BraindCode.

## Dans le pilotage du chantier

5. **create_project est asynchrone** : suivre avec `render_project_widget`,
   `get_message` et `get_project` — le statut de premier niveau n'est
   jamais terminal, on lit `response.status`.
6. **awaiting_input = pause** : montrer la demande à l'humain, répondre
   UNIQUEMENT avec sa décision par `respond_to_approval` (event_id + le
   message_id de la pause). Un nouveau `send_message` n'est PAS une
   réponse : il annule la pause en cours. Les secrets, clés Stripe et
   check-ins de crédits se règlent dans l'éditeur Lovable, jamais ici.
7. **Connecteurs par tableau de bord** : `add_connector` renvoie un lien
   profond — c'est l'humain qui finit dans le tableau de bord
   (request_human_validation de kind oauth ou api_key).
8. **set_project_knowledge REMPLACE tout** : lire `get_project_knowledge`
   d'abord, fusionner, puis écrire.
9. **Crédits** : create_project, send_message, remix_project consomment —
   on annonce avant, on groupe les demandes, on n'itère pas « pour voir ».
10. **deploy_project met EN LIGNE publiquement** : seulement après la
    validation humaine de kind mise_en_ligne (hook garde-mise-en-ligne).
