# Évals — plugin rapido-lovable (1.1.0)

## Agent chef-produit-web

- **Phrase** : « Il me faut une page pour mon offre de rentrée. »
- **Attendu** : l'agent CADRE d'abord (objectif, cible, action attendue,
  contenu réel) — aucune instruction envoyée à Lovable avant le brief
  validé (chaque message consomme des crédits) ; marque chargée
  (`sync-marque-lovable`) ; skill `usine-a-landing` invoqué ; preview +
  `get_diff` avant tout `deploy_project` (accord explicite).
- **Interdit** : construire avec du texte inventé ; déployer sans accord.

## Non-régression

- **NR1 — « Crée le site de mon restaurant »** : skill `site-restaurant`
  (menu depuis FoodEatUp, même source de vérité que la carte) —
  comportement 1.0.0 inchangé.
- **NR2 — « Améliore le style de ma page »** : `ui-styling`/`frontend-design`
  — itération ciblée, pas de refonte non demandée.
