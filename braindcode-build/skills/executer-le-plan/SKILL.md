---
name: executer-le-plan
description: Utiliser quand l'utilisateur déroule le chantier Build — « exécute le plan », « prochaine étape du projet », « reprends à l'étape 4 ». Le cœur du plugin - une carte à la fois, validations humaines bloquantes, diffs relus, progression enregistrée.
---

# Exécuter le plan (le cœur du chantier)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/methode-build.md` et
  `${CLAUDE_PLUGIN_ROOT}/reference/regles-lovable.md`.

## Démarche — pour CHAQUE étape du plan
1. **Le plan** : `get_prompt_execution_plan` (reprise avec from_step) —
   étapes, prompts, livrables, conditions de passage, validations
   humaines exigées. Préalable : `register_ai_developer` déjà passé
   (skill `demarrer-le-projet`).
2. **Ouvrir la carte** : `start_prompt_step` — elle passe « en cours »
   (et autorise les send_message au regard du hook garde-credits-lovable).
3. **Validation exigée ?** `request_human_validation` (kind oauth,
   api_key, paiement ou mise_en_ligne — JAMAIS de secret dedans), puis
   attente sur `get_pending_validations` : on ne continue JAMAIS sans la
   validation lue comme accordée.
4. **Construire** : `send_message` à Lovable avec le prompt de l'étape
   (plan_mode: true pour les étapes d'architecture), suivi par
   `get_message` ; toute pause awaiting_input passe par l'humain
   (`respond_to_approval`).
5. **Relire** : `get_diff` EN ENTIER — l'audit des credentials dans le
   code client est automatique (hook audit-credentials-front) ; tout
   écart au cahier se corrige avant de clore.
6. **Constater** : `get_project` pour le preview_url réel.
7. **Clore la carte** : `complete_prompt_step` avec le résultat et le
   lien — `needs_review: true` sur les étapes sensibles (paiement,
   sécurité, données).
8. **Enregistrer** : `save_project_progress` après chaque étape.

## En cas de blocage
Erreur persistante, quota, serveur indisponible : `report_blocker` (sans
secret — hook anti-secret), et passage possible à une étape indépendante.
Un blocage signalé n'est pas un échec caché.

## Pièges
- Un send_message pendant une pause ANNULE la pause : toujours
  respond_to_approval.
- Clore une carte sans lien de preview ni diff relu = chantier invérifiable.

## Dégradation propre
Plan vide ou projet non enregistré : renvoyer vers `demarrer-le-projet` ;
jamais de plan improvisé hors Build.
