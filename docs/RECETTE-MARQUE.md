# Recette de release — couche marque RapidoCMS

Date : 2026-07-14 · Plugins : `rapidocms` 1.11.0, `rapido-suite` 1.4.1 ·
Compte de test : company_id 321.

Cette recette valide la vague « couche marque » (brands, assets,
`images_to_image`) avant release. Elle distingue ce qui a été **vérifié en réel
via les outils MCP live** de ce qui relève d'une **session Claude Code
interactive** (commandes `/plugin`).

## 1. Install-readiness (structurel)

- `python3 scripts/valider-plugins.py` → **TOUT VALIDE** (12 plugins, 38 JSON,
  330 frontmatters).
- `python3 scripts/tester-skills.py` → **0 FAIL / 0 WARN / 0 INFO** (inclut les
  14 cas hooks de la couche marque + résolution des références
  `${CLAUDE_PLUGIN_ROOT}`).
- Slugs (`name`) inchangés et alignés sur `.claude-plugin/marketplace.json`.

> Note : les commandes interactives `/plugin marketplace add ./rapido-plugins`,
> `/plugin install rapidocms@rapido`, `/reload-plugins` s'exécutent dans une
> **session Claude Code interactive** (impossibles depuis cet environnement non
> interactif). La validation ci-dessus couvre la conformité structurelle que ces
> commandes vérifient au chargement (JSON, frontmatters, chemins de hooks/refs).

## 2. Scénarios déroulés EN RÉEL (MCP live)

### 2.1 Boucle corrective `images_to_image` ✅
- **Round 1** — `images_to_image(size=standard, images=<logo public>,
  prompt="bannière plate bleue, oiseau origami")`
  → `image_url.original.success = true`, rendu R1 =
  `…/ia_6a573c3f5841f0.67256066.jpg`.
- **Round 2 (correctif chirurgical)** — rendu R1 repassé **en 1re référence** +
  la référence d'origine, `prompt="corrige UNIQUEMENT le fond… ne change rien
  d'autre"`
  → `success = true`, rendu R2 = `…/ia_6a573c67623518.19039646.jpg`.
- **Verdict** : la mécanique de la boucle corrective de `studio-visuel-marque`
  fonctionne bout en bout ; format de réponse conforme
  (`image_url.original.content`) ; 2 références acceptées (≤ limite 3).

### 2.2 Blocage hook déterministe ✅
Exécution réelle des scripts avec payload stdin :
- `valide_charte_hook.py` + `create_brand couleurs="bleu"` → **deny** (exit 2,
  message pédagogique).
- `valide_charte_hook.py` + `images_to_image` **4 URLs** → **deny** (exit 2,
  « limite vérifiée est 3 »).
- `valide_charte_hook.py` + `create_brand couleurs="#0055FF,#FFFFFF"` →
  **allow** (exit 0).
- `garde-destructif.py` + `delete_brand` → **ask** (JSON `permissionDecision`).

### 2.3 Contrat des outils (rappel, vérifié en amont de l'audit)
- `create_brand` renvoie l'`id` (brand_id) ; `get_brand(nom)` renvoie un
  tableau avec `assets[]` ; `upload_file_tool` ne renvoie pas d'id (résolution
  via `list_all_files`) ; `add_asset` prend l'id du fichier, `remove_asset`
  l'id du LIEN ; couleurs non validées côté serveur (d'où le hook).

## 3. Effets de bord assumés
- Les 2 rendus `images_to_image` (R1, R2) restent dans la bibliothèque CMS :
  **aucun outil de suppression de fichier** n'existe (documenté dans
  `rapidocms/reference/outils-marque.md`). Renommables/retirables via l'UI CMS.

## 4. À dérouler en session interactive (non couvert ici)
Sur un poste avec Claude Code interactif, pour une recette 100 % bout en bout :
1. `/plugin marketplace add ./` (racine du dépôt = marketplace `rapido`) puis
   `/plugin install rapidocms@rapido` et `/reload-plugins`.
2. Rejouer les scénarios de `rapidocms/tests/evals.md` (§ « Recette couche
   marque ») en langage naturel, en vérifiant le routage et les confirmations.

## Verdict
**Recette OK** : install-readiness verte, boucle corrective `images_to_image`
et blocages hooks vérifiés en réel. Release autorisée.
