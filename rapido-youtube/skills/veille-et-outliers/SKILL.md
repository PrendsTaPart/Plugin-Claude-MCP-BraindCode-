---
name: veille-et-outliers
description: Utiliser quand l'utilisateur fait sa veille YouTube — « trouve les outliers de la semaine », « quelles vidéos surperforment dans ma niche ? », « idées du jour ». Suivi de chaînes, outliers filtrés, motifs analysés, idées adaptées - on s'inspire, on ne copie jamais.
---

# Veille et outliers

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Démarche
1. **Le panel** : `yt_track_channel` pour suivre une chaîne (sur
   demande), `yt_list_tracked_channels` pour le panel courant.
2. **Les outliers** : `yt_find_outliers` avec les filtres réels —
   fenêtre temporelle, format (long/Short), score minimal,
   taille maximale des chaînes (les petits qui percent valent plus que
   les géants).
3. **Le motif** : `yt_analyze_outlier_pattern` sur les retenus — qu'est-ce
   qui fait marcher CE format (angle, promesse, miniature, durée).
4. **Les idées** : `yt_get_daily_ideas` — adaptées à la chaîne, croisées
   avec les motifs relevés.
5. **Restitution** : widget outliers (multiplicateur, vues/heure, piste
   d'adaptation) — chaque piste est une ADAPTATION à nos sujets, jamais
   une copie de titre, de miniature ou de concept signé.

## Pièges
- Un multiplicateur énorme sur une chaîne géante dit peu : filtrer par
  taille de chaîne d'abord.
- La veille nourrit `recherche-de-mots-cles` et `titre-description-seo` —
  pas de publication directe depuis une idée brute.

## Dégradation propre
Panel vide : le dire et proposer 3-5 chaînes à suivre (choix humain),
jamais un panel auto-constitué.
