# rapido-direction — Chef de cabinet du dirigeant

Chef de cabinet du dirigeant : Gmail, Google Calendar et Google Drive (compte connecté de chacun) unifiés avec CRM, FoodEatUp et n8n — journée du dirigeant, tri de boîte mail en brouillons, secrétariat commercial, coffre documents, délégation du récurrent.

## Skills (5)

| Skill | Quand l'utiliser |
|---|---|
| `coffre-documents` | Classer un document ou retrouver un contrat, une facture, un fichier. Gère le Drive du compte… |
| `delegation-recurrence` | Demande de direction est récurrente |
| `journee-du-dirigeant` | Sa journée, un briefing complet ou |
| `secretariat-commercial` | Prospect a écrit, ou pour organiser un RDV avec un contact |
| `tri-boite-mail` | Trier ses mails, viser l'inbox zero ou répondre à un mail. Classe la boîte du compte connecté… |

## Agents (1)

- **`assistant-direction`** — Chef de cabinet du dirigeant.

## Serveurs MCP requis

`gmail`, `google-calendar`, `google-drive`, `rapidocrm`, `foodeatup`, `n8n` — connexion et clés : voir « Prérequis & connecteurs » du [README racine](../README.md). Aucune clé n'est stockée dans le dépôt.

## Déclencheurs (exemples réels)

- « tous les lundis… »
- « à chaque fois que… »
- « par quoi je commence »

## Version & conventions

v1.1.0 — historique dans [CHANGELOG.md](CHANGELOG.md). Skills en français (« Utiliser quand… »), calculs par script stdlib, garde-fous déterministes, rien d'inventé (KB `./rapido-kb/` prioritaire).
