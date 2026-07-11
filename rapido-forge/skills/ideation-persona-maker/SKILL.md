---
name: ideation-persona-maker
description: "Utiliser quand l'utilisateur veut créer 2-3 personas détaillés représentant ses clients idéaux avec leurs motivations, frustrations et comportements (parcours idéation StartupsForge)."
---

# Persona Maker

**Catégorie** : Idéation  
**Durée** : 20-30 min

## Pourquoi

Le persona est la fondation de TOUTES tes décisions produit, marketing et commerciales. Sans une compréhension profonde de ton client idéal, tu risques de créer un produit que personne ne veut acheter. 82% des startups échouent car elles ne comprennent pas leur marché.

## Objectif

Créer 2-3 personas détaillés représentant tes clients idéaux avec leurs motivations, frustrations et comportements.

## Livrable attendu

Fiches persona complètes avec nom, photo, démographie, objectifs, douleurs et comportements d'achat

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Identifier les données démographiques** — Âge, sexe, localisation, profession, niveau de revenus, situation familiale
2. **Lister les objectifs et motivations** — Que cherche à accomplir ton persona ? Quels sont ses rêves professionnels/personnels ?
   > Prompt: Liste 5 objectifs principaux pour un [MÉTIER] âgé de [ÂGE] ans qui cherche à [BESOIN]
3. **Identifier les frustrations (pain points)** — Quels problèmes l'empêchent d'atteindre ses objectifs ? Qu'est-ce qui l'énerve au quotidien ?
   > Prompt: Quelles sont les 5 plus grandes frustrations d'un [PERSONA] concernant [DOMAINE] ?
4. **Analyser les comportements d'achat** — Où cherche-t-il des solutions ? Quels critères de décision ? Budget typique ?
5. **Créer la fiche finale** — Consolide toutes les infos dans une fiche structurée avec photo et citation fictive

## Pro tips

- Commence par UN seul persona principal, pas 5 - tu pourras en ajouter plus tard
- Base-toi sur des données réelles (interviews, analytics) et non sur des suppositions
- Donne un vrai prénom à ton persona pour humaniser tes discussions d'équipe
- Inclus une citation fictive qui résume sa frustration principale

## Erreurs fréquentes

- Créer un persona trop générique qui pourrait s'appliquer à tout le monde
- Ne pas valider avec de vrais utilisateurs potentiels
- Confondre persona (qui achète) et utilisateur (qui utilise)
- Oublier les canaux de communication préférés

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/ideation/ideation-persona-maker.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-suite:dossier-startup-360` — persona consigné dans ./rapido-kb/startup/
