# Recettes de vente événementielles (n8n) — vendre hors des heures de bureau

> Trois workflows **déclenchés par événement** (pas en CRON pur) : ils réagissent
> au lead chaud, au client gagné et au signal de churn. Format identique aux
> routines marketing (`rapido-marketing/reference/routines.md`) : déclencheur,
> workflow en pseudo-nœuds, table mémoire, garde-fous.
>
> **Règles maison** : le volume vit en n8n (pas d'appels modèle un par un) ; toute
> action visible reste en **brouillon confirmé** ; **une recette sans table mémoire
> n'est pas installable** (anti-doublon impossible). Identifiants au registre unifié
> `reference/registre-routines.md` (préfixe `OPS-*`). Installation **recette par
> recette, sur confirmation**, via `rapido-n8n:usine-automatisations` — **ce fichier
> ne crée aucun workflow sur l'instance**.

## OPS-LEAD-CHAUD — réponse au lead chaud
- **Objectif** : ne jamais laisser refroidir un lead à fort intent, même la nuit.
- **Déclencheur** : **Webhook** sur soumission d'un formulaire CRM à fort intent
  (score/segment défini en KB).
- **Workflow (pseudo-nœuds)** : Webhook → normaliser la soumission → CRM :
  créer/retrouver l'entreprise (SIRET/email) → **ajouter au pipeline étape
  « Qualifié »** → lire 2 **créneaux libres réels** Google Calendar → **email
  interne** (fiche prospect + 2 créneaux) → **préparer un brouillon Gmail** de
  réponse (jamais envoyé). **JAMAIS de réponse directe au prospect.**
- **Table mémoire** : `ops_leads_chauds` (`date`, `soumission_id`, `entreprise_id`,
  `traite_le`, `resolu`) — anti-double-traitement (ne pas re-traiter une soumission déjà ouverte).
- **Garde-fous** : réponse au prospect = **brouillon** (humain confirme) ; créneaux
  Calendar **réels** (pas inventés) ; notification **interne** seulement.

## OPS-CLIENT-GAGNE — onboarding du client gagné
- **Objectif** : déclencher tout l'onboarding à la seconde où un devis passe à « accepté ».
- **Déclencheur** : détection d'un **devis passé à « accepté »** (polling court ou webhook CRM).
- **Workflow (pseudo-nœuds)** : détection → CRM : **deal → gagné** → **facture
  d'acompte en brouillon** → RapidoRH : **projet + Kanban standard** → Google
  Calendar : **événement kick-off** → **email de bienvenue en brouillon** → CRM :
  **tâche relance ambassadeur J+60** (`programme-ambassadeurs`).
- **Table mémoire** : `ops_onboardings` (`date`, `devis_id`, `entreprise_id`,
  `projet_id`, `facture_id`, `statut`) — un onboarding par client gagné, pas de doublon.
- **Garde-fous** : facture et emails en **brouillon confirmé** ; projet créé **après
  vérification anti-doublon** ; aucun montant inventé.

## OPS-ALERTE-CHURN — sentinelle de rétention
- **Objectif** : repérer les clients qui décrochent avant qu'ils ne partent.
- **Déclencheur** : **Schedule** hebdomadaire (cron KB).
- **Workflow (pseudo-nœuds)** : Schedule → clients **sans activité 30 j** (aucune
  campagne CRM, aucun post CMS publié, aucune commande FoodEatUp) → **prioriser par
  valeur** (CA historique) → **email interne** : liste priorisée + **plan de
  sauvetage en 3 gestes** par client.
- **Table mémoire** : `ops_churn_alertes` (`date`, `entreprise_id`, `signale_le`,
  `resolu`) — **ne pas re-signaler** un client déjà ouvert non résolu.
- **Garde-fous** : alerte **interne** seulement (aucun contact client d'office) ;
  priorisation par valeur **réelle** ; plan de sauvetage proposé, jamais exécuté seul.

## Installation
Proposer chaque recette avec son déclencheur, son périmètre et sa table mémoire ;
**installer seulement celles confirmées** via `rapido-n8n:usine-automatisations`.
Un workflow sans sa table mémoire n'est pas installé.
