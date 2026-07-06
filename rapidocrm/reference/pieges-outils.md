# Pièges des outils MCP (rapidocrm) — référence rapide

Consulter ce tableau au moindre doute avant d'appeler un outil.

| Outil | Paramètres pièges | Erreur fréquente | Parade |
|---|---|---|---|
| (tous) | `company_id` / `user_id` optionnels | Les passer systématiquement, ou les inventer | Ils sont déduits de la session authentifiée : ne les fournir que si la session ne les donne pas |
| Factures (`create_facture`, statut) | `statut` ∈ brouillon, en_attente, payee, en_retard | Rétrograder une facture `payee`, supprimer une facture émise | Transitions DGFiP uniquement : brouillon → en_attente → payee ; en_attente → en_retard → payee. Sinon : avoir. (Hook deny sur cible interdite) |
| `delete_*` (contacts, entreprises, contrats, produits, templates) | `confirm` | Suppression lancée sans confirmation | `confirm: true` obligatoire — et confirmation UTILISATEUR explicite avant (hook ask) |
| `create_devis` / `create_facture` | `taux_tva` en % ; `total_ttc`/`total_tva` auto-calculés | TTC calculé de tête et passé en dur | Fournir `total_ht` + `taux_tva`, laisser l'API calculer |
| `create_facture` | `devis_id` optionnel | Facture créée sans lien au devis accepté | Toujours passer `devis_id` quand la facture vient d'un devis |
| `schedule_email` / `schedule_sms` | `date_envoi` format `YYYY-MM-DD HH:MM:SS` | Date sans heure ou format libre | Format complet avec secondes |
| `send_sms` | `message` prioritaire sur `template_id` ; `numero` international | Template ignoré car message fourni ; numéro local | Choisir message OU template ; numéros en `+33...` |
| `send_email` / `send_newsletter` | cibles (`contact_id`/`employe_id`/`destinataire` ; `target`/`cible`) | Envoi de masse involontaire via `target` = Entreprises | Annoncer l'ampleur, confirmation avant tout envoi |
| `lancer_campagne` | passe le statut à `en_cours` | Lancement d'une campagne déjà en cours/terminée ou sur segment vide | Vérifier statut + `recalculer_segment` non vide + confirmation |
| `prospecter_*` | workflows N8N (latence possible) | Ajout au pipeline sans dédoublonnage | `rechercher_prospects` / `search_entreprises` avant `ajouter_prospect_pipeline` |
| `deplacer_prospect_etape` | `payload` (étape cible) | Étape devinée | Lire les étapes réelles via `get_pipeline` d'abord |
| `update_commercial_objectifs` / `set_commercial_status` | modifient le pilotage d'équipe | Ajustement silencieux d'objectifs | Accord explicite de l'utilisateur avant |
