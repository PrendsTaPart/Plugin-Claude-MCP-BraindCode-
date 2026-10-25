---
description: Suivre une leçon de l'Académie (vidéo + quiz + exercice)
argument-hint: "<slug ou sujet de la leçon>"
---

Dérouler le skill `lecon-guidee` sur la leçon demandée :

- l'argument ressemble à un slug (kebab-case) → l'utiliser tel quel ;
- sinon, le résoudre d'abord via le skill `trouver-un-tuto`
  (`rechercher_tutoriels`, paramètre `question`) et confirmer la fiche
  choisie avant de lancer ;
- sans argument : reprendre la leçon en cours s'il y en a une, sinon
  proposer `lecon_suivante` (skill `parcours-sur-mesure`).
