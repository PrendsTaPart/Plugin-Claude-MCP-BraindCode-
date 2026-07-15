# La règle des 100 (et « Open to Goal »)

> **Idées** : Alex Hormozi, *$100M Leads* (2023). **Distillation source** :
> founder-playbook (MIT © 2026 AgentSeal). Reformulation FR — voir `NOTICE.md`.

## La règle des 100

Le **minimum vital de publicité quotidienne**. Chaque jour, faire **UN** de :
- **100 contacts froids** (appels, emails, DM) ;
- **100 minutes** de création de contenu ;
- **100 minutes** de travail sur les pubs ;
- **100 €** dépensés en pub.

Le tenir **100 jours** avant de conclure « ça ne marche pas ». La plupart des
« ce canal ne marche pas » sont en réalité « je n'ai pas tenu le volume assez
longtemps » (voir les cas dans la fiche source `cases.md`).

## Open to Goal (niveau avancé)

Quand on démarre : la règle des 100 est **basée sur l'effort** (des entrées).
Quand on scale : passer à **Open to Goal** — travailler jusqu'à atteindre un
**résultat** précis, pas un nombre d'actions.

| Stade | Règle |
|---|---|
| Démarrage | Règle des 100 (effort) |
| Scaling | Open to Goal (résultat) |

## Exemple Rapido / FoodEatUp
Un traiteur qui lance son offre entreprise : **100 messages/jour** aux bureaux du
quartier pendant 100 jours (contact froid), tracés dans le CRM — au lieu de
20 messages sur 2 semaines puis « le démarchage ne marche pas ».

## Outils MCP Rapido pressentis

| Besoin | Outils MCP Rapido |
|---|---|
| Tenir le volume de contacts froids | rapidocrm `prospecter_maps`/`prospecter_entreprise`, `schedule_email`/`schedule_sms`, `rechercher_prospects` |
| Automatiser la cadence quotidienne | n8n (`usine-automatisations`) : un workflow qui prépare les 100 envois/jour |
| Mesurer l'atteinte (Open to Goal) | rapidocrm `get_conversion_par_canal`, `get_stats_pipeline` ; skill `catalogue-kpi` |
| Contenu 100 min/jour | rapidocms `create_draft_tool`/`schedule_draft_tool` |

> Le « compteur » du jour (nb d'envois, minutes) se suit dans le CRM / le journal
> de routines, jamais estimé de mémoire.

## 🆕 Mise à jour marché 2026 (sourcée)

La règle des 100 reste valable, mais le marché 2025-2026 la **nuance** (détail :
`docs/methodo/etat-de-lart-2026.md`) :

- **Le volume est plafonné par la délivrabilité** en email : ~500/j par boîte
  Gmail, ~300/j Outlook → au-delà, rotation de boîtes chauffées. Le « 100/jour »
  ne veut pas dire une seule boîte. Source :
  [mailpool.ai](https://www.mailpool.ai/blog/deliverability-lessons-from-1-million-cold-emails-sent-in-2025) (2025) — chiffres **INCERTAIN**.
- **Volume vs signal** : Hormozi mise sur le volume ; les équipes outbound
  2025-2026 combinent **volume + signaux d'intention** (enrichissement waterfall,
  timing) pour éviter de brûler des domaines sur des cibles froides. Source :
  [factors.ai](https://www.factors.ai/blog/clay-vs-apollo-for-outbound) (2026).
- **Contenu & GEO** : « 100 min de contenu/jour » gagne à viser aussi la
  **citation par les IA** (réponse en 40-60 mots, fraîcheur) — voir la note GEO de
  `01-core-four.md`.

## Frontières
- **Quel** canal appliquer la règle → `01-core-four.md` / `08-arbres-de-decision.md`.
- **Scaler** une fois que ça marche → `05-more-better-new.md`.
