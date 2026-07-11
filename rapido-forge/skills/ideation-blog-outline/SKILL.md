---
name: ideation-blog-outline
description: "Utiliser quand l'utilisateur veut rédiger un article de blog complet et optimisé SEO (parcours idéation StartupsForge)."
---

# Blog Outline

**Catégorie** : Idéation  
**Durée** : 60-90 min

## Pourquoi

Un article pilier de 2000+ mots peut générer du trafic SEO pendant des années. C'est un investissement à long terme qui établit ton expertise.

## Objectif

Rédiger un article de blog complet et optimisé SEO.

## Livrable attendu

Article de 1500-2500 mots avec structure SEO, images et CTA

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Choisir le mot-clé principal** — Volume de recherche + intention + difficulté
2. **Analyser le top 10 Google** — Structure, longueur, angles des concurrents
3. **Créer l'outline détaillé** — H1, H2, H3 avec mots-clés LSI
4. **Rédiger section par section** — Introduction hook, corps informatif, conclusion CTA
   > Prompt: Écris la section [H2] de mon article sur [SUJET]. 300 mots, ton [STYLE], inclure exemple concret
5. **Optimiser et formater** — Images, liens internes, meta description

## Pro tips

- La première phrase doit accrocher immédiatement
- Utilise des sous-titres descriptifs (pas juste 'Introduction')
- Inclus 2-3 liens internes vers tes autres pages

## Erreurs fréquentes

- Article trop générique sans angle unique
- Pas assez de profondeur sur le sujet
- Ignorer l'intent de recherche

## Données & serveurs MCP

- **RapidoCMS** (`rapidocms`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/ideation/ideation-blog-outline.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapidocms:generation-article-blog` — article complet SEO/GEO avec score qualité
