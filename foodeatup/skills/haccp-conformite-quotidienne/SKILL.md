---
name: haccp-conformite-quotidienne
description: Utiliser quand l'utilisateur parle de relevé de température, HACCP, contrôle réception, étiquette DLC, checklist hygiène ou conformité du jour. Couvre la routine quotidienne de conformité sanitaire d'un restaurant.
---

# Conformité HACCP quotidienne

## Étape 0 — Établissement (obligatoire)

S'assurer d'avoir l'`establishment_id`. S'il n'est pas connu dans la conversation, le
demander à l'utilisateur AVANT tout appel d'outil. Tous les outils ci-dessous l'exigent.

## Workflow

1. **Relevés de température** — pour chaque équipement (frigo, congélateur…), appeler
   `add_temperature` (`establishment_id`, `equipment_id`, `temperature`, `measured_at`
   optionnel, défaut = maintenant).
   - NE JAMAIS inventer une température : chaque valeur doit être fournie par
     l'utilisateur. Si une valeur manque, la demander.
2. **Contrôle des non-conformités** — appeler `list_haccp_temperatures`
   (`establishment_id`, filtres optionnels `start_date`, `end_date`, `equipment_id`,
   `type`) et signaler explicitement toute valeur hors seuil à l'utilisateur.
   Seuils indicatifs : frigo 0–4 °C, congélateur ≤ −18 °C, liaison chaude ≥ 63 °C —
   utiliser les seuils propres à l'équipement s'ils sont connus.
3. **Réception de livraison (si livraison ce jour)** — appeler `create_haccp_reception`
   (`establishment_id`, `date_controle` YYYY-MM-DD, `heure_controle` HH:MM,
   `etat_livraison` = `conforme` | `non_conforme`).
   - Si `non_conforme` : renseigner impérativement `non_conformites` (liste).
   - Renseigner `temperature_produits_frais`, `fournisseur_id` ou `fournisseur_nom`,
     `reference_bl` quand l'information est disponible.
4. **Checklists hygiène** — lister les modèles avec `list_hygiene_checklists`
   (`establishment_id`), puis valider avec `create_hygiene_checklist_validation`
   (`establishment_id`, `template_id`, `reponses` clé/valeur, `zone_controle` et
   `commentaires` optionnels). Ne cocher que ce que l'utilisateur confirme.
5. **Étiquettes DLC** — pour chaque produit à étiqueter, appeler `create_haccp_label`
   (`establishment_id`, `ingredient_name` ; optionnels : `dlc`, `type` parmi
   Fait/ouvert, Prêt à manger, Surgelé, Frais, Vente — défaut Frais —, `quantity`,
   `unit`, `storage_location`, `temperature`).
   - Le numéro de lot (`lot_number`) est auto-généré si absent : ne pas en inventer un.

## Garde-fous

- Aucune valeur mesurée (température, réponse de checklist) ne doit être supposée.
- Toute non-conformité détectée (température hors seuil, livraison `non_conforme`)
  doit être signalée en fin de workflow avec une action corrective proposée.
- Terminer par un récapitulatif : relevés faits, non-conformités, réceptions,
  checklists validées, étiquettes créées.
