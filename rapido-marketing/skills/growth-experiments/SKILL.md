---
name: growth-experiments
description: Utiliser quand l'utilisateur veut des expériences de croissance, un A/B test, un backlog growth, ou faire du CRO. Priorise les hypothèses par score ICE, définit un protocole d'expérience rigoureux, délègue l'exécution, lit les résultats par script et rend un verdict PASS/FAIL/INCONCLUSIF.
---

# Growth experiments — backlog ICE, protocole, verdict chiffré

## Étape 0 — Charger (obligatoire)
- `${CLAUDE_PLUGIN_ROOT}/reference/priorite-mcp.md` et `garde-fous-marketing.md`.
- `./rapido-kb/marketing/` (`benchmarks.md`, `apprentissages.md`) si présents.

## Méthode

### 1. Backlog scoré ICE
Rassembler les hypothèses (impact, confidence, ease notés 1-10) →
`python3 "${CLAUDE_PLUGIN_ROOT}/skills/growth-experiments/scripts/ice_score.py"`
avec `{"hypotheses": [{nom, impact, confidence, ease}]}` → backlog **trié**
(jamais priorisé de tête).

### 2. Protocole par expérience (avant de lancer)
Pour chaque test : **hypothèse** (« si… alors… parce que… »), **métrique**
unique, **taille d'échantillon minimale**, **durée**, **critère d'arrêt**.
Un test sans protocole écrit ne se lance pas.

### 3. Exécution (déléguée au bon skill)
- **Pub** → skill `tests-ab-meta` (rapido-meta-ads).
- **Landing** → variantes via `create_editor_template` (rapidocrm) ou skill
  `usine-a-landing` (Lovable).
- **Objet / email** → variantes via skill `email-sequence`.
- Toute activation/envoi **confirmé** (hook `garde-envois`).

### 4. Lecture des résultats (jamais de tête)
`python3 "${CLAUDE_PLUGIN_ROOT}/skills/growth-experiments/scripts/ab_result.py"`
avec `{"controle": {n, conversions}, "variante": {n, conversions},
"seuil_min_echantillon": …}` → taux, uplift, z, **verdict PASS / FAIL /
INCONCLUSIF** (test z à deux proportions). Un échantillon insuffisant =
**INCONCLUSIF**, jamais « ça marche ».

### 5. Capitaliser
Leçon datée → `./rapido-kb/marketing/apprentissages.md` (via `mise-a-jour-kb`).

## Livrable type
Backlog priorisé ICE + protocole de l'expérience en cours + verdict chiffré du
dernier test + prochaine hypothèse à tester.

## Cas d'usage croisés
- Outillage A/B (méthode statistique, MDE) → skill `scale-ab-testing`.
- Cartes de chaleur / enregistrements de session (CRO) → skill `scale-heatmaps`.
- Mesurer le goulot d'un tunnel avant de tester → skill `tunnel-de-vente-360`.

## Garde-fous
Priorisation et verdict **par script** ; protocole écrit avant tout test ;
INCONCLUSIF assumé si échantillon insuffisant ; envois/activations confirmés ;
leçons datées.
