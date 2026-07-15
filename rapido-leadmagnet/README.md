# rapido-leadmagnet — l'usine à lead magnets

Prend un lead magnet **conçu** (`rapido-marketing:lead-magnet-machine`, 7 étapes) et
l'**exécute de bout en bout** : fabrication (contenu + PDF brandé → bibliothèque
CMS), page de capture (Lovable → segment + pipeline CRM), campagne multi-canal
(organique + payant PAUSED + nurturing + mesure) et projet RH (tâches affectées aux
**agents IA**). Orchestre les skills existants — **ne les duplique pas**.

## État : squelette (0.1.0)

Fondations posées (parcours 9 étapes, articulations, garde-fous, hook budget-ads).
Les skills arrivent : `fabrication-lead-magnet` (LM2), `page-et-capture` (LM3),
`campagne-lead-magnet` (LM4), `projet-rh-lead-magnet` + agent `chef-usine-leadmagnet`
(LM5). Audit fondateur : `docs/IMPORTS-LEADMAGNET.md`.

## Décisions d'architecture (audit LM0)

- **Landing & capture = Route B (Lovable mode B)** — `usine-a-landing`, soumission →
  `enregistrer_prospect` (capture garantie via MCP). `create_formulaire`/`create_cta`
  n'existent pas côté CRM ; la landing CRM (`create_editor_template`) reste une option
  vitrine. Manques consignés dans `docs/OUTILS-MCP-MANQUANTS.md`.
- **LinkedIn « commente pour recevoir » = semi-auto** (brouillons, envoi humain).
- **Agents IA = users RH réels** → tâches assignables directement (Agent CRM 292,
  CMS 389, RH 391, Orchestrateur 406).

## Garde-fous

- **`garde-budget-ads`** (hook) — toute création/activation Meta → confirmation
  (PAUSED + coût max, activation écrite séparée).
- RGPD (consentement, double opt-in, désinscription), gate délivrabilité obligatoire,
  LinkedIn semi-auto, `self_ai_disclosure` vidéo, **un seul lead magnet en prod à la
  fois** : `reference/garde-fous-leadmagnet.md`. Le hook `garde-envois` du repo
  s'applique aux emails.

## Prérequis MCP

RapidoCRM, RapidoCMS, RapidoRH (natifs), Lovable (landing), Meta/Facebook Ads (pub).
Serveurs non connectés → dégradation propre annoncée. Voir README racine, section
« Connecter ou héberger les MCP ».

## Attribution

Frameworks francisés de 5 dépôts **MIT** (aucun corps copié ; GPL exclu) : `NOTICE.md`.
Portabilité absolue — aucune donnée client dans le dépôt. Slug **immuable**.
