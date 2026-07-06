# Attributions — skills externes du plugin rapido-suite

Skills importés depuis **anthropics/knowledge-work-plugins**
(https://github.com/anthropics/knowledge-work-plugins), pack `small-business`,
commit `564d560c8ea71505a08695c42e9e9bf994e65c7a`, licence **Apache License 2.0** (copie du LICENSE dans
chaque dossier de skill).

| Skill | Chemin d'origine |
|---|---|
| `monday-brief` | `small-business/skills/monday-brief` |
| `business-pulse` | `small-business/skills/business-pulse` |
| `cash-flow-snapshot` | `small-business/skills/cash-flow-snapshot` |
| `invoice-chase` | `small-business/skills/invoice-chase` |

Modifications locales : mention MCP/KB ajoutée en fin de `description` ; section « Adaptation Rapido » ajoutée en tête de chaque SKILL.md (mapping QuickBooks/PayPal/HubSpot/Slack… vers les équivalents Rapido).

Fusion (pas de copie) : `friday-brief` (`small-business/skills/friday-brief`) a été FUSIONNÉ dans le skill maison `revue-hebdo-business` (comparaison vs période précédente, top ventes, format « wins & watches ») au lieu d'être copié — recoupement trop fort.

## Ajout du 2026-07-06 — anthropics/skills

| Skill | Dépôt d'origine | Licence | Date |
|---|---|---|---|
| `skill-creator` | anthropics/skills (commit `9d2f1ae1`) | Apache 2.0 (LICENSE.txt du skill, conservé) | 2026-07-06 |

Sert à créer et améliorer les skills maison de la marketplace (le skill
`onboarding-restaurateur` de foodeatup a été créé avec sa méthodologie).
Modification locale du 2026-07-06 : deux noms de scripts d'EXEMPLE cités dans
la prose (`create_docx.py`, `build_chart.py`) — absents de la source, vérifié
sur un clone frais — reformulés en description générique pour ne plus être
pris pour des références de fichiers réelles. Aucun autre changement.

> Note du 2026-07-06 : la description du frontmatter de chaque skill listé ici a été traduite en français (« Utiliser quand… ») pour le déclenchement — le corps du skill reste inchangé. Une clé `source:` de traçabilité a été ajoutée au frontmatter.
