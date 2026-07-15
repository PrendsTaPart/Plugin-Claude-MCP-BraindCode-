---
name: onboarding-restaurateur
description: Utiliser quand un nouveau client restaurateur démarre sur FoodEatUp, ou quand l'utilisateur dit « installe mon restaurant », « configure mon établissement », « on démarre de zéro », « importe ma carte et mon équipe ». Met en place l'établissement de bout en bout — carte, zones et tables, équipe, premier relevé HACCP — avec confirmation par étape.
---

# Onboarding restaurateur (mise en place complète)

## Étape 0 — Références et établissement (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
   règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).
2. **Établissement** : il n'existe PAS d'outil MCP de création d'établissement —
   l'établissement naît à l'inscription au compte FoodEatUp. Récupérer
   l'`establishment_id` du client (le demander ; s'il n'a pas encore de compte,
   le guider vers l'inscription FoodEatUp dans son interface, puis reprendre ici).
   Aucun autre appel avant d'avoir cet ID.
3. Si `./rapido-kb/` existe : lire `entreprise.md` (horaires, fuseau) et
   `produits-services.md` (la carte y est peut-être déjà décrite) — ne pas
   redemander ce que la KB sait. Proposer d'ailleurs l'onboarding entreprise
   (`onboarding-entreprise`, plugin rapido-suite) en complément si la KB est vide.

## Principe

Une mise en place = 4 chantiers, DANS L'ORDRE (la salle a besoin des zones, le
relevé HACCP a besoin que l'établissement vive). Une confirmation PAR chantier
avant d'écrire — jamais les 4 sur un seul accord.

## Workflow

1. **La carte (import en un appel)** — collecter la carte du client :
   catégories (2 niveaux max), plats avec `name`, `description`, `price`, et
   formules éventuelles (sections > groupes + notes de conditions).
   - Vérifier l'existant d'abord : `list_dishes` + `list_categories` —
     `import_storefront_menu` est IDEMPOTENT sur les NOMS (reprendre les noms
     exacts, sinon doublons).
   - Faire valider l'arborescence complète (catégories + plats + prix +
     formules), puis UN SEUL appel : `import_storefront_menu`
     (`establishment_id`, `categories`, `formules`).
   - Prix STRICTEMENT fournis par le client — aucun prix inventé ni « estimé ».
2. **La salle (zones puis tables)** — demander le plan de salle (zones : salle,
   terrasse, bar… ; nombre de tables et couverts par zone) :
   - `create_zone` pour chaque zone (vérifier `list_zones` avant — pas de
     doublon) ;
   - `create_table` pour chaque table, rattachée à sa zone ; contrôler le
     résultat avec `list_tables` puis `floor_plan_status` (toutes les tables
     doivent apparaître en `free`).
3. **L'équipe** — pour chaque employé : `create_employee` (identité, poste,
   coordonnées fournies par le client — `list_employees` d'abord pour éviter
   les doublons). Contrat si demandé : `create_employee_contract`. Les
   plannings viennent APRÈS l'onboarding (skill `planning-equipe`).
4. **Premier relevé HACCP (le geste fondateur)** — expliquer au client que la
   conformité commence au jour 1 :
   - identifier les équipements froids (frigos, congélateurs) : leurs
     `equipment_id` viennent de l'interface FoodEatUp ou d'un relevé
     existant (`list_haccp_temperatures`) — les demander s'ils sont inconnus,
     ne JAMAIS les deviner ;
   - GARDE-FOU ANTI-DONNÉE-INVENTÉE : chaque température est LUE par le client
     sur son thermomètre et dictée — jamais supposée, jamais « typique ». (Le
     hook du plugin refusera de toute façon toute valeur hors -30 °C / +90 °C.)
   - `add_temperature` par équipement (`establishment_id`, `equipment_id`,
     `temperature`) ; signaler immédiatement toute valeur hors seuil (frigo
     0-4 °C, congélateur ≤ -18 °C) ;
   - présenter les checklists disponibles (`list_hygiene_checklists`) et
     proposer la première validation (`create_hygiene_checklist_validation`).
5. **Tour du propriétaire (vérification finale)** — dérouler une lecture de
   contrôle : `list_dishes` (carte en ligne), `floor_plan_status` (salle),
   `list_employees` (équipe), `list_haccp_temperatures` (premier relevé). Puis
   passer le relais aux routines : `briefing-du-jour` chaque matin,
   `haccp-conformite-quotidienne`, `service-salle` pour les premières
   réservations.

## Garde-fous

- Une confirmation PAR chantier (carte, salle, équipe, HACCP) — récapituler ce
  qui va être créé avant chaque vague d'appels.
- Rien d'inventé : prix, noms de plats, zones, identités d'employés,
  températures et `equipment_id` viennent du client ou de la KB.
- Import de carte : les noms exacts font foi (idempotence) ; un deuxième
  passage corrige, il ne duplique pas — mais seulement si les noms matchent.
- Récapitulatif final par chantier avec les IDs créés (catégories, plats,
  zones, tables, employés, relevés) — exigé aussi par le hook de fin de tour.

## Taux de TVA (ajout SYNC S1)

Configurer les taux à l'installation : `create_tva` (`name`, `percentage`), `list_tva`.
