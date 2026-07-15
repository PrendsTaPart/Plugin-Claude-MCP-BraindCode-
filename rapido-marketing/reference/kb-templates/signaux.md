# Catalogue de signaux d'intention — volet fraîcheur du lead-scoring

> Modèle copié dans `./rapido-kb/marketing/signaux.md` à la 1re exécution du skill
> `lead-scoring`. **Uniquement des signaux observables par NOS sources.** Chaque
> signal : source MCP, poids par défaut, **durée de validité** (au-delà, le signal
> est périmé et ne compte plus). Poids éditables via `scoring.md`.
>
> Adapté de `docs/methodo/ops/signaux-intention.md` (distillation gtm-flywheel,
> MIT © 2026 ColdIQ — voir `docs/methodo/ops/NOTICE.md`). Reformulé, non-verbatim.

## Signaux first-party (captables directement)

| Signal (`type`) | Source MCP | Poids | Validité |
|---|---|---|---|
| Soumission de formulaire (`form_submit`) | `get_formulaire_soumissions` | 25 | 30 j |
| Clic sur un CTA (`cta_click`) | `list_cta` | 12 | 21 j |
| Réponse à une séquence (`reponse_sequence`) | `get_interaction_stats`, `get_historique_prospect` | 30 | 30 j |
| Mouvement de pipeline (`mouvement_pipeline`) | `get_pipeline`, `get_historique_prospect` | 20 | 45 j |

## Signaux d'actualité entreprise (via `rapidocrm:account-research`)

| Signal (`type`) | Source | Poids | Validité |
|---|---|---|---|
| Levée de fonds récente (`levee_fonds`) | `rapidocrm:account-research` (actualité) | 25 | 90 j |
| Recrutement / offre d'emploi (`recrutement`) | `rapidocrm:account-research` | 15 | 60 j |
| Changement de poste d'un contact clé (`changement_poste`) | `rapidocrm:account-research` | 20 | 60 j |

## Fraîcheur (3e facteur)
Chaque signal contribue **poids × fraîcheur**, avec
`fraîcheur = max(0, 1 − âge_du_signal / validité)` (décroissance linéaire ;
signal périmé → 0). Par type de signal, seule l'**occurrence la plus récente**
compte (le **volume** est déjà porté par l'axe engagement — pas de double compte).

## Limite (MCP manquant)
Les providers d'intent externes (ZoomInfo/Bombora/6sense — techno installée,
intent tiers) ne sont **pas** exposés : consigné dans
`docs/OUTILS-MCP-MANQUANTS.md` (entrée 4). En attendant, seuls les signaux
first-party + actualité via `account-research` sont exploités. Aucun signal inventé.
