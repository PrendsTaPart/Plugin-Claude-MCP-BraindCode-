---
name: ideation-logo-prompt
description: "Utiliser quand l'utilisateur veut créer un logo professionnel représentant l'identité de sa marque (parcours idéation StartupsForge)."
---

# Logo Prompt

**Catégorie** : Idéation  
**Durée** : 30-45 min

## Pourquoi

Ton logo est le symbole visuel de ta marque. C'est souvent la première chose que les clients voient et retiennent. Un logo professionnel augmente la confiance de 75% selon les études.

## Objectif

Créer un logo professionnel représentant l'identité de ta marque.

## Livrable attendu

Logo final en plusieurs formats (PNG, SVG) + déclinaisons (couleur, noir, blanc)

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Définir le brief créatif** — Style (moderne, vintage, minimal), couleurs, symboles à éviter
2. **Générer le prompt Midjourney** — Décris précisément le logo souhaité
   > Prompt: Minimal logo for [STARTUP], [STYLE], clean lines, vector, white background, no text --v 6
3. **Générer 20+ variations** — Teste différents styles et couleurs
4. **Sélectionner le top 3** — Vote en équipe ou avec des prospects
5. **Affiner le choix final** — Vectorise et décline en plusieurs formats

## Pro tips

- Un bon logo fonctionne en noir et blanc
- Teste ton logo en très petit (favicon) et très grand (panneau)
- Évite les tendances trop actuelles qui vieilliront mal

## Erreurs fréquentes

- Logo trop complexe ou détaillé
- Dépendance à une couleur spécifique
- Copier un logo existant (risques juridiques)

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **Canva** (`canva`, via le plugin `rapido-canva`) pour la production graphique

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/ideation/ideation-logo-prompt.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapidocms:prompt-engineering-visuel` — méthode de prompt image
- `rapidocms:prompts-visuels-pro` — protocole zéro faute pour texte incrusté
