# Pattern — Food (plat / boisson)

**Usage** : photo de plat appétissante (menu, réseaux resto, livraison).
**Média** : image. **Client type** : FoodEatUp.

## Pattern (à compléter aux [placeholders])

```
Photo culinaire de [plat] dressé dans/sur [contenant], garniture [détails].
Cadrage [vue de dessus 90° / trois-quarts 45°], composition [aérée],
[vapeur / fraîcheur] visible et crédible. Lumière naturelle douce [directionnelle,
côté fenêtre], ombres douces, couleurs fidèles et appétissantes. Arrière-plan
[table bois / surface unie couleur charte [hex]], accessoires discrets
([couverts / serviette]). Rendu photoréaliste, textures nettes. Espace négatif
pour texte menu. Ratio et résolution : [valeurs lues en live].
```

## Négatif (déléguer)

Base commune + type « Photo produit / plat » de `rapidocms:prompts-visuels-pro`
(`fake food, unappetizing, harsh shadows, dirty plate, steam overdone, …`).

## Moteurs compatibles

- **RapidoCMS** `generate_image` ; `images_to_image` sur une vraie photo de plat.
- **Higgsfield** modèles image (**`models_explore type:image` en live**).

## Rappels

- Le plat doit correspondre au **vrai menu** du client (données réelles).
- Vapeur/fraîcheur crédibles : trop de vapeur = artefact → l'exclure au négatif.

---
*Source : patterns distillés de `Hao0321/ai-media-generator` (MIT, references
food/commercial) — francisé, aucun texte verbatim. Voir `NOTICE.md`. Aucune IP tierce.*
