---
description: Volumétrie de données par boucle et seuils de fiabilité des recommandations
---

Mesure la volumétrie réelle par boucle (lecture seule) et dit si elle suffit
pour des recommandations fiables :

- ② `list_employees` ; ③ `list_stocks`, `list_production_plans` ;
  ④ `list_haccp_temperatures` (période) ; ⑤ `list_orders`,
  `list_reservations` ; ⑥ `list_clients`, `list_campaigns` ;
  ⑦ `list_redemptions`, `list_gift_cards` ; ⑧ `list_invoices`, `list_expenses`.

Sortie : tableau `[boucle | objets comptés | seuil de fiabilité | verdict]` avec
les seuils du skill `croisement-service` (3 commandes/jour observé, 10 ventes
par plat, 10 contacts par segment, 7 jours de campagne). Verdict « données
insuffisantes » = indiquer combien il en manque et comment les collecter,
jamais une recommandation quand même.
