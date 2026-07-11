# Rapport — recherche sémantique forge_recherche.py (2026-07-10)

TF-IDF stdlib hors-ligne + pont de synonymes FR→EN, catalogue.json
(180 skills). Top 3 affichés (le script en renvoie 5). Les 2 dernières
requêtes sont volontairement HORS PÉRIMÈTRE : scores ≈ 0 attendus —
le skill selecteur-framework doit alors le dire et renvoyer vers le
bon plugin, jamais forcer un framework.

## « je veux lancer un SaaS B2B pour restaurateurs »

- `scale-linkedin-ads-b2b` (score 0.4843, intermediaire) — prérequis manquants : `ideation-landing-page`, `ideation-persona-maker`
- `ideation-launch-plan` (score 0.2909, debutant) — prérequis manquants : `ideation-landing-page`, `ideation-launch-checklist`
- `scale-linkedin-pixel` (score 0.2557, intermediaire) — prérequis manquants : `ideation-landing-page`, `ideation-persona-maker`

## « comment je valide mon idée ? »

- `bootcamp-problem-validation` (score 0.3706, debutant) — prérequis manquants : `bootcamp-qualitative-study`
- `bootcamp-bmc-complete` (score 0.0, debutant) — prérequis manquants : `bootcamp-persona-deep`, `bootcamp-problem-validation`
- `bootcamp-brand-platform` (score 0.0, debutant)

## « aide-moi à structurer mes prix »

- `scale-pricing-strategy` (score 0.4216, expert) — prérequis manquants : `scale-unit-economics`
- `ideation-pricing-page` (score 0.4165, intermediaire) — prérequis manquants : `ideation-value-proposition`
- `ideation-course-outline` (score 0.2462, debutant)

## « préparer ma levée de fonds »

- `bootcamp-funding-strategy` (score 0.6158, debutant)
- `scale-fundraising-plan` (score 0.2975, expert) — prérequis manquants : `scale-unit-economics`, `scale-financial-projections`
- `scale-cap-table` (score 0.237, expert)

## « faire connaître mon produit sur LinkedIn »

- `ideation-linkedin-posts` (score 0.5307, debutant)
- `scale-linkedin-ads-b2b` (score 0.4775, intermediaire) — prérequis manquants : `ideation-landing-page`, `ideation-persona-maker`
- `scale-linkedin-pixel` (score 0.316, intermediaire) — prérequis manquants : `ideation-landing-page`, `ideation-persona-maker`

## « réduire mon churn et fidéliser mes clients »

- `scale-jtbd` (score 0.2791, intermediaire)
- `ideation-persona-maker` (score 0.2626, debutant)
- `scale-soncas` (score 0.2603, intermediaire)

## « répare mon imprimante »

- `bootcamp-bmc-complete` (score 0.0, debutant) — prérequis manquants : `bootcamp-persona-deep`, `bootcamp-problem-validation`
- `bootcamp-brand-platform` (score 0.0, debutant)
- `bootcamp-brand-storytelling` (score 0.0, debutant)
- ⚠️ meilleur score FAIBLE → hors périmètre, le sélecteur le dit (comportement attendu)

## « recette de cuisine pour ce soir »

- `bootcamp-bmc-complete` (score 0.0, debutant) — prérequis manquants : `bootcamp-persona-deep`, `bootcamp-problem-validation`
- `bootcamp-brand-platform` (score 0.0, debutant)
- `bootcamp-brand-storytelling` (score 0.0, debutant)
- ⚠️ meilleur score FAIBLE → hors périmètre, le sélecteur le dit (comportement attendu)

