# Pattern — Cinématique (plan de film)

**Usage** : plan vidéo cinématographique (intro de marque, teaser, ambiance).
**Média** : vidéo (ou image « still » cinématique).

## Pattern (à compléter aux [placeholders])

```
Plan cinématique [large / serré] de [sujet] dans [décor]. Mouvement caméra
[dolly avant lent / travelling latéral / statique sur trépied]. Lumière
[clair-obscur / lumière naturelle rasante / néons], palette [couleurs charte
[hex] ou ambiance décrite]. Atmosphère [décrite : brume, poussière, contre-jour].
Optique [grand angle / anamorphique], profondeur de champ [faible]. Rythme :
[un temps fort à N s]. Rendu grain fin, contraste maîtrisé. Durée : [valeur ∈
plage du modèle lue en live]. Son : [ambiance].
```

> **INTERDIT** : ne jamais écrire « façon [réalisateur] » ni « style [film] ».
> Décrire **l'effet** (symétrie, palette, type de lumière, mouvement) — jamais
> l'auteur ni l'œuvre. Voir `reference/regles-de-construction.md` (INTERDITS) et le
> tableau de reformulation.

## Moteurs compatibles

- **Higgsfield** — modèles vidéo cinématiques (familles Cinema Studio — **vérifier
  `models_explore type:video` en live** : `genre`, `resolution`, `duration_range`,
  audio). Génération **payante** → préflight `get_cost`.

## Rappels

- Décor et sujet réels/cohérents avec la marque. Pas de lieu ni monument
  identifiable sous IP.

---
*Source : structures distillées de `Hao0321/ai-media-generator` (MIT, references
cinematic-direction / camera-language). La `director-style-library` (31
réalisateurs nommés) est **volontairement EXCLUE** — artistes vivants / styles
protégés (cf. `docs/IMPORTS-PROMPTEUR.md`). Francisé, aucun texte verbatim. Voir
`NOTICE.md`. Aucune IP tierce, aucun nom de réalisateur.*
