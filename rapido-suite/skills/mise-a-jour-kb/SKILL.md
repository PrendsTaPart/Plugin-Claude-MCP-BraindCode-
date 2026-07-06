---
name: mise-a-jour-kb
description: Utiliser quand l'utilisateur veut mettre à jour la base de connaissance, signale un changement de prix, une nouvelle offre, un nouveau concurrent ou toute évolution de l'entreprise. Met à jour le(s) fichier(s) concerné(s) de ./rapido-kb/ et date la modification.
---

# Mise à jour de la base de connaissance

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.
Si `./rapido-kb/` n'existe pas : proposer le skill `onboarding-entreprise`
(rien à mettre à jour).

## Correspondance changement → fichier(s)

| Changement annoncé | Fichier(s) à mettre à jour |
|---|---|
| prix, nouvelle offre, produit abandonné, saisonnalité | `produits-services.md` (+ `propositions-valeur.md` si la promesse change) |
| nouveau différenciateur, preuve, garantie | `propositions-valeur.md` |
| nouveau segment/persona, canal | `cibles-personas.md` |
| nouveau concurrent, riposte | `concurrents.md` |
| logo, couleurs, typos | `charte-graphique.md` |
| ton, accroche qui a marché, mot interdit | `ton-et-accroches.md` |
| seuils, cadence de relance, remises, horaires | `processus-internes.md` |
| équipe, implantation, mission | `entreprise.md` |

Un changement peut toucher plusieurs fichiers — les traiter tous.

## Workflow

1. **Identifier le(s) fichier(s)** concerné(s) via le tableau ci-dessus (en cas
   de doute, demander).
2. **Relire la section** actuelle du fichier avant de la modifier (ne jamais
   écraser à l'aveugle ; le fichier peut avoir été édité à la main).
3. **Poser les questions ciblées** — uniquement ce qui manque pour écrire la
   mise à jour (2-3 questions max ; « je ne sais pas » = insérer le marqueur
   `### À COMPLÉTER`).
4. **Mettre à jour** le contenu (structuré, cohérent avec le style du fichier),
   sans toucher aux sections non concernées.
5. **Dater** : mettre à jour la ligne d'en-tête
   `> Dernière mise à jour : YYYY-MM-DD — <résumé du changement>`.
6. **Récapituler** : fichiers modifiés + résumé de chaque changement ; rappeler
   de committer `./rapido-kb/` si le client le versionne.

## Garde-fous

- Ne jamais inventer la nouvelle valeur (prix, seuil…) : elle vient de
  l'utilisateur ou d'un outil MCP.
- Une mise à jour qui contredit une donnée MCP live (ex. prix différent de
  `list_products`) : signaler l'écart et proposer de corriger AUSSI dans le
  système source via le skill/plugin concerné.
- Suppression d'une section entière : confirmation explicite avant.
