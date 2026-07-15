# Scoring des leads — pondérations éditables

> Modèle. Copié dans `./rapido-kb/marketing/scoring.md` à la première exécution
> du skill `lead-scoring`. Ajustez les poids à votre réalité ; le script
> `score_leads.py` lit ce modèle (aucun score calculé de tête).

## Modèle à 3 facteurs — fit × engagement × fraîcheur (poids par défaut à ajuster)

```json
{
  "fit": { "secteur_cible": 30, "taille_cible": 20, "region_cible": 10 },
  "engagement": { "form_submit": 20, "cta_click": 10, "rdv": 30, "email_open": 5 },
  "cap_engagement": 3,
  "intention": {
    "form_submit":        { "poids": 25, "validite_jours": 30 },
    "cta_click":          { "poids": 12, "validite_jours": 21 },
    "reponse_sequence":   { "poids": 30, "validite_jours": 30 },
    "mouvement_pipeline": { "poids": 20, "validite_jours": 45 },
    "levee_fonds":        { "poids": 25, "validite_jours": 90 },
    "recrutement":        { "poids": 15, "validite_jours": 60 },
    "changement_poste":   { "poids": 20, "validite_jours": 60 }
  },
  "seuils": { "chaud": 70, "tiede": 40 }
}
```

- **fit** = critères booléens (poids ajouté si vrai), issus de `icp.md`.
- **engagement** = compteurs (poids × min(compte, cap)) — porte le **volume**.
- **intention** = signaux datés (poids × **fraîcheur**), catalogue et validités
  dans `signaux.md` — porte la **fraîcheur** ; par type, seule l'occurrence la
  plus récente compte (pas de double compte avec l'engagement).
- **seuils** : `chaud` ≥ 70, `tiede` ≥ 40, sinon `froid` (à calibrer ; l'ajout de
  l'axe intention peut faire monter les totaux — recalibrer après une passe).
