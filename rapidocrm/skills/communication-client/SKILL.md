---
name: communication-client
description: Utiliser quand l'utilisateur veut envoyer un email ou un SMS, planifier un envoi, ou contacter une entreprise. Part de la fiche entreprise, choisit la cible et le canal, avec template quand disponible.
---

# Communication client

## Workflow

1. **Partir de la fiche entreprise** — `get_entreprise` (`id` ou `q` recherche
   libre) pour vérifier l'entreprise et récupérer son `entreprise_id`. Si
   l'entreprise n'est pas trouvée, utiliser `search_entreprises` et demander
   confirmation.
2. **Choisir la cible** :
   - un contact précis → `contact_id` (retrouver via `list_contacts` /
     `get_contact`) ;
   - un employé de l'entreprise → `employe_id` ;
   - une adresse/numéro direct → `destinataire` (email) ou `numero` (SMS, format
     international `+33...`).
3. **Utiliser un template quand disponible** — `list_templates_email` /
   `list_templates_sms` puis passer `template_id`. Sinon rédiger le contenu et le
   faire valider par l'utilisateur avant envoi.
4. **Envoyer ou planifier** :
   - Email immédiat → `send_email` (`entreprise_id`, `sujet` requis ; `contenu` ou
     `template_id` ; cible de l'étape 2) ;
   - Email planifié → `schedule_email` (`entreprise_id`, `date_envoi`
     YYYY-MM-DD HH:MM:SS, `sujet` ; `target` ∈ Contacts | Employes | Entreprises ou
     `destinataires` liste d'emails) ;
   - SMS immédiat → `send_sms` (`entreprise_id` ; `message` prioritaire sur
     `template_id`) ;
   - SMS planifié → `schedule_sms` (`entreprise_id`, `date_envoi`) ;
   - Newsletter → `send_newsletter` (`entreprise_id` ; `cible` ; `date_envoi`
     optionnelle = envoi immédiat si absente).

## Garde-fous

- Confirmation explicite de l'utilisateur avant TOUT envoi immédiat (récapituler :
  canal, destinataire, sujet/contenu). Un envoi parti ne se rappelle pas.
- Pour un envoi planifié, confirmer la date/heure exacte et le fuseau implicite.
- Ne jamais envoyer à une liste (`target`/`cible` = Entreprises/Contacts/Employes)
  sans annoncer l'ampleur de l'envoi ; pour du vrai envoi de masse segmenté,
  rediriger vers le skill campagne-marketing.
- Tracer les échanges importants avec `log_activity`.
