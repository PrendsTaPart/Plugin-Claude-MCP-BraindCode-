---
name: choisir-la-chaine
description: Utiliser quand l'utilisateur change de chaîne YouTube cible — « passe sur la chaîne RapidoCMS », « quelle chaîne est active ? », « mets Formation Braindcode en favorite ». Lecture d'abord, bascule sur accord, et la règle du channel_id explicite rappelée.
---

# Choisir la chaîne de travail

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/chaines.md` — 4 chaînes (FoodEatUp,
  RapidoCMS, RapidoCRM, Formation Braindcode), PAS de chaîne RapidoRH.

## Démarche
1. **Lire** : `yt_list_channels` (noms réels, jamais d'identifiant
   deviné) et `yt_get_channel_status` — active, favorite, divergence.
2. **Basculer SUR ACCORD** (hook garde-chaine : ask) :
   `yt_switch_channel` (change la cible par défaut de TOUS les envois
   suivants) ou `yt_set_favorite_channel` (cible de secours).
3. **La règle qui reste** : même après bascule, toute écriture du plugin
   passe un channel_id EXPLICITE et annonce le NOM de la chaîne — la
   bascule est un confort, pas une sécurité.

## Pièges
- Active ≠ favorite : quand elles divergent, yt_get_channel_status le
  signale — le répéter à l'utilisateur avant toute publication.
- Une vidéo d'académie RapidoRH n'a pas de chaîne dédiée : demander la
  chaîne de destination, ne jamais la déduire.

## Dégradation propre
Chaîne demandée introuvable dans yt_list_channels : la liste réelle est
montrée, rien n'est créé ni supposé.
