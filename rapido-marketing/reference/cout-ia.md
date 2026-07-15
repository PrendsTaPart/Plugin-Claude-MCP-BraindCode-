# Coût IA — règle d'exécution (pilotage marketing)

Principe : dépenser l'intelligence là où elle compte, pas ailleurs. Cette règle
gouverne le **PLAN** de `pilotage-marketing` (estimation du coût d'une action).

## Les trois modes
- **Calculs → script (stdlib)** : tout chiffre — ICE, KPI, taux, scores, agrégats
  — est produit par un script à formule affichée, **jamais** par le modèle.
  Déterministe, sans coût de tokens, vérifiable.
- **Jugement → modèle** : arbitrages, priorisation finale, lecture de contexte,
  rédaction. Le modèle **décide**, il ne **calcule** pas.
- **Volume → batch / n8n** : les tâches répétitives et de masse (relances,
  surveillance, rapports périodiques) passent par des **routines n8n**
  (`rapido-n8n:usine-automatisations`), pas par des appels modèle un par un.

## Conséquence pour PLAN
Estimer le coût d'une action = **compter les appels modèle** qu'elle implique :
- action de **calcul** → coût quasi nul (script) ;
- action de **jugement ponctuel** → un appel modèle ;
- action de **volume** traitée à la main → **signal de la déléguer** à une routine
  n8n (voir `reference/routines.md`).

Une action de volume qui reste manuelle est un coût évitable : le PLAN la
requalifie en routine plutôt que de la répéter.
