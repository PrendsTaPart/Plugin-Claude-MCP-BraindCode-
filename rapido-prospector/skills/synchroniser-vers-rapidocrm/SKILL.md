---
name: synchroniser-vers-rapidocrm
description: Utiliser quand l'utilisateur veut passer des prospects Prospect dans RapidoCRM — « pousse ces prospects dans le CRM », « synchronise Prospect avec RapidoCRM », « mets les qualifiés dans le pipeline ». Anti-doublons CRM d'abord, puis enregistrement et entrée de pipeline.
---

# Synchroniser les prospects vers RapidoCRM

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (section serveur
  optionnel) ;
- vérifier que le serveur RapidoCRM répond dans la session : ABSENT, le
  volet est sauté EN LE DISANT (aucune simulation).

## Démarche
1. **Choisir** : `list_clients` (Prospect) filtré sur les fiches QUALIFIÉES
   (statut, contact valide) — montrer la sélection.
2. **Anti-doublons CRM** : `rechercher_prospects` (RapidoCRM) sur chaque
   fiche (nom, ville, téléphone, e-mail) — un prospect déjà au CRM ne se
   recrée pas, on le signale.
3. **Enregistrer** : `enregistrer_tous_prospects` pour le lot validé, puis
   `ajouter_prospect_pipeline` pour l'entrée d'étape — après accord sur la
   liste finale.
4. **Journal** : `add_log` côté Prospect (action « sync-crm », count).

## Délégation (ne pas recopier)
- Le pipeline, les relances et la revue vivent côté plugin rapidocrm
  (skill `prospection-pipeline`, skill `coaching-pipeline`) : ce skill ne
  fait que le PONT Prospect → CRM.
- Le sourcing Google Maps → CRM direct est le skill `sourcing-gmaps`
  (rapido-gmaps) : si la demande part de Maps et non de la base Prospect,
  c'est lui qui s'applique.

## Pièges
- Deux bases = deux vérités : toujours dédoublonner CÔTÉ CIBLE (étape 2),
  même si la base Prospect est propre.
- Ne pousser que les champs utiles (minimisation) ; pas de notes libres
  contenant des données sensibles.

## Dégradation propre
RapidoCRM non branché ou en erreur : restituer l'erreur, garder la
sélection prête, proposer de relancer quand le connecteur répond.
