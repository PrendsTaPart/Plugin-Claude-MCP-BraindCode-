# Notes de release

## Boucle de vente — loop-engineering (2026-07-15)

Complète le loop-engineering du marketplace **sans rien refonder** (loop-engine-v2,
pilotage-marketing, autonomie.md et hooks inchangés — tout s'y branche).

- **Registre unifié des routines** (`reference/registre-routines.md`) — catalogue
  canonique préfixé par domaine (`FIN-*`/`STARTUP-*`/`GROWTH-*`/`VIDEO-*`/`MKT-*`/
  `VENTE-*`/`OPS-*`) ; anciens noms `R4…R9`, `R-MKT-*` conservés en **alias**
  (rétrocompatibilité, aucun déclencheur cassé). **Registre des KPIs** : source unique
  des formules = `rapido-startup:catalogue-kpi`.
- **`rapidocrm:pilotage-commercial`** (`1.6.0`) — orchestrateur de la boucle
  commerciale (Sense→Plan→Act→Feed→Report), calculs délégués à `catalogue-kpi`.
  Routines **`VENTE-HYGIENE`** (hygiène /100), **`VENTE-RELANCES`** (relances
  quotidiennes, table `vente_relances_journal`), **`VENTE-REVUE`** (couverture).
- **`rapidocrm:expansion-clients`** + **`programme-ambassadeurs`** — tunnel
  Studio→Agence→SaaS + programme 10 %/20 %, routine **`VENTE-EXPANSION`**.
- **`rapido-n8n` (`1.3.0`)** — recettes événementielles **`OPS-LEAD-CHAUD`**,
  **`OPS-CLIENT-GAGNE`**, **`OPS-ALERTE-CHURN`** (tables mémoire obligatoires ;
  installées sur confirmation, aucun workflow créé d'office).
- **KPI anti-divergence** — `catalogue-kpi` décrété source des formules ;
  `attribution-kpi-marketing` réduit à ce qui lui est propre (attribution par canal,
  LTGP/ROI ≠ LTV), commentaires « source : catalogue-kpi ».
- Descriptions `marketplace.json` périmées corrigées (rapido-startup, rapido-marketing).
- **Validation** : `valider-plugins.py` TOUT VALIDE (17 plugins) ; `tester-skills.py`
  0 FAIL/0 WARN/0 INFO ; dry-run lecture seule « pilote mon commercial » →
  `get_stats_pipeline_global` OK (chaîne SENSE résolue, données réelles).

Plugins touchés : `rapidocrm` 1.4.3→1.6.0, `rapido-n8n` 1.2.0→1.3.0,
`rapido-marketing` 0.16.1→0.16.3, `rapido-startup` 1.9.0→1.9.1.

---

# Notes de release — v1.0.0 (2026-07-10)

## Ajout — rapido-forge 1.1.0 (2026-07-10)

Tags (taxonomie fermée à 12) + niveaux sur les 180 exercices, prérequis
(graphe validé sans cycle, CI), `catalogue.json` machine-readable,
recherche sémantique hors-ligne (TF-IDF stdlib, synonymes FR→EN) + skill
`selecteur-framework`, agents branchés sur le catalogue, et orchestrateur
`lancement-projet-360` côté rapido-suite (1.2.0) — Forge pense, les
plugins exécutent.

## Ajout — rapido-forge 1.0.0 (2026-07-10)

Nouveau plugin **rapido-forge** : la source StartupsForge (PrendsTaPart)
mise aux conventions Rapido — 180 exercices en 3 parcours (dont les
46 skills bootcamp enrichis d'une méthode pas à pas), ~146 renvois croisés
vérifiés vers les plugins métier, 4 agents mentors (directeur-programme +
3 mentors de parcours). Livrables consignés dans
`./rapido-kb/startup/forge/`, hooks garde-ecriture-kb et rappel
« argent réel » Meta Ads.

Première version publique de la **marketplace Rapido** : des plugins Claude
Code pour piloter une entreprise via les systèmes Rapido (FoodEatUp,
RapidoCRM, RapidoCMS, RapidoRh) et leurs outils satellites (Canva, Lovable,
Meta Ads, n8n, Google Workspace).

## En chiffres

- **11 plugins**, **119 skills**, **17 agents** (personas) — chiffres
  recomptés depuis les fichiers au moment du tag.
- **8 plugins avec hooks** déterministes — 13 scripts de garde testés
  fonctionnellement sur stdin, plus des hooks Stop (récapitulatif exigé) et
  SessionStart (détection de la KB).
- 40 des 119 skills importés de 4 dépôts open source, attribués et licenciés ;
  audit de vérité des 3 serveurs Rapido CLOS (100 % des outils couverts ou
  ignorés volontairement avec raison — reference/audit-tools-2026-07-10.md).
- 2 scripts de validation stdlib + une CI GitHub Actions qui les rejoue.

## Les 5 points forts

1. **Garde-fous déterministes** — indépendants du modèle : confirmation
   forcée sur le destructif et les dépenses réelles (Meta Ads), refus pur des
   patterns interdits (transitions de facture hors DGFiP, températures
   invraisemblables, budgets au-delà du plafond maison), mode production n8n
   verrouillé — y compris quand le paramètre est absent.
2. **Base de connaissance `./rapido-kb/`** — construite par l'onboarding dans
   le répertoire de travail du CLIENT (jamais dans les plugins) : seuils,
   charte, personas et ton PRIMENT partout sur les défauts secteur ; le dépôt
   reste un produit portable, sans aucune donnée client.
3. **Dossier startup 360** (`rapido-suite`) — la mémoire de l'entreprise en
   8 fichiers (vision, persona, marché, offre, identité, traction, pitch,
   roadmap) que tous les agents lisent avant de produire, avec chiffres
   sourcés MCP et publication CMS/RH.
4. **Skills tiers attribués** — 40 skills d'anthropics/knowledge-work-plugins,
   anthropics/skills, wondelai/skills et nextlevelbuilder : LICENSE dans
   chaque dossier, ATTRIBUTIONS.md par plugin, clé `source:` dans chaque
   frontmatter, descriptions francisées pour le déclenchement, corps
   originaux intacts.
5. **CI de validation** (`.github/workflows/validation.yml`) — à chaque push
   et pull request : validation structurelle, batterie de tests
   skills/agents/hooks (0 FAIL, 0 WARN exigés), compilation de tous les .py,
   `bash -n` de tous les .sh — sans aucune dépendance pip (100 % stdlib).

## Limites connues

- **`N8N_MCP_URL` requise** pour `rapido-n8n` et le volet automatisations de
  `rapido-direction` (URL du serveur MCP de votre instance n8n). Sans elle,
  dégradation propre. Les comptes tiers (Canva, Lovable, Meta Ads,
  HyperFrames, Google) s'authentifient via leurs connecteurs/OAuth.
- ~~Endpoints Google à confirmer~~ — **résolu en 1.0.1** : les URLs de
  `rapido-direction/.mcp.json` sont désormais celles de la documentation
  officielle Google Workspace MCP
  (`gmailmcp`/`calendarmcp`/`drivemcp.googleapis.com/mcp/v1`, vérifiées le
  2026-07-06). La doc Gmail confirme au passage le design « brouillons
  uniquement » du plugin : le serveur crée des drafts et labellise, il
  n'envoie pas.
- **67 outils MCP « à vérifier en ligne »** : les catalogues facebook-ads,
  n8n et Google vivent sur les serveurs distants — checklist manuelle avant
  usage intensif dans `tests/rapports/outils-a-verifier-en-ligne.md`.
- Le contenu des 40 skills tiers reste en anglais (seules leurs descriptions
  de déclenchement sont francisées).

## Contribuer

Conventions, structure d'un skill/plugin, principe anti-donnée-inventée et
validation obligatoire avant PR : voir [CONTRIBUTING.md](CONTRIBUTING.md).
Sécurité et signalement de vulnérabilité : [SECURITY.md](SECURITY.md).
Licence : [Apache 2.0](LICENSE).
