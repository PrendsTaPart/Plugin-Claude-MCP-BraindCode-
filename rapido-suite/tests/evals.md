# Évals — plugin rapido-suite (1.3.0)

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
