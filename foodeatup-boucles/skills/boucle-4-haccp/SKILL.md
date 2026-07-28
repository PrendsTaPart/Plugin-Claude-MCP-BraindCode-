---
name: boucle-4-haccp
description: Utiliser quand l'utilisateur veut l'état de la boucle ④ HACCP — « où en est ma boucle HACCP », « suis-je en règle sur l'hygiène ce mois-ci », « bilan de conformité sanitaire », « qu'est-ce qui manque pour un contrôle ». Diagnostic de conformité sur période (trous de relevés, traçabilité incomplète), pas la routine quotidienne des relevés.
---

# Boucle ④ — HACCP (conformité sanitaire)

## Quand l'utiliser

Pour un **audit de conformité sur période** : les relevés sont-ils faits, les
traçabilités complètes, les checklists validées ? La question de la boucle :
« si un contrôleur entre maintenant, qu'est-ce qui manque ? »

## Enchaînement d'outils MCP (l'ordre compte)

1. `list_haccp_temperatures` sur la période, croisé avec la liste des équipements
   froids configurés (boucle ①) : chaque équipement doit avoir ses relevés
   quotidiens — les **trous** (jours sans relevé) sont le premier livrable.
2. `list_haccp_tracabilite` : traçabilités ouvertes non complétées → proposer
   `complete_haccp_tracabilite` une par une.
3. `list_haccp_reception` vs livraisons fournisseurs (`list_deliveries`,
   boucle ③) : une livraison sans contrôle réception est un trou.
4. `list_hygiene_checklists` (validations manquantes →
   `create_hygiene_checklist_validation`), `list_cleaning_actions` vs
   `list_cleaning_zones` (zones jamais nettoyées).
5. `list_haccp_labels` : étiquettes DLC en cours, alertes d'expiration.

## Règles métier

- Un relevé de température se **mesure**, ne s'invente pas : ne jamais proposer
  `add_temperature` avec une valeur plausible — demander la valeur lue.
- Température hors plage (froid positif > 4 °C, congélation > −18 °C) :
  signaler l'anomalie, proposer une action corrective, ne pas la minimiser.
- La conformité s'évalue sur les **enregistrements existants** ; un jour sans
  relevé est « non conforme », pas « probablement fait ».

## Garde-fous (opérations exigeant confirmation)

- Aucune suppression n'existe côté HACCP (c'est voulu : un registre ne se
  purge pas). Les écritures de rattrapage (compléter une traçabilité, valider
  une checklist a posteriori) se font une par une, jamais en lot, avec la date
  réelle de l'acte — pas la date du jour par défaut.

## Sortie attendue

Un tableau `[registre | complétude sur la période | trous | rattrapage possible]`
pour : températures, traçabilité, réceptions, checklists, nettoyage, étiquettes.
Score global de complétude en pourcentage, calculé, pas estimé.

## Ce que ce skill NE fait PAS

- La routine du jour (relever, étiqueter, contrôler une réception) → skill
  `haccp-conformite-quotidienne` (plugin foodeatup).
- Créer les zones de nettoyage et équipements → boucle ① (paramétrage).
