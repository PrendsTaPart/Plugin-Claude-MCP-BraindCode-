---
name: contrats-clients
description: Utiliser quand l'utilisateur parle de contrat client, de template de contrat, de faire signer un contrat ou de relancer un contrat non signé. Gère le cycle template → contrat envoyé → signature → relance.
---

# Contrats clients

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (règles communes)
et, pour rédiger contenus et relances, `${CLAUDE_PLUGIN_ROOT}/reference/charte-graphique.md`.
KB : `propositions-valeur.md` (clauses de valeur) + `processus-internes.md`
(cadences de relance).

## Cycle de vie d'un contrat

`brouillon → en_attente (envoyé) → signe`. Un contrat signé ne se modifie
plus : tout changement passe par un avenant (nouveau contrat).

## Workflow

1. **Template d'abord** — vérifier l'existant avec `list_contrat_templates` ;
   sinon `create_contrat_template` (`titre`, `contenu` HTML/texte avec
   variables dynamiques, `description`) ; pour amender un modèle existant :
   `update_contrat_template` (`id` requis ; `titre`/`contenu`/`description`)
   — les contrats DÉJÀ émis ne changent pas. Faire valider le contenu
   juridique par l'utilisateur — vous rédigez, il assume.
2. **Créer et envoyer le contrat** — `create_contrat` (`entreprise_id`,
   `contrat_template_id`, `date_debut`/`date_fin` YYYY-MM-DD).
   - ⚠️ PIÈGE : `send_email` vaut TRUE par défaut — l'email part
     IMMÉDIATEMENT à la création. Récapituler destinataire (`destinataire`,
     fallback = email de l'entreprise), sujet et message AVANT l'appel, ou
     passer `send_email: false` pour préparer sans envoyer.
   - `message_email` personnalisé (prioritaire) ou `template_email_id`.
3. **Suivre les statuts** — `list_contrats` / `get_contrat` ;
   `update_contrat_status` (`id`, `statut` ∈ brouillon | en_attente | signe ;
   `signature_value` pour marquer signé). Ne marquer `signe` que sur
   confirmation réelle de signature — jamais pour « faire avancer ».
4. **Relancer les non-signés** — `list_contrats` filtrés `en_attente` :
   cadence maison de `./rapido-kb/processus-internes.md` si elle existe, sinon
   défaut J+7 (courtoise) / J+14 (ferme) en le signalant. Relance via
   `send_email` / `schedule_email` (confirmation avant envoi), tracée par
   `log_activity`.
5. **Contrat signé** — féliciter, proposer la suite : facturation
   (`devis-facture-relance`) et onboarding client (`onboarding-client-360`,
   plugin rapido-suite).

## Garde-fous

- Jamais de `create_contrat` sans validation du destinataire (l'envoi est
  immédiat par défaut).
- `update_contrat_status` vers `signe` : uniquement sur preuve/confirmation de
  l'utilisateur ; `delete_contrat`/`delete_contrat_template` : confirmation
  explicite (hook ask).
- Dates de contrat cohérentes (fin > début) ; contenu juridique validé par
  l'utilisateur, pas de clauses inventées.
