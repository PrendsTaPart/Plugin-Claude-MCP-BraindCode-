---
name: dossier-startup-360
description: Utiliser quand l'utilisateur veut structurer les données de sa startup, créer son dossier fondateur (vision, persona, marché, offre, pitch), ou donner aux agents IA le contexte complet de l'entreprise. Construit et maintient ./rapido-kb/startup/ et publie les documents dans la bibliothèque CMS et les projets RH.
---

# Dossier startup 360 — la mémoire de l'entreprise pour les agents IA

Modèle inspiré des parcours d'incubation IA (type StartupForge : vision board,
validation marché, identité, pitch) : TOUT ce qu'un agent doit savoir sur la
startup vit dans `./rapido-kb/startup/`, en fichiers markdown versionnés.
Chaque agent des plugins Rapido lit ce dossier AVANT de produire.

## Étape 0 — État des lieux

1. Lire `./rapido-kb/startup/` s'il existe — lister ce qui est rempli / vide.
2. Croiser avec les données live : `get_company` + `get_brand` (rapidocms),
   `get_dashboard_general_stats` (rapidocrm), `list_products`. Signaler tout
   écart entre la KB et les données API : la donnée LIVE fait foi pour les
   chiffres, la KB fait foi pour la stratégie.
3. Ne JAMAIS remplir un fichier avec des hypothèses : chaque section vide se
   remplit par les réponses de l'utilisateur ou les données MCP, sinon elle
   reste marquée `À COMPLÉTER`.

## Structure du dossier — 8 fichiers

```
./rapido-kb/startup/
├── 01-vision.md          # Vision, mission, valeurs, problème résolu (vision board)
├── 02-persona.md         # Cible(s) : démographie, douleurs, canaux, objections
├── 03-marche.md          # Taille, tendances, concurrents (forces/faiblesses/prix)
├── 04-offre.md           # Produits/services, prix, proposition de valeur unique
├── 05-identite.md        # Marque : ton, charte (renvoi charte-graphique.md), interdits
├── 06-traction.md        # Chiffres clés, jalons, preuves sociales — daté, sourcé MCP
├── 07-pitch.md           # Elevator pitch 30 s, pitch 3 min, structure du deck
└── 08-roadmap.md         # Objectifs trimestre, chantiers en cours, prochaine étape
```

Chaque fichier commence par `> Dernière mise à jour : [date] — source : [user/MCP]`.

## Workflow de création (interview guidée)

1. **Interviewer par bloc** — un fichier à la fois, questions courtes, dans
   l'ordre 01 → 08. Reformuler chaque réponse et la faire valider avant de
   l'écrire. La proposition de valeur (04) se teste : « En une phrase :
   pour [persona], [offre] est le seul [catégorie] qui [bénéfice unique]. »
2. **Compléter par les MCP** : traction (06) depuis rapidocrm
   (`get_revenue_summary`, `get_top_clients`) et rapidocms (`post_insights`) —
   chiffres datés et sourcés, jamais de mémoire.
3. **Écrire les fichiers** dans `./rapido-kb/startup/`.

## Publication des documents

Quand un bloc est validé, produire le document propre correspondant
(one-pager vision, fiche persona, executive summary, pitch) puis :
- **Bibliothèque CMS** : `upload_file_tool` (rapidocms — `type: "document"`,
  `name` explicite ex. « Pitch — v2026-07 », `file_url`) pour qu'il serve aux
  contenus et campagnes.
- **Projets RH** : rattacher au projet concerné via RapidoRh —
  `create-project-link-tool` (URL du document uploadé) pour que l'équipe le
  trouve depuis son Kanban. Vérifier le projet cible avec
  `get-projects-list-tool` avant, ne jamais deviner un ID.

## Usage par les autres agents (règle transverse)

Tout agent Rapido (directeur-general, responsable-marketing, prompt-designer,
directeur-commercial…) doit, si `./rapido-kb/startup/` existe :
- lire 01-vision, 02-persona et 05-identite avant toute production de contenu ;
- lire 04-offre avant tout contenu BOFU ou commercial (les prix viennent de
  là ou du MCP, jamais inventés) ;
- citer sa source (« persona — rapido-kb/startup/02-persona.md »).

## Maintenance

- Revue mensuelle : lors de `revue-hebdo-business` ou `comite-de-direction`,
  vérifier que 06-traction et 08-roadmap datent de moins de 30 jours —
  sinon proposer la mise à jour (skill `mise-a-jour-kb`).
- Tout pivot (cible, prix, positionnement) déclenche la mise à jour des
  fichiers impactés AVANT toute nouvelle campagne.

## Pièges

- Remplir le dossier « pour faire joli » avec des généralités : chaque ligne
  doit être actionnable par un agent (un persona sans douleurs ni objections
  ne sert à rien à `redaction-commerciale`).
- Dupliquer la charte graphique dans 05-identite : y mettre le TON et les
  interdits, renvoyer vers `./rapido-kb/charte-graphique.md` pour le visuel.
- Chiffres de traction sans date ni source : invérifiables, donc inutilisables.

## Squelette initial

À créer dans le répertoire de travail du CLIENT (jamais dans le plugin) au
premier passage du workflow :

- `01-vision.md` — vision, mission, valeurs et problème résolu, en phrases courtes validées par le fondateur.
- `02-persona.md` — une fiche par cible : démographie, douleurs, déclencheurs d'achat, canaux, objections types.
- `03-marche.md` — taille et tendances du marché, tableau concurrents (forces, faiblesses, prix, notre parade).
- `04-offre.md` — produits/services avec prix, et la proposition de valeur unique en une phrase testée.
- `05-identite.md` — ton de voix, vocabulaire et interdits de la marque (le visuel reste dans charte-graphique.md).
- `06-traction.md` — chiffres clés datés et sourcés (MCP), jalons atteints, preuves sociales.
- `07-pitch.md` — elevator pitch 30 s, pitch 3 min, plan du deck slide par slide.
- `08-roadmap.md` — objectifs du trimestre, chantiers en cours, prochaine étape unique et datée.
