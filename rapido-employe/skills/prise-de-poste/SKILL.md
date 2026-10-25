---
name: prise-de-poste
description: Utiliser quand Claude employé démarre sa journée de travail, que l'utilisateur dit « prends ton poste », « démarre ta journée », « relis ton cadre », ou au début de toute session de travail commercial FoodEatUp. Relit le brief et le plan de travail du jour dans l'Academy et écrit l'instantané du cadre que tous les gardes relisent.
---

# Prise de poste (le cadre d'abord, toujours)

Famille engagée : **apprendre** (lectures Academy + un fichier d'état local).

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`. Si
`./rapido-kb/` existe, garder `entreprise.md` sous la main (zone, ton).

## Workflow

1. **`get_claude_brief`** — qui est l'utilisateur, progression, prochaine
   mission, points faibles, mémoire retenue, savoir d'équipe, décisions du
   responsable, règles maison. Saluer et restituer en 3 lignes.
2. **`get_work_plan`** — arrêt/marche, budget (mensuel, plafond et dépense du
   jour, restant), niveau d'autonomie des 8 familles, quotas du jour,
   prochaine mission, routines à exécuter, journée type.
3. **Agent arrêté** (`actif: false`) : le dire, produire uniquement le
   rapport (skill `rapport-de-fin-de-journee`) et s'arrêter là. Les gardes
   refusent de toute façon toute écriture.
4. **Écrire l'instantané du cadre** dans `.claude/state/cadre-employe.json`
   (créer le dossier au besoin) avec exactement :
   `horodatage` (UTC ISO, maintenant), `actif`, `autonomie` (famille →
   niveau), `quotas_jour`, `budget` — tels que renvoyés, sans retouche.
   C'est ce fichier que les hooks relisent ; périmé après 24 h.
5. **Restituer le plan du jour** : niveaux par famille, quotas restants,
   budget restant, prochaine mission, routines dues — puis proposer le widget
   `plan-de-travail-du-jour` (`${CLAUDE_PLUGIN_ROOT}/scripts/render_widget.py`).
6. Enchaîner selon la journée type renvoyée : chiffres d'abord (skill
   `point-du-matin`), puis apprentissage (skill `chemin-de-formation`,
   30 min au plus), puis routines (skill `executer-mes-routines`).

## Garde-fous

- Le cadre vient de `get_work_plan` du jour — jamais d'une session passée ni
  d'un souvenir. Pas de cadre écrit = gardes en confirmation sur tout.
- L'instantané reprend la réponse telle quelle : on ne « corrige » jamais son
  propre niveau d'autonomie (hook garde-auto-gouvernance en filet).
- Serveur Academy absent : le dire et s'arrêter — sans cadre, pas d'employé.
