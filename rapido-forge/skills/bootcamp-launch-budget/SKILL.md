---
name: bootcamp-launch-budget
description: "Utiliser quand l'utilisateur veut estime le budget nécessaire au lancement (bootcamp 5 jours StartupsForge — Jour 5)."
---

# Budget de Lancement

**Bootcamp 5 jours — Jour 5**  
**Catégorie** : Finance  
**Framework** : Startup Budget Template  
**Durée** : 35 min

## Objectif

Estime le budget nécessaire au lancement

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Lister les postes de lancement** — produit, marque, site, contenu, ads, juridique, outils
2. **Chiffrer chaque poste** — devis réels ou fourchettes sourcées, pas d'estimation au doigt mouillé
3. **Séparer indispensable / différable** — le lancement minimal viable coûte combien ?
4. **Ajouter 20 % d'imprévu** — systématique, non négociable
5. **Consigner et suivre** — budget validé en KB, dépenses réelles saisies au fil de l'eau (CRM)

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **Stripe** (`stripe`, lecture seule) — montants en CENTIMES, convertir avant tout calcul ; calculs par script (skill `catalogue-kpi`), jamais de tête

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/bootcamp/bootcamp-launch-budget.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapidocrm:gestion-depenses` — saisie réelle des dépenses (TTC = HT + TVA)
