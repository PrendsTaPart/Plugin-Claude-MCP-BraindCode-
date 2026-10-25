---
name: prospecter-une-zone
description: Utiliser quand l'utilisateur veut lancer une prospection Prospector Hub sur une zone — « prospecte les boulangeries de Lille », « trouve des restaurateurs sur Lyon via Prospect », « lance la prospection n8n ». Déroule run_prospection → dédoublonnage → accord → add_clients → add_log.
---

# Prospecter une zone (serveur Prospect)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
  `${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md` ;
- `./rapido-kb/prospection.md` s'il existe.

## Démarche
1. **Termes** : `prospection_terms` SANS paramètre (lecture). Si la zone ou
   la spécialité demandée n'y est pas, proposer l'ajout — add_kind +
   add_value SEULEMENT après accord (le hook garde-publication demande).
2. **Historique** : `prospection_history` sur la zone — si elle a déjà été
   prospectée récemment, le dire avant de relancer (coût webhook n8n).
3. **Lancer** : `run_prospection` (city, speciality) — ANNONCER que c'est
   un appel au webhook n8n (coût externe) et que les résultats ne sont PAS
   enregistrés par le serveur.
4. **Dédoublonner** : sauvegarder la réponse brute et la base
   (`list_clients`, mêmes zone/spécialité puis élargi) en JSON temporaire,
   puis `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/dedoublonner.py nouveaux.json
   existants.json rapport.json` — critères affichés : placeId, site,
   téléphone E.164, e-mail, nom+adresse normalisés.
5. **Montrer** le rapport : nouveaux / doublons (avec le critère) / fiches
   sans contact. L'humain tranche ce qui s'enregistre.
6. **Enregistrer** : `add_clients` des SEULS nouveaux validés, avec `city`
   et `speciality`. Puis `add_log` (action, message, count).
7. **Suite CRM** : si RapidoCRM est branché dans la session, proposer le
   skill `synchroniser-vers-rapidocrm` — sans l'enchaîner d'office.

## Pièges
- `run_prospection` ne sauvegarde rien : sans l'étape 6, tout est perdu.
- Jamais d'`add_clients` sans dédoublonnage : le hook anti-doublon le
  rappelle (ask), et une base sale coûte des quotas d'envoi plus tard.
- Le sourcing Google Maps vers RapidoCRM existe déjà : skill
  `sourcing-gmaps` (plugin rapido-gmaps). Ce skill-ci alimente la base
  PROSPECT ; ne pas dupliquer l'autre chemin.

## Dégradation propre
Webhook n8n en erreur : restituer le message du serveur, consigner
(`add_log`), ne pas réessayer en boucle.
