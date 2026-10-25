---
name: repondre-a-une-question-d-usage
description: Utiliser quand un client demande comment faire dans FoodEatUp, que l'utilisateur dit « il demande comment relever une température », « réponds-lui avec le bon tutoriel », « montre-lui l'écran des plannings ». Trouve le tutoriel vidéo, prépare la réponse en brouillon Gmail avec le lien, et montre l'écran du logiciel.
---

# Répondre à une question d'usage (le tutoriel fait la réponse)

Famille engagée : **service-client** (Brouillon — la réponse part en
brouillon, l'humain envoie).

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow

1. **`rechercher_tutoriels`** (serveur tutoriel, paramètre `question`) — la
   fiche qui répond ; **`tutoriels_du_module`** pour partir de l'écran du
   logiciel quand le client nomme un écran plutôt qu'un sujet.
2. **Sujet non couvert** : `audit_formation` — le dire au client tel quel
   (« pas encore en vidéo, voici la marche écrite si la fiche l'a, sinon
   j'escalade ») — jamais une marche à suivre inventée.
3. **La réponse** : brouillon Gmail (`reply` sur le fil… NON — `create_draft`
   en réponse, l'envoi direct est bloqué) avec : la phrase de réponse, LE
   LIEN de la fiche (`obtenir_lien_tutoriel`), la durée de la vidéo, et
   l'astuce du chef si la fiche en porte une.
4. **Montrer l'écran** : `foodeatup_lien_ecran` (Academy) — le lien profond
   vers l'écran du logiciel dont on parle, joint à la réponse.
5. **Noter** : la demande et sa réponse au journal ; une question récurrente
   se signale (skill `construire-l-outil-manquant` si c'est un trou d'outil,
   routine « demandes entrantes » sinon).

KPI : `premiere-reponse`, `resolution-premier-contact`.
Formations : `support-client` (8 missions), `logiciel`.

## Garde-fous

- La réponse technique vient du tutoriel ou de la doc servie — jamais de
  mémoire (un lien se copie d'une réponse d'outil, hook anti-lien côté
  valeurs d'exemple).
- Quota `reponsesJour` compté ; brouillon toujours, envoi humain.
- Un incident (bug, panne, client fâché) s'ESCALADE au responsable au lieu
  de se « rattraper » par écrit.
