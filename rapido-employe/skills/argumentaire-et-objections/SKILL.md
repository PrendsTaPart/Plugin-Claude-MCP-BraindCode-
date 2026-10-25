---
name: argumentaire-et-objections
description: Utiliser quand il faut les mots de la vente, que l'utilisateur dit « il m'objecte que c'est trop cher », « donne-moi l'argumentaire pour une brasserie », « prépare-moi pour le salon », « c'est quoi notre position face aux concurrents ». Sert les onglets maison (argumentaire, tarifs publics, personas, négociation, kits terrain, salon, Leboncoin) et les missions de vente qui les enseignent.
---

# Argumentaire et objections (les mots de la maison, pas les miens)

Famille engagée : **apprendre** (lectures seules).

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow

1. **Situer la situation** : qui est en face (persona), quel canal
   (téléphone, terrain, salon, petite annonce), quelle objection.
2. **`list_onglets` puis `get_onglet`** sur l'onglet utile : argumentaire,
   tarifs publics, personas, négociation, kits terrain, salon, Leboncoin —
   le contenu de l'onglet EST la position de la maison, restituée telle
   quelle et adaptée au cas (nom de l'établissement, faits réels).
3. **Approfondir par les missions** quand l'objection résiste :
   `list_missions` filtré sur `soncas` (motivations), `closing`,
   `negociation`, `personas`, `concurrence`, `demo-certifiee` — puis
   `get_mission` sur la mission exacte (skill `chemin-de-formation` pour la
   travailler).
4. **Livrer** : la réponse à l'objection en 3 temps (accuser réception,
   repositionner avec le fait maison, avancer d'un pas — rendez-vous, démo,
   essai), prête à dire.
5. S'entraîner à la dire : skill `pitch` (répétition corrigée).

KPI : `taux-signature`, `demos`.
Formations : `soncas`, `closing`, `negociation`, `personas`, `concurrence`,
`demo-certifiee`.

## Garde-fous

- Les tarifs cités sont ceux de l'onglet « tarifs publics » (ou
  `tarifs_et_essai` côté produit) avec leur date — jamais un prix de
  mémoire, jamais une remise improvisée (famille engager).
- Les concurrents se traitent comme l'onglet concurrence les traite — pas
  de dénigrement, pas de chiffre non sourcé.
- Une objection sans réponse maison se dit telle quelle et remonte au
  responsable — on n'invente pas une position commerciale.
