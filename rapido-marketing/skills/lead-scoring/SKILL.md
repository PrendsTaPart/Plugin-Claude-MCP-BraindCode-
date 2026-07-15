---
name: lead-scoring
description: Utiliser quand l'utilisateur veut scorer ses leads, savoir quels prospects prioriser aujourd'hui, ou mettre en place un lead scoring. Applique un modèle transparent à 3 facteurs — fit ICP × engagement × fraîcheur du signal (intention) — aux données CRM réelles via un script, sort une file de priorisation du jour avec 3 actions par tranche, et n'écrit dans le CRM qu'après confirmation.
---

# Lead Scoring — fit ICP × engagement × fraîcheur, transparent et par script

> Modèle **transparent et éditable** : le score n'est jamais « de tête ». Note
> M0 : RapidoCRM n'expose **pas** de champ de score natif (à demander au backend
> Tunis) — en attendant, le score vit dans la KB et l'output, et l'action passe
> par le déplacement d'étape + les tâches, après confirmation.

## Étape 0 — Charger (obligatoire)
- `${CLAUDE_PLUGIN_ROOT}/reference/priorite-mcp.md` et `garde-fous-marketing.md`.
- `./rapido-kb/marketing/scoring.md` (**pondérations éditables, 3 facteurs**) et
  `./rapido-kb/marketing/signaux.md` (**catalogue de signaux + validités**) —
  absents, les créer depuis `${CLAUDE_PLUGIN_ROOT}/reference/kb-templates/` après
  validation.
- `./rapido-kb/marketing/icp.md` s'il existe (définit l'axe *fit*) — sinon
  `icp-generator` d'abord.

## Le modèle (3 facteurs)
- **Fit ICP** (critères booléens) : secteur/taille/région cible… → poids si vrai.
- **Engagement** (compteurs, capés) : soumission, clic CTA, RDV, ouverture… →
  poids × min(compte, cap). Porte le **volume**.
- **Intention = fraîcheur du signal** : chaque signal daté du catalogue
  `signaux.md` compte **poids × fraîcheur**, `fraîcheur = max(0, 1 − âge/validité)`
  (un signal périmé ne compte plus). Par type, seule l'occurrence **la plus
  récente** compte — pas de double compte avec l'engagement.
- **Seuils** `chaud`/`tiede`/`froid`, tout dans `scoring.md`, éditable.

## Méthode

1. **Collecter les données CRM réelles** (jamais inventer un signal absent) :
   - Fit : `./rapido-kb/marketing/icp.md`.
   - Engagement & first-party : `get_pipeline`, `get_interaction_stats`,
     `get_historique_prospect`, `get_formulaire_soumissions`, `list_cta`
     (**si disponibles** — cf. M0, peuvent être vides).
   - **Signaux d'actualité** (levée, recrutement, changement de poste) : via
     `rapidocrm:account-research` — **dater** chaque signal (pour la fraîcheur).
2. **Calculer par script** (jamais de tête) :
   `python3 "${CLAUDE_PLUGIN_ROOT}/skills/lead-scoring/scripts/score_leads.py"`
   avec `{"model": <scoring.md>, "date_reference": <aujourd'hui>, "leads": [...]}`
   (chaque lead : `fit`, `engagement`, `signaux:[{type,date}]`) → par lead :
   fit_score, engagement_score, **intention_score**, total, tranche +
   **décomposition** (formule + fraîcheur par signal affichées).
3. **Restituer — file de priorisation du jour** : tableau trié par total +
   **3 actions par tranche** :
   - **chaud** → RDV via `rapido-direction:secretariat-commercial` ;
   - **tiède** → nurturing via `machine-inbound` ;
   - **froid** → réactivation via `rapidocrm:campagne-marketing` (envoi confirmé).
4. **Écrire dans le CRM UNIQUEMENT après confirmation** : déplacement d'étape
   (`deplacer_prospect_etape`), tag/tâche de suivi (`create_task`) ou RDV
   (`create_rdv`) — récapitulatif groupé, une validation.

## Livrable type
File de priorisation du jour (fit + engagement + intention + total + tranche),
répartition par tranche, plan d'actions par tranche. Modèle cité (poids de
`scoring.md`, signaux de `signaux.md`).

## Cas d'usage croisés
- Définir l'axe *fit* (l'ICP entreprise) → `icp-generator`.
- Enrichir les signaux d'actualité → `rapidocrm:account-research`.
- Prendre les RDV des leads chauds → `rapido-direction:secretariat-commercial`.
- Nurturing des tièdes → `machine-inbound`.

## Garde-fous
Score **par script**, pondérations et **validités éditables et affichées** ;
signaux tirés du CRM/`account-research` live, **jamais inventés** ; signal
**périmé = 0** ; **aucune** écriture CRM (étape/tâche) sans confirmation ; RGPD
respecté. Intent tiers (ZoomInfo/Bombora…) = **MCP manquant**
(`docs/OUTILS-MCP-MANQUANTS.md`).
