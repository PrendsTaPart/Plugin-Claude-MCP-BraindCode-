# Benchmark founder-playbook — par livre (M1-ter)

> Comparaison des 10 dossiers distillés du dépôt MIT
> [getagentseal/founder-playbook](https://github.com/getagentseal/founder-playbook)
> (© 2026 AgentSeal) à nos skills existants. **Reformulation FR intégrale**,
> ≤ 1 citation courte par fiche, **double attribution** (auteur + AgentSeal MIT),
> aucun extrait de livre. Licence : `docs/methodo/100m-leads/NOTICE.md`.

## Écarts avec le regroupement du prompt initial (contrôle appliqué)
Le prompt initial classait 6 livres « sans équivalent maison ». Vérification
faite skill par skill, **6 des 10 ont en réalité un équivalent** :

| Livre | Équivalent maison trouvé | Prompt initial | Réel |
|---|---|---|---|
| spin-selling | `rapido-forge:scale-spin-selling` | sans équiv. | **patch** |
| blue-ocean | `rapido-forge:scale-blue-ocean` | sans équiv. | **patch** |
| obviously-awesome | `rapido-forge:bootcamp-positioning-map` (Perceptual Map) | sans équiv. | **fiche + articulation** |
| monetizing-innovation | `rapido-forge:scale-pricing-strategy` (3 modèles + WTP) | sans équiv. | **fiche + articulation** |
| lean-startup | `rapido-forge:ideation-lean-canvas` (Ash Maurya, adjacent) | sans équiv. | **fiche + articulation** |
| traction | aucun (forge = Ansoff/Growth, pas de sélection de canal) | sans équiv. | **fiche complète** |
| 100m-offers / mom-test / storybrand / made-to-stick | équivalents connus | avec équiv. | **patch** |

Règle de décision appliquée : recouvrement ≥ ~50 % → **patch** ; partiel →
**fiche + articulation** ; nul → **fiche complète**.

---

## Benchmark par livre

| Livre (auteur) | Ils couvrent, pas nous | Nous couvrons, pas eux (fierté maison) | Verdict |
|---|---|---|---|
| **Traction** (Weinberg & Mares) | Bullseye 5 étapes, **19 canaux**, règle des 50 %, Critical Path, Law of Shitty Click-Throughs | notre `core-four-strategie` (4 canaux + règle des 100 + More Better New), exécution **branchée MCP** | **fiche** `docs/methodo/traction/` |
| **Obviously Awesome** (Dunford) | 5+1 composantes, 3 styles de positionnement, 10 étapes, positioning≠messaging≠branding | `bootcamp-positioning-map` (Perceptual Map), `storybrand-messaging`, `icp-generator` (segments réels CRM) | **fiche+articulation** |
| **Monetizing Innovation** (Ramanujam) | 9 règles, WTP (5 méthodes), Leaders/Fillers/Killers, Good/Better/Best + fences, pricing comportemental, price integrity | `scale-pricing-strategy` (3 modèles + WTP), `money-math-acquisition` (LTGP:CAC), `catalogue-kpi` | **fiche+articulation** (comble **Pricing Strategy**) |
| **Lean Startup** (Ries) | Build-Measure-Learn, MVP-expériment, Innovation Accounting, 10 pivots, 3 moteurs de croissance | `ideation-lean-canvas` (le canvas), `growth-experiments` (ICE + A/B par script), `mom-test` | **fiche+articulation** |
| **SPIN Selling** (Rackham) | Questions **Problem** détaillées, Implied→Explicit, 4 étapes d'entretien, FAB redéfini, 4 issues/Advance | `scale-spin-selling` (S/I/N partiels), `scale-bant-qualification`, `negotiation` | **patch** `scale-spin-selling` |
| **Blue Ocean** (Kim & Mauborgne) | Six Paths, 3 Tiers of Noncustomers, Buyer Utility Map, Strategic Sequence | `scale-blue-ocean` (ERRC + Strategy Canvas) | **patch** `scale-blue-ocean` |
| **$100M Offers** (Hormozi) | 4 catégories d'obstacles, vecteurs de livraison, matrice trim & stack | `hundred-million-offers` (Value Equation, starving crowd, stacking, MAGIC, garanties) — **large couverture** | **patch** (mineur) |
| **The Mom Test** (Fitzpatrick) | type « Ideas/Features », Filter Test | `mom-test` (3 règles, compliments/fluff, commitment currency, customer slicing) | **patch** (mineur) |
| **Building a StoryBrand** (Miller) | test des 5 secondes, Marketing Roadmap 5 tâches | `storybrand-messaging` (SB7, guide, one-liner, brandscript) | **patch** (mineur) |
| **Made to Stick** (Heath) | tableau symptôme→principe | `made-to-stick` (SUCCESs complet + curse of knowledge) | **patch** (mineur) |

## Fierté maison à conserver (ce que NOUS avons et pas eux)
- **Exécution réelle branchée MCP** (RapidoCRM/CMS/RH) — eux restent au niveau
  méthodo/document.
- **Calculs par script** (LTGP:CAC, scoring, funnel, A/B z-test) — formule affichée.
- **Garde-fous déterministes** (confirmations, RGPD, budgets) et **mémoire** KB.
- **Orchestrateurs** (machine-inbound/outbound, tunnel-de-vente-360) + équipe d'agents.

## Livrables (M1-ter)
- Fiches : `docs/methodo/{traction,obviously-awesome,monetizing-innovation,lean-startup}/<livre>.md`.
- Patchs : `docs/methodo/patchs/{scale-spin-selling,scale-blue-ocean,hundred-million-offers,mom-test,storybrand-messaging,made-to-stick}.md`.
- MAJ : `docs/methodo/INDEX.md`, `docs/MATRICE-COUVERTURE.md`.
