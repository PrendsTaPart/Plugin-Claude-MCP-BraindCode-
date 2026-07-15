# Prérequis E5 — agent-vocal-jarvis (à réunir avant le skill)

> Le skill `agent-vocal-jarvis` (E5) crée et gouverne des **agents vocaux
> ElevenLabs** qui décrochent et passent de vrais appels, branchés sur FoodEatUp
> via un pont n8n. Deux prérequis d'infrastructure doivent être en place **avant**
> E5 ; ils sont indépendants du squelette E1.

## 1. Connecteur Twilio (URL d'environnement à ajouter)

- E5 s'appuie sur le **MCP Twilio** (et les skills `twilio-developer-kit`) pour le
  pont téléphonique. **Twilio n'est pas connecté** dans la session actuelle.
- **Action (infra)** : ajouter le connecteur Twilio à l'environnement (URL + auth en
  variable d'environnement, **aucun secret dans le dépôt**), comme les autres
  connecteurs Rapido.

## 2. Numéro de téléphone provisionné (décision E0)

- `make_outbound_call` **exige un numéro provisionné** (piège 4) — l'outil apparaît
  dans la liste même sans numéro. `list_phone_numbers` doit renvoyer un numéro.
- **Décision E0 (b)** : provisionner un **numéro ElevenLabs** (coût à chiffrer) **ou**
  router les appels par le **pont Twilio existant**. À trancher pendant E0-local.

## État d'avancement

| Prérequis | État | Qui |
|---|---|---|
| Connecteur Twilio (env) | ⏳ à ajouter | infra / utilisateur |
| Numéro provisionné (ElevenLabs vs Twilio) | ⏳ décision E0 | utilisateur (E0-local) |
| Catalogue outils ElevenLabs (testeur) | ⏳ livré par E0-local | audit E0 |

> **E2→E6 (dont E5) restent en attente de E0-local.** E5 ne peut démarrer qu'une
> fois (1) Twilio connecté, (2) le numéro tranché, (3) E0 terminé (voix de marque +
> catalogue outils). Le garde-fou `garde-appels` (E1) est déjà en place et testé.
