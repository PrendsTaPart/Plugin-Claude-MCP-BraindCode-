---
name: catalogue-de-connecteurs
description: Utiliser quand le catalogue de connecteurs Build se consulte ou s'enrichit — « quels connecteurs existent sur Build ? », « détaille le connecteur RapidoCRM », « propose un connecteur manquant ». Familles lues/écrites et actions sensibles restituées, proposition après aperçu.
---

# Catalogue de connecteurs Build

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/carte-des-interconnexions.md`.

## Démarche
1. **Lire** : `list_connectors` — le catalogue officiel ; `get_connector`
   pour une fiche : familles de données LUES et ÉCRITES, actions
   sensibles, prérequis d'auth.
2. **Choisir** : le connecteur du cahier des charges vient d'ici — pas
   d'un souvenir ; les actions sensibles de la fiche deviennent les
   validations humaines du plan.
3. **Proposer** : un connecteur manquant passe par `propose_connector`
   APRÈS aperçu complet de la proposition (nom, familles, actions
   sensibles, auth) — hook garde-build : ask.

## Pièges
- La fiche connecteur décrit le CONTRAT, pas l'état de ta session : la
  connexion réelle se vérifie par tools/list du serveur concerné.

## Dégradation propre
Connecteur absent du catalogue ET du besoin immédiat : documenter l'écart
dans le cahier des charges plutôt que proposer un connecteur bâclé.
