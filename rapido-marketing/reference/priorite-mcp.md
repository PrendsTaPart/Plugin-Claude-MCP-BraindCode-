# Priorité MCP — Rapido-first

Règle centrale du plugin : **tout workflow tente d'abord la voie Rapido**. Un
serveur secondaire n'est utilisé que si la **capacité n'existe pas** côté Rapido.

## Hiérarchie des serveurs

1. **RapidoCRM** — *vérité client*. Contacts, entreprises, pipeline, segments,
   campagnes, formulaires/CTA, devis/factures, fidélité, analytics de conversion.
   C'est la source de vérité sur QUI est le client et OÙ il en est.
2. **RapidoCMS** — *vérité contenu & marque*. Marques/assets, brouillons,
   planification, campagnes de contenu, insights de posts, génération visuelle.
   Source de vérité sur la charte et le contenu publié.
3. **RapidoRH** — *exécution projet & marque employeur*. Projets, tâches, équipe,
   dailies. Pour la capacité de delivery et la marque employeur.
4. **Secondaires** (capacité absente côté Rapido uniquement) :
   `facebook-ads` (Meta), `canva`, `lovable`, `n8n`, `gmail`, `google-calendar`.

## Règle de routage

Pour chaque besoin, dans l'ordre :
1. **Existe-t-il un outil Rapido** (CRM > CMS > RH) qui le fait ? → l'utiliser.
2. Sinon seulement, **serveur secondaire** dédié (ex. pub payante → `facebook-ads` ;
   automatisation récurrente → `n8n` ; design avancé → `canva` ; landing full-stack
   → `lovable` ; outreach 1-à-1 hors CRM → `gmail`).
3. Toujours **annoncer** la voie choisie et pourquoi (Rapido d'abord).

Exemples :
- Email marketing / newsletter → **RapidoCRM** (`send_newsletter`,
  `schedule_email`), pas un outil tiers.
- Landing + capture → **RapidoCRM** `create_editor_template` (type `landing_page`)
  + `list_formulaires`/`list_cta` ; `lovable` seulement si besoin d'une app.
- Pub payante → **facebook-ads** (capacité absente côté Rapido).

## Mode dégradé (serveur indisponible)

Si un serveur nécessaire est **absent ou injoignable** : le **signaler
explicitement** (« RapidoCMS indisponible, je ne peux pas planifier le post »),
proposer la voie de repli si elle existe, et **continuer sans bloquer** le reste
du workflow — **jamais** inventer la donnée manquante. La disponibilité réelle
prime sur toute hypothèse.

## Renvois
- Détail de la couverture par capacité + outils manquants côté serveurs :
  `docs/MATRICE-COUVERTURE.md` (M0).
- Garde-fous d'exécution : `reference/garde-fous-marketing.md`.
- Pièges par outil : `reference/pieges-outils.md`.
