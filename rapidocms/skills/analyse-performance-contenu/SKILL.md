---
name: analyse-performance-contenu
description: Utiliser quand l'utilisateur demande quels posts marchent, une analyse de ses stats ou un bilan du mois. Lit les insights réels, identifie les patterns gagnants et livre 3 recommandations actionnables.
---

# Analyse de performance du contenu

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
règles pendant toute l'exécution (IDs, données, formats, erreurs).

## Workflow (lecture seule)

1. **Périmètre** — préciser la période (défaut : 30 derniers jours) et les
   réseaux analysés.
2. **Collecter les données réelles** :
   - `list_scheduled_posts` (`start_date`/`end_date` `Y-m-d`, filtre `social`)
     pour retrouver les posts de la période ;
   - `post_insights` (`post_ids`, MAX 10 par appel — découper en lots) pour les
     métriques par post ;
   - `ingishts_campagne` (`campagne_id`) pour les campagnes de la période
     (`list_campagnes` pour les retrouver).
   Aucun chiffre inventé : un post sans insights est signalé, pas estimé.
3. **Identifier les PATTERNS gagnants** — croiser les posts performants sur
   4 axes :
   - **Format** : image vs vidéo vs texte — lequel sur-performe ?
   - **Sujet/pilier** : quel thème engage le plus ?
   - **Créneau** : jour et heure des meilleurs posts (ces données priment sur
     les créneaux génériques du `community-manager`) ;
   - **Réseau** : où l'audience répond-elle le mieux ?
   Comparer au MÊME indicateur (engagement, portée…) et ne conclure un pattern
   qu'avec au moins 3 posts concordants — sinon le dire (« signal faible »).
4. **Restituer le bilan** :
   ```
   📈 BILAN CONTENU — {période}
   Top 3 posts (réseau, format, pilier, chiffres)
   Flop 3 posts (et hypothèse de cause)
   Patterns : format / sujet / créneau / réseau
   🎯 3 RECOMMANDATIONS pour le mois suivant
   ```
5. **3 recommandations ACTIONNABLES, pas plus** — chacune : quoi changer +
   pourquoi (le chiffre qui la justifie) + comment (le skill à utiliser, ex.
   `calendrier-editorial` pour re-répartir les piliers, `prompt-engineering-visuel`
   si le format image sous-performe).

## Garde-fous

- Skill en LECTURE SEULE : ne rien créer/modifier/annuler ; les ajustements
  passent par `calendrier-editorial` sur demande de l'utilisateur.
- Distinguer corrélation et cause : un bon post au bon créneau ne prouve pas le
  créneau — le noter quand l'échantillon est petit.
- Toujours indiquer la période, les réseaux couverts et les posts exclus faute
  de données.
