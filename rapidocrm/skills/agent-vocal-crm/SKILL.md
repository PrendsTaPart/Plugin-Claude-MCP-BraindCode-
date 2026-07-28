---
name: agent-vocal-crm
description: Utiliser quand l'utilisateur parle de l'agent vocal du CRM ou d'appels téléphoniques automatisés — « configure mon agent vocal », « fais appeler cette entreprise par l'IA », « lance une tournée d'appels de prospection vocale », « quel est le script de l'agent vocal ». Configuration et déclenchement d'appels réels par agent vocal, toujours confirmés.
---

# Agent vocal CRM (configuration & appels réels)

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` si présent et
   l'appliquer.
2. Charger le script d'appel et les limites maison de `./rapido-kb/` s'ils
   existent (ils priment sur tout défaut).

## 1. Configuration (lecture puis écriture récapitulée)

- `get_agent_vocal_config` D'ABORD : script actuel, voix, horaires d'appel,
  limites. Toujours relire avant de modifier — jamais de configuration de tête.
- `update_agent_vocal_config` : toute modification est récapitulée avant/après
  (le script vocal parle à de vrais prospects au nom de l'entreprise — une
  formulation ratée coûte des relations, pas des tokens).
- Horaires : jamais de configuration autorisant des appels hors plages légales
  de démarchage téléphonique (France : jours ouvrés, 10h-13h / 14h-20h,
  jamais le dimanche ni jours fériés) — le signaler si la config le permet.

## 2. Appeler une entreprise (acte réel, confirmé)

- **`appeler_entreprise_vocal` déclenche un VRAI appel téléphonique** à un
  vrai interlocuteur → garde-fou du plugin : confirmation utilisateur
  obligatoire, avec récapitulatif « qui est appelé, avec quel script,
  pour quel objectif ».
- Avant de proposer l'appel : `get_entreprise` + `get_historique_prospect` —
  on n'appelle pas quelqu'un qu'on a eu hier, ni un prospect qui a demandé
  à ne plus être contacté (le vérifier dans l'historique).

## 3. Tournée de prospection vocale (série d'appels, confirmée)

- **`prospecter_et_appeler_vocal` enchaîne prospection ET appels réels en
  série** → même garde-fou, et récapitulatif AVANT : critères de ciblage,
  volume estimé d'appels, script utilisé. Jamais de tournée « pour voir ».
- Après la tournée : `get_historique_prospect` sur les appelés,
  `log_activity` pour tracer ce qui doit l'être, et passage des intéressés
  dans le pipeline (skill `prospection-pipeline`).

## Ce que ce skill NE fait PAS

- La prospection écrite (scraping, enregistrement de prospects, pipeline) →
  skill `prospection-pipeline`.
- Les emails et SMS → skill `communication-client` (mêmes garde-fous d'envoi).
- Les agents vocaux téléphoniques ElevenLabs → plugin rapido-elevenlabs.
