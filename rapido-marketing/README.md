# rapido-marketing

Marketing & acquisition **Rapido-first** : le plugin qui orchestre la génération
de leads, le tunnel de conversion, le nurturing, la publicité et l'analytics en
**priorisant les serveurs Rapido** (CRM → CMS → RH), les MCP secondaires en
repli seulement.

> **Version 0.10.0.** Socle (priorité MCP, garde-fous, hooks) + 4 skills
> **méthodo** (distillation $100M Leads). Les skills d'**exécution**
> (machine-inbound/outbound, tunnel-de-vente-360) suivent.

## Socle (livré en 0.1.0)

| Fichier | Rôle |
|---|---|
| `reference/priorite-mcp.md` | hiérarchie Rapido-first + règle de routage + mode dégradé |
| `reference/garde-fous-marketing.md` | envois confirmés, RGPD, délivrabilité, budgets pub, KPI par script |
| `reference/pieges-outils.md` | pièges des outils marketing des 3 serveurs (repris de M0) |
| `hooks/` | `garde-envois` (confirmation forcée sur tout envoi) + Stop récap-actions |
| `reference/memoire.md` | mapping des 5 périmètres de mémoire + tables n8n |
| `reference/kb-templates/` | 6 modèles `rapido-kb/marketing/` (créés à la 1re exécution) |

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
| `machine-inbound` ✅ | orchestrateur inbound CMS-first (contenu → RDV) |
| `machine-outbound` ✅ | orchestrateur outbound CRM-first (ICP → RDV) |
| `tunnel-de-vente-360` ✅ | flagship : conçoit + construit le tunnel en 5 actes |
| `attribution-kpi-marketing` ✅ | attribution single-touch + CAC/LTV/ROI par canal (script) |
| `growth-experiments` ✅ | backlog ICE + verdict A/B par script (PASS/FAIL/INCONCLUSIF) |
| `sales-intelligence-fireflies` ✅ | mining d'objections depuis les RDV réels (Fireflies, connecteur optionnel) |
| `delivrabilite-email` ✅ | gate pré-envoi (outbound/newsletter) + runbook incident |
| `pilotage-marketing` ✅ | orchestrateur Sense→Plan→Act→Feed→Report + routines n8n |
| `attribution-canal` | orchestration `get_conversion_par_canal` (multi-touch à venir) |
| `tunnel-conversion` | landing → formulaire/CTA → segment → email → stats |
| `sequences-nurturing` | speed-to-lead + nurture multicanal via n8n |
| `revops-cockpit` | vue revenu unifiée (transverse) |

## Serveurs MCP

RapidoCRM, RapidoCMS, RapidoRH (prioritaires) + facebook-ads, canva, lovable,
n8n, gmail, google-calendar (repli). Variable d'env : `N8N_MCP_URL` (n8n).

## Connecteurs optionnels

Certains skills exploitent un connecteur **optionnel** que le plugin **ne
déclare pas** (aucune dépendance dure) : il s'ajoute côté utilisateur, et le
skill fonctionne en mode dégradé s'il est absent.

### Fireflies (transcripts de RDV) — skill `sales-intelligence-fireflies`

- **URL** : `https://api.fireflies.ai/mcp`
- **Ajout dans Claude Code** (transport HTTP) :

  ```bash
  claude mcp add --transport http fireflies https://api.fireflies.ai/mcp
  ```

- **Authentification** : à la charge de l'utilisateur (compte Fireflies), gérée
  par Claude Code au moment de la connexion.
- ⚠️ **Aucune clé ni secret dans ce dépôt** (règle du marketplace). Le connecteur
  n'est **pas** listé dans `.mcp.json` : il reste optionnel et local à
  l'utilisateur. Sans lui, `sales-intelligence-fireflies` explique comment
  l'ajouter puis s'arrête proprement (aucun appel d'outil, aucune erreur brute).

## Anti-collision avec rapido-suite
`pilotage-marketing` est le **sous-domaine marketing** de
`rapido-suite:pilotage-entreprise`. Si les **deux plugins sont installés**, la
suite **invoque `pilotage-marketing`** pour son volet marketing au lieu de le
dupliquer. Invoqué seul, `pilotage-marketing` pilote le marketing de bout en bout.
(Règle miroir dans le README de rapido-suite.)

## Garanties
Tout envoi (email/SMS/newsletter/campagne/publication/activation pub) demande
une **confirmation humaine explicite** ; RGPD (consentement + effacement)
respecté ; scores et KPI **calculés par script**, jamais de tête.
