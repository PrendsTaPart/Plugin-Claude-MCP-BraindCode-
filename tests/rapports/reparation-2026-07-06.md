# Rapport de clôture — réparation du rapport tester-skills.py (2026-07-06)

## Avant / après

| Compteur | Avant | Après |
|---|---|---|
| FAIL | 3 | **0** |
| WARN | 153 | **0** |
| INFO (outils à catalogue distant, à vérifier en ligne) | — | **67** (checklist : `outils-a-verifier-en-ligne.md`) |

`python3 scripts/tester-skills.py` sort désormais en code 0 ; le détail des
INFO s'affiche avec `--verbose`.

## Corrections par famille

### 1. Chartes graphiques de repli (3 FAIL → 0)

Un repli ne doit pas contenir de placeholders : les 3
`reference/charte-graphique.md` (rapidocms, rapidocrm, rapido-suite) reçoivent
des valeurs génériques neutres IDENTIQUES (primaire `#1E293B`, secondaire
`#64748B`, accent `#3B82F6`, fonds `#F8FAFC`/`#0F172A` ; Inter/system-ui ;
aucun logo par défaut — `get_brand` ou demander) et un avertissement encadré
en tête : charte de repli, ordre réel `./rapido-kb/charte-graphique.md` →
`get_brand` → ce fichier, usage à SIGNALER dans la réponse.

### 2. Câblage MCP réel (~30 WARN → 0)

- **foodeatup/.mcp.json** : serveur `rapidocrm` déclaré (les 3 skills
  small-business — handle-complaint, margin-analyzer, price-check — supposent
  un CRM) + bandeau « Nécessite les MCP foodeatup ET rapidocrm » dans chacun.
- **rapido-suite/.mcp.json** : `lovable` et `facebook-ads` déclarés (les
  revues agrègent tout le business) — les sections des skills étaient déjà
  optionnelles (« sinon sauter en le mentionnant »).
- **rapido-meta-ads/.mcp.json** : `foodeatup` déclaré (audiences-crm construit
  les audiences depuis les clients du restaurant) ; passage précisé
  « `list_clients` (FoodEatUp) ».
- **Noms d'outils corrigés** :
  - supports-commerciaux (rapido-canva) : `get_devis` → `list_devis`.
    Nota : le `get_quote` suggéré n'existe que côté FoodEatUp — aucun outil de
    lecture unitaire de devis dans le catalogue rapidocrm.
  - visuels-sociaux-canva : `update_fill` (inexistant) → flux réel
    `start-editing-transaction` → `perform-editing-operations` →
    `commit-editing-transaction`.
  - margin-analyzer : `list_transactions` (PayPal) → `list_orders`
    (FoodEatUp) / `get_revenue_summary` (RapidoCRM).
  - devis-facture-relance : la mention d'`update_invoice_status` était déjà
    correcte (le passage dit qu'AUCUN outil de ce type n'existe côté CRM —
    il n'existe que côté FoodEatUp) : reformulée pour ne plus ressembler à une
    référence d'outil du plugin.
- **Découplage** : campagne-marketing (rapidocrm) renvoie le volet réseaux
  sociaux au plugin rapidocms (skill orchestration-campagne) au lieu de citer
  `add_post_campagne` ; studio-creatif (rapido-canva) renvoie la vérification
  des crédits Lovable au plugin rapido-lovable.
- **skill-creator (rapido-suite)** : `build_chart.py` / `create_docx.py`
  absents de la source (vérifié sur un clone frais d'anthropics/skills) —
  c'étaient des noms d'EXEMPLE dans la prose : reformulés en description
  générique, noté dans ATTRIBUTIONS.md.

### 3. Descriptions tierces francisées (~40 WARN → 0)

Les 40 skills tiers des 8 plugins concernés ont leur `description` de
frontmatter réécrite en français « Utiliser quand… » (déclenchement pour des
utilisateurs francophones), fidèle au contenu, avec une clé `source:` de
traçabilité (dépôt, commit, licence). Le CORPS de chaque skill reste
l'original attribué. Note ajoutée dans chaque ATTRIBUTIONS.md. Le test
« Utiliser quand » du testeur est redevenu BLOQUANT pour tous les skills.

Cas particuliers :
- `made-to-stick` : les `Lorem ipsum` du corps sont des exemples pédagogiques
  entre guillemets — le testeur ignore désormais les motifs cités entre
  guillemets droits (comme il ignorait déjà backticks et blocs de code).
- `business-pulse/reference/thresholds.md` : les 3 `TODO` remplacés par des
  seuils par défaut documentés « (défaut secteur — personnalisable dans
  ./rapido-kb/) ».

### 4. Whitelist des catalogues distants (67 WARN → 67 INFO)

`SERVEURS_CATALOGUE_DISTANT` ajouté au testeur (facebook-ads, n8n, gmail,
google-calendar, google-drive, canva, lovable, hyperframes) : un outil
attribuable à l'un d'eux passe en **INFO** (compté séparément, détail via
`--verbose`), plus en WARN. La vérification en ligne — le seul test
inautomatisable hors-ligne — est tracée dans
`tests/rapports/outils-a-verifier-en-ligne.md` (67 citations, cases à cocher
par serveur candidat, à valider MCP connectés avant release).

## Les 2 décisions prises

1. **Chartes de repli génériques** : le repli est utilisable tel quel (palette
   neutre documentée « ne représente aucune marque », usage signalé), la
   personnalisation vit dans `./rapido-kb/` et `get_brand` — plus aucun
   placeholder dans le produit.
2. **Descriptions tierces francisées** : la description (mécanisme de
   déclenchement) est traduite au format maison ; le corps attribué reste
   intact — l'attribution reste honnête (LICENSE par dossier + ATTRIBUTIONS.md
   + clé `source:`).

## Ce qui était déjà sain (inchangé)

- HOOKS : 10/10 plugins OK — les 8 gardes passent leurs tests fonctionnels
  stdin (ask/deny/allow).
- Aucun FAIL sur les skills maison : les 3 FAIL et l'essentiel des WARN
  venaient des chartes de repli et de l'intégration des skills tiers.
