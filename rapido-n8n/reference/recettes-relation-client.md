# Recettes relation client (n8n)

> Format maison : déclencheur, pseudo-nœuds, table mémoire, garde-fous. Identifiants au
> registre unifié (`RC-*`). Installation **sur confirmation**, recette par recette, via
> `usine-automatisations` — aucun workflow créé d'office. Tout envoi client en **brouillon**.

## RC-HEBDO — point service client (lundi)
- **Déclencheur** : Schedule cron `0 7 * * 1`.
- **Workflow** : Schedule → tickets ouverts par priorité/ancienneté + délais 1re réponse
  vs SLA (KB) + réclamations FoodEatUp → **email interne** (SLA dépassés priorisés
  SLA×valeur) + récurrences consolidées.
- **Table mémoire** : `rc_support_journal` (`date`, `sla_depasses`, `volume`,
  `recurrences`) — série + anti-double-signalement des récurrences.
- **Garde-fous** : alerte **interne** ; réponses **déléguées** (brouillons) ; SLA depuis KB.

## RC-NPS-TRIMESTRE — vague NPS (trimestriel)
- **Déclencheur** : Schedule trimestriel.
- **Workflow** : Schedule → lancer la vague NPS (via animation-client) → collecter →
  segmenter promoteurs/passifs/détracteurs → **actions par segment en brouillon** (sauvetage,
  geste, ambassadeur + avis).
- **Table mémoire** : `rc_nps_vagues` (`vague`, `nps`, `promoteurs`, `passifs`,
  `detracteurs`) — série trimestrielle.
- **Garde-fous** : envois **confirmés** ; NPS par formule ; segments réels.

## RC-SANTE-MENSUEL — santé du portefeuille (mensuel)
- **Déclencheur** : Schedule mensuel.
- **Workflow** : Schedule → collecter récence/paiement/tickets/NPS par client → **score
  de santé** (script health_score) → **email interne** : portefeuille vert/orange/rouge +
  clients rouges avec prochaine action.
- **Table mémoire** : `rc_sante_journal` (`mois`, `client_id`, `score`, `couleur`) —
  suivi de tendance ; ne pas re-signaler un rouge déjà ouvert non résolu.
- **Garde-fous** : score **par script** (formule) ; données réelles ; alerte **interne**.

## Installation
Proposer chaque recette avec sa cadence et sa table mémoire ; **installer seulement les
confirmées**. Un workflow sans table mémoire n'est pas installé.
