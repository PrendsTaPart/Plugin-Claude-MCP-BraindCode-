# Core Four — les 4 seules façons de faire de la pub

> **Idées** : Alex Hormozi, *$100M Leads* (2023). **Distillation source** :
> founder-playbook (MIT © 2026 AgentSeal). Reformulation FR, non-reproduction
> du livre — voir `NOTICE.md`.

## Le principe

Toute acquisition tient dans **deux axes** : à qui on parle (audience **chaude**
= elle vous connaît / **froide** = inconnus) et comment (**1-à-1** ou
**1-à-plusieurs**). Ça donne **quatre** cases, et rien d'autre :

| | Audience chaude | Audience froide |
|---|---|---|
| **1-à-1** | Contact chaud (warm outreach) | Contact froid (cold outreach) |
| **1-à-plusieurs** | Contenu gratuit | Publicité payante |

**Règle d'or** : **maîtriser UN canal** avant d'en ajouter un deuxième. Étaler
son énergie sur les quatre dès le départ = les quatre restent médiocres.

## Vocabulaire (à ne pas confondre)

| Terme | Définition |
|---|---|
| **Lead** | une personne que vous pouvez contacter |
| **Lead engagé** | une personne qui a montré de l'intérêt |
| **Lead qualifié** | une personne qui peut payer et va probablement acheter |

Un lead engagé vaut bien plus qu'un nom froid. **Qualité > volume.**

## Exemple Rapido / FoodEatUp

Un restaurant FoodEatUp qui veut remplir son midi :
- **Contact chaud** : écrire un à un aux clients fidèles (base CRM) pour la
  nouvelle formule ;
- **Contenu gratuit** : posts RapidoCMS (recette, coulisses) à son ton ;
- **Contact froid** : message aux entreprises du quartier (déjeuner d'équipe) ;
- **Pub payante** : campagne Meta géolocalisée sur la zone de chalandise.
On en **choisit un** selon les ressources (voir `08-arbres-de-decision.md`).

## Outils MCP Rapido pressentis

| Canal | Outils MCP Rapido |
|---|---|
| Contact chaud (1-à-1) | rapidocrm `list_contacts`/`get_contacts_segment`, `send_email`/`send_sms`, `create_task` ; Gmail `create_draft` |
| Contenu gratuit (1-à-plusieurs) | rapidocms `create_draft_tool`/`schedule_draft_tool`, `create_campagne`, `post_insights` |
| Contact froid (1-à-1) | rapidocrm `prospecter_maps`/`prospecter_entreprise`, `rechercher_prospects`, `schedule_email`/`schedule_sms` |
| Pub payante (1-à-plusieurs) | rapido-meta-ads `ads_create_campaign`→`ad_set`→`creative`→`ad` (PAUSED), `ads_create_custom_audience` (lookalike) |

> Chiffres et cadences ne se calculent jamais de tête : passer par le skill
> `catalogue-kpi` (rapido-startup) pour les taux (voir `04-ltgp-cac.md`).

## Frontières
- **Quel** canal démarrer selon les ressources → `08-arbres-de-decision.md`.
- **Scaler** un canal qui marche → `05-more-better-new.md`.
- **Déléguer** l'acquisition → `07-lead-getters.md`.
