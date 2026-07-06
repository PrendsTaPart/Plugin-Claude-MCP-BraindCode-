---
name: price-check
description: Utiliser quand l'utilisateur veut vérifier ses prix ou voir ses marges par produit avant une décision tarifaire. Produit un tableau marge par produit et trois scénarios de prix pour une vision financière complète. Accepte un nom de produit en argument. S'appuie sur les MCP foodeatup/rapidocrm et sur ./rapido-kb/ pour les seuils maison.
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


Run the pricing analysis. Pull cost and revenue data, build the margin table, and model three pricing scenarios — so the owner can see the numbers clearly before deciding what to charge.

Parse arguments:
- `PRODUCT_NAME` (optional) — specific product or service to analyze; if omitted, analyze all active products

## Step 1 — Current margin baseline

Using the `margin-analyzer` skill workflow:

1. Pull QuickBooks revenue by product/service for the last 90 days.
2. Pull COGS or direct costs per product from QuickBooks (if categorized).
3. Pull PayPal gross sales for the same products to cross-validate.
4. Calculate current gross margin per product: (revenue − COGS) ÷ revenue.

Build the margin table:

```
Product          | Revenue  | COGS     | Gross Margin | Margin %
{product}        | ${amt}   | ${amt}   | ${amt}       | {X}%
```

Flag any product with margin below 20% as a risk.

## Step 2 — Three pricing scenarios

For each product (or the specified product), model three scenarios. Do NOT recommend a price — present data only.

**Scenario A — Hold current price**
- Project revenue at current price × current volume
- Project margin at current COGS

**Scenario B — Price increase (+10% to +20%, owner to specify)**
- Project revenue assuming 0%, 5%, and 10% volume loss at new price
- Show the break-even volume needed to maintain current profit

**Scenario C — Price decrease (−10%, to drive volume)**
- Project revenue assuming 10%, 20%, and 30% volume increase
- Show the volume needed to match current profit

Present each scenario as a data table, not a recommendation.

## Step 3 — Customer messaging brief

Produce a plain-language brief (for price increase scenarios) the owner can use to communicate a change to customers:
- One paragraph explaining the change
- Three key message options (direct, value-focused, empathetic)
- Suggested timing and channel (email, invoice note, in-person)

## Connector failures

If QuickBooks is unreachable, stop — margin analysis requires QB revenue and cost data. If PayPal is missing, run from QB-only and note "PayPal not connected — cross-validation against PayPal sales skipped."

## Approval gates

- **Never recommend a specific price.** Provide data views only — pricing decisions belong to the owner.
- **Flag if COGS data is incomplete** (many QB setups don't track per-product COGS) and note the gap.
- **Never update any prices in QB, PayPal, or any connected system.**

## Output

Present the margin table, then the three scenario tables side-by-side. If a price increase scenario is being considered, append the customer messaging brief. End with: "Which scenario would you like to explore further?"
