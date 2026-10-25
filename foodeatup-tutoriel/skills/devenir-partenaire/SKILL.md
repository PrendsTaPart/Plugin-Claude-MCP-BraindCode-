---
name: devenir-partenaire
description: Utiliser quand quelqu'un veut travailler AVEC FoodEatUp plutôt que s'en servir, dit « devenir formateur FoodEatUp », « revendre le logiciel », « installer des caisses », « apporteur d'affaires », « c'est quoi le programme partenaire », « quelle commission ». Présente les quatre voies du réseau, leurs conditions annoncées et le chemin de candidature — sans jamais annoncer un montant hors réponse.
---

# Devenir partenaire (les quatre voies du réseau)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.

## Workflow

1. **Vue d'ensemble ou profil précis** : `reseau_partenaires_foodeatup` —
   sans paramètre, les quatre voies résumées ; avec `profil` (`formateur`,
   `revendeur`, `installateur`, `apporteur-affaires`), la promesse, les
   conditions annoncées, le profil recherché, les étapes de candidature, la
   FAQ et l'adresse de la page de candidature.
2. **Aider à choisir** : croiser le profil de la personne (métier actuel,
   réseau, compétences) avec les `profils recherchés` renvoyés — proposer
   UNE voie principale argumentée, les autres en alternative.
3. **Se former au rôle** : chaque profil a son parcours de formation (champ
   renvoyé par l'outil + modules `partenaire-*` du catalogue, skill
   `explorer-un-module`). État des vidéos : `audit_formation` — plusieurs
   modules partenaires n'ont pas encore de vidéo en ligne, le dire.
4. **Préparer les vidéos du rôle** (un partenaire qui produit du contenu) :
   `brief_video_partenaire` (`profil` ou `titre`) — respecter le ton imposé.
5. **Candidater** : renvoyer vers l'adresse de candidature RENVOYÉE par
   l'outil ; la candidature se fait là-bas, pas dans la conversation.

## Garde-fous

- **Jamais un montant (commission, rémunération, remise) absent de la
  réponse du serveur** — si la réponse ne chiffre pas, dire « les conditions
  se précisent à la candidature » et pointer la page.
- Aucun concurrent nommé, aucune promesse de résultat chiffré (« vous
  gagnerez X €/mois ») — règle des briefs, étendue à toute la conversation
  partenaire.
- Les conditions annoncées se citent avec leur source (la réponse du jour) ;
  elles peuvent changer — ne pas s'engager à leur place.
