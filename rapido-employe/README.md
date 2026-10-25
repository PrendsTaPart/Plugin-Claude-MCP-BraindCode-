# rapido-employe

**Claude employé commercial de FoodEatUp.** Il se forme lui-même avec
l'Academy (serveur MCP « FoodEatUp formation »,
`https://formation.foodeatup.fr/mcp`), puis prospecte, relance, prépare les
démonstrations et les devis, communique, sert les clients, mesure et
s'améliore chaque vendredi — à travers tous les serveurs de l'écosystème,
**toujours dans le cadre fixé par son responsable**.

## Le modèle : le cadre se relit, il ne se code pas

C'est l'Academy qui dit à Claude ce qu'il a le droit de faire, jamais ce
plugin. À chaque prise de poste : `get_claude_brief` puis `get_work_plan` —
huit familles d'actions (apprendre, configurer, préparer, prospecter,
publier, service-client, développer, engager) chacune à son niveau (Aperçu,
Brouillon, Confirmé), des quotas du jour, un budget contrôlé par
`record_expense`. L'instantané du cadre vit dans
`.claude/state/cadre-employe.json` (périmé après 24 h) et HUIT HOOKS
testés le font respecter : « engager » est toujours une décision humaine,
l'envoi Gmail direct est interdit au profit du brouillon, Claude ne
gouverne jamais son propre cadre, rien ne se paie sans dépense inscrite et
acceptée, la mémoire ne range jamais un secret.

## La journée type

| Moment | Commande | Ce qui se passe |
|---|---|---|
| Prise de poste | `/prise-de-poste` | brief + plan du jour, cadre écrit pour les gardes |
| Les chiffres | `/point-du-matin` | chaque KPI lu À SA SOURCE, enregistré, tâches choisies par l'écart aux objectifs |
| L'école (30 min) | `/apprendre` | mission, quiz, révision, mise en pratique réelle |
| Les routines | `/routines` | celles du registre Academy, dans leur niveau et les quotas |
| Le métier | `/prospecter`, `/relances`, `/demo`, `/devis`, `/semaine-com` | brouillons et aperçus, accord avant tout envoi |
| Le vendredi | `/vendredi` | expériences, verdicts, rétrospective, rapport sur gabarit |
| Le soir | `/rapport` | dix lignes au responsable (email_report si le rôle le permet, sinon brouillon Gmail) |

`/cadre` affiche à tout moment autonomie, quotas consommés et budget
restant. `/outil-manquant` fait construire ce qui manque (préproduction
Lovable, l'humain publie). `/former-equipe` n'existe pas ici : la formation
du client passe par le plugin `foodeatup-tutoriel`.

## Phrases d'exemple

« Prends ton poste et fais ton point du matin » · « Prospecte Montpellier,
cible brasseries » · « Prépare le devis du Bistrot de la Gare » · « Il
m'objecte que c'est trop cher » · « Fais ta boucle du vendredi » · « Où en
est ta certification ? »

## Ce que ce plugin NE fait PAS (et qui le fait)

Sourcing Google Maps avancé → `rapido-gmaps` · lead magnets de bout en
bout → `rapido-leadmagnet` · copy fine des réseaux → `rapido-copywriter` ·
publicité payante → `rapido-meta-ads` · boîte mail du dirigeant →
`rapido-direction` · pilotage transverse → `rapido-suite`. Ce plugin
ORCHESTRE et délègue — il n'en recopie aucun.

## Faire tourner l'employé en tâche planifiée (proposé, jamais activé d'office)

Les routines vivent dans l'Academy et Plan'It — voir
`reference/registre-routines.md` du dépôt (renvoi, pas de duplication).
Pour une vraie journée automatique, l'utilisateur PEUT créer deux tâches
planifiées dans son orchestrateur (Plan'It, ou les tâches planifiées de
Claude) :

- chaque matin ouvré : « /prise-de-poste puis /point-du-matin puis
  /routines » ;
- chaque vendredi après-midi : « /vendredi puis /rapport ».

Rien n'est créé par le plugin lui-même : c'est une décision de
l'utilisateur, avec les gardes actifs dans la session planifiée comme
partout (budget 0 € = aucune dépense ; agent arrêté = rapport seulement).

## Prérequis et dégradation

- **Academy obligatoire** : `.mcp.json` la déclare avec un jeton personnel
  en `${ACADEMY_MCP_TOKEN}` (généré sur la page « Connecter Claude »,
  affiché une seule fois — jamais dans un fichier). Sans elle, pas de
  cadre : le plugin s'arrête en le disant.
- Serveurs requis : foodeatup, foodeatup-tutoriel, site, social, rapidocrm,
  rapidocms, rapidorh, planit. Optionnels : studio-print et prospector-hub
  (adresses d'instance en `${STUDIO_PRINT_MCP_URL}` /
  `${PROSPECTOR_HUB_MCP_URL}`), build, lovable, gmail, google-drive — un
  optionnel absent fait sauter son volet EN LE DISANT.
- Budget actuel du cadre : 0 €/mois — toute action payante est refusée tant
  que le responsable ne l'a pas changé dans l'application.

## Installation

```
/plugin marketplace add PrendsTaPart/Plugin-Claude-MCP-BraindCode-
/plugin install rapido-employe@rapido
```
