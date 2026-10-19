---
name: haccp-huiles-cycles-thermiques
description: Utiliser quand l'utilisateur parle d'huile de friture, de friteuse, de test de polaires, de filtration ou de changement d'huile, ou de refroidissement rapide, de cellule de refroidissement ou de remise en température d'un lot. Tient le carnet d'huile et les cycles thermiques HACCP (démarrage, relevés, clôture avec conformité calculée par le serveur).
---

# HACCP — huiles de friture et cycles thermiques

Complète `haccp-conformite-quotidienne` (températures des enceintes, réceptions,
DLC, nettoyage) sur deux registres que les contrôles sanitaires demandent :
le **carnet d'huile** et les **cycles de refroidissement / remise en température**.

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
   règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).
2. S'assurer d'avoir l'`establishment_id` (le demander si absent) avant tout appel.
3. Règle « Résolution des noms » (directives § 1 ter) : tout nom parlé ou
   écrit (produit, ingrédient, plat, équipement, table, recette) se résout
   via `search_entities` AVANT tout autre appel — si `ambiguous=true`,
   présenter les candidats et DEMANDER confirmation. Jamais d'ID deviné.

## 1. Carnet d'huile

1. **État des friteuses** — `list_fryers` (`establishment_id`) : friteuses
   actives et état de leur huile. Le point de départ de toute question
   « faut-il changer l'huile ? ».
2. **Test d'huile** — `add_oil_test` (`establishment_id`, `equipment_id` de la
   friteuse ; `method` ∈ `testeur` | `bandelette` | `visuel`) :
   - `testeur` / `bandelette` → `polar_pct` (composés polaires, mesure RÉELLE
     dictée par l'utilisateur) et `oil_temp` si connue ;
   - `visuel` → `visual_result` ∈ `acceptable` | `defavorable` | `indetermine`,
     **jamais de `polar_pct`** : un contrôle visuel ne mesure pas les polaires ;
   - au seuil critique, le serveur exige `corrective_action` : la demander à
     l'utilisateur (changement, filtration…), ne jamais l'inventer.
3. **Filtration** — `add_oil_filtration` : consigne l'acte ; elle **n'efface
   pas** une non-conformité relevée par un test précédent.
4. **Changement d'huile** — `add_oil_change` (`volume_l` et `oil_type` REQUIS,
   fournis par l'utilisateur).
5. **Historique** — `list_oil_logs` (`equipment_id` optionnel, 100 opérations
   par page, `offset`) : le carnet présenté au contrôleur.

`logged_at` (ISO 8601) seulement si l'acte n'a pas eu lieu maintenant ;
`request_key` = clé d'idempotence (rejouer un appel sans doublon).

## 2. Cycles de refroidissement / remise en température

1. **Démarrer** — `start_thermal_cycle` (`kind` ∈ `refroidissement` | `remise`,
   `product_name`, `lot_ref` UNIQUE, `quantity`, `unit`, `start_temp` à cœur
   MESURÉE). Relier quand c'est connu : `recipe_id`, `plat_id`,
   `production_plan_id` (production du jour), `equipment_id` (cellule),
   `parent_cycle_id` (remise d'un lot refroidi).
2. **Relevés** — `add_thermal_reading` (`cycle_id`, `temp` mesurée, `read_at`
   si différé) à chaque relevé dicté. Jamais de relevé interpolé.
3. **Clôturer** — `close_thermal_cycle` (`cycle_id`, `end_temp` mesurée,
   `destroyed` true/false). Le **serveur calcule la conformité** ; en cas
   d'écart il exige `corrective_action` (destruction du lot, réchauffage…) —
   décision de l'utilisateur, à annoncer clairement.
4. **Suivi** — `list_thermal_cycles` (`status` ∈ `en_cours` | `conforme` |
   `non_conforme` | `abandonne`) : signaler tout cycle `en_cours` oublié et
   tout `non_conforme`.

## Garde-fous

- **Aucune température, aucun % de polaires inventé** : chaque valeur vient
  d'une mesure dictée par l'utilisateur ; si elle manque, la demander.
- Une non-conformité n'est jamais « effacée » : filtration ou nouveau test se
  consignent EN PLUS, l'historique reste.
- `destroyed` et `corrective_action` = décision humaine, jamais posée d'office.
- Récapituler en fin de séquence : tests/filtrations/changements (IDs),
  cycles démarrés/clôturés (IDs + conformité rendue par le serveur).
