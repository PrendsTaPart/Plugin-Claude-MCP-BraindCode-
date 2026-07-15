# Signaux d'intention — volet du lead-scoring

> **Source distillée** : gtm-flywheel (`signal-scoring/` : intent-signals,
> lead-prioritization, trigger-mapping) MIT © 2026 ColdIQ. Reformulé FR,
> non-verbatim (voir `NOTICE.md`). Enrichit le skill `lead-scoring`.

## L'idée
Au-delà du fit ICP et de l'engagement, un **3e signal** : l'**intention** —
événements qui indiquent qu'un compte est « en marché » maintenant.

## Types de signaux (mappés à ce qui est captable côté Rapido)
| Signal d'intention | Captable via | Sinon |
|---|---|---|
| Visite répétée d'une page clé | `get_formulaire_soumissions`, CTA (`list_cta`) | — |
| Ouverture/clic email répétés | `get_interaction_stats` | — |
| Changement de poste / recrutement | (enrichissement) | **MCP manquant** (intent data) |
| Levée de fonds récente | (enrichissement) | **MCP manquant** |
| Techno installée | (enrichissement) | **MCP manquant** |

## Trigger mapping (événement → action)
Chaque signal fort déclenche une action outbound priorisée (relance, RDV) —
jamais une action visible sans confirmation. Automatisable via **n8n** (MCP
disponible).

## Mapping Rapido
Le score d'intention **s'ajoute** au modèle 2 axes de `lead-scoring` (fit ×
engagement) comme **bonus de priorisation**, calculé par script (jamais de tête).
Les providers d'intent externes (ZoomInfo/Bombora/6sense) sont des **MCP
manquants** — à remonter à Tunis ; en attendant, on exploite les signaux
first-party (formulaires, CTA, interactions CRM).

→ Cible : **volet « signaux » de `lead-scoring` (M5)**.
