---
name: pilotage-seo
description: Utiliser quand l'utilisateur dit « pilote mon SEO », « fais le point SEO », veut une boucle de pilotage organique (Sense → Plan → Act → Feed → Report) ou un rapport SEO une page. Orchestre l'acquisition organique de bout en bout — audit technique, mots-clés, netlinking, performance GSC/GA4, tendances — priorisation ICE, délégation contenu/outreach, capitalisation. Sous-domaine organique de pilotage-marketing.
---

# Pilotage SEO — le Loop Engine de l'organique

Orchestrateur : il **ne fait rien lui-même**, il diagnostique, priorise, délègue,
capitalise et rend compte. Boucle **Sense → Plan → Act → Feed → Report**. Calculs
KPI via `rapido-startup:catalogue-kpi` (jamais de tête).

## Anti-collision
- **`rapido-marketing:pilotage-marketing`** : ce skill est le **sous-domaine SEO** du
  pilotage marketing. **Si `rapido-marketing` est installé**, `pilotage-marketing`
  **invoque ce skill** pour son volet organique (au lieu de le dupliquer) — même
  règle miroir que `pilotage-entreprise ↔ pilotage-marketing`. Invoqué seul, il
  pilote le SEO de bout en bout.

## Gouvernance
- **Si `rapido-suite` installé** : `rapido-suite/reference/autonomie.md` (lecture
  autonome ; écriture confirmée ; actions sensibles une par une). **Sinon** : tout
  écrit = confirmation. Coûts DataForSEO annoncés (`reference/garde-fous-seo.md`).

## SENSE — lecture seule (les 5 skills)
- **Technique** → `audit-seo-technique` (OnPage : erreurs, balises, vitesse, maillage).
- **Mots-clés** → `recherche-mots-cles` (volumes, difficulté, intention).
- **Netlinking** → `netlinking` (profil de liens, new/lost, gap concurrents).
- **Performance** → `performance-organique` (GSC positions/CTR + GA4 conversions ;
  fraîcheur précisée).
- **Tendances** → `tendances-marche` (Google Trends, TikTok best-effort).
- **Mémoire** → `./rapido-kb/seo/` (apprentissages, seo-cibles, netlinking) récents.

## PLAN — priorisation ICE
- Score ICE des actions candidates (jamais de tête) :
  `python3 "${CLAUDE_PLUGIN_ROOT}/skills/pilotage-seo/scripts/prioriser_seo.py"`
  (impact × confidence × ease). **Coût DataForSEO** des requêtes prévues **annoncé**
  avant les grosses passes ; volume récurrent → routine n8n (`SEO-HEBDO`/`SEO-MENSUEL`).

## ACT — délégation (chaque écriture confirmée)
- **Contenu** (nouvelles pages, corrections title/meta) → tools **RapidoCMS** après
  accord (`create_draft_tool`, `edit_card_page`) ; sujets → `rapidocms:calendrier-editorial`.
- **Outreach netlinking** → `rapidocrm:draft-outreach` (brouillons confirmés).
- **Jamais de modification de contenu publié sans confirmation.**

## FEED — capitalisation
- 1-3 leçons datées et **sourcées** (chiffre réel) dans `./rapido-kb/seo/apprentissages.md` ;
  `seo-cibles.md` / `netlinking.md` mis à jour (via `rapido-suite:mise-a-jour-kb`).
  2 échecs sur la même action → escalade humaine.

## REPORT — une page
**📊 positions & striking distance** | **✅ actions menées** | **🔴 décisions** |
**⏭️ prochaine itération** | **📋 récap** (pages éditées, coût DataForSEO consommé,
fraîcheur GSC).

## Garde-fous
Gouvernance `autonomie.md` (sinon tout écrit confirmé) ; priorisation **par script** ;
KPI via `catalogue-kpi` ; coûts DataForSEO annoncés, volume → n8n ; **fraîcheur GSC
dite** ; GA4/Google Ads **lecture seule** ; sous-domaine de `pilotage-marketing`.
