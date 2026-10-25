---
name: video-courte
description: Utiliser quand une vidéo courte se fabrique dans Plan'It, que l'utilisateur dit « fais-moi un Reel sur… », « génère une vidéo de 30 secondes », « où en est ma vidéo ». Calcule et annonce le coût en crédits par script, compose, suit l'état, puis passe le relais à rapidocms pour un brouillon — jamais de publication directe.
---

# Vidéo courte (le coût d'abord, le brouillon ensuite)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow

1. **Le coût, par script** :
   `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/credits_autonomie.py video <durée_s>`
   — formule affichée : **crédits = max(5, ⌈durée/2⌉)** (1 crédit par
   tranche de 2 s, 5 minimum ; durée 10 à 60 s). Annoncer le coût ET le
   solde (get_kpi_home) AVANT de composer.
2. **`compose_video`** sur l'accord — sujet, format (Reel/TikTok/Short),
   durée, voix. La réponse donne l'URL, un titre, une légende, des hashtags.
   (Outil payant : le hook garde-planit demande confirmation.)
3. **`get_composed_video`** — en cours, prête ou en échec ; retrouver l'URL
   et la légende.
4. **Le relais** : la vidéo prête part en BROUILLON via le plugin
   `rapidocms` (sa chaîne brouillon → accord → programmation). JAMAIS de
   publication directe depuis ce skill — Plan'It fabrique, le CMS publie
   après validation humaine.

## Garde-fous

- Durée hors 10-60 s : la demander à nouveau, pas d'arrondi silencieux.
- Le coût annoncé est celui de la formule — pas d'« environ » ; solde
  insuffisant = le dire et s'arrêter (jamais une promo inventée pour
  compenser : `list_promotions` fait foi).
- La légende et les hashtags renvoyés se relisent avant tout brouillon
  (aucun chiffre non sourcé).
