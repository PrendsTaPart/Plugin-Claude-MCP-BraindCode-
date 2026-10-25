---
name: prospecter-une-zone
description: Utiliser quand l'employé cherche de nouveaux restaurants, que l'utilisateur dit « prospecte ta zone aujourd'hui », « trouve les établissements du quartier gare », « alimente le pipeline de la zone ». Trouve les établissements, écarte les doublons, enregistre au pipeline, puis lance la séquence validée — toujours en Aperçu.
---

# Prospecter une zone (trouver, dédoublonner, séquencer)

Familles engagées : **preparer** (fiches et pipeline, Brouillon) puis
**prospecter** (séquences, Aperçu — accord à chaque envoi).

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.
2. Cadre du jour en main (skill `prise-de-poste`) ; zone et cible depuis les
   objectifs (`get_deployment_plan`) ou la KB.

## Workflow

1. **Trouver** : `prospecter_maps` (RapidoCRM) sur la zone et la cible — une
   zone et une spécialité à la fois, la liste reste lisible. Pour un
   sourcing géo-ciblé poussé (scoring ICP, enrichissement), DÉLÉGUER au
   plugin `rapido-gmaps` (skill `sourcing-gmaps`) — on ne recopie pas sa
   mécanique.
2. **Dédoublonner, toujours** : `rechercher_prospects` sur chaque fiche
   avant d'écrire — un doublon ne s'enregistre pas.
3. **Enregistrer** : `enregistrer_prospect` puis `ajouter_prospect_pipeline`
   — fiches réelles (nom, ville, spécialité issus de la recherche), en tête
   du pipeline.
4. **Séquencer** (si Prospector Hub est branché) : `prospection_history`
   pour ne pas refaire une recherche, puis `run_prospection` sur un MODÈLE
   VALIDÉ par le responsable — famille prospecter : l'appel se montre et
   attend l'accord (les outils du hub n'ont pas d'aperçu : l'aperçu, c'est
   nous). Hub absent : volet sauté en le disant, la relance passera par les
   brouillons Gmail (skill `relancer-j3-j7`).
5. **Compter** : prospects trouvés / ajoutés / écartés (doublons), au journal.

KPI : `taux-prospection-rdv`, `rdv-tenus`, `pipeline`.
Formations : `prospection` (7 missions), `prospector-hub` (9), `rapidocrm`.

## Garde-fous

- Jamais de liste achetée, jamais de contact inventé : tout vient de la
  prospection outillée (anti-donnee-inventee en filet).
- Quotas du jour (`envoisJour`) comptés par le journal ; atteints = on
  s'arrête (garde-envois en filet).
- Un « non » se note (`log_activity`) et arrête la séquence pour ce
  prospect.
