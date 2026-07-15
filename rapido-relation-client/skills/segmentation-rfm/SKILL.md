---
name: segmentation-rfm
description: Utiliser quand l'utilisateur veut segmenter ses clients, une analyse RFM, identifier ses champions/clients à risque/endormis, ou cibler par valeur. Récence × Fréquence × Montant sur les factures et commandes réelles, calcul par script, segments (champions, fidèles, à risque, endormis, perdus) avec action type par segment routée vers campagne-marketing ou animation-client.
---

# Segmentation RFM — cibler par valeur réelle

Qui sont vraiment vos meilleurs clients, et lesquels décrochent — sur les vrais achats.

## Étape 0 — règles KB
- `./rapido-kb/relation-client/fidelite.md` : segments → actions (jamais en dur).

## Sense (achats réels)
- **Récence** (dernier achat), **Fréquence** (nb d'achats), **Montant** (CA cumulé) :
  `list_factures` (CRM) et commandes `foodeatup:list_orders` selon le produit.

## Plan (score par script)
- `python3 "${CLAUDE_PLUGIN_ROOT}/skills/segmentation-rfm/scripts/rfm.py"` — R/F/M en
  **quintiles 1-5** (R inversé), **formule affichée** → segment (champions, fidèles, à
  risque, endormis, perdus).

## Act (actions par segment, confirmées)
- **Champions/fidèles** → animation, ambassadeurs (`rapidocrm:animation-client`,
  `programme-ambassadeurs`). **À risque/endormis** → réactivation ciblée
  (`rapido-marketing:campagne-marketing`). **Perdus** → win-back ou clôture. Tout envoi
  **confirmé** (brouillon).

## Feed
- Historiser dans `./rapido-kb/relation-client/rfm-historique.md` (date, tailles de segments).

## Frontière
- `boucle-nps` segmente par **satisfaction** ; **moi = par valeur transactionnelle** (RFM).
  `sante-client` = score composite ; moi = segmentation d'achat. Complémentaires.

## Garde-fous
Segmentation **par script** (formule affichée) sur achats **réels** ; actions
**confirmées** ; historisation datée ; règles depuis la KB.
