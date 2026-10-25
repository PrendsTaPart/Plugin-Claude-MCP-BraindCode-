---
name: sequences-linkedin
description: Utiliser quand l'utilisateur prépare ses messages LinkedIn à l'avance — « programme la séquence LinkedIn de la semaine », « planifie un message pour cette connexion jeudi ». Modèles par connexion et calendrier, en rappelant que rien ne part tout seul.
---

# Séquences LinkedIn (préparer, sans jamais envoyer)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (calendrier =
  enregistrement seul).

## Démarche
1. **Choisir les connexions** : `list_linkedin_connections`
   (`enrichedOnly: true` de préférence) — cibles réelles, pas de liste
   inventée.
2. **Modèles par connexion** : `list_linkedin_templates` (connectionId),
   `add_linkedin_template` / `update_linkedin_template` — texte
   personnalisé par les champs réels de la fiche (entreprise, poste).
3. **Programmer** : `add_linkedin_scheduled_message` (connectionId,
   message OU templateId, scheduledAt heure de Paris) — répartir sur les
   jours pour rester sous le quota quotidien.
4. **Relire la semaine** : `list_linkedin_scheduled_messages` (période) —
   équilibre de la charge, pas deux messages à la même personne la même
   semaine (croiser `list_linkedin_message_history`).
5. **Ajuster** : `update_linkedin_scheduled_message` /
   `delete_linkedin_scheduled_message` (confirmation pour la suppression).

## À dire à chaque fois
RIEN ne part automatiquement : la séquence programmée attend le rituel
quotidien (skill `linkedin-du-jour`), où chaque envoi est confirmé un par
un. C'est le fonctionnement du serveur, pas une option.

## Pièges
- Programmer plus que le quota quotidien = file intraitable : caler le
  volume sur `scripts/quotas.py`.
- La copy LinkedIn se travaille avec le plugin rapido-copywriter (skill
  `copy-linkedin`) ; ici on PLANIFIE.

## Dégradation propre
Connexion non enrichie dans la cible : la programmer quand même est
inutile (l'envoi échouera) — renvoyer d'abord vers `reseau-linkedin`.
