# Directives communes d'utilisation des outils (rapidocrm)

Règles applicables à TOUTE exécution de skill de ce plugin.
Au moindre doute sur un outil (paramètres pièges, formats, enums), consulter
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-outils.md`.

## 1. Résolution d'ID d'abord

- Ne JAMAIS deviner un ID : `entreprise_id`, `contact_id`, `facture_id`,
  `segment_id`, IDs de campagnes, de commerciaux, de templates…
- Récupérer chaque ID via l'outil de liste/recherche correspondant
  (`search_entreprises`, `list_contacts`, `list_factures`, `list_commerciaux`,
  `list_templates_email`…) ou le demander à l'utilisateur, AVANT d'agir.
- `company_id` / `user_id` sont déduits de la session authentifiée : ne les
  passer explicitement que si la session ne les fournit pas.

## 2. Confirmation avant action destructrice ou irréversible

Récapituler l'action et obtenir un accord explicite de l'utilisateur avant :
- toute suppression (`delete_contact`, `delete_entreprise`, `delete_contrat`,
  `delete_product`, `delete_template_email`, `delete_template_sms`…) ;
- tout ENVOI immédiat (`send_email`, `send_sms`, `send_newsletter`) et tout
  lancement de campagne (`lancer_campagne`) — un envoi parti ne se rappelle pas ;
- tout changement de statut légal de facture (voir règles ci-dessous).
Une confirmation PAR action ; annoncer l'ampleur avant tout envoi de masse.

## 3. Ne jamais inventer de données

Montants (HT/TTC), taux de TVA, dates d'échéance, coordonnées : toujours fournis
par l'utilisateur ou lus via l'API. Valeur manquante → la demander.

## 4. Locale et formats

- Monnaie : euros. Dates ISO `YYYY-MM-DD` ; envois planifiés au format
  `YYYY-MM-DD HH:MM:SS` (`schedule_email`, `schedule_sms`).
- Statuts de facture : `brouillon`, `en_attente`, `payee`, `en_retard`.
  Transitions autorisées (logique DGFiP) : `brouillon → en_attente → payee` ou
  `en_attente → en_retard → payee`. INTERDIT : rétrograder une facture `payee`
  ou supprimer une facture émise — proposer un avoir.
- Statuts de devis : `brouillon`, `en_attente`, `accepte`, `refuse`, `expire`.

## 5. Gestion d'erreur

Si un outil échoue : expliquer clairement la cause probable, ne PAS boucler ni
réessayer aveuglément, proposer l'alternative manuelle (ex. action dans
l'interface RapidoCRM).

## 6. Récapitulatif de fin de séquence

Terminer chaque séquence par la liste des objets créés/modifiés avec leurs IDs
(prospects, entrées pipeline, segments, campagnes, devis, factures, envois
programmés) et tracer les échanges importants avec `log_activity`.
