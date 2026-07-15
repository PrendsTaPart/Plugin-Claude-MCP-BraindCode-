---
name: audit-seo-technique
description: Utiliser quand l'utilisateur veut un « audit SEO », demande « pourquoi mon site ne ranke pas », « erreurs techniques du site », un audit OnPage ou un diagnostic de crawl. Audite un domaine via DataForSEO OnPage (erreurs de crawl, balises, vitesse, maillage interne), sortie priorisée par impact ; les corrections de contenu sont déléguées aux tools RapidoCMS après confirmation.
---

# Audit SEO technique (DataForSEO OnPage)

Diagnostique la santé technique d'un domaine et **priorise par impact**. **Ne
modifie rien** : les corrections passent par RapidoCMS **après accord**.

## Étape 0
Lire `${CLAUDE_PLUGIN_ROOT}/reference/garde-fous-seo.md` (coûts, lecture seule,
contenu publié). Cible : le domaine du client (`./rapido-kb/seo/seo-cibles.md`).

## Sense (lecture — DataForSEO OnPage)
- Lancer un crawl OnPage du domaine (famille `on_page` DataForSEO) : **erreurs de
  crawl** (4xx/5xx, redirections), **balises** (title/meta dupliqués ou manquants,
  Hn), **vitesse** (Core Web Vitals si dispo), **maillage interne** (pages
  orphelines, profondeur), **indexabilité** (robots, canonicals).
- **Coût** : une requête OnPage volumineuse est **annoncée avant** (garde-couts-seo).

## Plan (priorisation par impact)
- Classer les problèmes : **bloquants** (non indexé, 5xx) > **fort impact** (title
  dupliqués sur pages piliers) > **hygiène** (alt manquants). Impact estimé sur la
  visibilité, pas de tête — chiffres du rapport à l'appui.

## Act (corrections déléguées, après confirmation)
- Les corrections de **contenu/balises** sont **proposées** puis, **sur accord**,
  exécutées via les tools RapidoCMS (`edit_card_page`, `create_draft_tool`…) —
  jamais de modification de contenu publié sans confirmation.
- Les corrections **serveur/technique** (redirections, robots) sont **listées** pour
  l'équipe technique (hors périmètre d'écriture de ce plugin).

## Report — une page
Score de santé, top problèmes **priorisés par impact** (avec la page concernée et le
chiffre source), corrections proposées, coût DataForSEO consommé.

## Garde-fous
Lecture d'abord ; coût DataForSEO annoncé ; corrections **confirmées** via RapidoCMS ;
données réelles, jamais inventées ; serveur absent = le dire.
