---
name: calendrier-iris
description: Utiliser quand l'utilisateur veut voir, valider ou refuser les publications proposées — « montre le calendrier d'Iris », « qu'est-ce qui est prévu cette semaine », « valide le post de mardi », « refuse celui-là ». Calendrier glissant 7 jours avec la raison de chaque contenu, validation carte par carte, planification confirmée.
---

# Calendrier glissant (7 jours, pas un mois)

Un calendrier mensuel est périmé au dixième jour : le stock a changé, un plat
est sorti, un créneau s'est rempli. Iris propose SEPT jours, recalculés sur
les données du jour.

## Affichage

- Vue semaine : une carte par proposition — canal, jour/heure, miniature ou
  description du visuel, et **LA RAISON en évidence** (« Parce que… »). Sans la
  raison, la carte n'est pas montrée.
- Source : `./rapido-kb/iris/calendrier.md` (propositions et statuts) +
  `list_drafts_tool` / `list_scheduled_posts` (état réel côté CMS — le CMS
  fait foi, signaler tout écart avec le fichier local).
- À chaque affichage : re-vérifier que la raison tient toujours (le surstock
  est-il encore là ? `list_stocks` ; le créneau toujours creux ?
  `reservation_availability`). Une raison morte = proposition retirée, dit
  explicitement.

## Trois actions par carte

1. **Valider** → `schedule_draft_tool` (date/heure/canal). Le garde-fou du
   plugin exige la confirmation : c'est le SEUL chemin vers la publication,
   et il passe par un humain. Statut → `planifie`.
2. **Modifier** → texte éditable, canal/horaire modifiables ; « régénérer le
   visuel » et « régénérer le texte » sont des actions SÉPARÉES (skill
   `fabrique-contenu-iris`), chacune avec son coût annoncé.
3. **Refuser** → demander le motif en un choix rapide : pas le bon moment ·
   pas le bon visuel · pas le bon texte · sujet non pertinent. Consigner le
   motif dans `./rapido-kb/iris/apprentissage.md` — c'est ce qui alimente
   l'apprentissage (skill `mesure-apprentissage-iris`).

## Règles

- Fréquence maximale, canaux actifs, plages horaires autorisées et sujets
  interdits : lus dans `./rapido-kb/iris/parametres.md` s'il existe (créé à la
  première demande de réglage). Une proposition hors plage n'est pas montrée.
- Annulation d'une planification : `cancel_schedules_post` (garde rapidocms).
- Aucun raccourci : pas de « valide tout » — chaque carte se valide une par
  une, c'est le prix de l'image publique.

## Ce que ce skill NE fait PAS

- Détecter/fabriquer → skills `moteur-opportunites-iris` et
  `fabrique-contenu-iris`.
- Le calendrier éditorial généraliste (hors signaux d'exploitation) → plugin
  rapidocms (skill `calendrier-editorial`).
