---
name: ideation-cash-flow
description: "Utiliser quand l'utilisateur veut créer un plan de trésorerie mensuel sur 12 mois (parcours idéation StartupsForge)."
tags: [finance]
niveau: intermediaire
---

# Cash Flow

**Catégorie** : Idéation  
**Durée** : 45-60 min

## Pourquoi

Le cash flow est la première cause de faillite des startups. Même rentable, une startup peut mourir si elle manque de trésorerie.

## Objectif

Créer un plan de trésorerie mensuel sur 12 mois.

## Livrable attendu

Tableau cash flow avec alertes

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Lister les encaissements** — Quand l'argent rentre réellement
2. **Lister les décaissements** — Quand tu paies vraiment
3. **Calculer le solde mensuel** — Encaissements - Décaissements
4. **Identifier les creux** — Mois où tu risques d'être négatif
5. **Prévoir les solutions** — Ligne de crédit, factoring, etc.

## Pro tips

- Ajoute une marge de sécurité de 20%
- Négocie des délais de paiement fournisseurs
- Facture rapidement, relance automatiquement

## Erreurs fréquentes

- Confondre facturation et encaissement
- Pas de buffer de sécurité
- Ignorer la saisonnalité

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **Stripe** (`stripe`, lecture seule) — montants en CENTIMES, convertir avant tout calcul ; calculs par script (skill `catalogue-kpi`), jamais de tête

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/ideation/ideation-cash-flow.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-suite:cash-flow-snapshot` — projection sur encaissements réels
