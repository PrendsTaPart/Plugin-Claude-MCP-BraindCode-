# Pattern — Personnage cohérent (mascotte / avatar de marque)

**Usage** : personnage original réutilisable (mascotte, avatar, héros de marque)
avec cohérence entre les rendus.
**Média** : image (base) → vidéo.

## Pattern (à compléter aux [placeholders])

```
Personnage ORIGINAL : [espèce / type], [traits distinctifs], tenue [couleurs
charte [hex]], expression [attitude]. Style [illustration / 3D / photoréaliste],
cohérent et reproductible. Pose [pose], cadrage [plan]. Fond [uni charte /
contextuel]. Feuille de référence : [vues face / profil / trois-quarts] pour
garantir la cohérence. Ratio et résolution : [valeurs lues en live].
```

## Cohérence entre rendus

- Réutiliser une **image de référence** du personnage validé (via `images_to_image`
  RapidoCMS, ou les mécanismes de personnage/référence du moteur).
- Chez **Higgsfield** : vérifier en live les modèles à identité/référence
  (`models_explore` + `show_characters` / `show_reference_elements`) — **ne rien
  supposer**, lire les rôles de médias acceptés.

## Moteurs compatibles

- **Higgsfield** (modèles à référence / personnage — **en live**).
- **RapidoCMS** `images_to_image` (référence = URL publique < 5 Mo, max 3).

## Rappels

- **Personnage 100 % original** : aucun trait repris d'un personnage sous licence
  (héros, mascotte de marque tierce), même « inspiré de ».

---
*Source : structures distillées de `rediumvex/ai-video-generator-claude` (MIT) et
`Hao0321/ai-media-generator` (MIT). Le concept « cohérence via référence » recoupe
`rapido-higgsfield:personnages-univers`. Francisé, aucun texte verbatim. Voir
`NOTICE.md`. Personnage original, aucune IP tierce.*
