---
description: Prospecter une zone via le webhook n8n, dédoublonner, enregistrer les seuls nouveaux sur accord
argument-hint: <ville> <spécialité>
---

Lance le skill `prospecter-une-zone` sur la ville et la spécialité passées
en argument : prospection_terms en lecture, run_prospection (coût webhook
annoncé), dédoublonnage par script (rapport montré), add_clients des seuls
nouveaux validés, add_log. Sans argument : demander la zone — ne jamais en
choisir une.
