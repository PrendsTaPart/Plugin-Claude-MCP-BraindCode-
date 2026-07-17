# Protocole « boucle d'amélioration » — le Loop Engineering appliqué aux routines

> Chaque routine est un **système mesurable**. On l'améliore comme un plat : on goûte
> (mesure réelle), on **change UNE chose**, on regoûte. **Règle d'or, encodée partout :
> une seule variable modifiée par cycle — sinon on ne sait pas ce qui a marché.**

Les fiches d'amélioration vivent dans la collection `data/prompts-collections/boucles.json`
(KPI, formule, requêtes MCP, période) : **la fiche fait foi** pour une routine donnée.

## Les 5 temps (dans l'ordre, sans en sauter)

### 1. MESURER
- **Uniquement** les requêtes MCP listées par la fiche de la routine — **jamais d'autre
  source**. Périodes **comparables** (même durée, même fenêtre).
- Donnée indisponible côté MCP → **« pas de visibilité sur {X} »** + entrée
  `docs/OUTILS-MCP-MANQUANTS.md`. Un **proxy** de remplacement est **annoncé comme tel**,
  jamais substitué en silence.

### 2. CALCULER
- Tout chiffre passe par le skill `catalogue-kpi` (scripts/calcul_kpi.py, hook « KPI sans
  script »). **Formule affichée**, jamais de calcul de tête.
- **Ne jamais moyenner en silence** : médiane si la distribution est asymétrique, et on
  dit laquelle. Comparer des périodes **comparables**.

### 3. JUGER
- Seuil lu dans **`./rapido-kb/processus-internes.md`** (défauts secteur dans
  `reference/seuils-defaut.md`, cités comme tels).
- **Pas de seuil en KB = le PROPOSER d'abord** (valeur + justification), ne pas l'inventer
  ni décider sans lui.

### 4. AJUSTER — **UNE modification par cycle**
Une seule variable parmi : **seuil · heure · fréquence · ton · ciblage · prompt de tâche
relais · workflow n8n** (via `rapido-n8n:surveillance-automatisations`). Toujours annoncer
**ancienne → nouvelle** valeur.
- **Niveau 1 — proposé** : la modification est présentée, jamais appliquée seule.
- **Niveau 2 — appliqué après confirmation** : une confirmation par système, IDs récapitulés.
- **Niveau 3 — JAMAIS** en boucle (envoi externe, dépense, publication) : préparé et signalé.

> Deux modifications demandées en même temps → **refus motivé** : « une variable à la fois,
> sinon la re-mesure est ininterprétable ». On séquence sur deux cycles.

### 5. JOURNALISER
Dans `./rapido-kb/startup/routines-journal.md` : **routine, KPI avant, modification
appliquée, date de re-mesure**. Sans avant/après daté, la boucle n'a pas eu lieu.

## Garde-fous

- **Une variable à la fois** — la règle qui rend la boucle interprétable.
- **Mesure réelle ou rien** : pas de proxy silencieux, pas de KPI de tête, pas de seuil inventé.
- **Cohorte témoin** quand c'est possible (ex. garder l'ancien réglage sur un sous-ensemble)
  pour attribuer l'effet.
- **Autonomie gouvernée** (`reference/autonomie.md`) : niveau 3 jamais automatique.
