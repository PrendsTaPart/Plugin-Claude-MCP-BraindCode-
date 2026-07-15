---
name: pilotage-commercial
description: Utiliser quand l'utilisateur dit « pilote mon commercial », « fais le point ventes », veut une boucle de pilotage commercial (Sense → Plan → Act → Feed → Report) : hygiène des données → relances → conversion → encaissement. Orchestre la vente de bout en bout — diagnostic pipeline/devis/impayés/objectifs, priorisation valeur×probabilité×urgence, délégation aux skills d'exécution, capitalisation, rapport une page — gouverné par la politique d'autonomie. Calculs délégués à catalogue-kpi.
---

# Pilotage commercial — le Loop Engine de la vente

Orchestrateur : il **ne fait rien lui-même**, il diagnostique, priorise, délègue
aux skills d'exécution, capitalise et rend compte. Boucle **Sense → Plan → Act →
Feed → Report**. **Aucun calcul local** : tout KPI (couverture, taux de win, durée
de cycle) passe par `rapido-startup:catalogue-kpi` (source unique des formules).

## Anti-collision

- **`rapido-suite:pilotage-entreprise`** : ce skill est le **sous-domaine
  commercial** du pilotage transverse. **Si `rapido-suite` est installé**,
  `pilotage-entreprise` **invoque ce skill** pour son volet commercial (SENSE +
  PLAN + ACT ventes) **au lieu de le dupliquer** (règle miroir, comme
  `rapido-marketing:pilotage-marketing`). Invoqué seul, il pilote la vente de bout en bout.
- **`rapido-marketing:pilotage-marketing`** : lui **génère les leads** (haut du
  tunnel) ; moi je les **convertis en cash** (bas du tunnel). Aucun recouvrement.
- **`coaching-pipeline`** (rapidocrm) : lui = **revue ponctuelle** des deals (« où
  en sont mes deals »). Moi = **la boucle orchestrée complète** (hygiène → relances
  → revue → capitalisation, avec routines). J'**invoque** coaching-pipeline en SENSE.

## Gouvernance (obligatoire)
- **Si `rapido-suite` est installé** : charger `rapido-suite/reference/autonomie.md`
  — lecture en autonomie totale ; **écriture confirmée** ; **actions sensibles
  (envoi, relance, création de devis/tâche) confirmées une par une** ; échec → arrêt
  à l'étape + récap des IDs déjà créés.
- **Sinon (mode prudent par défaut)** : **tout écrit = confirmation explicite**.
- Filet : le hook `garde-envois` (rapido-marketing, s'il est installé) reste actif
  sur les envois RapidoCRM ; sinon tout envoi part en **brouillon confirmé**.

## SENSE — lecture seule (le carburant)
Collecter, même période partout, sans rien inventer (serveur absent = volet sauté
en le disant) :
- **Pipeline & deals** → `coaching-pipeline` (deals dormants, étapes engorgées, prochaine action par deal).
- **Devis & encaissement** → `devis-facture-relance` (devis expirants, impayés, relances graduées).
- **Objectifs commerciaux** → `performance-commerciale` (objectifs par commercial, atteinte).
- **Couverture pipeline** → `forecast` (pipeline pondéré vs objectif restant).
- **Hygiène des données** → routine `VENTE-HYGIENE` (voir Routines) : deals sans activité, devis sans expiration, entreprises sans contact, impayés.
- **Mémoire** → `./rapido-kb/commercial/apprentissages.md` **récents** (les leçons priment) + `benchmarks.md`.

## PLAN — priorisation chiffrée
1. **Prioriser par `valeur × probabilité × urgence`** (valeur du deal × probabilité
   de l'étape × urgence de l'échéance) — valeurs **lues dans le CRM** (`get_pipeline`,
   `get_stats_pipeline`), formule **affichée**, jamais de tête. La **couverture**
   (pipeline pondéré ÷ objectif restant) et tout ratio sont calculés par
   `rapido-startup:catalogue-kpi`, pas ici.
2. **Anti-doublon Kanban** : AVANT de créer une tâche, **lire le Kanban RapidoRH**
   (liste des tâches du projet commercial) — une action déjà au Kanban n'est **pas recréée**.
3. **Volume → routine** : une action récurrente (relances quotidiennes, hygiène
   hebdo) est requalifiée en routine `VENTE-*` (n8n via `rapido-n8n:usine-automatisations`),
   pas en appels modèle un par un.

## ACT — délégation (chaque action sensible confirmée)
- Router vers les skills d'exécution **rapidocrm existants** :
  - relances devis/impayés → `devis-facture-relance` (brouillons gradués) ;
  - deals dormants / prochaine action → `coaching-pipeline` ;
  - nouveaux prospects à qualifier → `prospection-pipeline` ;
  - rédaction d'une proposition/relance → `redaction-commerciale` ;
  - suivi d'objectifs → `performance-commerciale`.
- **Tout envoi / relance = confirmation** (`garde-envois` + autonomie.md), **brouillon
  par défaut**. Créer les tâches retenues au Kanban après vérification anti-doublon.

## FEED — capitalisation & réaffectation
- **Capitalisation** : 1-3 leçons datées et **sourcées** (chiffre réel) dans
  `./rapido-kb/commercial/apprentissages.md` ; `benchmarks.md` mis à jour si un taux
  change (via `rapido-suite:mise-a-jour-kb`). **Taux de win et durées de cycle**
  calculés par `rapido-startup:catalogue-kpi`, jamais de tête. Pas de leçon sans preuve chiffrée.
- **Échec** : réaffecter (autre angle / autre relance). **2 échecs sur le même deal
  → escalade humaine** avec diagnostic. Ne pas boucler à l'infini.

## REPORT — une page
- **📊 Pipeline pondéré & couverture vs objectif** (formules `catalogue-kpi`) | **✅
  actions menées** | **🔴 top 5 actions à décider** (par valeur×probabilité×urgence) |
  **⏭️ prochaine itération** | **📋 récap des IDs** (devis, relances, tâches créées).

## Routines récurrentes (proposées, installées sur confirmation)
Registre unifié `reference/registre-routines.md` (racine) — préfixe `VENTE-*` :
- **`VENTE-HYGIENE`** (hebdo lundi) : score d'hygiène des données /100 (deals sans
  activité 14+ j, devis sans expiration, entreprises sans contact, impayés 30+ j).
- **`VENTE-RELANCES`** (quotidien 14h) : devis expirants → brouillons de relance ;
  deals dormants classés par valeur, une prochaine action chacun ; anti-double-relance.
- **`VENTE-REVUE`** (hebdo lundi, après HYGIENE) : pipeline par étape, couverture,
  conversion par étape vs benchmarks, décisions.
Fichiers dans `references/routines/` ; installer **seulement** celles confirmées
(chaque routine a sa table mémoire).

## Garde-fous
Gouvernance `autonomie.md` (sinon mode prudent = tout écrit confirmé) ; **KPI par
`catalogue-kpi`, jamais de tête ni en local** ; priorisation formule affichée ;
**anti-doublon Kanban avant création** ; 2 échecs → escalade ; données live > KB >
défauts, jamais inventées ; sous-domaine de `rapido-suite:pilotage-entreprise` (pas
de duplication) ; **je convertis, `pilotage-marketing` génère** (frontière nette).
