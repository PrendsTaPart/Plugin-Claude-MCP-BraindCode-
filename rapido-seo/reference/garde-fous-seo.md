# Garde-fous SEO

> Les serveurs SEO ne sont pas encore connectés dans cette session : les skills
> sont écrits d'après les grammaires **documentées** (GA4, GSC, DataForSEO) ; les
> noms d'outils exacts se confirment à la connexion (checklist README).

## (a) Coûts DataForSEO — facturation À L'APPEL
- DataForSEO facture **chaque requête**. Toute requête **> ~10 unités estimées**
  (backlinks bulk, SERP en volume, Labs sur listes) est **annoncée avec son coût
  estimé AVANT exécution** (même logique que `rapido-marketing:reference/cout-ia.md`).
- Le **volume récurrent** (rank tracking hebdo) vit **en n8n** (`rapido-n8n`), pas en
  appels conversationnels. Plafond mensuel dans `./rapido-kb/` (jamais en dur).
- Garde automatique : hook `garde-couts-seo` (ask sur familles facturées sans
  `cout_confirme`).

## (b) GA4 & Google Ads MCP — lecture seule *by design*
- Les serveurs **GA4** et **Google Ads** sont **read-only**. Ne **jamais promettre
  d'écriture** : ces skills **analysent et recommandent**, ils n'exécutent pas de
  changement de campagne/propriété.

## (c) Fraîcheur GSC
- Les données **Search Console** ont **2-3 jours de retard** et les **requêtes rares
  sont anonymisées**. Tout rapport le **précise** (« données au J-3, requêtes rares
  masquées »). Pas de conclusion sur une tendance de moins de 3 jours.

## (d) Contenu publié
- **Jamais de modification de contenu publié sans confirmation.** Les corrections
  (balises, textes) passent par les **tools RapidoCMS après accord** explicite —
  la couche SEO **propose**, RapidoCMS exécute sous ses propres garde-fous.

## Rappels
Données live > KB > défauts, jamais inventées ; un serveur absent = volet **sauté en
le disant** (dégradation propre) ; calculs KPI via `rapido-startup:catalogue-kpi`
(source unique), jamais de tête.
