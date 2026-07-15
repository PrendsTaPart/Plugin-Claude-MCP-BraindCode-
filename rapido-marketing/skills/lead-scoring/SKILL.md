---
name: lead-scoring
description: Utiliser quand l'utilisateur veut scorer ses leads, savoir quels prospects prioriser, ou mettre en place un lead scoring. Applique un modèle transparent à 2 axes (fit ICP × engagement) aux données CRM réelles via un script, sort un tableau scoré avec des actions par tranche, et n'écrit dans le CRM qu'après confirmation.
---

# Lead Scoring — fit ICP × engagement, transparent et par script

> Modèle **transparent et éditable** : le score n'est jamais « de tête ». Note
> M0 : RapidoCRM n'expose **pas** de champ de score natif (à demander au backend
> Tunis) — en attendant, le score vit dans la KB et l'output, et l'action passe
> par le déplacement d'étape + les tâches, après confirmation.

## Étape 0 — Charger (obligatoire)
- `${CLAUDE_PLUGIN_ROOT}/reference/priorite-mcp.md` et `garde-fous-marketing.md`.
- `./rapido-kb/marketing/scoring.md` (**pondérations éditables**) — s'il n'existe
  pas, le proposer (2 axes, poids par défaut) et le créer après validation.
- `./rapido-kb/marketing/icp.md` s'il existe (définit l'axe *fit*) — sinon skill
  `icp-generator` d'abord.

## Le modèle (2 axes)
- **Fit ICP** (critères booléens) : secteur cible, taille cible, région cible… →
  poids si vrai.
- **Engagement** (compteurs) : soumission de formulaire, clic CTA, RDV, ouverture
  email… → poids × min(compte, cap).
- **Seuils** : `chaud` / `tiede` / `froid`. Tout est dans `scoring.md`, éditable.

## Méthode

1. **Collecter les données CRM réelles** : prospects du pipeline (`get_pipeline`),
   interactions (`get_interaction_stats`, `get_historique_prospect`), soumissions
   (`get_formulaire_soumissions`), clics CTA (`list_cta` **si disponibles** —
   vérifier, cf. M0 : peut être vide). Ne jamais inventer un signal absent.
2. **Calculer par script** (jamais de tête) :
   `python3 "${CLAUDE_PLUGIN_ROOT}/skills/lead-scoring/scripts/score_leads.py"`
   avec `{"model": <scoring.md>, "leads": [...]}` → chaque lead : fit_score,
   engagement_score, total, tranche + **décomposition** (formule affichée).
3. **Restituer** : tableau trié + **3 actions par tranche** :
   - **chaud** → proposer un RDV (skill `secretariat-commercial`, rapido-direction) ;
   - **tiède** → nurturing multicanal *(exécuteur `machine-inbound` — à livrer ;
     en attendant, skill `communication-client` / séquence via n8n)* ;
   - **froid** → réactivation (skill `campagne-marketing`, envoi confirmé).
4. **Écrire dans le CRM UNIQUEMENT après confirmation** : déplacement d'étape
   (`deplacer_prospect_etape`), tâche de suivi (`create_task`) ou RDV
   (`create_rdv`) — récapitulatif groupé, une validation.

## Livrable type
Tableau scoré (fit + engagement + total + tranche), répartition par tranche, et
le plan d'actions par tranche. Le modèle utilisé est cité (poids de `scoring.md`).

## Cas d'usage croisés
- Définir l'axe *fit* (l'ICP entreprise) → skill `icp-generator`.
- Prendre les RDV des leads chauds → skill `secretariat-commercial`.
- Machine outbound qui alimente le scoring → skill `predictable-revenue`.

## Garde-fous
Score **par script**, pondérations **éditables et affichées** ; signaux tirés du
CRM live, jamais inventés ; **aucune** écriture CRM (étape/tâche) sans
confirmation ; RGPD respecté.
