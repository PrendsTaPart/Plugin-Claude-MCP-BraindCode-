---
name: preparer-un-devis
description: Utiliser quand une démonstration appelle une proposition, que l'utilisateur dit « prépare le devis du Bistrot », « fais la proposition après la démo », « chiffre l'abonnement pour ce restaurant ». Reprend les produits de la grille, crée le devis en brouillon et prépare l'envoi — l'humain envoie, et tout prix hors grille part en demande d'accord.
---

# Préparer un devis (la grille, le brouillon, l'accord)

Familles engagées : **preparer** (Brouillon) — un prix hors grille ou une
remise bascule en **engager** (décision humaine, toujours).

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.
2. Cadre du jour en main. La grille tarifaire est celle des outils — jamais
   de mémoire.

## Workflow

1. **`list_products`** (RapidoCRM) — les produits et prix DE LA GRILLE ;
   côté produit FoodEatUp, les packs publics se vérifient par
   `tarifs_et_essai` (serveur tutoriel) avec leur date.
2. **`create_devis`** en BROUILLON — lignes aux prix de grille, TVA, durée
   de validité ; totaux calculés par l'outil, jamais de tête.
3. **Prix hors grille ou remise demandée** : STOP — demande d'accord au
   responsable (montant, raison, impact), rien n'est créé avant sa réponse.
   C'est la famille « engager » : toujours une décision humaine.
4. **Préparer l'envoi** : brouillon Gmail (`create_draft`) avec le devis
   joint ou référencé, texte sobre, expéditeur nommé — **l'humain envoie**.
5. **Noter** : `log_activity` (devis préparé), et la relance s'armera en
   J+3/J+7 (skill `relancer-j3-j7`).

KPI : `taux-signature`, `delai-signature`, `panier-moyen`.
Formations : `closing`, `negociation`.

## Garde-fous

- JAMAIS un montant inventé ni « arrondi » : grille et outils font foi, un
  prix absent se demande.
- Le devis reste brouillon jusqu'à l'envoi humain ; la facture, elle, est
  famille engager (hors de ce skill).
- Négociation : les positions viennent de la formation `negociation` et de
  l'onglet dédié — aucune concession chiffrée improvisée.
