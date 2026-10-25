---
name: alertes-kpi
description: Utiliser quand une alerte de seuil attend, que l'utilisateur dit « il y a une alerte sur mon accueil », « le seuil des crédits est franchi, on fait quoi », « traite l'alerte MRR ». Explique le seuil franchi et l'action proposée, et ne tranche qu'avec la décision explicite de l'utilisateur.
---

# Alertes KPI (expliquer, puis laisser décider)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow

1. **`get_kpi_home`** — les alertes en attente : quel KPI, quel seuil
   franchi, dans quel sens, quelle action le serveur propose.
2. **Expliquer** chacune : la valeur qui a franchi le seuil (avec sa date de
   relevé), ce que l'action proposée ferait concrètement, et ce qui se passe
   si on l'écarte. Si l'alerte touche une routine :
   `list_pending_routine_actions` et le bilan (`get_routine_report`) donnent
   le contexte.
3. **`decide_kpi_alert`** — UNIQUEMENT sur la décision explicite de
   l'utilisateur (accepter l'action proposée, ou écarter). Une alerte déjà
   traitée est refusée par le serveur : le dire, ne pas retenter.
4. Si la bonne réponse est plutôt une amélioration de routine : basculer sur
   le skill `auditer-mes-routines` au lieu de trancher l'alerte à chaud.

## Garde-fous

- Jamais décidé à la place de l'utilisateur (famille « tranchent » du hook
  garde-planit).
- L'explication cite les valeurs du serveur, datées — pas de dramatisation,
  pas de minimisation.
