---
name: haccp-conformite-quotidienne
description: Utiliser quand l'utilisateur parle de relevé de température, HACCP, contrôle réception, étiquette DLC, checklist hygiène, plan de nettoyage ou conformité du jour. Couvre la routine quotidienne de conformité sanitaire d'un restaurant.
---

# Conformité HACCP quotidienne

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
   règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).
2. S'assurer d'avoir l'`establishment_id`. S'il n'est pas connu dans la conversation,
   le demander à l'utilisateur AVANT tout appel d'outil. Tous les outils ci-dessous
   l'exigent.
3. Règle « Résolution des noms » (directives § 1 ter) : tout nom parlé ou
   écrit (produit, ingrédient, plat, équipement, table, recette) se résout
   via `search_entities` AVANT tout autre appel — fuzzy FR géré par le
   serveur (accents, pluriels) ; si `ambiguous=true`, présenter les
   candidats et DEMANDER confirmation avant d'agir. Jamais d'ID deviné.

## Workflow

1. **Relevés de température** — pour chaque équipement (frigo, congélateur…), appeler
   `add_temperature` (`establishment_id`, **`equipment_id` REQUIS**, `temperature` ;
   `measured_at` optionnel ISO 8601, défaut = maintenant).
   - NE JAMAIS inventer une température : chaque valeur doit être fournie par
     l'utilisateur. Si une valeur manque, la demander.
   - NE JAMAIS deviner l'`equipment_id` : le résoudre via `search_entities`
     (`types: ["equipment"]`) à partir du nom dicté (« frigo 3 ») — si
     `ambiguous=true`, demander confirmation avant d'enregistrer. Le hook
     anti-donnee-inventee refuse tout relevé sans `equipment_id`.
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
6. **Plan de nettoyage** — le contrôle du jour inclut désormais le nettoyage :
   - `list_cleaning_zones` (`establishment_id`) : zones et leurs POSTES de
     nettoyage — c'est le référentiel de ce qui est attendu ;
   - pour chaque poste que l'utilisateur CONFIRME avoir nettoyé,
     `record_cleaning_action` (`establishment_id`, `poste_nettoyage_id` — l'ID
     du POSTE, pas de la zone ; `statut` défaut `complete`, `commentaires`
     optionnel). Ne jamais enregistrer une action non confirmée ;
   - `list_cleaning_actions` (`establishment_id`, `date_from`/`date_to`) : le
     registre des actions réalisées, pour le contrôle et l'historique.

## KPI conformité du jour

Le contrôle du jour couvre désormais : températures + réceptions + DLC +
checklist hygiène + plan de nettoyage. KPI étendu : **actions de nettoyage
faites / attendues** (faites = `list_cleaning_actions` du jour ; attendues =
postes de `list_cleaning_zones`) — l'annoncer avec les non-conformités.

## Garde-fous

- Aucune valeur mesurée (température, réponse de checklist) ne doit être supposée ;
  aucune action de nettoyage enregistrée sans confirmation explicite.
- Toute non-conformité détectée (température hors seuil, livraison `non_conforme`,
  poste de nettoyage non fait) doit être signalée en fin de workflow avec une
  action corrective proposée.
- Terminer par un récapitulatif : relevés faits, non-conformités, réceptions,
  checklists validées, étiquettes créées, actions de nettoyage enregistrées
  (avec le ratio faites / attendues).
