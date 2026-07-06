# Changelog — plugin rapido-direction

## 1.0.0 — 2026-07-06

- Première version publique.

## 0.1.0 — 2026-07-06

- Version initiale — plugin GÉNÉRALISTE : chaque utilisateur connecte SON
  compte Google (OAuth individuel, URLs de serveurs publiques identiques pour
  tous). `.mcp.json` : gmail + google-calendar + google-drive + rapidocrm +
  foodeatup + n8n (${N8N_MCP_URL}).
- `README-installation.md` : connexion du compte Google (connecteurs
  claude.ai ou OAuth Claude Code), vérification par search_threads,
  dégradation propre si outils absents.
- `reference/regles-direction.md` : emails = brouillons UNIQUEMENT (Claude
  rédige, l'humain envoie — jamais contourné) ; agenda avec notification par
  défaut, suggest_time, fuseau lu dans rapido-kb/entreprise.md ; Drive =
  coffre officiel (Clients/<Nom>/, jamais de suppression) ; agenda TRIPLE
  (Calendar + get_today_schedule CRM + list_reservations FoodEatUp, toujours
  fusionnés) ; matrice ponctuel/récurrent/sensible.
- Hooks : ask sur corbeille/spam/suppression (Gmail/Drive, défensif) et
  delete_event (annulation notifiée aux invités) ; Stop avec récap brouillons
  (envoi restant humain), événements, classements, IDs CRM.
- Skills : `journee-du-dirigeant` (collecte parallèle, une page, 3
  priorités), `tri-boite-mail` (étiquettes, brouillons contextualisés CRM,
  escalade du sensible), `secretariat-commercial` (thread → CRM →
  suggest_time → brouillon → event + rdv + note), `coffre-documents`
  (classement sans suppression, contrats signés copiés, backup mensuel KB),
  `delegation-recurrence` (le récurrent part en workflow n8n).
- Agent `assistant-direction` : chef de cabinet — regroupe les RDV, défend
  2 h de deep work/jour, tout en brouillon, escalade litiges/remises>
  seuil KB/RH, matrice de routage ; Google complet + lecture CRM/FoodEatUp/
  n8n.
