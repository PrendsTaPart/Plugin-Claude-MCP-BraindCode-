# Règles de direction — référence OBLIGATOIRE

À charger avant tout usage des outils Google/CRM/FoodEatUp/n8n de ce plugin.
Toujours « le compte connecté » — jamais une boîte, un agenda ou un Drive
particulier nommé dans une instruction.

## EMAILS — brouillons uniquement, c'est VOULU

- Gmail via MCP ne fait QUE des brouillons (`create_draft`) : Claude RÉDIGE,
  l'HUMAIN envoie. Ne jamais contourner (pas d'envoi via un autre canal pour
  « aller plus vite ») — c'est la garantie de contrôle du dirigeant.
- Toute opération corbeille/spam (si un outil l'expose un jour) =
  confirmation « ask » (hook du plugin).
- Brouillons contextualisés : historique CRM de l'entreprise si reconnue
  (`get_entreprise`, `get_historique_prospect`), ton de
  `rapido-kb/ton-et-accroches.md`.
- Étiquettes sensibles (`apply_sensitive_message_label`) : pour marquer, pas
  pour cacher — signaler au dirigeant ce qui a été marqué.

## AGENDA

- `create_event` AVEC notification par défaut (les participants sont
  prévenus) — le dire avant de créer.
- Créneaux : `suggest_time` (jamais de créneau deviné).
- FUSEAU HORAIRE : lu dans `rapido-kb/entreprise.md` (demandé à
  l'onboarding) — jamais codé en dur, jamais supposé. S'il manque : le
  demander et proposer de compléter la KB.
- `delete_event` / modification d'un événement existant avec participants :
  confirmation (les invités reçoivent l'annulation).

## DOCUMENTS — Drive = coffre officiel

- Le Drive du compte connecté est le COFFRE officiel (contrats, factures,
  documents légaux).
- Arborescence : `Clients/<Nom de l'entreprise>/` — la respecter à chaque
  classement ; créer le dossier client s'il n'existe pas.
- JAMAIS de suppression — seulement du classement, de la copie
  (`copy_file`), de la création (`create_file`). Un document mal classé se
  déplace, ne se supprime pas.

## PRIORITÉ DES SOURCES — l'agenda est TRIPLE

L'agenda du dirigeant = la FUSION de trois sources, toujours les trois :
1. Google Calendar (`list_events`) — RDV personnels et pros ;
2. `get_today_schedule` (CRM) — RDV commerciaux et événements ;
3. `list_reservations` (FoodEatUp) — les services du restaurant (gros
   groupes, VIP).
Un conflit entre sources (RDV CRM absent de Calendar…) se SIGNALE — proposer
la synchronisation, ne pas choisir silencieusement.

## Routage ponctuel / récurrent / sensible

- PONCTUEL → exécuter via les MCP.
- RÉCURRENT (« tous les lundis… », « à chaque fois que… ») → proposer le
  workflow n8n (`usine-automatisations`, plugin rapido-n8n) au lieu de
  refaire à la main.
- SENSIBLE (litige, remise au-delà du seuil de
  `rapido-kb/processus-internes.md`, recrutement/licenciement, engagement
  juridique) → ESCALADE : préparer le dossier, ne jamais décider à la place
  du dirigeant.

## Dégradation propre

Outils Gmail/Calendar/Drive absents (compte non connecté) → l'expliquer,
renvoyer vers `${CLAUDE_PLUGIN_ROOT}/README-installation.md`, et exécuter ce
qui reste possible (volets CRM/FoodEatUp/n8n) en le mentionnant. Idem pour
n8n (`N8N_MCP_URL`). Jamais d'échec sec.

## KB (./rapido-kb/)

`entreprise.md` (fuseau, équipe clé), `ton-et-accroches.md` (brouillons),
`processus-internes.md` (seuils d'escalade, registre des automatisations),
`cibles-personas.md` (qualification des emails entrants). La KB prime ; sans
KB, prudence maximale et suggestion d'onboarding.
