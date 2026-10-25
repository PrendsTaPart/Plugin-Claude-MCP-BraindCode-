---
name: customer-success
description: Utiliser quand la relation client installée se travaille, que l'utilisateur dit « fais le point santé de nos clients », « le client n'utilise plus la caisse, que fait-on », « prépare la tournée customer success ». Applique la méthode customer-success de l'Academy — relation, paiement, matériel, support — pour garder les clients signés vivants.
---

# Customer success (garder les clients vivants)

Famille engagée : **service-client** (Brouillon) — toute action sortante en
brouillon, escalades au responsable.

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow

1. **La méthode** : missions des formations `customer-success` (8 missions :
   relation, paiement, matériel, support) et `relation-client` (newsletter,
   parrainage, avis, sondages) — `get_mission` sur le volet concerné.
2. **Le point santé** : pour chaque client suivi — usage (le client
   fait-il ses gestes : brief du jour, relevés), paiement (statut
   d'abonnement via la source KPI désignée), support (demandes ouvertes),
   avis récents. Un signal faible (usage qui tombe) se traite AVANT la
   résiliation. Pour un pilotage santé/NPS outillé complet, DÉLÉGUER au
   plugin `rapido-relation-client`.
3. **Les gestes** : réponse d'usage → skill
   `repondre-a-une-question-d-usage` ; avis → skill `repondre-aux-avis` ;
   re-formation → `foodeatup-tutoriel` ; matériel ou facturation → ESCALADE
   au responsable (famille engager côté argent).
4. **La tournée** : brouillons de prise de nouvelles pour les comptes sans
   contact depuis 30 jours — personnels, courts, sans vente forcée.
5. **Mesurer** : `record_kpi` (rétention, avis, délais) avec la source.

KPI : `avis-note`, `premiere-reponse`, `mrr` (la rétention le porte).
Formations : `customer-success` (8), `relation-client` (6),
`support-client` (8).

## Garde-fous

- Un remboursement, un geste commercial, une résiliation : ENGAGER —
  décision humaine, toujours, préparée en aperçu.
- La tournée n'est pas une campagne : pas de masse, pas de modèle froid —
  et toujours en brouillon.
