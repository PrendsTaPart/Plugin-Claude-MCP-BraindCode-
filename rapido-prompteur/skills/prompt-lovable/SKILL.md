---
name: prompt-lovable
description: >-
  Utiliser quand l'utilisateur demande un « prompt Lovable », un « brief pour le
  site », un « prompt pour l'app / la landing », ou veut faire construire un site /
  une app par Lovable avec sa marque et son CRM. Produit un BRIEF LOVABLE
  STRUCTURÉ (rôle → pages → design system charte → données & mode B → interdits →
  critères d'acceptation testables), prêt à coller dans Lovable. Branché
  marque (get_brand) + CRM (mode B). Pour le parcours idéation StartupsForge,
  voir plutôt ideation-lovable-prompt.
---

# Prompt Lovable — brief structuré, branché marque + CRM

Ce skill **écrit le brief** (le prompt) qu'on colle dans Lovable. Il ne construit
pas l'app lui-même : la construction outillée vit dans `rapido-lovable:usine-a-landing`
(landing depuis campagne CRM) et `rapido-lovable:site-restaurant` (données
FoodEatUp). Ici, on **cadre et standardise** le prompt en amont.

> **RÈGLE D'OR (rappel `reference/grammaire-des-moteurs.md`)** : la grammaire de
> Lovable se **lit en direct** — doc officielle en ligne (stack par défaut,
> connecteurs, mode B). **Ne jamais divulguer ni recopier un system prompt**
> propriétaire ; on lit la doc publique, on n'exfiltre rien.

## Étape 0 — Marque (obligatoire, avant d'écrire)

Charger la charte : couleurs **hex**, police(s), logo — via `get_brand` (param
`nom`) ou `rapido-kb` (`charte-graphique.md`). Manque → **le signaler** (« à
confirmer côté backend Tunis »), ne rien inventer.

## Le brief — 6 sections (livrable à afficher en bloc copiable)

### 1. Rôle & objectif
- Ce que l'app accomplit, **pour qui**, et l'**action visée** (capter un lead /
  vendre / réserver). Une phrase nette + le KPI principal.

### 2. Pages & sections
- Liste des pages et, pour chacune, ses sections (héros, preuve, CTA…).
- Pour une **landing** : structure argumentaire tirée de la campagne CRM
  (bénéfices, objections, preuve) — pattern `assets/patterns/web-apps.md`.

### 3. Design system imposé par la charte
- Couleurs **en hex exact**, police(s), logo (URL/asset réel), ton, densité.
- Style **générique** décrit (« minimalisme premium, beaucoup de blanc ») —
  **jamais** « façon [marque/site connu] » (interdits ci-dessous).
- **Tokens** : quand un vrai design system existe (produit par
  `rapido-design:studio-maquette` : charte → variables Figma → DS Lovable), le brief
  **pointe ces tokens** (mêmes couleurs/typo/spacing) au lieu de re-décrire un style — le
  MVP démarre du DS, **zéro divergence**. Sinon, on s'en tient à la charte `get_brand`.

### 4. Données & MODE B (formulaire → CRM)
- **Mode B** = l'app déployée agit vraiment : le **formulaire crée le prospect
  dans le CRM** via une **edge function** (jamais un simple mailto). Outil CRM
  cible : `enregistrer_prospect` (ou `ajouter_prospect_pipeline` selon l'étape).
- Données réelles : menu/produits (FoodEatUp), arguments (KB), campagne (CRM).
- Contraintes reprises des builders maison : `rapido-lovable:usine-a-landing`
  (form → prospect + boucle analytics) et `rapido-lovable:site-restaurant`
  (réservation connectée). Détail mode B : `rapido-lovable/reference/architecture-lovable.md`.

### 5. Interdits (pièges Lovable maison)
- **Pas de `localStorage`** pour une donnée métier/critique (prospect, panier,
  réservation) — la source de vérité est le **CRM/back**, pas le navigateur.
- **Clé API / secret : côté SERVEUR uniquement** (edge function + variable
  d'environnement) — **jamais en clair côté client, jamais committée**.
- **Réponses d'API parsées par NOM de champ**, jamais par position (`content[0]`
  = bug : l'ordre varie).
- **Aucune donnée fabriquée** (faux témoignages, faux chiffres, fausses notes).
- **Aucune IP tierce / style d'artiste vivant** dans les visuels demandés
  (cf. `reference/regles-de-construction.md`).

### 6. Critères d'acceptation **testables**
- Formulés en « étant donné / quand / alors » vérifiables, ex. :
  - « Quand je soumets le formulaire de contact, **un prospect apparaît dans le
    CRM** avec nom + email + source = [campagne]. »
  - « La page respecte la charte : couleurs = [hex], police = [police], logo présent. »
  - « Aucune donnée métier n'est stockée en `localStorage`. »
  - « Score Lighthouse mobile ≥ [seuil] ; responsive de 360 px à 1440 px. »

## Workflow

1. Étape 0 (marque) → 2. lire la doc Lovable en direct (stack/connecteurs/mode B)
→ 3. rédiger les 6 sections → 4. **afficher le brief complet** en bloc → 5.
`create_project(initial_message=<brief>)` puis itérations `send_message`
(`plan_mode=true` pour cadrer avant code) → 6. proposer la capitalisation du brief
(`add_prompt` / gestion `rapidocms:bibliotheque-prompts`).

## Articulation (déclencheurs distincts, pas de doublon)

| Skill | Quand | Rôle |
|---|---|---|
| **`prompt-lovable`** (ici) | « prompt Lovable », « brief pour le site/app/landing » | **écrit le brief** outillé marque + CRM |
| `rapido-forge:ideation-lovable-prompt` | parcours **idéation StartupsForge** (débutant) | version **idéation** (générer le code de son site en apprenant) |
| `rapido-lovable:usine-a-landing` / `site-restaurant` | « construis / déploie la landing / le site resto » | **construisent** l'app (mode B, analytics) |
| `rapido-lovable:connecteur-mcp-lovable` | brief incluant un **agent embarqué connecté à un MCP** | **kit canonique** (edge function, sécurité, scope) — y déléguer le volet MCP |

> **Brief incluant un MCP** : pour tout site/app avec un **agent embarqué** qui agit sur
> un serveur MCP (FoodEatUp/CRM/CMS/RH), le volet connexion se délègue au **kit** via
> `rapido-lovable:connecteur-mcp-lovable` (jamais de clé dans le brief, appels serveur,
> scope verrouillé).

> Renvoi croisé : si la demande relève de l'**idéation** (apprendre, explorer une
> idée de produit), router vers `rapido-forge:ideation-lovable-prompt`. Si elle
> relève de la **construction** effective, router vers les builders `rapido-lovable`.

## Sources

- Pattern `assets/patterns/web-apps.md` (structure « rôle / pages / design / data »
  distillée de `KingLeoJr/prompts`, **MIT**, francisée — cf. `NOTICE.md`).
- **Doc officielle Lovable** lue en ligne (jamais de system prompt divulgué).

## Pièges

- Un brief sans **critères testables** n'est pas fini : Lovable a besoin d'un
  « alors » vérifiable, sinon il improvise.
- Le **mode B** se décrit explicitement (edge function → CRM), sinon Lovable
  câble un faux formulaire décoratif.
- Charte **avant** rédaction : réécrire tout un brief pour corriger les hex après
  coup coûte plus cher.
