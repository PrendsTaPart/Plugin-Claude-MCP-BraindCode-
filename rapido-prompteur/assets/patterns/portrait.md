# Pattern — Portrait / photo d'équipe

**Usage** : portrait pro (avatar, page équipe, presse), headshot.
**Média** : image.

## Pattern (à compléter aux [placeholders])

```
Portrait [plan : buste / épaules] de [personne / rôle], expression [posée /
souriante naturelle], regard [caméra / légèrement de côté]. Tenue [style],
arrière-plan [uni couleur charte [hex] / studio flou]. Lumière [portrait douce
en fenêtre / trois points], carnation naturelle, peau texturée (pas lissée).
Objectif [85 mm], faible profondeur de champ, netteté sur les yeux. Rendu
photoréaliste éditorial. Ratio et résolution : [valeurs lues en live].
```

## Négatif (déléguer)

Base commune + type « Portrait / équipe » de `rapidocms:prompts-visuels-pro`
(`asymmetric eyes, waxy skin, uncanny valley, …`).

## Moteurs compatibles

- **Higgsfield** modèles portrait/UGC (familles Soul / réalistes — **vérifier
  `models_explore type:image` en live** : certains prennent un `soul_id`).
- **RapidoCMS** `generate_image` ; `images_to_image` pour styliser une vraie photo.

## Rappels

- Le portrait d'une **personne réelle** part de sa **vraie photo** (asset/URL),
  jamais d'un visage inventé présenté comme la personne.
- Pas de « style de [photographe vivant] » — décrire la lumière et l'optique.

---
*Source : structures distillées de `rediumvex/ai-video-generator-claude` (MIT,
skill personal-brand / ai-avatar) et `Hao0321/ai-media-generator` (MIT) —
francisé, aucun texte verbatim. Voir `NOTICE.md`. Aucune IP tierce.*
