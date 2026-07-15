---
name: prompt-image
description: >-
  Utiliser quand l'utilisateur veut un PROMPT d'image (pas l'image elle-même) — « prompt
  image », « prompt pour une photo de… », « prompt packshot », « prompt portrait »,
  « prompt visuel de marque ». Construit un prompt image STRUCTURÉ (sujet, style charte,
  composition, négatifs) à partir des patterns maison, lit la charte et les moteurs
  disponibles, propose des variantes + critique, puis ROUTE vers le bon moteur. Le
  prompteur prompte, il ne génère pas. Pour générer : rapidocms:prompt-engineering-visuel
  (CMS) ou rapido-higgsfield:studio-image-pro (premium). Pour un prompt vidéo : prompt-video.
---

# Prompt image — directeur multi-moteurs

Ce skill **écrit le prompt** image et **route** vers le moteur ; il **ne génère jamais**
lui-même (« le prompteur prompte, il ne dépense pas »). `rapidocms:prompt-engineering-visuel`
= la **méthode CMS** d'un moteur ; **ici** = le **directeur** qui structure et arbitre
entre moteurs.

## Étape 0 — charte, moteurs, garde-fous (obligatoire)

- **Charte** : `get_brand` (couleurs hex, police, logo) + `./rapido-kb/charte-graphique.md`.
  Manque → le signaler (« à confirmer côté backend Tunis »), ne rien inventer.
- `${CLAUDE_PLUGIN_ROOT}/reference/grammaire-des-moteurs.md` (grammaire par moteur),
  `reference/regles-de-construction.md`, `reference/ip-a-risque.md` (jamais d'IP tierce ni
  d'artiste vivant nommé dans le prompt).
- **Moteurs disponibles lus en direct** côté Higgsfield (via `rapido-higgsfield:studio-image-pro`,
  qui interroge le catalogue de modèles) — choisir selon le besoin, pas de modèle en dur.

## 1. Brief → prompt structuré

À partir du besoin, choisir le **pattern** (`${CLAUDE_PLUGIN_ROOT}/assets/patterns/` :
packshot, food, portrait, cinematique) et construire les blocs :
- **Sujet** (quoi, cadrage) ; **style** = **charte** (couleurs, ambiance, ton de la marque) ;
- **composition** (lumière, angle, focale, arrière-plan) ; **négatifs** (ce qu'on exclut).
Aucune marque/franchise/artiste vivant (`ip-a-risque.md`).

## 2. Variantes + critique

2-3 variantes du prompt (angle, ambiance), puis **critique** courte (laquelle sert le
mieux l'intention, laquelle risque le hors-charte). L'utilisateur tranche.

## 3. Router vers le moteur (générer = déléguer)

| Besoin | Route (le prompteur ne génère pas) |
|---|---|
| Visuel de marque / réseaux (CMS) | `rapidocms:prompt-engineering-visuel` puis `generate_image` / `images_to_image` |
| Packshot / portrait **premium 4K** (Higgsfield) | `rapido-higgsfield:studio-image-pro` |
| Personnage cohérent récurrent | `prompt-personnage` |

Toute génération payante passe par le **préflight coût** du skill exécutant
(`rapido-higgsfield:gouvernance-credits`) — jamais de dépense décidée ici.

## 4. Capitaliser

Prompt qui a bien marché → `rapidocms:bibliotheque-prompts` (`add_prompt`) pour
réutilisation. Boucle d'amélioration : `reference/boucle-apprentissage.md`.

## Articulation (pas de doublon)

| Skill | Rôle |
|---|---|
| **`prompt-image`** (ici) | **écrit le prompt** image + arbitre le moteur (directeur multi-moteurs) |
| `rapidocms:prompt-engineering-visuel` | méthode de prompt **côté CMS** (un moteur) |
| `rapido-higgsfield:studio-image-pro` | **exécute** la génération premium (coût confirmé) |

## Sources

Patterns francisés (`assets/patterns/`) distillés de dépôts **MIT** (Hao0321, ZeroLu) —
**structures uniquement**, aucun texte ni IP tierce (cf. `NOTICE.md`).

## Pièges

- **Ne jamais générer ici** : ce skill produit un prompt et route ; la dépense appartient
  au moteur (préflight coût).
- **Charte avant tout** : réécrire un prompt hors-charte coûte plus cher après coup.
- **Zéro IP tierce / artiste vivant** dans le prompt (`ip-a-risque.md`).
