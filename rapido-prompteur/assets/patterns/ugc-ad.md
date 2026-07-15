# Pattern — UGC / pub authentique

**Usage** : vidéo (ou image) « créateur » authentique pour TikTok/Reels, pub produit.
**Média** : vidéo (ou image). 

## Pattern vidéo (à compléter aux [placeholders])

```
Vidéo verticale [9:16] façon UGC : [personne] filme [elle-même / le produit] à
[lieu du quotidien, lumière naturelle], parle face caméra de manière décontractée.
Elle dit : "[réplique courte, texte réel]". Démo : [geste produit], la caméra
[pousse légèrement / suit] sur [bénéfice montré]. Aspect téléphone tenu à la main,
légers mouvements, texture réaliste, pas de lumière de studio artificielle.
Espace pour sous-titres en haut. Rythme : [temps fort placé à N s]. Durée :
[valeur ∈ plage du modèle lue en live]. Son : [ambiance / voix].
```

## Moteurs compatibles

- **Higgsfield** — modèles vidéo UGC / Marketing Studio (**vérifier
  `models_explore type:video` en live** : hooks/settings, avatars, produits,
  `duration_range`). Génération **payante** → préflight `get_cost`.
- Assemblage / sous-titres : **`rapido-video:montage-express`** (libre).

## Rappels

- Réplique = **texte réel** (jamais inventé). Produit = **asset réel**.
- Pas de créateur nommé, pas de marque tierce dans le décor.

---
*Source : structures distillées de `rediumvex/ai-video-generator-claude` (MIT,
skills testimonial-story / ai-avatar) et `Hao0321/ai-media-generator` (MIT, UGC) —
francisé, aucun texte verbatim. Voir `NOTICE.md`. Aucune IP tierce.*
