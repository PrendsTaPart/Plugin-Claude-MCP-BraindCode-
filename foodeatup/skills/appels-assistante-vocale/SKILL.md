---
name: appels-assistante-vocale
description: Utiliser quand l'utilisateur parle des appels téléphoniques reçus par Caroline (l'assistante vocale du restaurant), d'appels manqués, de rappels clients à faire, de réclamations au téléphone ou de suivi des appels. Liste et lit les appels, prépare le pitch de rappel, consigne les notes de suivi et marque les appels traités.
---

# Appels de l'assistante vocale (Caroline)

Caroline décroche pour le restaurant ; l'équipe rappelle. Ce skill organise le
**suivi** : rien n'est envoyé au client, aucun appel n'est passé.

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
   règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).
2. S'assurer d'avoir l'`establishment_id` (le demander si absent) avant tout appel.
3. Règle « Résolution des noms » (directives § 1 ter) : tout nom parlé ou
   écrit (produit, ingrédient, plat, équipement, table, recette) se résout
   via `search_entities` AVANT tout autre appel — si `ambiguous=true`,
   présenter les candidats et DEMANDER confirmation. Jamais d'ID deviné.

## Workflow

1. **À traiter** — `list_calls` (`suivi: "a_traiter"`, `date` ou
   `date_from`/`date_to` ; défaut aujourd'hui ; filtres `intent` ∈ commande |
   question | reservation | reclamation | autre, `status` ∈ reussi | transfere |
   echoue | manque | en_cours). Présenter : heure, client reconnu, intention,
   résumé, commande née ou non. Réclamations et appels manqués EN TÊTE.
2. **Détail** — `get_call` (`call_id`) : transcription complète, notes de
   l'équipe. `with_transcript: true` sur `list_calls` seulement si demandé
   (réponses longues).
3. **Préparer le rappel** — `generate_callback_pitch` (`call_id`, ou `date`
   pour tous les appels non traités du jour, les plus urgents d'abord) :
   accroche, contexte, proposition, question de clôture, script prêt à lire.
   **Proposition seulement** : l'équipe rappelle elle-même.
4. **Consigner** — `add_call_note` (`call_id`, `body` ≤ 2000 caractères) avec
   ce que l'utilisateur rapporte du rappel (« rappelé 15 h, table confirmée »).
5. **Clore** — `mark_call_handled` (`call_id`) quand le rappel est FAIT ;
   `handled: false` pour rouvrir.

## Passerelles

- Réclamation → `handle-complaint` (contexte client, réponse, geste) ;
  réservation à confirmer → `service-salle` ; commande → `gestion-commandes`.
- Le paramétrage de Caroline (voix, consignes) n'est pas dans ce MCP.

## Garde-fous

- Ne jamais marquer traité un appel que l'utilisateur n'a pas confirmé avoir
  rappelé ; une note décrit un fait rapporté, jamais une supposition.
- Les numéros de téléphone ne sont recopiés que si l'utilisateur en a besoin
  pour rappeler.
- Récapituler : appels lus, notes ajoutées (IDs), appels marqués traités.
