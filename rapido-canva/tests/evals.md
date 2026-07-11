# Évals — plugin rapido-canva (1.0.1)

## Déclenchements

| # | Phrase | Attendu |
|---|---|---|
| C1 | « Fais-moi un visuel Instagram pour la promo » | `visuels-sociaux-canva` — design au format natif du réseau, charte depuis `./rapido-kb/charte-graphique.md`, export PNG puis enchaînement pipeline RapidoCMS (brouillon, planification confirmée) |
| C2 | « Crée mon menu à imprimer » | `menu-restaurant-design` — contenu RÉEL depuis FoodEatUp (plats, prix — jamais inventés), design Canva, export PDF |
| C3 | « Prépare la présentation du CODIR » | `presentation-codir` — chiffres sourcés (MCP/KB), 1 slide par domaine, export |
| C4 (frontière) | « Rédige le post qui accompagne le visuel » | rapidocms (`pipeline-contenu-social`) — le texte du post n'est pas du design |

## Agent

- **`studio-creatif`** — « Décline la campagne sur tous les formats » :
  réutilise les templates existants (`search-designs` d'abord), respecte la
  charte (hex exacts de la KB, jamais approximés), exporte dans les bons
  formats, récapitule les liens Canva créés.

## Prérequis serveur

- Canva est un serveur à CATALOGUE DISTANT (OAuth) : si la connexion est
  absente/expirée, le skill le DIT et s'arrête — aucun design décrit
  « de tête », aucun lien inventé.

## Non-régression

- **NR1 — « Applique ma charte »** : `brand-guidelines-anthropic` /
  `theme-factory` — les couleurs viennent de `./rapido-kb/`
  (charte-graphique.md), pas des défauts du template.
- **NR2 — exports** : tout export annoncé avec son format réel (PNG/PDF)
  et l'URL retournée par Canva — jamais d'URL fabriquée.
