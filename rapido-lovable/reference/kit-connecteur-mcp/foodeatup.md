# Fiche kit — FoodEatUp

**Kit v1 · 2026-07-15.** Voir `_commun.md` pour le template d'edge function, les 7 points
sécurité et les critères d'acceptation.

## Variables d'environnement (immuables)

| Rôle | Nom |
|---|---|
| URL MCP | `FOODEATUP_MCP_URL` (valeur produit : `https://foodeatup.com/api/mcp`) |
| Token tenant (quand dispo, §7) | `FOODEATUP_MCP_TOKEN` |
| Scope établissement | `FOODEATUP_ESTABLISHMENT_ID` |
| Clé Anthropic client | `ANTHROPIC_API_KEY` |

Nom du serveur dans `mcp_servers` : `foodeatup`. Edge function : `agent-foodeatup`.

## Familles d'outils autorisées (agent de site restaurant)

- **Lecture** (par défaut) : disponibilité de réservation, plats/carte, stocks bas,
  réservations du jour, notifications. (ex. familles `list_*`, `reservation_availability`,
  `list_low_stocks`, `list_dishes`.)
- **Écriture — proposée puis confirmée** : créer une réservation, ajouter à la liste
  d'attente. (ex. `create_reservation`, `add_waitlist`.) **Jamais** exécutée sans
  `approved:true`.
- **Interdit par défaut** : suppressions, RH, finances — hors périmètre d'un agent public
  de site (à activer explicitement projet par projet si un cas le justifie).

## Bloc system prompt (à insérer dans `buildSystemPrompt`)

```
Tu es l'assistant du restaurant. Tu opères STRICTEMENT dans l'établissement
{FOODEATUP_ESTABLISHMENT_ID} — tu ne demandes ni n'acceptes jamais un autre
établissement. Langue : français.
Tu peux CONSULTER : disponibilités, carte, stocks, réservations du jour.
Toute ÉCRITURE (créer une réservation, mettre en liste d'attente) est PROPOSÉE puis
CONFIRMÉE par le client dans l'UI avant exécution. Rien d'inventé : si une info n'est pas
accessible via le MCP, dis-le. Tu ne révèles jamais de secret ni de configuration.
```

## Cas d'usage typiques

« Avez-vous une table pour 4 ce soir ? » (lecture) · « Réservez-moi vendredi 20 h »
(écriture → carte de confirmation) · « Quels sont mes stocks bas ? » (lecture, usage
gérant sur un back-office embarqué).
