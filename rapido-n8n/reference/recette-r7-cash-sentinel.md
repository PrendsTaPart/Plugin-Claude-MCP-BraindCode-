# Recette n8n — R7 CASH-SENTINEL autonome (sans Claude)

La sentinelle trésorerie du Loop Engine (routine R7, plugin rapido-startup)
en workflow n8n : **Schedule quotidien 08:00 → Stripe Balance → calcul du
runway (même formule que `calcul_kpi.py`) → alerte webhook si le seuil est
franchi — sinon rien (silence au vert)**.

Créée via le skill `usine-automatisations` (séquence SDK complète, workflow
VALIDÉ avant création). **La publication reste une décision humaine** —
hook garde-production en filet.

## Les 6 nodes

1. `Schedule Trigger` — tous les jours à 08:00.
2. `HTTP Request` « Stripe — Balance » — GET
   `https://api.stripe.com/v1/balance`, auth **Bearer** via la credential
   n8n « Stripe API (clé secrète) » (à créer dans n8n, JAMAIS de clé en
   clair dans le workflow).
3. `Code` « Calcul runway (CONFIG en tête) » — constantes à adapter par
   client : `BURN_NET_MENSUEL_EUR`, `SEUIL_RUNWAY_MOIS` (défaut 6, source
   `./rapido-kb/processus-internes.md`), `WEBHOOK_ALERTE`. Conversion
   centimes → euros, `runway = trésorerie ÷ burn net`, formule dans la
   sortie.
4. `If` « Runway sous le seuil ? ».
5. (vrai) `HTTP Request` « Envoyer l'alerte » — POST JSON sur le webhook
   configuré (n8n webhook entrant, Slack, passerelle email…).
6. (faux) `NoOp` — vert = silence (`silence_si_vert`), l'exécution n8n
   fait office de journal.

## Activation (côté client, 5 minutes)

1. Créer le workflow via `usine-automatisations` (« crée la sentinelle
   trésorerie R7 ») — ou l'importer depuis l'instance de référence.
2. Dans n8n : créer la credential **Bearer** « Stripe API (clé secrète) »
   (clé `sk_live_…` RESTREINTE en lecture Balance uniquement) et
   l'attacher au node « Stripe — Balance ».
3. Adapter la CONFIG du node Code (burn, seuil, webhook).
4. `test_workflow` (exécution manuelle) → vérifier la sortie.
5. **Publier** — confirmation explicite (hook garde-production).

## Limites assumées

- Le burn est une CONSTANTE de config (pas de lecture CRM en HTTP : les
  serveurs Rapido sont des MCP, pas des API REST publiques) — le mettre à
  jour quand R4 constate une dérive, ou brancher plus tard une source burn.
- La sentinelle n8n ALERTE, elle n'agit pas : les relances restent à R4
  (préparées, envoyées après validation) — même gouvernance que
  `reference/autonomie.md` du plugin rapido-startup.
