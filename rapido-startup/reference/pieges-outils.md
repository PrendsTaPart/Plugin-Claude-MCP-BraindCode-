# Pièges des outils MCP (rapido-startup) — référence rapide multi-serveurs

Condensé des pièges critiques des serveurs orchestrés (Stripe + les 4
serveurs Rapido). Au moindre doute sur un outil précis, consulter le
`reference/pieges-outils.md` du plugin dédié.

| Outil | Paramètres pièges | Erreur fréquente | Parade |
|---|---|---|---|
| FoodEatUp (quasi tous) | `establishment_id` EXPLICITE requis | Appel sans ID | Le demander avant tout appel FoodEatUp (contrairement aux 3 autres serveurs, la session ne le fournit pas) |
| CRM/CMS/RH (tous) | `company_id`/`user_id` déduits de la session | Les passer ou les inventer | Ne les fournir que si la session ne les donne pas |
| `finance_summary` (FoodEatUp) | `date_from`/`date_to` défaut = mois en cours | Période incohérente avec les autres serveurs | MÊME période partout dans une comparaison multi-serveurs |
| Factures CRM (statuts) | transitions DGFiP limitées | Rétrograder `payee`, supprimer une facture émise | brouillon → en_attente → payee ; en_attente → en_retard → payee ; sinon avoir (hook deny) |
| `create_campagne` | existe sur CRM ET CMS avec des schémas DIFFÉRENTS | Paramètres de l'un passés à l'autre | CRM : canal/segment/statut ; CMS : drapeaux facebook/instagram/linkedin/tiktok à 1/0 |
| `schedule_email`/`schedule_sms` (CRM) vs `schedule_draft_tool` (CMS) | formats de date différents | Format CRM utilisé côté CMS | CRM : `YYYY-MM-DD HH:MM:SS` ; CMS : `post_date` `Y-m-d` + `post_heure` `H-i-s` (tirets) |
| `schedule_draft_tool` (CMS) | `post_heure` au format STRICT `H-i-s` (schéma vérifié le 2026-07-10) | Envoyer `HH:MM:SS` (deux-points) | `18-30-00`, jamais `18:30:00` |
| `ingishts_campagne` (CMS) | orthographe | Nom « corrigé » → introuvable | Utiliser le nom exact du serveur |
| `post_insights` (CMS) | max 10 posts | Lots trop gros | Découper en lots de 10 |
| `create-user-tool` (RH) | rôle/département requis, invitation immédiate | Utilisateur avant rôle | Ordre : permissions → rôle → département → utilisateur (tout valider avant) |
| `create-daily-tool` (RH) | 1/jour, 0,5–24 h, membres | Doublon de daily | `get-dailies-tool` du jour avant |
| Priorités RH | projet 1-3 (1=basse) vs tâche 0-2 (0=urgent) | Échelles confondues | Vérifier l'échelle selon l'outil |
| `add_temperature` (FoodEatUp) | plage plausible | Valeur inventée | Relevé réel uniquement (hook deny hors -30/+90 °C) |
| Stripe (tous) | lecture vs écriture | Écrire pendant une routine d'analyse | **Stripe = LECTURE SEULE dans les routines** ; toute écriture (`stripe_api_write` : remboursement, facture, coupon…) n'arrive que sur demande explicite, avec confirmation (hook `garde-stripe-write` + approbation native Stripe) |
| Montants Stripe | `amount` en CENTIMES (plus petite unité de la devise) | Lire `12990` comme 12 990 € | 12990 = 129,90 € : diviser par 100 (devises à décimales) avant tout affichage ou calcul, via un script — jamais de tête |
| Écritures multi-serveurs | irréversibilité en chaîne | 2 serveurs modifiés sur une validation | Confirmation PAR SYSTÈME ; en cas d'échec : stop + liste de ce qui est créé |
