---
name: qualifier-et-nettoyer-la-base
description: Utiliser quand l'utilisateur veut nettoyer sa base Prospect — « fais le ménage dans mes prospects », « quels clients ont un téléphone invalide ? », « dédoublonne et qualifie la base ». Rapport qualité par script, corrections update_client, suppressions fiche par fiche.
---

# Qualifier et nettoyer la base

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` ;
- `${CLAUDE_PLUGIN_ROOT}/reference/conformite-prospection.md` (exactitude,
  minimisation).

## Démarche
1. **Lire** : `list_clients` avec `search` / `city` / `speciality` selon la
   demande (paginer par limites raisonnables).
2. **Rapport qualité par script** (formules affichées) :
   - téléphones : `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/normaliser_telephone.py
     --json tels.json` — E.164, mobiles FR, invalides ;
   - e-mails invalides (forme), fiches incomplètes (ni e-mail ni téléphone
     ni site), doublons internes via
     `${CLAUDE_PLUGIN_ROOT}/scripts/dedoublonner.py` (base contre
     elle-même).
3. **Corriger** : `update_client` fiche par fiche — téléphone normalisé,
   e-mail corrigé, statut de prospection tenu à jour (le statut sert aux
   segments de campagne). Montrer chaque correction avant de l'écrire.
4. **Supprimer** : `delete_client` UNIQUEMENT sur confirmation explicite,
   fiche par fiche — la suppression est définitive (hook
   garde-destructif-prospect). Proposer d'abord un statut « écarté ».
5. **Journal** : `add_log` avec le bilan (corrigées, écartées, supprimées).

## Pièges
- Ne jamais « deviner » un e-mail ou compléter un numéro : un contact
  invalide se corrige depuis une source réelle ou reste vide.
- Une demande « ne me contactez plus » ne se traite PAS par delete_client :
  elle va dans la liste d'opposition de ./rapido-kb/prospection.md (tous
  canaux), la fiche peut rester pour mémoire.

## Dégradation propre
Base vide ou filtre sans résultat : le dire tel quel et proposer
`prospecter-une-zone`.
