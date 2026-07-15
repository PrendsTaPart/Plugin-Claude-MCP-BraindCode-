# Garde-fous TikTok Ads (verrouillé — argent réel)

> MCP officiel TikTok Ads (annoncé 05/2026) **non connecté** ici : skills écrits
> d'après le cycle campagne documenté ; noms d'outils exacts confirmés à la connexion.
> Plateforme récente → verrous **plus stricts** que `rapido-meta-ads`.

## Création toujours inactive
- **Toute entité créée doit l'être en état inactif/brouillon** quand l'API le permet.
- **Si un outil ne propose PAS d'état pausé**, **NE PAS l'utiliser pour créer** —
  seulement pour **lire**. (Mieux vaut ne rien créer qu'une entité active non voulue.)
- Garde automatique : hook `garde-argent-reel-tiktok` → **DENY** sur toute création
  détectée en état actif.

## Budget & activation
- **Budget max affiché AVANT toute proposition** (devise réelle du compte).
- **Activation = confirmation écrite explicite** et **séparée** de la création.
- **Jamais plus de X €/jour sans validation** — X dans `./rapido-kb/` (budget pub
  max/jour TikTok), jamais en dur.
- Garde : hook → **ASK** sur activation / présence de budget.

## Reporting & arbitrage
- Comparaison inter-plateformes (TikTok vs Meta) sur **mêmes KPIs, même période** via
  `rapido-startup:catalogue-kpi` (source unique des formules).
- Données réelles > KB > défauts, jamais inventées ; serveur absent = le dire.

## Récapitulatif obligatoire (Stop)
Toute écriture → récap : IDs, **STATUT en toutes lettres** (INACTIF par défaut),
budgets réels, **coût max** de ce qui est ACTIVE, plafond KB rappelé.
