# Pattern — Hooks viraux (accroche 0-2 s)

**Usage** : concevoir l'accroche d'une vidéo courte (TikTok/Reels/Shorts) pour
maximiser la rétention dès les 2 premières secondes.
**Média** : vidéo (accroche) + prompt.

## Grille du hook (à compléter aux [placeholders])

```
Ouverture [9:16], durée totale [valeur ∈ plage du modèle lue en live].
- 0-2 s : [pattern interrupt visuel — mouvement, changement, question à l'écran]
  → "[accroche texte réelle, courte]".
- 2-5 s : [confirmation du hook : bénéfice / tension] .
- 5-15 s : [temps forts / révélation / preuve].
Sous-titres lisibles en haut. Rythme : coupe nette à [N s]. Son : [trending /
voix]. Sujet : [sujet], décor : [décor].
```

## Où va l'analyse virale (pas de doublon)

Le **diagnostic viral** (score de rétention, force du hook, risques) reste dans
**`rapido-higgsfield:analyse-video-virale`** (et `virality_predictor` côté moteur).
Ce pattern **cadre l'écriture** du hook ; il ne refait pas l'analyse.

## Moteurs compatibles

- **Higgsfield** modèles vidéo courts / Marketing Studio / Personal Clipper
  (**`models_explore type:video` en live**). Génération **payante**.
- Sous-titres / coupe : **`rapido-video:montage-express`** (libre).

## Rappels

- Accroche = **texte réel**, promesse tenue par la suite de la vidéo.
- Pas de son sous copyright non autorisé (droits musique — cf. `rapido-video`).

---
*Source : structures distillées de `rediumvex/ai-video-generator-claude` (MIT,
skill viral-hook : budget temporel 0-2 / 2-5 / 5-15 s) — francisé, aucun texte
verbatim. Voir `NOTICE.md`. Aucune IP tierce.*
