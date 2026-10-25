---
name: blog
description: Utiliser quand l'utilisateur tient son blog via Prospector Hub — « planifie un article de blog », « passe l'article en ligne », « liste les brouillons du blog ». add/update_blog_post, passage au statut publié sur accord explicite.
---

# Blog (articles planifiés)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Démarche
1. **Lire** : `list_blog_posts` (période, statut) — brouillons, planifiés,
   publiés.
2. **Créer** : `add_blog_post` (title, content, image_url, scheduled_at,
   status BROUILLON par défaut). La rédaction longue se travaille avec le
   plugin rapidocms (skill `generation-article-blog`) quand il est
   installé — ce skill-ci planifie et met en ligne côté Prospect.
3. **Retoucher** : `update_blog_post` (contenu, date, image).
4. **Publier** : passage `status: "publie"` SEULEMENT après relecture
   montrée et accord explicite (hook garde-publication). Montrer le titre,
   l'accroche et la date avant.
5. **Supprimer** : `delete_blog_post` sur confirmation (définitif).

## Pièges
- Un chiffre, un prix ou une promesse dans un article suit les mêmes
  règles que partout : sourcé ou absent.
- Pas de lien de lead magnet temporaire dans un article (lien signé qui
  expire) : pointer la page de capture.

## Dégradation propre
Pas de contenu prêt : planifier le créneau (brouillon daté) plutôt que
publier un texte bâclé.
