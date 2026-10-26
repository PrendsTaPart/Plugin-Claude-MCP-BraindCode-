---
name: tests-ab-miniatures
description: Utiliser quand l'utilisateur teste deux miniatures — « lance un A/B sur cette vidéo », « quelle miniature gagne ? », « résultat du test ». Comparaison d'abord, test sur accord (48 h par phase), verdict restitué exactement comme l'outil le donne.
---

# Tests A/B de miniatures

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (loi n° 7).

## Démarche
1. **Préparer** : deux miniatures prêtes (skill `atelier-miniatures`),
   `yt_compare_thumbnails` (gratuit) pour vérifier qu'elles diffèrent
   assez pour apprendre quelque chose.
2. **Lancer SUR ACCORD** (hook garde-public : la miniature visible
   change) : `yt_start_ab_test` — 48 h par phase par défaut, annoncées.
3. **Lire** : `yt_get_thumbnail_insights` — et restituer EXACTEMENT le
   verdict de l'outil : gagnant seulement au-delà de 95 % de confiance
   ET 100 impressions par phase ; sinon « non concluant, miniature A
   restaurée ». Une donnée absente n'est JAMAIS comptée comme zéro.
4. **Capitaliser** : le motif gagnant (couleur, visage, texte) nourrit
   le kit et les prochaines générations — widget comparateur-miniatures.

## Pièges
- Conclure à mi-test parce que « B a l'air devant » : non — le serveur
  tranche aux seuils, pas l'impression.
- Tester deux miniatures quasi identiques n'apprend rien : la
  comparaison préalable le dit.

## Dégradation propre
Trop peu d'impressions sur la chaîne : le dire — un A/B sur 40
impressions ne conclura jamais, mieux vaut publier et mesurer.
