---
name: handle-complaint
description: Utiliser quand un client se plaint (email, avis, ticket) et qu'il faut traiter la réclamation de bout en bout : contexte récupéré, réponse rédigée, correctif opérationnel proposé. Accepte un email ou un ID de ticket en argument. S'appuie sur les MCP foodeatup/rapidocrm pour les données réelles et sur ./rapido-kb/ pour les seuils maison.
source: anthropics/knowledge-work-plugins (commit 564d560c), Apache 2.0
allowed-tools: Read, WebFetch, Bash
---

> Nécessite les MCP **foodeatup** ET **rapidocrm** (tous deux déclarés dans
> le `.mcp.json` du plugin).

## Adaptation Rapido (lire d'abord)

Ce skill vient d'un contexte US générique. Dans cette marketplace, remplacer
systématiquement ses outils par les équivalents Rapido :

| Outil cité dans ce skill | Équivalent à utiliser ici |
|---|---|
| QuickBooks / PayPal / Square / Stripe (finances, ventes) | FoodEatUp : `finance_summary`, `list_orders`, `list_invoices`, `list_expenses` ; RapidoCRM : `get_revenue_summary`, `list_factures`, `list_depenses` |
| HubSpot (CRM, pipeline) | RapidoCRM : `get_pipeline`, `get_entreprise`, `get_historique_prospect`, `list_devis`, `log_activity` |
| Gmail (envoi d'emails) | RapidoCRM : `send_email` / `schedule_email` (confirmation avant envoi) ; ou brouillons via le plugin rapido-direction |
| Google Drive / Calendar | plugin rapido-direction (`coffre-documents`, agenda) ou RapidoCRM `agenda-rdv` |
| Slack (notifications) | pas d'équivalent — restituer dans la conversation, ou notification via un workflow n8n (plugin rapido-n8n) |
| Zendesk / Shopify | pas d'équivalent direct — support : `log_activity` (CRM) ; vente en ligne : carte vitrine FoodEatUp |
| CSV uploads | inutile si les MCP répondent — les données viennent des serveurs |

Les seuils, cadences et benchmarks du skill sont des DÉFAUTS US : les seuils
maison de `./rapido-kb/processus-internes.md` priment (les citer).


Run the complaint resolution workflow by chaining two skills. Read the complaint, gather context, draft a response, and suggest a fix so it doesn't happen again.

Parse arguments:
- `EMAIL_OR_TICKET_ID` (optional) — ID de fil email (rapido-direction), ID de ticket
  CRM, ou "latest" pour la plainte non résolue la plus récente. Sinon, demander à
  l'exploitant de coller le texte de la plainte.

## Step 1 — Load the complaint

Récupérer la plainte :

1. If an ID was given: charger le fil depuis la boîte mail (plugin rapido-direction) ou le ticket CRM.
2. If "latest": prendre la plainte non résolue la plus récente (email support / activité CRM).
3. If neither: ask the owner to paste the complaint text directly.
4. Identify: customer name, order/account info, what they're upset about, what they're asking for.

## Step 2 — Pull context

1. Historique client : RapidoCRM (`get_contact`, `get_historique_prospect`,
   `get_loyalty_points`) et/ou FoodEatUp (`get_client` + `list_orders` du client).
2. Commande concernée : FoodEatUp `list_orders` / `get_order` (statut), `list_invoices`
   (paiement/avoir) — pas de PayPal/Stripe dans cet écosystème.
3. Summarize: "This is a {new/returning} customer, ${lifetime_value} in purchases, {0/N} prior complaints. Their current issue is {one sentence}."

## Step 3 — Draft response

Pour une réponse au ton juste, s'appuyer sur `rapidocrm:draft-response` (situations
client délicates). Sinon, rédiger directement :

1. Draft a reply matched to the severity and the customer's history:
   - First-time complainers with high LTV → empathetic, generous
   - Repeat complainers → professional, firm, solution-focused
   - Abusive tone → professional, brief, boundary-setting
2. Include: acknowledgment, explanation (if known), resolution offer, next step.
3. Present the draft to the owner. Do NOT send.

## Step 4 — Suggest operational fix

1. Vérifier si la plainte recoupe un thème connu (plaintes similaires déjà tracées dans
   le CRM via `log_activity`, ou notes `./rapido-kb/`).
2. If it's a pattern: "This is the {Nth} complaint about {issue} this month. Consider: {specific operational change}."
3. If it's isolated: "This looks like a one-off. No pattern detected."

## Connector failures

Si le CRM et la boîte mail (rapido-direction) sont injoignables, demander à l'exploitant
de coller le texte de la plainte — le skill fonctionne en saisie manuelle. Si FoodEatUp
est injoignable, sauter la recherche de commande et noter « statut de commande
indisponible — travail à partir du texte de la plainte uniquement ».

## Approval gates

- **Never send a response without explicit owner approval.** Drafts only.
- **Never issue refunds or credits automatically.** Present the option; the owner decides.
- **Never close tickets or resolve disputes without owner confirmation.**

## Output

Present the customer context summary, the drafted response, and any pattern-based operational suggestion. Ask: "Want to send this response, edit it, or handle it differently?"
