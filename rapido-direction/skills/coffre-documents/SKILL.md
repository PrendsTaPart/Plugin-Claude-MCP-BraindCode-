---
name: coffre-documents
description: Utiliser quand l'utilisateur veut classer un document ou retrouver un contrat, une facture, un fichier. Gère le Drive du compte connecté comme coffre officiel — arborescence Clients/<Nom>/, classement sans suppression, sauvegarde de la KB.
---

# Coffre documents (Drive × CRM × FoodEatUp)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/regles-direction.md` (Drive =
coffre officiel, jamais de suppression). Outils Drive absents → expliquer +
`README-installation.md`.

## Workflow

1. **Retrouver** — `search_files` (nom, type, contenu) ; `read_file_content`
   pour vérifier qu'on tient le bon document ; répondre avec le LIEN direct
   du fichier (et son chemin).
2. **Classer** — arborescence officielle : `Clients/<Nom de l'entreprise>/`
   (créer le dossier client au besoin). Un document mal rangé se DÉPLACE ou
   se COPIE (`copy_file`) au bon endroit — jamais de suppression.
3. **À la signature d'un contrat CRM** — quand `update_contrat_status` passe
   un contrat à `signe` (skill `contrats-clients`, plugin rapidocrm) :
   copier le PDF du contrat dans `Clients/<Nom>/` (via `create_file` /
   `copy_file`) — le Drive est le coffre, le CRM garde la référence
   (`log_activity` avec le lien Drive).
4. **Factures et documents FoodEatUp** — même logique : les documents
   officiels (factures fournisseurs, rapports d'hygiène) se classent dans
   l'arborescence (`Fournisseurs/<Nom>/`, `Conformité/`).
5. **Sauvegarde mensuelle de la KB** — une fois par mois (ou sur demande) :
   `create_file` d'une copie des fichiers de `./rapido-kb/` vers un dossier
   `Rapido-KB/backup-YYYY-MM/` du Drive. Proposer d'en faire un workflow n8n
   (skill `delegation-recurrence`) plutôt que d'y penser à la main.

## Garde-fous

- JAMAIS de suppression ni d'écrasement : les versions se succèdent
  (backup daté), les erreurs se reclassent.
- Vérifier les permissions avant de partager un lien
  (`get_file_permissions`) : un contrat client ne se partage pas en
  « tous ceux qui ont le lien ».
- Documents sensibles (contrats, salaires) : ne pas recopier leur contenu
  dans la conversation au-delà du nécessaire — le lien suffit.
