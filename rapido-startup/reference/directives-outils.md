# Directives d'utilisation des outils (rapido-startup)

Règles communes à tous les skills et agents du plugin — à charger en Étape 0.

## Sources et priorités

1. **Données opérationnelles** (revenus, abonnements, factures, clients) :
   les MCP LIVE d'abord — Stripe pour l'encaissement, RapidoCRM pour le
   pipeline et la facturation, FoodEatUp pour le restaurant. Jamais de
   mémoire, jamais d'estimation inventée : une donnée indisponible se dit.
2. **Contexte entreprise** (offre, prix affichés, personas, ton, seuils
   maison) : `./rapido-kb/` PRIME — notamment
   `./rapido-kb/processus-internes.md` pour les seuils financiers.
3. **Benchmarks** : `${CLAUDE_PLUGIN_ROOT}/reference/seuils-defaut.md`
   UNIQUEMENT si la valeur est absente de la KB, en le signalant
   (« défaut secteur, personnalisable dans ./rapido-kb/ »).

## Stripe — règles absolues

- **LECTURE SEULE dans les routines** (revues, analyses, tableaux de bord) :
  `stripe_api_read` / `stripe_api_search` / `fetch_stripe_resources`
  uniquement. JAMAIS d'écriture (`stripe_api_write`) déclenchée par une
  routine — une écriture Stripe (remboursement, création de facture, coupon)
  n'arrive que sur demande explicite de l'utilisateur, avec confirmation
  (hook `garde-stripe-write` + approbation native Stripe).
- **Les montants Stripe sont en CENTIMES** (plus petite unité de la devise) :
  diviser par 100 avant tout affichage ou calcul pour les devises à
  décimales. Tout calcul passe par un script embarqué — jamais de tête.
- L'authentification est individuelle (OAuth mcp.stripe.com) : chaque
  utilisateur connecte SON compte.

## Règles transverses (héritées de la marketplace)

- Confirmation PAR SYSTÈME avant toute écriture multi-serveurs ; en cas
  d'échec en chaîne : arrêt propre + liste de ce qui a été créé.
- Anti-donnée-inventée : chaque chiffre vient d'un outil, de la KB ou de
  l'utilisateur ; un trou se marque `### À COMPLÉTER`.
- MÊME période sur tous les serveurs dans une comparaison.
- Récapitulatif par serveur (IDs créés/modifiés) en fin de tour.
- Consulter `${CLAUDE_PLUGIN_ROOT}/reference/pieges-outils.md` avant tout
  appel à un outil inhabituel.
