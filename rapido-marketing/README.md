# rapido-marketing

Marketing & acquisition **Rapido-first** : le plugin qui orchestre la génération
de leads, le tunnel de conversion, le nurturing, la publicité et l'analytics en
**priorisant les serveurs Rapido** (CRM → CMS → RH), les MCP secondaires en
repli seulement.

> **Version 0.4.0.** Socle (priorité MCP, garde-fous, hooks) + 4 skills
> **méthodo** (distillation $100M Leads). Les skills d'**exécution**
> (machine-inbound/outbound, tunnel-de-vente-360) suivent.

## Socle (livré en 0.1.0)

| Fichier | Rôle |
|---|---|
| `reference/priorite-mcp.md` | hiérarchie Rapido-first + règle de routage + mode dégradé |
| `reference/garde-fous-marketing.md` | envois confirmés, RGPD, délivrabilité, budgets pub, KPI par script |
| `reference/pieges-outils.md` | pièges des outils marketing des 3 serveurs (repris de M0) |
| `hooks/` | `garde-envois` (confirmation forcée sur tout envoi) + Stop récap-actions |

## Skills (✅ = livré ; autres à venir — voir `docs/MATRICE-COUVERTURE.md`)

| Skill prévu | Comble |
|---|---|
| `core-four-strategie` ✅ | choix de canal + cadence + scaling (fiches 01/03/05/08) |
| `lead-magnet-machine` ✅ | aimant à prospects en 7 étapes (fiche 02) |
| `money-math-acquisition` ✅ | LTGP:CAC, acquisition financée client (fiche 04) |
| `lead-getters-systeme` ✅ | parrainage/employés/agences/affiliés (fiche 07) |
| `icp-generator` ✅ | ICP entreprise fondé sur les clients gagnés (script) |
| `lead-scoring` ✅ | scoring fit×engagement par script (écriture CRM confirmée) |
| `social-selling-linkedin` ✅ | profil + contenu + scripts DM prêts à copier (pas d'auto-DM) |
| `geo-optimization` ✅ | audit GEO déterministe + corrections (script) |
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
