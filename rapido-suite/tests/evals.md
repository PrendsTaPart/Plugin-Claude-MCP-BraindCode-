# Évals — plugin rapido-suite (1.4.0)

## Sync marque KB ↔ RapidoCMS

| # | Phrase | Attendu |
|---|---|---|
| S1 | « Configure mon entreprise » (charte remplie, rapidocms installé) | `onboarding-entreprise` : après la charte, **Phase 3 bis Miroir CMS** — mapping validé → `gestion-marques`/`create_brand` → écrit `> Miroir CMS : brand_id <id> — dernière sync <date>` dans `charte-graphique.md` |
| S2 (dégradé) | idem mais rapidocms absent / MCP indisponible | Miroir CMS **signalé et sauté sans bloquer** ; la KB est créée normalement |
| S3 | « Change les couleurs de la marque en #0F172A » (brand_id présent en KB) | `mise-a-jour-kb` : met à jour `charte-graphique.md`, **propose la sync descendante** `edit_brand` (couleurs seules) après confirmation, met à jour la date de sync — jamais silencieux |
| S4 (frontière) | « Change les couleurs » mais **aucun brand_id** en KB | `mise-a-jour-kb` : met à jour la KB seulement, dit qu'aucune marque miroir n'est liée |
| S5 | « Onboarde le nouveau client » | `onboarding-client-360` acte CMS : `create_brand` + logo via `bibliotheque-assets`, `brand_id`/`asset_id` consignés au récap |

## pilotage-entreprise

| # | Phrase | Attendu |
|---|---|---|
| P1 | « Pilote mon entreprise » | `pilotage-entreprise` — Étape 0 (KB entière + autonomie.md + vérif serveurs), puis les 5 phases sur TOUS les domaines ; KPI via `catalogue-kpi` uniquement ; récap groupé AVANT toute écriture ; report une page |
| P2 (frontière) | « Mon lundi » | `monday-brief` DIRECT — format lundi dédié, pas la boucle transverse |
| P3 (frontière) | « Lance R7 » | `loop-engine-v2` (plugin rapido-startup) — routine unitaire, pas le pilotage complet |

## lancement-projet-360 (orchestrateur)

| # | Phrase | Attendu |
|---|---|---|
| O1 | « Je veux lancer un SaaS » | `lancement-projet-360` — acte 1 (Penser : routage directeur-programme, livrables en KB), puis ARRÊT validation avant l'acte 2 |
| O2 | « On crée une nouvelle marque de A à Z » | `lancement-projet-360` — actes déroulés un par un ; identité via `rapidocms:gestion-marques` (confirmation niveau 2) ; jamais deux actes sans validation |
| O3 (négatif) | « Crée un post » | rapidocms (`pipeline-contenu-social`) DIRECT — demande unitaire, pas l'orchestrateur |

- ATTENDU transverse : tout livrable méthodo écrit dans la KB AVANT son
  exécution ; récapitulatif par acte avec les IDs réels créés dans les
  systèmes ; toute dépense (crédits Lovable, ads) confirmée au moment T —
  ads TOUJOURS en PAUSED (hooks rapido-meta-ads en filet).

## Non-régression

- **NR1 — « Mon lundi » / « brief du lundi »** : `monday-brief` inchangé
  (lecture seule multi-serveurs, une page).
- **NR2 — « Structure les infos de ma startup pour les agents »** :
  `dossier-startup-360` inchangé (mémoire 8 fichiers, chiffres sourcés).
