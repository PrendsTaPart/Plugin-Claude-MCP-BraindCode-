---
name: revenus-stripe
description: Utiliser quand l'utilisateur demande ses revenus via Prospector Hub — « quel est mon MRR ? », « où en sont les abonnements ? », « chiffre d'affaires Stripe ». stripe_stats lu par script, MRR présenté en estimation, rapport agrégé sans e-mail client.
---

# Revenus Stripe (lecture agrégée)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (MRR = estimation).

## Démarche
1. **Lire** : `stripe_stats` — clients, paiements, abonnements actifs,
   chiffre d'affaires, MRR estimé.
2. **Restituer par script** :
   `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/mrr.py stripe.json
   [historique.json]` — chaque chiffre tel que servi, « MRR estimé »
   jamais raccourci en « MRR », évolution calculée SEULEMENT si un
   historique local de relevés existe (formule affichée).
3. **Tenir l'historique** : proposer d'enregistrer le relevé du jour dans
   un fichier local de la KB (date + chiffres) pour que l'évolution
   devienne calculable — jamais de courbe sans points réels.
4. **Widget** : mrr-stripe sur demande (chiffres + mention d'estimation).
5. **Lien avec l'entonnoir** : `scripts/entonnoir.py` prend ce relevé pour
   la marche « clients » — voir skill `tableau-de-bord-prospection`.

## Pièges
- Rapport AGRÉGÉ : aucun e-mail client, aucun détail nominatif de
  paiement dans la restitution ni dans le journal.
- Le pilotage financier d'ensemble (prévisionnel, trésorerie) vit dans le
  plugin rapido-direction : ici on lit UN connecteur Stripe.

## Dégradation propre
Champ absent de la réponse : « — », jamais estimé ; serveur non connecté :
le dire.
