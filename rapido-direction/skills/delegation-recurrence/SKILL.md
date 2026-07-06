---
name: delegation-recurrence
description: Utiliser dès qu'une demande de direction est récurrente — « tous les lundis… », « à chaque fois que… », ou une tâche refaite à la main pour la énième fois. Transforme la routine en workflow n8n au lieu de la refaire manuellement.
---

# Délégation du récurrent (pont vers n8n)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/regles-direction.md` (matrice
ponctuel/récurrent/sensible).

## La règle transverse

Chaque fois qu'une demande de direction est RÉCURRENTE, la réponse n'est pas
de la faire — c'est de PROPOSER de la transformer en workflow n8n qui la fera
sans Claude. Détecter :
- les formulations explicites : « tous les lundis… », « chaque matin… »,
  « à chaque fois que… » ;
- les répétitions implicites : la même demande revenue 2-3 fois (« encore le
  récap des devis ? on l'automatise ? »).

## Workflow

1. **Nommer la routine** — déclencheur (horaire ou événement), action,
   destinataire de la sortie (brouillon Gmail ? notification ?).
2. **Vérifier le catalogue** — la routine matche peut-être une recette
   existante (`recettes-metier`, plugin rapido-n8n : relance-devis,
   alerte-stock, recap-hebdo, anniversaires…) — partir de la recette.
3. **Une fois la routine faite À LA MAIN une première fois** (pour valider le
   format de sortie avec l'utilisateur), proposer :
   « Je peux fabriquer le workflow n8n qui le fera automatiquement — on le
   met en place ? »
4. **Déléguer la fabrication** — skill `usine-automatisations` (plugin
   rapido-n8n) : cycle complet, publication confirmée, registre KB. Prérequis
   `N8N_MCP_URL` (sinon expliquer via `rapido-n8n/README-installation.md`).
5. **Respecter les niveaux d'autonomie** — les sorties externes du workflow
   (emails clients) restent en BROUILLON tant que
   `processus-internes.md` n'autorise pas l'envoi direct ; les sorties
   internes (notification au dirigeant) sont libres.

## Garde-fous

- Ne pas automatiser une tâche SENSIBLE (litiges, jugements humains — matrice
  de regles-direction.md) : elle reste ponctuelle et escaladée.
- Une routine automatisée reste SURVEILLÉE : rappeler
  `surveillance-automatisations` dans la revue hebdo.
- Ne pas sur-automatiser : si la routine change chaque semaine, elle n'est
  pas mûre pour un workflow — le dire.
