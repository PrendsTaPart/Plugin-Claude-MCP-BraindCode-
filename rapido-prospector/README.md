# rapido-prospector

**Toute la prospection commerciale depuis Claude Code**, au-dessus du
serveur MCP Prospect (« Prospector Hub ») : trouver des établissements par
zone et spécialité, tenir une base propre et dédoublonnée, écrire et
envoyer des campagnes e-mail, SMS et LinkedIn **sous contrôle humain**,
tenir le calendrier éditorial, le blog, les vidéos, les webinaires et les
lead magnets, suivre chaque prospect et mesurer l'entonnoir jusqu'au MRR
Stripe. Serveur : `https://prospect-pebble.lovable.app/mcp` (66 outils
relevés, OAuth au premier appel — aucun jeton dans le dépôt). RapidoCRM en
option pour la synchronisation.

## Le contrat du plugin

- **Aucun envoi réel sans accord humain sur CET envoi** : les 5 outils
  d'envoi (e-mail, SMS, appel, invitation et message LinkedIn) passent par
  un ask systématique ; les champs confirm posés par le modèle ne valent
  jamais confirmation.
- **Quotas et fenêtre horaire** : `./rapido-kb/prospection.md` (gabarit
  fourni) — sans KB, défauts prudents, appels automatisés à ZÉRO. Si le
  cadre Academy de rapido-employe existe, le plus petit quota gagne.
- **Conformité refusée, pas rattrapée** : e-mail sans identité
  d'expéditeur ou sans désinscription = deny ; SMS sans STOP = deny ;
  appel automatisé non activé dans la KB = deny ; destinataire de la liste
  d'opposition = l'envoi entier est refusé.
- **Base propre d'abord** : run_prospection ne sauvegarde rien ;
  dédoublonnage par script (5 critères affichés) avant tout
  enregistrement ; aucun contact deviné.
- **12 suppressions définitives** avec leurs cascades rappelées dans la
  question ; publications (webinaire actif, statut « publie ») sur accord.
- **Chiffres honnêtes** : MRR Stripe = estimation, formules des scripts
  affichées, champ absent = « — ».

## Journée type

| Moment | Commande | Ce qui se passe |
|---|---|---|
| Ouverture | `/prospect` | entonnoir, envois vs quotas, file LinkedIn, MRR estimé, 3 priorités |
| Sourcing | `/prospecter Lille boulangerie` | webhook n8n, dédoublonnage, accord, add_clients, journal |
| Matin LinkedIn | `/linkedin-du-jour` | file du jour, anti-répétition, envois un par un sur accord |
| Campagne | `/campagne-email`, `/campagne-sms` | segment, modèle conforme, aperçu, quota, accord, envoi, statuts |
| Suivi | `/relances` | chronologie 4 canaux, relances dues, envoi sur accord |
| Contenus | `/calendrier`, `/webinaire`, `/lead-magnet` | brouillons d'abord, mise en ligne sur accord |
| Comptes | `/mrr`, `/journal` | Stripe agrégé (estimation dite), audit du journal |

## Phrases d'exemple

« Où en est ma prospection ? » · « Prospecte les pizzerias de Lyon » ·
« Envoie la campagne de démo aux boulangers — montre-moi d'abord » ·
« Fais le LinkedIn du matin » · « Qui dois-je relancer ? » · « Crée le
webinaire de novembre, sans l'activer » · « Quel est mon MRR ? »

## Articulation avec les autres plugins (délégation, pas de recopie)

`rapido-gmaps` source Google Maps → RapidoCRM ; ce plugin alimente la base
PROSPECT. Le pipeline et les relances CRM vivent dans `rapidocrm` ; la
cadence outbound et le social selling se conçoivent dans
`rapido-marketing` ; la copy dans `rapido-copywriter` ; la fabrication des
lead magnets dans `rapido-leadmagnet` ; la publication réelle des posts
dans `rapidocms` ; la génération vidéo dans `rapido-higgsfield` /
`rapido-video`. rapido-prospector est **l'exécutant Prospector Hub** de
tout ce monde.

## Appels automatisés : désactivés par défaut

`place_call` (appels robotisés Twilio, synthèse vocale) est l'outil le
plus encadré juridiquement : quota à 0 et refus du hook tant que
`appels_automatises.actives` n'est pas `true` dans la KB, avec une base
légale documentée. `reference/conformite-prospection.md` est marqué **« à
faire valider par un juriste »**.

## Installation

```
/plugin marketplace add PrendsTaPart/Plugin-Claude-MCP-BraindCode-
/plugin install rapido-prospector@rapido
```

Puis copier `rapido-kb-template/prospection.md` dans `./rapido-kb/` et le
remplir (quotas, identité d'expéditeur, désinscription, STOP, liste
d'opposition). L'authentification Prospect est l'OAuth du premier appel.
