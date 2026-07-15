---
name: lead-getters-systeme
description: Utiliser quand l'utilisateur veut mettre en place un programme de parrainage, faire générer des leads par ses clients, employés, agences ou affiliés, ou déléguer son acquisition au-delà de sa capacité personnelle. Choisit le type de lead getter selon la maturité et cadre le programme, puis délègue l'exécution.
---

# Système de Lead Getters — faire générer des leads par d'autres

> **Idées** : Alex Hormozi, *$100M Leads* (2023). **Distillation** :
> `docs/methodo/100m-leads/07-lead-getters.md` (source MIT founder-playbook).
> Reformulé, citations < 15 mots.

## Étape 0 — Charger (obligatoire)
- Fiche `docs/methodo/100m-leads/07-lead-getters.md`.
- `./rapido-kb/marketing/` si présent (base clients, fidélité, équipe).
- `${CLAUDE_PLUGIN_ROOT}/reference/garde-fous-marketing.md`.

## Méthode

1. **Prérequis** : n'ajouter des lead getters **qu'après** avoir maîtrisé le
   canal soi-même (sinon rien à copier). Vérifier : offre qui convertit, tracking,
   bonne expérience client.
2. **Choisir le type** (règle de décision selon la maturité) :
   **Clients** (référencement — le plus qualifié) → **Employés** (3D :
   Documenter, Démontrer, Dupliquer) → **Affiliés** (matériel + attribution +
   paiement rapide) → **Agences** (résultats prouvés dans le vertical).
3. **Référencement** : bâtir la **bienveillance** d'abord (tenir ses promesses,
   rapidité, extras), PUIS demander (après une victoire, à l'achat, événement,
   bonus à débloquer). Programme = mutuel, facile (1 clic), récompense claire,
   traçable, versée vite.

## Livrable type
Un **plan de lead getters** : type prioritaire + pourquoi, mécanique de
récompense (structure symétrique « X pour toi / X pour l'ami » par défaut),
plan de tracking, condition de passage au type suivant.

## Délégation de l'exécution
- **Parrainage / jeux concours / fidélité** → skill `animation-client`
  (rapidocrm : `lancer_jeu_concours_entreprise`, `get_loyalty_points`,
  sondages), actions visibles = **confirmées**.
- **Audiences (affiliés/superfans en pub)** → skill `audiences-crm`
  (rapido-meta-ads), consentement RGPD.
- **Employés (former, suivre)** → skills RH (`create-project-tool`,
  `create-task-tool`) et `detection-surcharge` (rapidorh).

## Anti-collision avec `rapidocrm:programme-ambassadeurs`
Ce skill **choisit le TYPE** de programme (parrainage / affiliation / ambassadeurs /
apporteurs pro) selon la maturité et **cadre** la stratégie — il ne l'opère pas. Une
fois le **programme ambassadeurs BraindCode** décidé (10 % client / 20 % apporteur),
son **exécution** (éligibilité, propositions, suivi des commissions, relances J+60)
revient à `rapidocrm:programme-ambassadeurs`. Règle miroir documentée dans les deux SKILL.md.

## Frontière avec `rapido-marketing:operations-influenceurs`
Ce skill **choisit le TYPE** de programme d'apport (parrainage / affiliation /
ambassadeurs / **influenceurs**) — **stratégie**. Une fois l'influence retenue,
l'**opération** des collaborations (sourcing → brief → contrat → tracking → ROI) revient
à `operations-influenceurs`. (`rapido-forge:scale-influencer-marketing` conçoit la
stratégie d'influence en exercice.) Frontière documentée des trois côtés.

## Cas d'usage croisés
- Amplifier le bouche-à-oreille → skill `contagious` (STEPPS).
- Rôles d'une machine commerciale (SDR/AE/CSM) → skill `predictable-revenue`.
- Fidéliser avant de faire parrainer → skill `animation-client`.

## Garde-fous
Consentement **RGPD** avant toute audience/séquence ; envois/publications
**confirmés** ; récompenses et budgets tracés, jamais un montant inventé.
