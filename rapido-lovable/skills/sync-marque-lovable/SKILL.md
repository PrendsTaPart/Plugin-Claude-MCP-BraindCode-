---
name: sync-marque-lovable
description: Utiliser quand l'utilisateur veut synchroniser sa marque sur Lovable ou appliquer sa charte à toutes ses apps. Pousse la charte, le ton et les offres de la KB dans le knowledge et un skill du workspace Lovable — toute app future les respecte.
---

# Synchronisation de marque (KB × Lovable)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/architecture-lovable.md`. Prérequis :
`./rapido-kb/` existante — sinon proposer d'abord l'onboarding
(`onboarding-entreprise`, plugin rapido-suite) : on ne synchronise pas une
marque vide.

## Workflow

1. **Lire la KB** — `charte-graphique.md` (hex, typos, logos, interdits),
   `ton-et-accroches.md` (voix, vocabulaire, mots interdits),
   `produits-services.md` + `propositions-valeur.md` (offres, promesse).
   Les `### À COMPLÉTER` ne se synchronisent pas : lister ce qui manque et
   proposer de compléter d'abord (`mise-a-jour-kb`).
2. **Lire l'existant — OBLIGATOIRE avant d'écrire** —
   `get_workspace_knowledge` (`workspace_id` via `list_workspaces`) :
   `set_workspace_knowledge` REMPLACE TOUT (max 10 000 caractères).
3. **Fusionner** — conserver les instructions existantes non liées à la
   marque (conventions de code, préférences techniques), y intégrer la
   section marque : palette hex exacte, typos, ton et mots interdits, règles
   d'usage du logo, offres phares. Rester sous 10 000 caractères (prioriser :
   charte > ton > offres).
4. **Valider puis écrire** — montrer le knowledge fusionné à l'utilisateur,
   puis `set_workspace_knowledge` (`workspace_id`, `content`).
5. **Créer le skill workspace** — `create_workspace_skill`
   (`skill_name: "charte-<société>"`, `markdown` = SKILL.md complet avec
   frontmatter `name` identique + `description`, corps = la charte applicable
   par l'agent Lovable : couleurs, composants, ton, do/don't).
   Réservé aux admins/owners du workspace — si refus de droits, le dire et
   proposer que l'admin le fasse.
6. **Vérifier** — `get_workspace_knowledge` relu + `list_workspace_skills` ;
   annoncer : toute app future construite sur ce workspace respectera la
   marque sans qu'on la répète dans chaque message.

## Garde-fous

- JAMAIS de `set_workspace_knowledge` sans `get_workspace_knowledge` + fusion
  + validation utilisateur (remplacement total).
- Resynchroniser après chaque évolution de la charte dans la KB
  (`mise-a-jour-kb` → proposer ce skill dans la foulée).
- Le knowledge ne contient ni secrets ni données personnelles — c'est de
  l'instruction de marque, pas des données.
