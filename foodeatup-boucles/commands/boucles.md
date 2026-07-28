---
description: État des 8 boucles FoodEatUp en un écran (une ligne par boucle, lecture seule)
---

Donne l'état des 8 boucles du livre blanc en un écran, une ligne par boucle :
`[n° | boucle | indicateur clé | état ✅/⚠️/🔴 | action n°1]`.

Pour chaque boucle, applique le skill correspondant (`boucle-1-configuration` à
`boucle-8-comptabilite`) en mode minimal : seulement les 1-2 lectures MCP de
tête de chaque skill, pas le diagnostic complet. Lecture seule stricte.
Termine par la boucle la plus rouge et propose d'ouvrir son détail via
`/boucle <n>`, ou le croisement via `/croisement`.
