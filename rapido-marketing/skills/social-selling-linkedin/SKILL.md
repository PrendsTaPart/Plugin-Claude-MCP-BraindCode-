---
name: social-selling-linkedin
description: Utiliser quand l'utilisateur parle de social selling, veut prospecter sur LinkedIn, optimiser son profil LinkedIn de fondateur, ou construire une séquence LinkedIn. Produit une stratégie de profil, une cadence de contenu perso et des scripts de connexion/DM prêts à copier — jamais envoyés automatiquement.
---

# Social selling LinkedIn — présence + outreach conforme

> **Périmètre honnête.** Le MCP RapidoCMS **publie** sur les pages/comptes
> connectés (via `pipeline-contenu-social`) mais **n'automatise PAS les DM ni les
> invitations LinkedIn** (aucun connecteur — cf. matrice M0 : LinkedIn Outreach
> MANQUANT). Ce skill produit donc de la **stratégie**, du **contenu** et des
> **scripts prêts à copier** que l'utilisateur envoie **lui-même** (conformité
> LinkedIn — pas d'automatisation de DM).

## Étape 0 — Charger (obligatoire)
- `${CLAUDE_PLUGIN_ROOT}/reference/priorite-mcp.md` et `garde-fous-marketing.md`.
- `./rapido-kb/marketing/icp.md` s'il existe (cible) — sinon skill `icp-generator`.
- `./rapido-kb/` : `propositions-valeur.md`, `ton-et-accroches.md`,
  `cibles-personas.md`.

## Méthode

### (a) Stratégie de profil (fondateur)
Aligner le profil personnel sur l'**ICP** et la KB : accroche (headline =
promesse pour la cible), « à propos » façon récit (déléguer le message à
`storybrand-messaging` si besoin), preuves, CTA. Livrer les textes prêts à coller
dans LinkedIn.

### (b) Cadence de contenu perso
Définir un rythme (règle des 100 : ~100 min/jour de contenu, cf.
`core-four-strategie`). **Déléguer la production et la planification** au skill
`pipeline-contenu-social` **sur le compte personnel connecté** (ex. compte
`6Z5izYBhkC` — à confirmer via `list_connected_accounts`, jamais un id inventé).

### (c) Scripts de connexion / DM PRÊTS À COPIER
Rédiger invitations et messages personnalisés **depuis les données CRM du
prospect** (`get_entreprise`, skill `account-research`) : accroche ACA
(reconnaître/complimenter/demander, cf. fiche `docs/methodo/100m-leads/06-aca.md`),
valeur avant l'ask. **Jamais envoyés automatiquement** — l'utilisateur copie et
envoie lui-même. Fournir 2-3 variantes.

### (d) Suivi CRM
Chaque conversation **engagée** = prospect créé/mis à jour dans le pipeline via
`enregistrer_prospect` (rapidocrm) — **après confirmation**. Tracer l'étape et la
prochaine action.

## Livrable type
Profil optimisé (textes prêts) + plan de contenu délégué + **jeu de scripts
d'invitation/DM personnalisés** + plan de suivi CRM.

## Cas d'usage croisés
- Production/planification des posts → skill `pipeline-contenu-social`.
- Recherche du prospect avant le DM → skill `account-research`.
- Ton du profil et des messages → skill `storybrand-messaging`.
- Cadence et choix de canal → skill `core-four-strategie`.

## Garde-fous
**Aucune** automatisation d'invitation/DM LinkedIn (conformité) ; publication de
contenu **confirmée** ; `enregistrer_prospect` après accord ; données du prospect
issues du CRM, jamais inventées ; RGPD respecté.
