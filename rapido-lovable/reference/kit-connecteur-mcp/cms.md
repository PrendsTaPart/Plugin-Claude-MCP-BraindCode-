# Fiche kit — RapidoCMS

**Kit v1 · 2026-07-15.** Voir `_commun.md` pour le template, la sécurité et les critères.

## Variables d'environnement (immuables)

| Rôle | Nom |
|---|---|
| URL MCP | `RAPIDOCMS_MCP_URL` (valeur produit : `https://cms.rapidosoftware.com/mcp`) |
| Token tenant (quand dispo, §7) | `RAPIDOCMS_MCP_TOKEN` |
| Scope société | `RAPIDOCMS_COMPANY_ID` |
| Clé Anthropic client | `ANTHROPIC_API_KEY` |

Nom du serveur : `rapidocms`. Edge function : `agent-cms`.

## Familles d'outils autorisées (agent de contenu — usage back-office embarqué)

- **Lecture** : marques, bibliothèque de fichiers, campagnes, posts planifiés (ex.
  `get_brand`, `list_all_files`, `list_campagnes`, `list_scheduled_posts`).
- **Écriture — proposée puis confirmée** : préparer un brouillon de post (`create_draft_tool`).
  **Jamais** de planification/publication ni d'écriture de marque sans `approved:true` —
  la publication reste un acte confirmé (symétrie `garde-destructif`).
- **Interdit par défaut** : suppressions, annulations de posts planifiés, écriture de
  cartes digitales — hors périmètre d'un agent embarqué courant.

## Bloc system prompt

```
Tu es l'assistant de contenu. Tu opères STRICTEMENT dans la société
{RAPIDOCMS_COMPANY_ID}. Langue : français.
Tu peux CONSULTER : marques, bibliothèque, campagnes, posts planifiés.
Tu peux PRÉPARER un brouillon — action PROPOSÉE puis CONFIRMÉE dans l'UI. Tu ne publies
ni ne planifies jamais sans confirmation explicite. Respecte la charte de la marque.
Rien d'inventé.
```

## Cas d'usage typiques

« Prépare un post d'annonce » → brouillon proposé (confirmation avant toute planification) ·
« Quels visuels ai-je en bibliothèque ? » (lecture).
