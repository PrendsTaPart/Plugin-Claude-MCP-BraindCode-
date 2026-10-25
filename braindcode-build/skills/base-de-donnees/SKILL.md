---
name: base-de-donnees
description: Utiliser quand l'extension Build a besoin de sa base — « active la base du projet », « vérifie les données en SQL », « ajoute une table ». get_database_status d'abord, activation sur accord, SELECT libre, toute écriture SQL montrée et confirmée.
---

# Base de données du projet Lovable

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/regles-lovable.md`.

## Démarche
1. **État** : `get_database_status` — provisionnée ou non, avant toute
   promesse d'écran « avec données ».
2. **Activer** : `enable_database` SUR ACCORD (hook
   garde-lovable-ecritures) — l'activation engage le projet.
3. **Vérifier** : `query_database` en SELECT pour les contrôles (données
   de recette, volumes, cohérence) — c'est la voie libre.
4. **Écrire** : toute requête SQL d'écriture est MONTRÉE TEXTUELLEMENT et
   confirmée avant d'être lancée (le hook demande ; DROP et TRUNCATE sont
   refusés net). Le schéma lui-même se construit de préférence par
   prompts Lovable (migrations outillées), pas en SQL manuel.
5. **Consigner** : la structure retenue va dans le cahier des charges
   (save_project_spec) et le knowledge du projet.

## Pièges
- Des données personnelles de test réalistes n'ont rien à faire dans une
  base de démo : données fictives marquées comme telles.
- query_database sur la base de PROD d'un produit Rapido : hors périmètre
  — ici on ne touche que la base du projet Lovable.

## Dégradation propre
Base non provisionnée et activation refusée : le dire et maquetter les
écrans sur données statiques fictives, marquées.
