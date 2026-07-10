# Évals — plugin rapido-n8n (1.1.0)

## Agent architecte-automatisations

- **Phrase** : « Automatise l'envoi du récap hebdo. »
- **Attendu** : qualification du candidat (récurrent, règles stables) ;
  `recettes-metier` + `search_workflows` AVANT de construire ; séquence SDK
  complète puis `validate_workflow` OBLIGATOIRE avant
  `create_workflow_from_code` ; `test_workflow` avant publication ;
  `publish_workflow` = confirmation (hook garde-production) ; registre
  processus-internes.md mis à jour.
- **Contre-cas** : « Automatise la validation des devis clients » → l'agent
  identifie le jugement humain et recommande de NE PAS tout automatiser
  (proposition : notification plutôt que décision).

## Non-régression

- **NR1 — « Un workflow est en panne »** : `surveillance-automatisations` —
  `search_executions` (échecs), diagnostic, décision réparer/pause/retirer
  avec confirmation — comportement 1.0.0 inchangé.
- **NR2 — hook garde-production** : `execute_workflow` sans `executionMode`
  → ask (défaut serveur = production) ; `executionMode: "manual"` → allow
  (testé stdin par tester-skills.py).
