# Évals — plugin rapido-leadmagnet (0.1.0, squelette)

Stade squelette : garde-fous + fondations. Les évals de déclenchement des skills
arrivent avec eux (LM2→LM5).

## Garde-fous (hook `garde-budget-ads`, testé au testeur)

| Entrée | Décision attendue |
|---|---|
| `mcp__facebook-ads__ads_create_campaign` | **ask** (PAUSED + coût max) |
| `mcp__facebook-ads__ads_activate_entity` | **ask** |
| `mcp__facebook-ads__ads_boost_ig_post` | **ask** |
| `mcp__facebook-ads__ads_get_ad_accounts` (lecture) | **allow** |
| `mcp__rapidocrm__enregistrer_prospect` | **allow** (hors périmètre du hook) |

## Anti-déclenchements (à respecter dans les skills)

- « Conçois-moi un lead magnet » / « quel lead magnet créer » →
  **`rapido-marketing:lead-magnet-machine`** (conception), pas l'usine.
- « Landing page produit » (hors lead magnet) → **`rapido-lovable:usine-a-landing`**.
- « Newsletter simple » → **`rapido-marketing`** campagne marketing, pas l'usine LM.

## Principes vérifiés

- L'usine **exécute** un concept déjà validé ; elle ne re-conçoit pas.
- Landing & capture = Route B (Lovable mode B) — décision LM0.
- RGPD, gate délivrabilité, LinkedIn semi-auto, Meta PAUSED, un seul LM en prod.
- Rien d'inventé ; preuves = données CRM réelles ; stats par script.
