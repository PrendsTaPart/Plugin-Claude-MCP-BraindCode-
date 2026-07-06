---
name: coaching-pipeline
description: Utiliser quand l'utilisateur demande une revue de pipeline, « où en sont mes deals » ou quoi relancer. Méthode de revue — deals dormants, devis expirants, étapes engorgées — avec une prochaine action par deal.
---

# Coaching pipeline (revue de deals)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).

## Calculs (script obligatoire)

Utiliser le script pour tout calcul ; ne jamais calculer de tête. Après la
collecte (étapes 1-4 ci-dessous), construire le JSON d'entrée
`{date_reference, seuil_dormant_jours, etapes: [{nom, probabilite, deals:
[{nom, montant, derniere_activite}]}]}` et exécuter :
`python3 "${CLAUDE_PLUGIN_ROOT}/skills/coaching-pipeline/scripts/funnel_metrics.py" <fichier.json>`
Le script renvoie les taux de conversion par étape, le maillon faible, les
deals dormants (> seuil jours) et la valeur brute/pondérée du pipeline —
restituer ces chiffres tels quels (y compris la note méthodo : conversions
sur instantané, pas cohorte).

## Méthode de revue — 4 angles, données réelles uniquement

1. **État du pipeline** — `get_pipeline` (deals par étape) et
   `get_stats_pipeline` / `get_stats_pipeline_global` (taux de conversion par
   étape, `periode` cohérente — défaut `month`).
2. **Deals dormants** — deals sans mouvement depuis plus de X jours. Seuil
   MAISON de `./rapido-kb/processus-internes.md` s'il existe (citer la
   source) ; sinon défaut 14 jours, en le signalant. Vérifier l'historique
   réel de chaque deal suspect avec `get_historique_prospect` — un deal n'est
   « dormant » que si son historique le confirme.
3. **Devis expirant bientôt** — `list_devis` : statut `en_attente` dont la
   `date_fin` (validité) tombe sous 7 jours → relance prioritaire avant
   expiration.
4. **Étapes engorgées** — comparer le volume par étape à la conversion : une
   étape qui accumule (beaucoup d'entrées, peu de sorties) est le maillon faible
   à traiter en premier.

## Sortie — une revue actionnable

```
🔍 REVUE PIPELINE — {période}

📊 FUNNEL : volumes et conversion par étape ; maillon faible identifié
😴 DORMANTS (> X j) : deal | étape | dernier contact | prochaine action
⏳ DEVIS EXPIRANTS (< 7 j) : deal | montant | expire le | prochaine action
🚧 ÉTAPE ENGORGÉE : laquelle, pourquoi, quoi faire

✅ ACTIONS (max 5, priorisées) : une ligne = un deal + une action + une échéance
```

RÈGLE : chaque deal listé repart avec UNE prochaine action concrète et datée
(relancer via `schedule_email`, poser un RDV via `create_rdv`, déplacer d'étape
via `deplacer_prospect_etape`, clôturer via `close_opportunity`) — jamais un
constat sans action. Les dates de relance suivent la cadence MAISON de
`./rapido-kb/processus-internes.md` si elle existe (citer la source), sinon le
défaut J+3 / J+7 / J+15 en le signalant.

## Garde-fous

- La revue est en LECTURE SEULE : les actions proposées ne s'exécutent qu'après
  validation de l'utilisateur, deal par deal (ou liste validée en bloc).
- Clôturer un deal en perdu (`close_opportunity`) : confirmation explicite +
  motif consigné via `log_activity`.
- Pour la rédaction des relances : skill `redaction-commerciale`.
