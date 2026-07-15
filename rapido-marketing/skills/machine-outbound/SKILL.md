---
name: machine-outbound
description: Utiliser quand l'utilisateur veut lancer la prospection, monter une machine outbound, remplir son pipeline, ou construire une séquence de cold email. Orchestre la chaîne outbound CRM-first, de l'ICP au RDV — sourcing, priorisation par scoring, gate de délivrabilité obligatoire, séquences multi-touch nourries par les objections réelles, qualification, mesure — en confirmant chaque lot d'envoi et en respectant le RGPD.
---

# Machine outbound v2 — de l'ICP au RDV, CRM-first

Skill **orchestrateur** : il enchaîne les skills d'exécution et pose garde-fous,
KPI et conformité. Il **s'appuie sur la méthodo** du skill
`rapidocrm:predictable-revenue` (machine outbound B2B, rôles SDR/AE/CSM, ANUM) —
**la référencer, ne pas la dupliquer**. Voie Rapido d'abord (CRM), n8n pour le
récurrent.

**Prérequis** : `delivrabilite-email` (gate d'envoi) et `lead-scoring` (priorisation
3 facteurs) installés — utilisés aux étapes 2 et 3.

## Étape 0 — Charger (obligatoire)
- `${CLAUDE_PLUGIN_ROOT}/reference/priorite-mcp.md` et `garde-fous-marketing.md`.
- `./rapido-kb/marketing/icp.md` **OBLIGATOIRE** (critères de ciblage) — absent →
  invoquer `icp-generator` d'abord.
- `docs/methodo/etat-de-lart-2026.md` **§4 délivrabilité** et les fiches
  `docs/methodo/ops/` (coldoutboundskills : cadence, copy, délivrabilité).
- **`./rapido-kb/marketing/objections.md` s'il existe** (produit par
  `sales-intelligence-fireflies`) → les **réponses aux objections fréquentes
  nourrissent le copy** des séquences (accroches qui traitent l'objection dominante).
- **Lire `apprentissages.md` et `benchmarks.md` AVANT de proposer un plan** — les
  leçons et taux passés **priment**. Fichiers absents → créés depuis
  `${CLAUDE_PLUGIN_ROOT}/reference/kb-templates/` (voir `reference/memoire.md` ;
  mémoire d'exécution = tables n8n).

## Pipeline

### 1. Sourcing (workflows CRM officiels UNIQUEMENT)
- Prospecter selon l'ICP : `prospecter_maps`, `prospecter_entreprise`,
  `prospecter_prospect`, `rechercher_entreprise_siret` (rapidocrm).
- **Déduplication** : `rechercher_prospects` **avant tout ajout**.
- **Validation de la liste par l'utilisateur**, puis `enregistrer_tous_prospects`.
- **Conformité** : **aucun** achat de listes, **aucun** scraping hors ces outils
  CRM officiels (garde-fous-marketing §c).

### 2. Priorisation (on écrit d'abord aux mieux scorés)
- `lead-scoring` (**fit ICP × engagement × fraîcheur du signal**) sur les prospects
  sourcés → file de priorisation ; **les lots partent des mieux scorés d'abord**.
- Enrichissement/angle par prospect prioritaire : `rapidocrm:account-research`
  (contexte) + `rapidocrm:draft-outreach` (angle). **Personnalisation obligatoire**
  (règle du skill `rapidocrm:redaction-commerciale`) : jamais de message générique.
- **Option vidéo d'outreach premium** (les ~10 prospects les mieux scorés) : vidéo
  personnalisée via `rapido-higgsfield:usine-video-marketing` (si installé), **coût
  confirmé** avant génération — réservée aux comptes à fort potentiel.

### 3. GATE OBLIGATOIRE — délivrabilité (bloquant, sur CHAQUE lot)
- Avant tout envoi, invoquer **`delivrabilite-email`** : scorecard de liste +
  `spam_check` de la copy + plafonds/cadence de `delivrabilite.md`.
- **Un lot refusé (note sous le seuil KB) = PAS D'ENVOI, point.** Corriger la liste
  (dédoublonnage, retrait des emails de rôle/invalides) puis rejouer le gate.
  **Aucun contournement** — la règle n'a pas de dérogation dans ce skill.

### 4. Séquences multi-touch (chaque lot confirmé)
- **Cadence** (ajustable via KB) : **J0** email, **J3** relance, **J7** valeur,
  **J14** break-up. Rédigée avec `rapidocrm:redaction-commerciale`, **enrichie des
  hooks d'objections** (`objections.md`) ; planifiée via `schedule_email` (rapidocrm).
- **Volumes progressifs / plafond quotidien** : imposés par le gate (étape 3) et
  `delivrabilite.md` — jamais au-delà.
- **CHAQUE lot d'envoi confirmé explicitement** (hook `garde-envois`).
- **Suivi des réponses** → `deplacer_prospect_etape` (rapidocrm).
- **Anti-doublon des relances** : mémoire via table n8n → déléguer au skill
  `rapido-n8n:memoire-operationnelle`.

### 5. Qualification → RDV
- Grille reprise du skill `rapido-forge:scale-bant-qualification`.
- RDV pris → skill `rapido-direction:secretariat-commercial` (Google Calendar +
  `create_rdv` CRM).

### 6. Mesure
- Envoyés / réponses / RDV / opportunités **par séquence et par segment ICP** →
  `python3 "${CLAUDE_PLUGIN_ROOT}/skills/machine-outbound/scripts/stats_outbound.py"`
  (stdlib, taux calculés, jamais de tête), comparés à
  `./rapido-kb/marketing/benchmarks.md`.
- **Livrable** : rapport une page (taux par séquence/segment + vs benchmark +
  3 actions).

## Conformité (RGPD — encodée en dur, non négociable)
- **Consentement et base légale** rappelés avant toute séquence ; l'intérêt
  légitime B2B ne dispense pas de l'information ni du droit d'opposition.
- **Désinscription honorée IMMÉDIATEMENT** : retrait de la séquence + tag/étape
  CRM (`deplacer_prospect_etape` / `log_activity`), sans délai.
- **Pas d'achat de listes**, **pas de scraping** hors des workflows CRM
  officiels de l'étape 1.

## Modes dégradés
- n8n absent → séquences **manuelles confirmées** (anti-doublon via
  `rechercher_prospects` avant chaque relance).
- Envoi de masse indisponible → prioriser les prospects à **score élevé** en
  1-à-1 (`send_email` unitaire confirmé, après gate).
- `objections.md` absent → séquences sans hooks d'objections (signaler que
  `sales-intelligence-fireflies` les enrichirait).

## Capitalisation automatique (obligatoire)
À chaque **clôture de campagne/expérience** : **1 à 3 leçons datées et SOURCÉES**
(chiffre issu du script) dans `apprentissages.md` (format `date | contexte |
leçon | preuve | skill source`), et **mise à jour de `benchmarks.md`** si un taux
de référence change — via `mise-a-jour-kb`. Pas de leçon sans preuve chiffrée.

## Cas d'usage croisés
- Méthode outbound complète (rôles, ANUM) → `rapidocrm:predictable-revenue`.
- Priorisation des prospects → `lead-scoring`.
- Gate d'envoi → `delivrabilite-email`.
- Objections réelles pour le copy → `sales-intelligence-fireflies`.
- Rédaction des messages → `rapidocrm:redaction-commerciale`.
- Définir la cible → `icp-generator`.

## Garde-fous
`icp.md` prérequis ; **gate `delivrabilite-email` sur chaque lot (refus = pas
d'envoi)** ; **chaque lot d'envoi confirmé** (hook `garde-envois`) ; sourcing via
CRM officiel seulement ; RGPD (consentement + désinscription immédiate) ; taux
**par script** ; voie Rapido d'abord.
