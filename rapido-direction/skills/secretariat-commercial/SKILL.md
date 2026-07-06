---
name: secretariat-commercial
description: Utiliser quand un prospect a écrit, ou pour organiser un RDV avec un contact. Lit le fil email, crée/retrouve l'entreprise au CRM, propose des créneaux réels, prépare le brouillon de réponse, puis crée l'événement et le RDV CRM à la confirmation.
---

# Secrétariat commercial (Gmail × CRM × Calendar)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/regles-direction.md` (brouillons
only, notifications d'événements, fuseau KB).

## Workflow

1. **Lire le fil** — `get_thread` : qui écrit, quelle demande, quelle
   urgence.
2. **CRM d'abord** — `search_entreprises` / `list_contacts` sur l'expéditeur :
   - reconnu → charger le contexte (`get_entreprise`,
     `get_historique_prospect`) ;
   - inconnu → créer (`create_entreprise` + `create_contact`) et ajouter au
     pipeline (`ajouter_prospect_pipeline`) avec confirmation.
3. **Créneaux RÉELS** — Calendar `suggest_time` (durée du RDV, fuseau de
   `rapido-kb/entreprise.md`, plages de travail) : 2-3 créneaux libres.
   Respecter les règles de l'`assistant-direction` (regrouper les RDV,
   protéger le deep work).
4. **Brouillon de réponse** — `create_draft` : réponse contextualisée
   proposant les 2-3 créneaux, ton de la marque. L'utilisateur relit et
   ENVOIE lui-même.
5. **À la confirmation du prospect** (nouveau message ou indication de
   l'utilisateur) :
   - Calendar `create_event` (avec Meet si visio ; les participants sont
     NOTIFIÉS par défaut — le rappeler avant) ;
   - CRM `create_rdv` (`entreprise_id`, type Visioconférence/Téléphonique/
     Présentiel, `date_debut`/`date_fin` YYYY-MM-DD HH:MM:SS, `mode_envoi`
     confirmé) ;
   - tâche de PRÉPARATION : note des points à préparer (deal, historique,
     objections probables — `concurrents.md` si concurrentiel).
6. **Tracer** — résumer le fil email dans la fiche CRM (`log_activity` :
   demande, créneaux proposés, RDV posé) — le CRM reste la mémoire
   commerciale.

## Garde-fous

- Pas de double création : vérifier `get_today_schedule` + `list_rdvs` avant
  de créer (le RDV existe peut-être déjà).
- Événement et RDV CRM doivent raconter la MÊME chose (heure, type, lieu) —
  c'est la fusion d'agenda qui le vérifie ensuite.
- Litige ou demande juridique dans le fil → escalade, pas de réponse
  automatique.
