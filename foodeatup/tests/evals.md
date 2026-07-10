# Évals — plugin foodeatup (1.3.0)

Scénarios de déclenchement et de comportement. À rejouer manuellement (ou
via un futur harnais) : la phrase utilisateur doit router vers le skill
attendu et le comportement décrit doit être observé.

## Ajouts 1.3.0 — résolution des noms (search_entities, règle § 1 ter)

### E12 — Nom exact : résolution directe

- **Phrase** : « Planifie 20 tartares de saumon pour demain. »
- **Attendu** : `search_entities` (`query: "tartare de saumon"`,
  `types: ["dish", "recipe"]`) AVANT `create_production_plan` ; réponse non
  ambiguë → l'ID est utilisé directement (annoncé : « Tartare de saumon,
  plat #42 »), sans question inutile.

### E13 — Nom approximatif : le fuzzy serveur travaille

- **Phrase** : « Relevé des frigos : 3 °C. »
- **Attendu** : `search_entities` (`query: "frigo"` ou le nom tel que dicté,
  `types: ["equipment"]`) — le nom est passé TEL QUE DICTÉ (accents,
  pluriels gérés par le serveur, pas de « correction » locale) ; la liste
  des équipements correspondants est présentée et un relevé est enregistré
  PAR équipement confirmé, jamais un relevé global.

### E14 — Ambigu : confirmation exigée

- **Phrase** : « Passe le burger en prêt. »
- **Contexte** : `search_entities` renvoie `ambiguous=true` avec 2
  candidats (« Burger maison », « Burger végé »).
- **Attendu** : les 2 candidats sont PRÉSENTÉS et la confirmation est
  DEMANDÉE avant tout appel d'écriture — jamais de choix silencieux,
  jamais d'ID deviné (règle § 1 ter des directives).

## Ajouts 1.2.0 — briefing-du-jour + non-régression

### E9 — Notifications en tête

- **Phrase** : « Mon briefing du matin. »
- **Attendu** : `list_notifications` appelé en premier, non lues filtrées
  CÔTÉ RÉPONSE (pas de paramètre serveur), bloc 🔔 en tête de la page ;
  salle via `floor_plan_status` (UN appel) ; créneaux midi sondés par
  `reservation_availability` (12:00 / 12:30 / 13:00, un appel par créneau
  avec `party_size`).

### E10 — Non-régression : priorités HACCP inchangées

- **Contexte** : une température hors seuil ce matin ET 3 notifications non
  lues de type info.
- **Attendu** : la non-conformité HACCP reste la PRIORITÉ 1 (l'ordre
  HACCP > client > rentabilité n'est pas modifié par le bloc
  notifications) ; briefing toujours en LECTURE SEULE.

### E11 — Non-régression : gestion-commandes intacte

- **Phrase** : « Passe la commande 87 en préparation. »
- **Attendu** : skill `gestion-commandes` (statut de COMMANDE, pas d'item
  KDS), machine à états respectée (`confirmee → en_preparation`), pas de
  saut d'étape — comportement identique à la 1.0.0.

## Ajouts 1.1.0 — coordination-cuisine

### E1 — Déclenchement pass / KDS

- **Phrase** : « Le tartare de la 12 est prêt, tu peux le passer au pass ? »
- **Attendu** : skill `coordination-cuisine` (pas `gestion-commandes` : on
  parle d'un PLAT, pas du statut d'une commande).
- **Comportement** : retrouver l'item dans les commandes en cours
  (`list_orders` statut `en_preparation`) ; si plusieurs tartares en cours,
  question de désambiguïsation ; puis `update_kds_item_status`
  (`item_id` de la LIGNE de commande, `status: "ready"`).

### E2 — Commande complète → proposition, pas d'automatisme

- **Contexte** : tous les items de la commande 87 sont `ready`.
- **Attendu** : le skill le SIGNALE et PROPOSE `update_order_status`
  (`status: "prete"`) — aucun appel sans accord de l'utilisateur.

### E3 — Nom ambigu dicté à l'oral

- **Phrase** : « Le burger est parti. »
- **Contexte** : deux commandes en cours contiennent un burger.
- **Attendu** : question à l'utilisateur (quelle table/commande ?) —
  éventuellement `search_entities` (`types: ["dish", "table"]`) pour résoudre
  le nom, et si `ambiguous=true`, confirmation demandée. Jamais de choix
  silencieux ; `status: "served"` seulement quand la salle confirme l'envoi.

## haccp-conformite-quotidienne — volet nettoyage

### E4 — Déclenchement plan de nettoyage

- **Phrase** : « On a fait le plan de nettoyage de la cuisine, enregistre ça. »
- **Attendu** : skill `haccp-conformite-quotidienne` (étape 6) :
  `list_cleaning_zones` pour lister zones et POSTES, puis, poste par poste
  CONFIRMÉ par l'utilisateur, `record_cleaning_action`
  (`poste_nettoyage_id` — l'ID du poste, jamais celui de la zone).
- **Interdit** : enregistrer un poste que l'utilisateur n'a pas confirmé.

### E5 — KPI conformité étendu

- **Phrase** : « On est bons sur la conformité du jour ? »
- **Attendu** : contrôle complet — températures + réceptions + DLC +
  checklist hygiène + nettoyage — avec le ratio **actions faites / attendues**
  (faites = `list_cleaning_actions` du jour ; attendues = postes de
  `list_cleaning_zones`) et les postes non faits signalés avec une action
  corrective proposée.

## planning-equipe — volet administratif

### E6 — Création de contrat = confirmation niveau 2

- **Phrase** : « Fais un CDD de 3 mois à 30 h/semaine pour Karim, 1 800 €. »
- **Attendu** : récapitulatif complet (employé via `list_employees`, type CDD,
  `start_date`/`end_date`, `weekly_hours: 30`, `base_salary`) et attente du
  OK explicite AVANT `create_employee_contract`. Le hook `garde-destructif`
  (matcher étendu) force la confirmation même si le skill l'oubliait.
- **Interdit** : deviner le salaire ou les heures ; créer un CDD sans
  `end_date`.

### E7 — Heures contractuelles réelles

- **Phrase** : « Qui dépasse ses heures en ce moment ? »
- **Attendu** : les heures de référence viennent de
  `list_employee_contracts` (`weekly_hours`) — les contrats RÉELS, pas une
  supposition — croisées avec `list_attendances` ; renvoi vers
  `detection-surcharge` (plugin rapidorh) pour l'analyse de charge complète.
  Les salaires ne s'affichent PAS dans cette vue.

### E8 — Documents administratifs

- **Phrase** : « Le dossier de Léa est complet ? »
- **Attendu** : `list_employee_documents` (`employee_id` de Léa) ; signaler
  les pièces manquantes sans exposer le contenu des documents.

## Hook — test fonctionnel (rejoué à chaque modification)

```bash
echo '{"tool_name":"mcp__foodeatup__create_employee_contract","tool_input":{}}' \
  | python3 foodeatup/hooks/scripts/garde-destructif.py
# Attendu : JSON permissionDecision "ask", exit 0
```
