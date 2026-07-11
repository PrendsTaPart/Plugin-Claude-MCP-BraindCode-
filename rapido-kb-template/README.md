# rapido-kb/ — Base de connaissance de votre entreprise

> Template vierge. Copiez ce dossier à la racine de votre workspace Claude Code,
> renommez-le `rapido-kb/`, puis remplissez-le.

## À quoi ça sert
Ce dossier contient le **contexte propre à votre entreprise** (offre, prix, charte,
ton, concurrents…). Tous les skills et agents du plugin le lisent en priorité pour
agir « comme un expert de votre entreprise » et non de façon générique.

## Règles d'or
1. Ce dossier vit dans VOTRE dépôt, jamais dans le dossier du plugin (qui reste
   générique et se met à jour sans écraser vos données).
2. Committez-le dans votre git : il est versionnable et éditable à la main.
3. Ne mettez JAMAIS de secret ici (token, mot de passe, IBAN). Prix et marges OK.
4. Vous ne savez pas remplir un champ ? Laissez le marqueur `### À COMPLÉTER`.
   Ne mettez pas de fausse donnée : un trou assumé vaut mieux qu'une info inventée.

## Deux façons de le remplir
- **Automatique + interview** : lancez le skill d'onboarding (voir
  PROMPTS-CLAUDE-CODE.md). Il pré-remplit tout ce que vos MCP savent déjà, puis
  vous pose seulement les questions restantes.
- **À la main** : éditez directement les 8 fichiers markdown.

## Mise à jour
Un prix change, un concurrent apparaît ? Éditez le fichier concerné, ou demandez
« mets à jour ma base de connaissance : … ». Datez toujours l'en-tête.

## Après l'onboarding : le prompt de pilotage
Une fois `./rapido-kb/` rempli, **PROMPT-PILOTAGE.md** contient le prompt maître
qui lance le Loop Engine sur toute l'entreprise (Sense → Plan → Act → Feed →
Report), sa version courte et les variantes par moment de la semaine (lundi,
sentinelle quotidienne, board mensuel, vidéo, business pulse). Équivalent sans
rien coller : dites « **Pilote mon entreprise** » — le skill
`rapido-suite:pilotage-entreprise` encode la même boucle.

## Les 8 fichiers
| Fichier | Contenu |
|---|---|
| entreprise.md | identité, équipe, implantations, fuseau, devise, IDs par serveur |
| produits-services.md | offres, prix, marges cibles, best-sellers, saisonnalité |
| propositions-valeur.md | promesse par cible, différenciateurs, preuves, garanties |
| cibles-personas.md | segments clients, pains, déclencheurs, canaux |
| charte-graphique.md | hex, typos, logos, do/don't |
| ton-et-accroches.md | ton de voix, vocabulaire, mots interdits, accroches gagnantes |
| processus-internes.md | seuils (food cost, marges), relances, plafond pub, automatisations |
| concurrents.md | concurrents, leur force, vos parades |
