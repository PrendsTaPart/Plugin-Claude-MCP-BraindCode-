---
name: selecteur-framework
description: Utiliser quand l'utilisateur décrit un besoin sans nommer de framework (« comment je valide mon idée », « aide-moi à structurer mes prix ») ou demande quel exercice/framework utiliser. Recherche sémantique locale dans les 180 exercices, 3 propositions max, prérequis vérifiés contre le journal.
tags: [organisation]
niveau: debutant
---

# Sélecteur de framework

Le point d'entrée quand on ne sait pas QUEL exercice utiliser : la recherche
choisit, l'utilisateur décide.

## Workflow

1. **Reformuler le besoin en UNE phrase** (avec l'utilisateur si flou) —
   c'est la requête de recherche.
2. **Exécuter la recherche** :
   `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/forge_recherche.py" "<besoin>"`
   (filtres `--tags`, `--niveau`, `--parcours` si le contexte les impose ;
   le script lit le journal `./rapido-kb/startup/forge/parcours.md` et
   marque les prérequis déjà réalisés).
3. **Présenter les 3 MEILLEURS — jamais plus** : pour chacun, POURQUOI lui
   (le lien avec le besoin, en une phrase), son niveau, et ses prérequis
   manquants s'il y en a.
4. **Laisser choisir**, puis lancer le skill choisi.
   **Si des prérequis manquent : proposer D'ABORD le prérequis** — on ne
   saute pas une marche en le cachant (l'utilisateur peut passer outre en
   le disant, le journal le note).

## Garde-fous

- **Scores faibles = le dire.** Si le meilleur score est bas (aucun
  exercice ne correspond vraiment — ex. une demande hors périmètre
  startup), l'annoncer honnêtement et renvoyer vers le bon plugin du
  marketplace au lieu de forcer un framework.
- 3 options maximum — un sélecteur qui propose 10 choix n'a rien
  sélectionné.
- Le script tourne hors-ligne (TF-IDF stdlib) : aucun réseau requis ;
  `--embeddings` n'est qu'un bonus si sentence-transformers est installé
  (repli silencieux sinon).
- Niveau annoncé pour chaque proposition ; en cas de doute sur la maturité
  du projet, renvoyer au diagnostic du `directeur-programme`.
