---
name: boucle-2-equipe
description: Utiliser quand l'utilisateur veut l'état de la boucle ② Équipe — « où en est ma boucle équipe », « mon équipe est-elle au complet pour la semaine », « bilan RH de mon restaurant », « state des congés et du recrutement ». Diagnostic staffing/contrats/congés/recrutement, pas la manipulation fine d'un planning.
---

# Boucle ② — Équipe (staffing, contrats, congés, recrutement)

## Quand l'utiliser

Pour un **état de santé RH** de l'établissement : effectifs, couverture du
planning, congés en attente, pointages anormaux, recrutements en cours. Le but
est de détecter les trous de service avant qu'ils n'arrivent en salle.

## Enchaînement d'outils MCP (l'ordre compte)

1. `list_employees` (effectif actif), puis `list_employee_contracts`
   (contrats manquants ou expirés — un employé actif sans contrat est une alerte).
2. `list_plannings` sur les 7 prochains jours, croisé avec `list_reservations`
   (boucle ⑤) : un pic de couverts sans shift correspondant = trou de staffing.
3. `list_leaves` (demandes en attente → proposer `approve_leave` / `reject_leave`
   une par une, jamais en lot), `list_attendances` (pointages incohérents).
4. Recrutement : `list_job_applications` et `update_application_status` ;
   `create_job_offer` / `update_job_offer` si un poste reste découvert.
5. Actions courantes : `create_shift`, `assign_task`.

## Règles métier

- Une demande de congé n'est jamais approuvée sans vérifier la couverture du
  planning sur les dates concernées.
- Un trou de staffing se qualifie avec les réservations réelles, pas au ressenti.
- Les documents employés (`list_employee_documents`) se consultent, ne se
  divulguent pas : pas de données personnelles dans la synthèse.

## Garde-fous (opérations exigeant confirmation)

Interceptés par le hook du plugin (confirmation humaine obligatoire) :
- `create_employee_contract` — acte juridique ;
- `update_employee_schedule` — modifie le planning contractuel ;
- `delete_employee` — suppression irréversible.

## Sortie attendue

Un tableau `[sujet | état | risque | action proposée]` sur 5 sujets : effectif,
couverture planning, congés, pointages, recrutement. Trois actions maximum.

## Ce que ce skill NE fait PAS

- Construire ou remanier le planning shift par shift → skill `planning-equipe`
  (plugin foodeatup).
- Les projets/Kanban d'équipe hors restaurant → plugin rapidorh.
