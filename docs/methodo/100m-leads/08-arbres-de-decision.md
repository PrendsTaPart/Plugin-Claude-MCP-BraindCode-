# Arbres de décision — quel canal, quand, comment scaler

> **Idées** : Alex Hormozi, *$100M Leads* (2023). **Distillation source** :
> founder-playbook (MIT © 2026 AgentSeal). Reformulation FR — voir `NOTICE.md`.

## Arbre 1 — quel canal démarrer ?

```
As-tu 10 clients payants ?
├─ NON → contact chaud jusqu'à en avoir 10
└─ OUI → choisir selon les ressources :
         ├─ du temps, pas d'argent → contact froid OU contenu
         ├─ de l'argent, pas de temps → pub payante
         └─ les deux → contact froid + contenu
```

## Arbre 2 — tu fais déjà tourner des canaux ?

```
├─ étalé sur les 4 → couper à 1, le maîtriser
├─ un canal profitable → More Better New (05-more-better-new.md)
├─ capacité perso atteinte → recruter pour le faire tourner
└─ plusieurs canaux profitables → ajouter des lead getters (07)
```

## Matrice de sélection par profil de ressources

| Profil | Démarrage recommandé |
|---|---|
| 0 client, pas d'argent, du temps | contact chaud |
| 10+ clients, pas d'argent, du temps | contact froid OU contenu |
| 10+ clients, un peu d'argent, pas de temps | pub payante (petit budget) |
| 10+ clients, argent + temps | contact froid + contenu (en parallèle) |
| 50+ clients, profitable | ajouter la pub, puis les lead getters |

## Checklist « canal maîtrisé » (avant d'en ajouter un autre)
Un canal est **maîtrisé** quand :
- [ ] coût par lead prévisible à ~30 % près ;
- [ ] conversion en client prévisible à ~30 % près ;
- [ ] playbook documenté qu'une nouvelle recrue pourrait suivre ;
- [ ] les unit economics tiennent **sans** vous aux commandes ;
- [ ] on peut multiplier la dépense/le volume par 10 sans casser.

Tant que ce n'est pas vrai : **ne pas ajouter** de canal.

## Signaux d'alerte
- **Étalement** : 3-4 canaux en même temps, aucun profitable, incapable de
  nommer sa meilleure source de leads.
- **Contact froid cassé** : taux de réponse au ras du plancher du secteur, pas de
  réponse aux relances.
- **Contenu qui ne prend pas** : 3+ mois de posts, engagement mais aucun DM/vente.

## Exemple Rapido / FoodEatUp
Un food-truck qui démarre (0 client) : **contact chaud** (proches, marché local)
jusqu'à 10 clients, puis, avec un peu de budget, **une** campagne Meta locale —
pas les quatre canaux d'un coup.

## Outils MCP Rapido pressentis

| Décision | Outils MCP Rapido |
|---|---|
| Compter les clients / la maturité | rapidocrm `get_dashboard_kpis`, `get_top_clients`, `list_contacts` |
| Prévisibilité coût/conversion par canal | rapidocrm `get_conversion_par_canal`, `get_stats_pipeline` ; rapido-meta-ads `ads_insights_*` |
| Calcul des seuils (30 %, ×10) | skill `catalogue-kpi` (jamais de tête) |
| Documenter le playbook (mémoire) | rapido-suite `mise-a-jour-kb` → `./rapido-kb/processus-internes.md` |

## Frontières
- **Mécanique** de chaque canal → `01-core-four.md` (+ fiches source
  `frameworks.md`, `paid-ads.md`).
- **Scaler** → `05-more-better-new.md`. **Déléguer** → `07-lead-getters.md`.
