---
name: cahier-des-charges
description: Utiliser quand l'utilisateur rédige le cahier des charges d'une extension Build — « écris le CDC », « quels outils MCP le produit expose vraiment ? », « enregistre la spec ». get_spec_prompt, découverte réelle par tools/list, rédaction complète, save_project_spec.
---

# Cahier des charges (sur outils RÉELS)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/methode-build.md` (étape 02 : rien
  supposé) ;
- `${CLAUDE_PLUGIN_ROOT}/reference/carte-des-interconnexions.md`.

## Démarche
1. **Le gabarit** : `get_spec_prompt` — la structure attendue par Build.
2. **Découverte RÉELLE du MCP produit** : tools/list du serveur concerné
   (foodeatup, rapidocrm, rapidocms ou rapidorh, déclarés dans ce plugin) —
   familles de données, actions possibles, actions sensibles. AUCUN outil
   supposé ; une capacité absente est SIGNALÉE dans le cahier, pas
   contournée en silence.
3. **Compléter pour FoodEatUp** : `documentation_api_foodeatup` (serveur
   tutoriel) pour le fonctionnement technique, et les tutoriels pour les
   parcours métier réels.
4. **Rédiger** : périmètre, parcours, écrans, données, outils MCP (ceux du
   relevé), actions sensibles et leurs validations, sécurité (critère
   n° 3), paiement, jalons, critères de recette TESTABLES.
5. **Enregistrer** : `save_project_spec` — en plusieurs passes si le
   document est long ; relire ce que le serveur a accepté.

## Pièges
- Un cahier qui cite un outil inexistant produira des prompts Lovable
  faux : le relevé tools/list du jour fait foi, en cache pour la session.
- Les critères de recette non testables (« l'app est agréable ») ne
  passent pas l'étape tests : chaque critère a une vérification concrète.

## Dégradation propre
MCP produit non connecté : rédiger le cahier sur la partie indépendante et
marquer le volet outils « à relever en session connectée » — jamais de
liste d'outils imaginée.
