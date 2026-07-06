---
name: prospection-pipeline
description: Utiliser quand l'utilisateur veut prospecter, trouver des entreprises, ajouter au pipeline ou traiter un nouveau prospect. Choisit la bonne source de prospection, dédoublonne, puis alimente et fait avancer le pipeline.
---

# Prospection et pipeline

## Workflow

1. **Choisir la source de prospection** selon la demande :
   - Recherche géographique « métier + ville » → `prospecter_maps`
     (`speciality`, `city`) ;
   - Entreprise précise par nom ou SIRET → `prospecter_entreprise`
     (`nom` ou `siret`) ; pour une vérification SIRET seule :
     `rechercher_entreprise_siret` ;
   - Ciblage par code NAF / spécialité / date de création → `prospecter_prospect`
     (`code_naf`, `specialite`, `date`, `nom_societe`, `nombre` 1-100).
2. **Dédoublonner AVANT d'ajouter** : vérifier que le prospect n'existe pas déjà via
   `rechercher_prospects` (`q` recherche libre) et `search_entreprises` (`q`).
   Ne jamais créer de doublon dans le pipeline.
3. **Ajouter au pipeline** — `ajouter_prospect_pipeline` avec `entreprise_id` OU
   `contact_id` (pipeline par défaut si `pipeline_id` absent ; `etape_id` pour une
   étape précise).
4. **Assigner un responsable** — renseigner `responsable_id` dans
   `ajouter_prospect_pipeline` (retrouver l'ID via `list_commerciaux`). Si aucun
   responsable n'est indiqué, demander à l'utilisateur plutôt que d'assigner au hasard.
5. **Faire avancer les étapes** — `deplacer_prospect_etape` (`id` du prospect,
   `payload` avec l'étape cible). Consulter `get_pipeline` / `get_stats_pipeline`
   pour connaître les étapes existantes, et `get_historique_prospect` pour le
   contexte avant de déplacer.

## Garde-fous

- Enregistrer en masse (`enregistrer_tous_prospects`) uniquement sur demande
  explicite ; par défaut, passer par `enregistrer_prospect` au cas par cas après
  dédoublonnage.
- Ne jamais déplacer un prospect vers une étape sans confirmation de l'utilisateur
  sur l'étape cible.
- Terminer par un récapitulatif : prospects trouvés, doublons écartés, ajouts au
  pipeline, assignations.
