---
name: trouver-un-tuto
description: Utiliser quand on cherche une fiche précise, que l'utilisateur dit « il y a une vidéo sur les étiquettes DLC ? », « trouve-moi le tuto sur la caisse », « envoie-moi le lien du tutoriel », « c'est sur YouTube ? ». Recherche en langage libre, vérifie que le sujet est couvert, et rend la fiche sous la bonne forme (carte, lien, vidéo).
---

# Trouver un tuto (chercher, vérifier, montrer)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.

## Workflow

1. **`rechercher_tutoriels`** avec la demande en langage libre — le
   paramètre s'appelle `question` (piège vérifié : `q` échoue). Pour « tout
   le module X », préférer `lister_tutoriels` (`moduleSlug` ou
   `categorieSlug`) ; pour partir d'un écran du logiciel, le skill
   `explorer-un-module`.
2. **Aucun résultat probant** → `audit_formation` (éventuellement limité au
   `moduleSlug`) : si le sujet figure dans les manques connus ou n'est pas
   filmé, LE DIRE tel quel — jamais de marche à suivre inventée. Proposer de
   consigner le manque (skill `studio-production-tutos`).
3. **Présenter le résultat** selon le besoin :
   - fiche riche → `carte_tutoriel` (slug ; `vignetteIntegree: true` si le
     client n'affiche pas les images distantes), ou le widget
     `carte-tutoriel` pour une page locale ;
   - lien de la page à partager → `obtenir_lien_tutoriel` ;
   - fichier vidéo / YouTube → `obtenir_video_tutoriel` ;
   - tout le détail (étapes, astuce, prompts) → `obtenir_tutoriel`.
4. **Qui doit voir cette vidéo ?** → `parcours_metier_tutoriel` (slug, et
   `metierSlug` pour situer l'étape précédente/suivante du parcours).
5. Si l'utilisateur veut SUIVRE la leçon : enchaîner sur le skill
   `lecon-guidee` (vignette, quiz, exercice).

## Garde-fous

- Un slug vient toujours d'une réponse du serveur — le hook
  `anti-lien-invente` refuse les slugs en forme d'URL ou hors format.
- Plusieurs résultats proches : proposer les 2-3 meilleurs avec module et
  durée, laisser choisir — ne pas décider à la place de l'utilisateur.
- Sujet absent du catalogue = réponse honnête (« pas encore filmé »), appuyée
  sur `audit_formation`, pas une improvisation.
