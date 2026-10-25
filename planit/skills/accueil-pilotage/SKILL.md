---
name: accueil-pilotage
description: Utiliser quand on ouvre Plan'It, que l'utilisateur dit « où en est mon Plan'It », « fais-moi l'accueil de pilotage », « qu'est-ce qui attend une décision ». Lit l'accueil en un appel (crédits, autonomie, widgets, boucles, alertes), les décisions en attente et les promotions, et produit un écran + trois décisions à prendre — sans jamais en trancher une.
---

# Accueil de pilotage (l'écran du matin)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.

## Workflow

1. **`get_kpi_home`** — solde de crédits, jours d'autonomie, widgets posés
   (dernières valeurs), boucles en cours, alertes en attente. Aucun appel
   facturé : c'est l'instantané.
2. **`list_pending_routine_actions`** — propositions de routines et
   d'améliorations en attente, routines en pause (échecs, crédits), alertes
   liées. RIEN de tout cela ne se repropose ni ne se tranche ici.
3. **`list_routines` avec `has_pending: true`** — les routines qui attendent
   une décision, avec leur santé et leur coût mensuel.
4. **`list_promotions` (surface `home`)** — n'annoncer QUE ce que la liste
   renvoie, jamais un bonus déjà consommé.
5. **Produire l'écran** : widget `accueil-pilotage`
   (`${CLAUDE_PLUGIN_ROOT}/scripts/render_widget.py`) ou le même contenu en
   texte — puis **les trois décisions à prendre**, classées par impact
   (crédits bas, routine en échec, proposition qui attend…), chacune avec le
   skill qui la traite (`alertes-kpi`, `auditer-mes-routines`,
   `lancer-pause-reprise`).

## Garde-fous

- Ce skill LIT et PRÉSENTE : il ne tranche aucune des trois décisions —
  chaque décision part dans son skill, avec l'accord explicite de
  l'utilisateur.
- Une valeur de widget datée se donne avec sa date ; `throttled` = « pas
  fraîche » avec son âge.
- Serveur absent : le dire et s'arrêter (tout ce plugin dépend de Plan'It).
