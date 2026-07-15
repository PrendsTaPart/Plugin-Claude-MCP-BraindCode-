---
name: machine-outbound
description: Utiliser quand l'utilisateur veut lancer la prospection, monter une machine outbound, remplir son pipeline, ou construire une séquence de cold email. Orchestre la chaîne outbound CRM-first, de l'ICP au RDV — sourcing, enrichissement, séquences multi-touch, qualification, mesure — en confirmant chaque lot d'envoi et en respectant le RGPD.
---

# Machine outbound — de l'ICP au RDV, CRM-first

Skill **orchestrateur** : il enchaîne les skills d'exécution et pose garde-fous,
KPI et conformité. Il **s'appuie sur la méthodo** du skill `predictable-revenue`
(machine outbound B2B, rôles SDR/AE/CSM, ANUM) — **la référencer, ne pas la
dupliquer**. Voie Rapido d'abord (CRM), n8n pour le récurrent.

## Étape 0 — Charger (obligatoire)
- `${CLAUDE_PLUGIN_ROOT}/reference/priorite-mcp.md` et `garde-fous-marketing.md`.
- `./rapido-kb/marketing/icp.md` **OBLIGATOIRE** (critères de ciblage) — absent →
  invoquer le skill `icp-generator` d'abord.
- `docs/methodo/etat-de-lart-2026.md` **§4 délivrabilité** (warmup, plafonds,
  rotation, taux de réponse de référence).
- **Lire `./rapido-kb/marketing/apprentissages.md` et `benchmarks.md` AVANT de
  proposer un plan** — les leçons et taux passés **priment** sur les défauts.
  Fichiers absents → créés depuis `${CLAUDE_PLUGIN_ROOT}/reference/kb-templates/`
  (voir `reference/memoire.md` ; mémoire d'exécution = tables n8n).

## Pipeline

### 1. Sourcing (workflows CRM officiels UNIQUEMENT)
- Prospecter selon l'ICP : `prospecter_maps`, `prospecter_entreprise`,
  `prospecter_prospect`, `rechercher_entreprise_siret` (rapidocrm).
- **Déduplication** : `rechercher_prospects` **avant tout ajout**.
- **Validation de la liste par l'utilisateur**, puis `enregistrer_tous_prospects`.
- **Conformité** : **aucun** achat de listes, **aucun** scraping hors ces outils
  CRM officiels (garde-fous-marketing §c).

### 2. Enrichissement & angle
- Par prospect prioritaire (**priorité = score**, skill `lead-scoring`) :
  skill `account-research` (contexte) + skill `draft-outreach` (angle).
- **Personnalisation obligatoire** (règle du skill `redaction-commerciale`) :
  jamais de message générique de masse.

### 3. Séquences multi-touch
- **Cadence** (ajustable via KB) : **J0** email, **J3** relance, **J7** valeur,
  **J14** break-up. Écrite avec skill `redaction-commerciale`, planifiée via
  `schedule_email` (rapidocrm).
- **Volumes progressifs** et **plafond quotidien** définis dans
  `garde-fous-marketing.md` (warmup, ~500/j Gmail / 300/j Outlook, rotation —
  cf. état de l'art §4).
- **GATE OBLIGATOIRE avant tout lot** : invoquer `delivrabilite-email`
  (scorecard de liste + contrôle spam de la copy). Un lot noté **sous le seuil KB
  est REFUSÉ** — corriger la liste avant d'envoyer.
- **CHAQUE lot d'envoi confirmé explicitement** (hook `garde-envois`).
- **Suivi des réponses** → `deplacer_prospect_etape` (rapidocrm).
- **Version automatisée** : mémoire **anti-doublon** des relances via table n8n
  → déléguer au skill `memoire-operationnelle` (rapido-n8n).

### 4. Qualification
- Grille reprise du skill `scale-bant-qualification` (rapido-forge).
- RDV pris → skill `secretariat-commercial` (Google Calendar + `create_rdv` CRM).

### 5. Mesure
- Envoyés / réponses / RDV / opportunités **par séquence et par segment ICP** →
  `python3 "${CLAUDE_PLUGIN_ROOT}/skills/machine-outbound/scripts/stats_outbound.py"`
  (stdlib, taux calculés, jamais de tête), comparés à
  `./rapido-kb/marketing/benchmarks.md`.
- **Livrable** : rapport une page (taux par séquence/segment + vs benchmark +
  3 actions).

## Conformité (RGPD — encodée en dur)
- **Consentement et base légale** rappelés avant toute séquence ; l'intérêt
  légitime B2B ne dispense pas de l'information ni du droit d'opposition.
- **Désinscription honorée IMMÉDIATEMENT** : retrait de la séquence + tag/étape
  CRM (`deplacer_prospect_etape` / `log_activity`), sans délai.
- **Pas d'achat de listes**, **pas de scraping** hors des workflows CRM
  officiels de l'étape 1.

## Modes dégradés
- n8n absent → séquences **manuelles confirmées** (pas de mémoire auto : tenir
  l'anti-doublon via `rechercher_prospects` avant chaque relance).
- Envoi de masse indisponible → prioriser les prospects à **score élevé** en
  1-à-1 (`send_email` unitaire confirmé).

## Capitalisation automatique (obligatoire)
À chaque **clôture de campagne/expérience** : ajouter **1 à 3 leçons datées et
SOURCÉES** (chiffre issu du script) dans `./rapido-kb/marketing/apprentissages.md`
(format `date | contexte | leçon | preuve | skill source`), et **mettre à jour
`benchmarks.md`** si un taux de référence change — le tout via `mise-a-jour-kb`.
Pas de leçon sans preuve chiffrée.


## Cas d'usage croisés
- Méthode outbound complète (rôles, ANUM) → skill `predictable-revenue`.
- Priorisation des prospects → skill `lead-scoring`.
- Rédaction des messages → skill `redaction-commerciale`.
- Définir la cible → skill `icp-generator`.

## Garde-fous
`icp.md` prérequis ; **chaque lot d'envoi confirmé** (hook `garde-envois`) ;
sourcing via CRM officiel seulement ; RGPD (consentement + désinscription
immédiate) ; taux **par script** ; voie Rapido d'abord.
