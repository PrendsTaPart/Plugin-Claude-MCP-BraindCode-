# Pattern — Packshot produit

**Usage** : photo produit propre pour fiche e-commerce, pub, réseaux.
**Média** : image.

## Pattern (à compléter aux [placeholders])

```
Packshot de [produit] posé sur [surface neutre / fond uni couleur charte [hex]],
[angle : trois-quarts / face / vue de dessus], cadrage [serré / avec marge].
Lumière studio douce [direction : latérale / en dôme], reflets maîtrisés,
ombre portée légère et nette. Rendu photoréaliste, netteté élevée, texture du
matériau visible ([matériau]). Fond [uni / dégradé subtil] laissant un
[espace négatif] pour le texte ajouté en post-production. Ratio et résolution :
[valeurs lues en live pour le modèle].
```

## Négatif (déléguer)

Base commune + type « Photo produit » de `rapidocms:prompts-visuels-pro`
(`plastic look, harsh shadows, messy background, …`).

## Moteurs compatibles

- **RapidoCMS** `generate_image` (size `hd`/`standard`) ; `images_to_image` pour
  partir d'un vrai visuel produit (URL publique < 5 Mo).
- **Higgsfield** modèles image (ex. familles Nano Banana / GPT Image — **vérifier
  `models_explore type:image` en live** pour options/ratios).

## Rappels

- Couleurs de charte en **hex**. Prévoir l'espace texte, ne pas incruster le prix.
- Le vrai produit doit venir d'une **URL/asset réel** (pas de produit inventé).

---
*Source : structures de prompt distillées de `Hao0321/ai-media-generator` (MIT) et
`ZeroLu/awesome-nanobanana-pro` (MIT) — francisé et réécrit, aucun texte verbatim.
Voir `NOTICE.md`. Aucune IP tierce.*
