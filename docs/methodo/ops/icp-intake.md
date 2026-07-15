# ICP intake — critères durs vs préférences souples + tiering

> **Sources distillées** : coldoutboundskills (`icp-onboarding`) MIT © 2026
> GrowthEngineX ; gtm-flywheel (`icp-matrix-builder`) MIT © 2026 ColdIQ.
> Reformulé FR, non-verbatim (voir `NOTICE.md`). Enrichit le skill `icp-generator`.

## L'apport à intégrer
Notre `icp-generator` produit déjà `icp.md` par l'analyse des clients gagnés.
Ces dépôts ajoutent deux idées utiles :

### 1. Critères DURS vs préférences SOUPLES
- **Durs** (must-match, filtrage) : intitulés de poste, secteurs inclus/exclus,
  effectif (buckets), pays/régions, domaines exclus.
- **Souples** (nice-to-have, priorisation) : signaux/déclencheurs (levée récente,
  recrutement d'un rôle clé, techno installée), personas à prioriser.
- Règle : un **déclencheur est toujours souple** (il priorise, il ne filtre pas).

### 2. Tiering des comptes
Classer chaque compte : **Bullseye / Fort / Bon / Extension / Disqualifié**, avec
des **déclencheurs de disqualification** explicites.

## Correspondance avec `rapido-kb/marketing/icp.md`
| Champ intake | rapido-kb |
|---|---|
| business (nom, site, ton) | `entreprise.md` + `ton-et-accroches.md` |
| offre (CTA, lead magnet, promesse) | `offres.md` + `propositions-valeur.md` |
| critères durs | `icp.md` § segments prioritaires |
| préférences souples / triggers | `icp.md` § signaux d'achat |
| légal (mots interdits, secteur régulé) | `ton-et-accroches.md` + garde-fous |

## Mapping Rapido
Interview d'intake → `icp-generator` ; segments → `create_segment` (confirmé) ;
sourcing sur critères durs → `prospecter_maps`/`prospecter_entreprise`. Taxonomie
d'industries : remplacer la taxonomie Prospeo par les libellés RapidoCRM.

→ Cible : **`icp-generator` (M5)** — ajouter la distinction durs/souples + tiering.
