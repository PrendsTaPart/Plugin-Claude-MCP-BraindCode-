---
name: decouvrir-l-offre
description: Utiliser quand la question porte sur l'offre commerciale, que l'utilisateur dit « combien ça coûte », « il y a un essai gratuit ? », « c'est quoi les packs », « qu'est-ce que FoodEatUp sait faire pour une boulangerie ». Rend les tarifs publics, l'essai et les capacités — uniquement les montants renvoyés par le serveur, toujours avec la date de vérification.
---

# Découvrir l'offre (tarifs vérifiés, capacités sourcées)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.

## Workflow

1. **Prix, essai, packs** : `tarifs_et_essai` — restituer les packs, l'offre
   Premiers pas, l'essai et la mention TVA TELS QUE RENVOYÉS, et TOUJOURS
   citer la date `verifieLe` (« tarifs vérifiés le … »). Le champ
   `prudence` fait loi : options, crédits et prestations absents de la
   réponse → renvoyer vers `pageTarifs`, jamais improviser un montant.
2. **Capacités** : `capacites_foodeatup` (filtre `domaine` possible) — les
   domaines du produit, leurs compteurs et exemples de demandes, avec leur
   date. Piège vérifié : cet outil décrit le PRODUIT, pas les 36 outils de
   l'Académie.
3. **Adapté à mon activité ?** : `secteur_foodeatup` (restaurant,
   boulangerie, réseau/franchise) — le socle métier du secteur, ses postes,
   ses parcours.
4. **Comparaison à l'empilement d'outils séparés** : uniquement les chiffres
   du champ `empilementSepare` de `tarifs_et_essai`, avec son relevé et sa
   lecture — aucun autre comparatif, aucun concurrent nommé.
5. Conclure vers l'action : essai → le site (`pageTarifs`) ; apprendre →
   skill `demarrer-academie` ; devenir partenaire → skill
   `devenir-partenaire`.

## Garde-fous

- **Jamais un montant absent de la réponse du serveur.** Le hook
  `garde-tarifs-et-commissions` rappelle la règle et bloque l'écriture d'un
  montant sans date de vérification.
- Les questions du parcours convive (fidélité, QR code côté client) →
  skill `espace-convive`.
- Ce skill renseigne, il ne vend pas : pas de pression, pas de promesse de
  résultat chiffré.
