# Fiche kit — RapidoRH

**Kit v1 · 2026-07-15.** Voir `_commun.md` pour le template, la sécurité et les critères.

> **Note périmètre** : RapidoRH porte des données **internes** (employés, projets,
> tâches). Un agent RH embarqué est un **outil back-office** (portail interne), **jamais**
> un agent public de site vitrine. Activer avec discernement.

## Variables d'environnement (immuables)

| Rôle | Nom |
|---|---|
| URL MCP | `RAPIDORH_MCP_URL` (valeur produit : `https://rh.rapidosoftware.com/mcp/rapidorh`) |
| Token tenant (quand dispo, §7) | `RAPIDORH_MCP_TOKEN` |
| Scope société | `RAPIDORH_COMPANY_ID` |
| Clé Anthropic client | `ANTHROPIC_API_KEY` |

Nom du serveur : `rapidorh`. Edge function : `agent-rh`.

## Familles d'outils autorisées (portail interne authentifié)

- **Lecture** : projets, tâches, listes de tâches, utilisateurs, dailies (ex.
  `get-projects-list-tool`, `get-project-tasks-tool`, `get-users-list-tool`,
  `get-dailies-tool`).
- **Écriture — proposée puis confirmée** : créer une tâche/daily (`create-task-tool`,
  `create-daily-tool`), déplacer une tâche (`move-task-tool`). **Jamais** sans
  `approved:true`.
- **Interdit par défaut** : suppression d'utilisateur, gestion de rôles/permissions —
  jamais via un agent embarqué.
- **Authentification obligatoire** : cet agent n'est **jamais** public ; l'accès exige une
  session utilisateur authentifiée (Supabase auth), pas un anonyme.

## Bloc system prompt

```
Tu es l'assistant RH interne. Tu opères STRICTEMENT dans la société
{RAPIDORH_COMPANY_ID} et uniquement pour un utilisateur authentifié. Langue : français.
Tu peux CONSULTER projets, tâches, équipe, dailies. Tu peux CRÉER/DÉPLACER une tâche —
action PROPOSÉE puis CONFIRMÉE dans l'UI. Tu ne supprimes jamais d'utilisateur ni ne
modifies de rôle. Rien d'inventé.
```

## Cas d'usage typiques

Portail interne : « Crée une tâche pour l'équipe design » (proposée, confirmée) · « Qui
est surchargé ? » (lecture). **Pas** pour un site public.
