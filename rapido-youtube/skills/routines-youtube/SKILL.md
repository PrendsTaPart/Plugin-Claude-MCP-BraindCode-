---
name: routines-youtube
description: Utiliser quand l'utilisateur veut automatiser sa vie YouTube dans Plan'It — « propose la routine de veille hebdo », « automatise le momentum quotidien », « la routine commentaires chaque matin ». Cinq routines types avec leur KPI, proposées via le plugin planit, jamais acceptées sans accord.
---

# Routines YouTube (via Plan'It)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/quota-et-credits.md` (chaque routine
  qui publie consomme du quota à CHAQUE exécution).

## Démarche
1. **Choisir la routine** parmi les cinq types, chacune avec son KPI :
   - veille hebdomadaire des outliers → KPI vues des vidéos inspirées ;
   - momentum quotidien des vidéos de moins de 72 h → KPI vues/heure ;
   - commentaires sans réponse chaque jour → KPI délai de réponse ;
   - audit mensuel du catalogue → KPI taux de clic (miniatures/titres) ;
   - rapport du vendredi → KPI abonnés gagnés, part de miniatures
     testées (A/B).
2. **Proposer via le plugin planit** quand il est installé (c'est lui qui
   parle à l'orchestrateur) : sélection d'outils, `estimate_routine_cost`
   (coût ANNONCÉ), `propose_routine` — JAMAIS d'acceptation sans accord
   sur ce coût. Sans planit : la fiche de routine est livrée prête à
   proposer.
3. **Garde-fous de la routine** : lecture du quota en première étape,
   aucun envoi automatique en public, point d'arrêt humain sur toute
   écriture visible — repris du présent plugin.

## Pièges
- Une routine « momentum » avec refresh systématique consomme du quota
  chaque jour : le refresh reste sur accord ou s'espace.
- Le verdict hebdomadaire (garder/corriger/arrêter) appartient à
  l'humain.

## Dégradation propre
Plan'It absent : fiches de routines livrées (objectif chiffré,
déclencheur, outils, garde-fous, KPI) — rien de simulé.
