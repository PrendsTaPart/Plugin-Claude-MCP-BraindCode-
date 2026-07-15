# rapido-marketing

Marketing & acquisition **Rapido-first** : le plugin qui orchestre la génération
de leads, le tunnel de conversion, le nurturing, la publicité et l'analytics en
**priorisant les serveurs Rapido** (CRM → CMS → RH), les MCP secondaires en
repli seulement.

> **Version 0.1.0 — squelette.** Ce plugin fournit pour l'instant le socle
> (priorité MCP, garde-fous, pièges d'outils, hooks déterministes). Les skills
> sont ajoutés dans les versions suivantes.

## Socle (livré en 0.1.0)

| Fichier | Rôle |
|---|---|
| `reference/priorite-mcp.md` | hiérarchie Rapido-first + règle de routage + mode dégradé |
| `reference/garde-fous-marketing.md` | envois confirmés, RGPD, délivrabilité, budgets pub, KPI par script |
| `reference/pieges-outils.md` | pièges des outils marketing des 3 serveurs (repris de M0) |
| `hooks/` | `garde-envois` (confirmation forcée sur tout envoi) + Stop récap-actions |

## Skills prévus (à venir — voir `docs/MATRICE-COUVERTURE.md`)

| Skill prévu | Comble |
|---|---|
| `acquisition-100m-leads` | fiches `docs/methodo/100m-leads/` → skill exécutable |
| `icp-builder` | ICP (MANQUANT M0) — firmographies via CRM |
| `lead-scoring` | scoring Fit×Engagement (dépend d'un tool score backend) |
| `attribution-canal` | orchestration `get_conversion_par_canal` (multi-touch à venir) |
| `tunnel-conversion` | landing → formulaire/CTA → segment → email → stats |
| `sequences-nurturing` | speed-to-lead + nurture multicanal via n8n |
| `revops-cockpit` | vue revenu unifiée (transverse) |

## Serveurs MCP

RapidoCRM, RapidoCMS, RapidoRH (prioritaires) + facebook-ads, canva, lovable,
n8n, gmail, google-calendar (repli). Variable d'env : `N8N_MCP_URL` (n8n).

## Garanties
Tout envoi (email/SMS/newsletter/campagne/publication/activation pub) demande
une **confirmation humaine explicite** ; RGPD (consentement + effacement)
respecté ; scores et KPI **calculés par script**, jamais de tête.
