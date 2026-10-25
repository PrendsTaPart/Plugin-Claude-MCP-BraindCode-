---
name: skills-dans-lovable
description: Utiliser quand les consignes d'espace Lovable se gèrent — « pousse la charte en skill d'espace », « quelles consignes partagées existent ? », « mets à jour la skill sécurité MCP ». Lecture avant toute modification, écritures sur accord, consignes utiles à tous les projets.
---

# Skills d'espace Lovable (consignes partagées)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/regles-lovable.md` — c'est précisément
  ce qui mérite d'être poussé en consigne d'espace.

## Démarche
1. **Lire d'abord** : `list_workspace_skills`, puis `get_workspace_skill`
   sur CHAQUE skill à modifier — on ne remplace jamais un contenu qu'on
   n'a pas lu.
2. **Écrire SUR ACCORD** (hook garde-lovable-ecritures) :
   `create_workspace_skill` pour une consigne nouvelle,
   `update_workspace_skill` pour une évolution (diff montré avant) —
   candidates : la charte du produit, les règles de sécurité MCP (côté
   serveur, pas de secret front), les règles Lovable maison.
3. **Supprimer** : `delete_workspace_skill` sur confirmation explicite
   seulement.
4. **Portée dite** : une skill d'espace touche TOUS les projets de
   l'espace — l'annoncer avant chaque écriture, avec l'espace concerné
   (`get_me` pour les rôles : admin requis).

## Pièges
- Une consigne d'espace contradictoire avec le knowledge d'un projet crée
  des builds incohérents : vérifier les deux niveaux.

## Dégradation propre
Rôle insuffisant sur l'espace : le dire et livrer la consigne prête à
coller pour un admin.
