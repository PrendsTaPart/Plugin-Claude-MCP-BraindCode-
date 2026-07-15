# Scoring des leads — pondérations éditables

> Modèle. Copié dans `./rapido-kb/marketing/scoring.md` à la première exécution
> du skill `lead-scoring`. Ajustez les poids à votre réalité ; le script
> `score_leads.py` lit ce modèle (aucun score calculé de tête).

## Modèle à 2 axes (poids par défaut — à ajuster)

```json
{
  "fit": { "secteur_cible": 30, "taille_cible": 20, "region_cible": 10 },
  "engagement": { "form_submit": 20, "cta_click": 10, "rdv": 30, "email_open": 5 },
  "cap_engagement": 3,
  "seuils": { "chaud": 70, "tiede": 40 }
}
```

- **fit** = critères booléens (poids ajouté si vrai), issus de `icp.md`.
- **engagement** = compteurs (poids × min(compte, cap)).
- **seuils** : `chaud` ≥ 70, `tiede` ≥ 40, sinon `froid` (à calibrer).
