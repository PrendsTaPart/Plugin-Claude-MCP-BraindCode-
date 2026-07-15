# Budget média Higgsfield (KB client)

> Copié dans `./rapido-kb/budget-media.md` à la 1re exécution d'un skill du plugin.
> Le skill `gouvernance-credits` (H2) et le hook `garde-couts` lisent ce fichier.
> Ajuster aux crédits réels du workspace (voir `balance` / `show_plans_and_credits`).

## Plafond
- **Plafond mensuel** : (à renseigner) crédits.
- **Seuil de confirmation unitaire** : toute production estimée à plus de
  (à renseigner) crédits exige une confirmation explicite avant lancement.

## Compteur (tenu à jour après chaque production validée)
| Mois | Crédits consommés | Reste vs plafond |
|---|---|---|
| (à renseigner) | 0 | — |

## Règles rappelées
- `get_cost: true` en préflight : aucun chiffrage « de tête ».
- Au-dessus du seuil → confirmation ; au-dessus du plafond → **bloqué**.
- Voix (clonage/doublage) : droits/consentement obligatoires, indépendamment du coût.
