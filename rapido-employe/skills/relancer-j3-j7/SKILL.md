---
name: relancer-j3-j7
description: Utiliser quand les relances du matin sont dues, que l'utilisateur dit « fais tes relances J+3 et J+7 », « qui n'a pas répondu », « prépare les relances des devis en attente ». Lit le pipeline, prépare chaque relance en brouillon Gmail sur le modèle validé, et note la relance au CRM.
---

# Relancer à J+3 et J+7 (le brouillon, jamais l'envoi)

Familles engagées : **prospecter** (Aperçu) — la mécanique passe par des
BROUILLONS Gmail (famille preparer), l'humain envoie.

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.
2. Cadre du jour en main ; modèles de relance validés (KB ou décision du
   responsable dans `get_claude_brief`).

## Workflow

1. **`get_pipeline`** (RapidoCRM) — les prospects sans réponse : dernier
   contact à J+3 ou J+7 (calcul par date, montré), devis en attente
   (`list_devis` statut envoyé). Pour la revue de pipeline complète,
   DÉLÉGUER au plugin `rapidocrm` (skill `coaching-pipeline`).
2. **Préparer chaque relance** : brouillon Gmail (`create_draft`) sur le
   MODÈLE VALIDÉ — personnalisé des faits réels de la fiche (établissement,
   date d'échange, devis), avec l'expéditeur nommé et un moyen de refuser.
   Gmail absent : textes livrés dans la conversation, en le disant.
3. **Noter** : `log_activity` sur chaque fiche relancée (« relance J+3
   préparée le … ») — c'est ce qui rend le prochain calcul J+7 juste.
4. **Récapituler** : combien de relances préparées, lesquelles attendent
   l'envoi humain, lesquelles passent en « sans réponse » (à décider).

KPI : `rdv-tenus`, `appel-rdv`, `taux-signature`.
Formations : `prospection`, `closing`.

## Garde-fous

- L'envoi Gmail direct est INTERDIT (hook garde-envois : deny) — le
  brouillon est le livrable.
- Une relance par échéance et par prospect, pas plus : J+3, J+7, puis
  décision humaine — le harcèlement ne signe rien.
- Quota `envoisJour` compté quand l'humain fait envoyer en niveau Confirmé
  futur ; aujourd'hui tout part en brouillon.
