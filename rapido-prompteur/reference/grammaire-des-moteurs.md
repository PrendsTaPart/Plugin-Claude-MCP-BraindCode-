# Grammaire des moteurs — la RÈGLE D'OR

> **L'agent ne mémorise JAMAIS les paramètres d'un moteur.** Les modèles, leurs
> résolutions, ratios, durées, options et limites **changent sans préavis**. Un
> prompt bâti « de mémoire » sur des specs obsolètes échoue ou coûte des crédits
> pour rien. **On LIT la grammaire du moteur cible à chaque session, en direct,
> AVANT d'écrire le prompt.** Aucune spec n'est recopiée en dur dans un skill.

## La règle, noir sur blanc

1. **Identifier le média et le moteur cible** (image / vidéo / audio / 3D / web / design).
2. **LIRE la grammaire du moteur en direct** — voir le tableau ci-dessous. La
   lecture est **gratuite** (aucun crédit) et **fait autorité** sur toute
   mémoire ou tout exemple de ce dépôt.
3. **Vérifier les pièges du plugin concerné** (`reference/pieges-outils.md`) —
   fautes serveur, formats d'ID, contraintes non évidentes.
4. **Composer le prompt** avec les valeurs réellement disponibles (options,
   ratios, durées lues à l'étape 2), jamais des valeurs supposées.
5. En cas de doute sur « quel modèle », demander une **recommandation** au moteur
   lui-même (`models_explore` action `recommend`) plutôt que trancher de mémoire.

> **Si la lecture live n'a pas eu lieu ce tour, le prompt n'est pas prêt.** Le
> hook `Stop` du plugin le vérifie et réclame le récapitulatif (moteur + grammaire
> lue + prompt affiché).

## Tableau moteur → où lire ses contraintes (en direct)

| Moteur / surface | Média | Où lire la grammaire, en direct | Ce qu'on y lit | Coût |
|---|---|---|---|---|
| **Higgsfield** (serveur `huggsfield`) | image / vidéo / audio / 3D | `models_explore` — `action:'list'` (ou `search`/`get`) **filtré par `type`** (`image`, `video`, `audio`, `3d`) | par modèle : `parameters` (options/min/max), `aspect_ratios`, `durations`/`duration_range`, `medias` acceptés, `tags` | **0 crédit** |
| **Higgsfield** — choix du modèle | tous | `models_explore` — `action:'recommend'` (goal + input) | modèles recommandés pour l'objectif | **0 crédit** |
| **Higgsfield** — pièges & coûts | tous | `rapido-higgsfield/reference/pieges-outils.md` ; grille `docs/GRILLE-COUTS-HIGGSFIELD.md` ; skill `gouvernance-credits` | params dans `params`, `get_cost` préflight, coûts en crédits | 0 (lecture) |
| **RapidoCMS** (serveur `RapidoCMS`) | image | pièges `rapidocms/reference/pieges-outils.md` ; charte via `get_brand` (param `nom`) | `generate_image(prompt,size∈{hd,standard})` ; **`images_to_image`** : `images` = **URLs publiques en chaîne séparées par virgules, < 5 Mo chacune, 1 à 3 URLs**, `size∈{hd,standard}` | 0 (lecture) ; génération payante |
| **Lovable** (mode B — usine-à-landing) | web / app | doc Lovable (instructions serveur `Lovable`) ; skill `rapido-forge:ideation-lovable-prompt` ; contraintes usine-à-landing du client | stack par défaut, `create_project(initial_message)` / `send_message` (langue naturelle), `plan_mode`, connecteurs | 0 (lecture) ; build = crédits workspace |
| **Canva** (serveur `Canva`) | design | doc Canva (instructions serveur) ; `list-brand-kits` ; `get-export-formats` | grammaire `generate-design` / `generate-design-structured`, kits de marque, formats d'export | 0 (lecture) |

### Notes de lecture (rappels, PAS des specs à mémoriser)

- **Higgsfield** : les paramètres d'un `generate_*` passent **dans l'objet `params`**
  (prompt, medias, options du modèle). La liste des modèles évolue — toujours
  relire `models_explore`. Préflight coût = `get_cost` avant de facturer.
- **RapidoCMS `images_to_image`** : le champ `images` est une **chaîne d'URLs
  publiques** (pas un tableau, pas de fichier local), **< 5 Mo** chacune, **max 3**
  (au-delà, le serveur rejette — mesuré). Fichiers locaux → `upload_file_tool`
  d'abord pour obtenir une URL publique.
- **Lovable** : décrire l'app en **langage naturel** ; les préférences de stack
  se donnent dans le message initial (pas de sélecteur). `plan_mode=true` pour
  cadrer avant que l'agent Lovable n'écrive du code.
- **Canva** : partir d'un **brand kit** (`list-brand-kits`) et d'un **format
  d'export** réel (`get-export-formats`) plutôt que de supposer des dimensions.

## Pourquoi cette règle existe (rappel de l'audit)

L'audit d'imports (`docs/IMPORTS-PROMPTEUR.md`) a montré que les catalogues de
modèles (Nano Banana, Soul, Cinema Studio, Marketing Studio, …) et leurs options
(résolutions 1k/2k/4k, ratios, durées) **diffèrent par modèle et bougent**. La
seule source fiable est la lecture live du moteur. Ce dépôt fournit des
**patterns** (structures de prompt) et des **usages**, jamais un catalogue de
specs figé.
