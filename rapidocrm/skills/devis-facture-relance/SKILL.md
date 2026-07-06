---
name: devis-facture-relance
description: Utiliser quand l'utilisateur parle de devis, de facture, de relancer un impayé ou de changer le statut d'une facture. Gère le cycle devis → facture → suivi des statuts → relances.
---

# Devis, factures et relances

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (règles communes)
et, pour rédiger des emails de relance, `${CLAUDE_PLUGIN_ROOT}/reference/charte-graphique.md`
(ton de voix, do/don't).

## Statuts autorisés (ne jamais en inventer d'autres)

- **Devis** : `brouillon`, `en_attente`, `accepte`, `refuse`, `expire`.
- **Factures** : `brouillon`, `en_attente`, `payee`, `en_retard`.
- Transitions autorisées (logique DGFiP — une facture émise ne se supprime pas) :
  - devis : `brouillon → en_attente → accepte | refuse | expire` ;
  - facture : `brouillon → en_attente → payee` ou `en_attente → en_retard → payee`.
- INTERDIT : repasser une facture `payee` à un statut antérieur, ou supprimer une
  facture émise — proposer un avoir et le signaler à l'utilisateur.

## Workflow

1. **Créer le devis** — `create_devis` (`entreprise_id` requis ; `destinataire`,
   `total_ht`, `taux_tva` en % — `total_ttc`/`total_tva` auto-calculés sinon —,
   `remise` en %, `mode_paiement` ∈ Espèce | Carte bleu | Virement | Chèque,
   `delai_paiement` ex. « 30 jours », `date_fin` = validité, `statut` initial
   `brouillon` ou `en_attente`). Suivre les devis avec `list_devis` (et les
   factures avec `list_factures` / `get_facture`).
2. **Devis accepté → facture** — `create_facture` avec **`devis_id`** pour tracer le
   lien, en reprenant `entreprise_id` et les montants du devis. Ne facturer que sur
   devis `accepte` (sinon demander confirmation explicite).
3. **Changer un statut** — le statut se définit via le champ `statut`. Aucun outil
   dédié `update_invoice_status` n'existe sur ce serveur : respecter strictement les
   transitions ci-dessus et, si un changement de statut n'est pas possible via
   l'API, le dire à l'utilisateur au lieu de forcer ou de contourner.
4. **Relancer les impayés** :
   a. Identifier — `list_factures` filtrées `statut` = `en_retard` (ou `en_attente`
      échues, en vérifiant `date_fin`) ;
   b. Relancer — `send_email` (`entreprise_id`, `sujet`, `contenu` ou
      `template_id`) pour un envoi immédiat, ou `schedule_email` (`date_envoi`
      YYYY-MM-DD HH:MM:SS) pour planifier. Mentionner numéro de facture, montant
      TTC et échéance dans la relance.
   c. Tracer — `log_activity` pour consigner la relance sur la fiche entreprise.

## Garde-fous

- Jamais de transition de statut non listée ci-dessus ; s'appuyer sur les statuts
  valides renvoyés par l'API en cas d'écart.
- Confirmation explicite de l'utilisateur avant tout envoi de relance (contenu +
  destinataire), et avant de facturer un devis non `accepte`.
- Escalade des relances : 1ʳᵉ relance courtoise à J+7 après échéance, 2ᵉ ferme à
  J+21, mise en demeure à J+45 — proposer ce calendrier via `schedule_email`.
