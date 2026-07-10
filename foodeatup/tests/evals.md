# Évals — plugin foodeatup (1.1.0)

Scénarios de déclenchement et de comportement pour les ajouts de la 1.1.0.
À rejouer manuellement (ou via un futur harnais) : la phrase utilisateur doit
router vers le skill attendu et le comportement décrit doit être observé.

## coordination-cuisine

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
