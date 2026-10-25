---
name: mesurer-la-demo
description: Utiliser quand la démo publiée se mesure — « combien de visiteurs sur ma démo ? », « les stats de la vitrine », « donne la mesure de la boucle du projet ». Analytics Lovable réels, présentés comme KPI de vitrine et proposés comme source de la boucle.
---

# Mesurer la démo (analytics réels)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/methode-build.md` (étape 10 : la
  mesure).

## Démarche
1. **Mesurer** : `get_project_analytics` (visiteurs, pages vues, rebond,
   durée — avec répartitions) et `get_project_analytics_trend` (temps
   réel, 30 dernières minutes) sur le projet Lovable PUBLIÉ.
2. **Restituer tel quel** : chiffres datés, périmètre dit (la démo, pas
   le produit) ; un projet non déployé n'a pas d'analytics — le dire.
3. **KPI de vitrine** : ces chiffres alimentent la vitrine (fréquentation
   de la démo) et le pitch — sans extrapolation.
4. **Source de boucle** : proposer cette mesure comme source du KPI de la
   routine (skill `routine-et-boucle`) quand l'objectif du projet est
   l'usage de la démo — cible et alerte posées avec l'humain.

## Pièges
- Confondre visiteurs de la démo et utilisateurs du produit : deux
  mondes ; l'un ne prédit pas l'autre.

## Dégradation propre
Analytics indisponibles (projet non publié, données vides) : « — », et la
boucle prend une autre source réelle ou attend.
