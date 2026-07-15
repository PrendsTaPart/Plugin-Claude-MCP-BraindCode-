# Boucle d'apprentissage — la bibliothèque de prompts apprend

> **Principe** : un prompt n'est pas « bon » parce qu'on le décrète — il l'est
> parce que le **résultat réel** le prouve. Après production/publication, les
> skills exécutants rapportent les métriques réelles ; on en tire un tag
> **GAGNANT / NEUTRE** posé dans la bibliothèque (`edit_prompt`). L'agent
> `directeur-prompts` **pioche les GAGNANT d'abord** (`list_prompts`).
>
> **Aucun score inventé.** Seules les métriques réellement disponibles comptent ;
> un prompt sans métrique reste **INSUFFISANT** (non taggé).

## Le cycle

```
directeur-prompts compose ──► skill exécutant génère ──► publication/production
        ▲                                                        │
        │  pioche GAGNANT d'abord (list_prompts)                 │ résultats réels
        │                                                        ▼
  bibliothèque taggée ◄── edit_prompt(tag) ◄── score_prompts.py ◄── métriques MCP
        └──────────────► apprentissages.md (journal daté) ◄──────────┘
```

## Qui rapporte quoi (métriques RÉELLES uniquement)

| Source réelle | Métrique | D'où elle vient |
|---|---|---|
| RapidoCMS | `engagement_rate`, `impressions` | `post_insights` sur les posts issus du prompt |
| Higgsfield | `virality_score` | `virality_predictor` / `analyse-video-virale` |
| Bibliothèque | `reuse_count` | nombre de réutilisations du prompt (`list_prompts`) |

Une métrique **absente** n'est **jamais** remplacée par 0 : elle est « non
disponible » et n'entre pas dans le calcul.

## Le script — `scripts/score_prompts.py` (stdlib, sans réseau)

1. Les skills exécutants assemblent un **fichier de résultats** à partir des
   données MCP réelles :

   ```json
   {
     "prompts": [
       {"prompt_id": 12, "titre": "packshot — sneaker — studio",
        "metrics": {"engagement_rate": 0.061, "virality_score": 74, "reuse_count": 2}}
     ]
   }
   ```

2. Lancer :

   ```
   python3 scripts/score_prompts.py --results resultats.json --emit-edits
   ```

3. Le script écrit le journal `./rapido-kb/marketing/apprentissages.md` (daté) et
   imprime un **plan d'appels** `edit_prompt` :

   ```json
   { "edits": [ {"tool": "edit_prompt", "prompt_id": 12, "tag": "GAGNANT"} ] }
   ```

4. L'agent exécute ce plan (`edit_prompt`) pour poser le tag dans la bibliothèque.

## Formule (transparente, seuils surchargeables)

- **GAGNANT** : au moins un signal réel disponible **dépasse son seuil** —
  `engagement_rate ≥ 0.05` **ou** `virality_score ≥ 70` **ou** `reuse_count ≥ 3`.
- **NEUTRE** : au moins un signal réel disponible, **aucun seuil atteint**.
- **INSUFFISANT** : **aucun** signal réel disponible → non taggé (revenir plus tard
  avec de vraies métriques).

Seuils ajustables : `--seuil-engagement`, `--seuil-virality`, `--seuil-reuse`.
La formule est **affichée** dans le journal via les raisons de chaque classement
(ex. `engagement_rate=0.061 (seuil 0.05) ✓`) — jamais un score « de tête ».

## Où vit le journal

`./rapido-kb/marketing/apprentissages.md` — **côté client, gitignoré** (jamais dans
ce dépôt : données réelles de performance). Le script le crée s'il n'existe pas.
