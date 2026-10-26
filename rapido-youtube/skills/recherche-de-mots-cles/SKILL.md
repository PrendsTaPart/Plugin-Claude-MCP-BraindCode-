---
name: recherche-de-mots-cles
description: Utiliser quand l'utilisateur cherche ses mots-clés YouTube — « quels mots-clés pour cette vidéo ? », « recherche de requêtes en français », « la concurrence sur ce sujet ». Recherche en français pour la France ; l'estimation de concurrence coûte du quota et attend l'accord.
---

# Recherche de mots-clés

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/quota-et-credits.md`.

## Démarche
1. **Chercher** : `yt_research_keywords` en FRANÇAIS pour la France
   (langue et pays explicites) — volumes et suggestions.
2. **La concurrence** : le paramètre with_competition CONSOMME du quota —
   l'annoncer et ne le passer que sur accord, sur la liste courte.
3. **Choisir** : un mot-clé principal + 2-3 secondaires, par vidéo — le
   principal ira dans le titre et les 150 premiers caractères de la
   description (scripts/seo_checklist.py le vérifie).
4. **Transmettre** : la sélection nourrit `titre-description-seo` et le
   gabarit de miniature (mot-clé en gras).

## Pièges
- Des mots-clés anglais sur une chaîne française : volume flatteur,
  audience fantôme — rester sur le marché réel.
- Ne pas relancer la même recherche avec concurrence « pour voir » : le
  quota du jour est partagé avec les publications.

## Dégradation propre
Pas de résultat sur la niche : le dire et élargir AVEC l'utilisateur
(terme parent), jamais en silence.
