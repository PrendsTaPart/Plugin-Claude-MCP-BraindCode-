# Changelog — plugin rapido-forge

## 1.1.3 — 2026-07-15 — pont forge → opérations

- **Pontage forge → opérationnel** : 12 skills forge gagnent une section **« Passer à
  l'opérationnel »** pointant vers le skill métier qui applique la méthode aux données
  réelles (`scale-soncas → rapidocrm:preparation-rdv`, `scale-funnel-aarrr →
  funnel-aarrr-reel`, `scale-referral-program → programme-ambassadeurs`,
  `scale-upsell-crosssell → expansion-clients`, etc.). Règle complète :
  `reference/pont-forge-operations.md` (racine). Aucun autre changement dans les skills.

## 1.1.2 — 2026-07-15

- **Patch croisé `rapido-prompteur`** : `ideation-lovable-prompt` renvoie vers
  `rapido-prompteur:prompt-lovable` pour la **version outillée** (brief branché
  marque `get_brand` + CRM mode B + critères testables). Déclencheurs distincts :
  ici = parcours idéation StartupsForge ; là = brief prêt à exécuter.

## 1.1.1 — 2026-07-14

- Enrichissement `scale-spin-selling` (SPIN, Rackham) : besoin implicite→explicite,
  les 4 issues d'entretien + l'Advance, bénéfice (FAB) recadré, articulation
  scale-bant-qualification. Ajouts seuls, contenu maison inchangé.
- Enrichissement `scale-blue-ocean` (Kim & Mauborgne) : Six Paths, 3 cercles de
  non-clients, Buyer Utility Map, séquence stratégique, caveats d'honnêteté.
  Distillation founder-playbook (MIT © 2026 AgentSeal), reformulé.

## 1.1.0 — 2026-07-10

- **Taxonomie** : chaque skill porte `tags` (1-3, taxonomie FERMÉE à 12 :
  strategie, marketing, vente, produit, finance, juridique, marque,
  contenu, acquisition, data, organisation, pitch) et `niveau`
  (debutant / intermediaire / expert) — script idempotent
  `scripts/forge_enrichir_frontmatter.py` (racine du dépôt).
- **Prérequis** : 35 skills avec `prerequis:` (règles du brief + chaînage
  J1→J2 du bootcamp + analyse) — graphe VALIDÉ sans cycle (tri
  topologique) par `scripts/forge_catalogue.py`, rejoué en CI.
- **`reference/catalogue.json`** : l'index machine-readable des 180
  exercices (name, parcours, jour, description, tags, niveau, prerequis,
  voir_aussi, livrable_path) consommé par les agents et la recherche.
- **Recherche sémantique hors-ligne** : `scripts/forge_recherche.py`
  (TF-IDF stdlib + pont de synonymes FR→EN, filtres tags/niveau/parcours,
  prérequis manquants lus depuis le journal client ; `--embeddings`
  optionnel à repli silencieux) + **nouveau skill `selecteur-framework`**
  (3 propositions max, prérequis d'abord, hors-périmètre annoncé).
- **Agents branchés sur le catalogue** : recommandation = recherche +
  filtre niveau + vérification des prérequis contre le journal (jamais un
  skill aux prérequis non faits recommandé directement) ; les mentors
  annoncent le niveau et proposent de sauter les debutant quand la KB
  montre un niveau supérieur. `reference/parcours.md` § Catalogue &
  recherche (convention `- [x] <skill> — <date> — <verdict>`).
- Côté rapido-suite (1.2.0) : orchestrateur `lancement-projet-360` —
  Forge pense, les plugins exécutent, validation entre les 5 actes.
- tests : rapport-recherche.md (8 requêtes dont 2 hors périmètre) +
  13 cas (6 sélecteur, 4 prérequis, 3 niveau).

## 1.0.0 — 2026-07-10

- Version initiale : 180 exercices d'incubateur StartupsForge
  (PrendsTaPart) mis aux conventions du marketplace rapido, en 3 parcours —
  bootcamp 5 jours (46 skills `bootcamp-*`, enrichis d'une méthode pas à
  pas), roadmap idéation (72 skills `ideation-*`), roadmap scale (62 skills
  `scale-*`).
- 4 agents : `directeur-programme` (diagnostic de maturité + routage vers
  le bon parcours), `mentor-bootcamp`, `mentor-ideation`, `mentor-scale`.
- `reference/parcours.md` : cartographie des 3 parcours et du journal.
- Livrables TOUJOURS dans `./rapido-kb/startup/forge/` (journal :
  `parcours.md`) — hook garde-ecriture-kb en filet ; exécution réelle
  déléguée aux plugins métier (~146 renvois croisés vérifiés, 2 corrigés :
  `design:*` → `rapido-lovable:frontend-design` / `rapidocrm:mom-test`).
- `.mcp.json` : rapidocrm, rapidocms, rapidorh (les serveurs que les
  skills nomment pour les données réelles, lecture d'abord).
- Hook rappel « argent réel » sur les outils Meta Ads engageant une
  dépense (création en PAUSED, activation après accord explicite).
