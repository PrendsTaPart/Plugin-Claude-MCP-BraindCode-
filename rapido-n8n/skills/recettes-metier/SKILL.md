---
name: recettes-metier
description: Utiliser quand un besoin d'automatisation correspond à une recette métier Rapido connue — relances de devis, alertes de stock, rappels HACCP, leads entrants, récap hebdo, anniversaires clients. Catalogue de workflows prêts à déployer via l'usine à automatisations.
---

# Recettes métier (catalogue prêt-à-déployer)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-n8n.md`. Chaque recette se déploie via
le cycle complet du skill `usine-automatisations` (le design ci-dessous est le
POINT DE DÉPART, pas un raccourci du cycle).

## Niveau d'autonomie (s'applique à TOUTES les recettes)

Les envois externes réels (email à un client) démarrent en mode
« BROUILLON + notification au gérant » tant que
`rapido-kb/processus-internes.md` n'autorise pas explicitement l'envoi
direct. Les notifications internes (gérant, équipe) sont libres.

## Le catalogue

### relance-devis
Cron quotidien (matin) → HTTP vers l'API CRM : devis `en_attente` depuis
plus de 7 jours (ou la cadence maison) → email de relance depuis le template
CRM en BROUILLON + notification au commercial. Anti-doublon : table
`relances_envoyees` (skill `memoire-operationnelle`) — jamais deux relances
pour le même devis au même palier.

### alerte-stock
Cron matin (avant le service) → HTTP FoodEatUp : stocks bas (`is_low`) →
constituer le BROUILLON de commande fournisseur (articles regroupés par
fournisseur) + notification au gérant avec le récap. La commande réelle reste
une décision humaine.

### rappel-haccp
Cron 2×/jour (fin de matinée, fin de soirée) → HTTP FoodEatUp : relevés de
température du créneau manquants → notification à l'équipe (« relevés frigo
non faits »). Jamais de valeur enregistrée automatiquement — le rappel
uniquement.

### lead-entrant
Webhook n8n (reçoit le formulaire Lovable/site) → HTTP CRM : création du
contact + ajout au pipeline (étape d'entrée) avec anti-doublon (recherche
email d'abord) → email d'accueil en BROUILLON + notification au commercial.
Fournir l'URL du webhook à brancher côté Lovable.

### recap-hebdo
Cron vendredi 17 h → HTTP vers les API (CRM : CA, pipeline ; CMS : posts ;
FoodEatUp : finance) → email de synthèse INTERNE au dirigeant (envoi direct
autorisé : destinataire interne). Compléter, pas remplacer, la
`revue-hebdo-business` interactive.

### anniversaires-clients
Cron quotidien → HTTP CRM : clients dont c'est l'anniversaire → message de
fidélisation (ton de `ton-et-accroches.md`, offre de `processus-internes.md`
si définie) en BROUILLON + notification. Vérifier que la date de naissance
existe dans le CRM (sinon la recette ne produit rien — le dire).

## Usage

1. Quand un besoin matche une recette, la PROPOSER avec son design (un
   paragraphe) et les adaptations client (seuils maison, cadences KB).
2. Déployer via `usine-automatisations` (cycle complet : SDK → nodes → types
   → code → validation → test → publication confirmée → registre).
3. Adapter les seuils aux valeurs maison de la KB (cadence de relance, seuil
   de stock…) — citer la source.

## Recette prête : R7 CASH-SENTINEL (sentinelle trésorerie)

La routine R7 du Loop Engine (plugin rapido-startup) en workflow autonome —
nodes, CONFIG et étapes d'activation dans
`${CLAUDE_PLUGIN_ROOT}/reference/recette-r7-cash-sentinel.md`. Publication
toujours confirmée (hook garde-production).

## Recettes de vente événementielles (OPS-*)

Les trois workflows **événementiels** de la boucle de vente — **OPS-LEAD-CHAUD**
(réponse au lead chaud), **OPS-CLIENT-GAGNE** (onboarding du client gagné),
**OPS-ALERTE-CHURN** (sentinelle rétention) — sont décrits dans
`${CLAUDE_PLUGIN_ROOT}/reference/recettes-vente.md` (déclencheur, pseudo-nœuds,
table mémoire, garde-fous) et enregistrés au registre unifié
`reference/registre-routines.md` (préfixe `OPS-*`). Chaque recette a sa **table
mémoire** obligatoire ; installation **sur confirmation**, recette par recette.
