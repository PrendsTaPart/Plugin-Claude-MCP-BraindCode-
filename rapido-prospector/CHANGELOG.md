# Changelog — plugin rapido-prospector

## 0.1.0 — 2026-10-25 — Prospector Hub de bout en bout

Première version, bâtie sur le serveur MCP Prospect (« Prospector Hub »,
https://prospect-pebble.lovable.app/mcp — ressource OAuth Supabase,
authentification au premier appel, aucun jeton dans le dépôt). Inventaire :
**66 outils** (docs/inventaires/prospect-tools-live.txt), relevés depuis le
manifeste MCP publié du projet (commit 6ad9af2) et confirmés par sonde HTTP
(401 + .well-known/oauth-protected-resource). RapidoCRM déclaré en serveur
OPTIONNEL (même déclaration que le plugin rapidocrm) pour la
synchronisation ; absent, le volet est sauté en le disant.

- **19 skills** : tableau-de-bord-prospection, prospecter-une-zone,
  qualifier-et-nettoyer-la-base, synchroniser-vers-rapidocrm,
  modeles-de-messages, campagne-email, campagne-sms, appels-automatises
  (désactivé par défaut), reseau-linkedin, linkedin-du-jour,
  sequences-linkedin, relances-j3-j7, calendrier-editorial, blog, videos,
  webinaires, lead-magnets, revenus-stripe, journal-d-activite.
- **4 agents** : chasseur, redacteur-de-sequences,
  programmateur-de-contenus, controleur-conformite-et-mesure — alignés sur
  les agents Academy (Prescripteurs, Contenus, Relance et devis) quand
  rapido-employe est installé.
- **12 commandes** : /prospect, /prospecter, /nettoyer-base,
  /campagne-email, /campagne-sms, /linkedin-du-jour, /relances,
  /calendrier, /webinaire, /lead-magnet, /mrr, /journal.
- **8 widgets HTML** (charte FoodEatUp du gabarit officiel Academy) +
  scripts/render_widget.py — sortie dans .claude/widgets-rendus/ (ignoré
  par git : aucune donnée de prospect dans le dépôt).
- **7 scripts stdlib testés**, formules affichées : dedoublonner.py
  (5 critères), normaliser_telephone.py (E.164 FR, mobiles),
  segments_sms.py (GSM-7/UCS-2), quotas.py (min KB / cadre Academy),
  entonnoir.py, mrr.py (MRR = estimation), conformite.py.
- **7 hooks testés en CI (30 cas allow/ask/deny)** : garde-envois-prospect
  (ask systématique sur les 5 envois ; deny lot/quota/fenêtre, compteurs
  .claude/state/prospect-envois.json), garde-conformite (deny sans
  identité/désinscription/STOP, appels non activés, liste d'opposition),
  garde-destructif-prospect (12 delete_* avec cascade rappelée),
  garde-publication (webinaire actif, statuts « publie », configuration),
  anti-doublon (add_clients sans dédoublonnage du jour), SessionStart
  (règles d'envoi + quotas), journal-prospect (écritures masquées,
  compteurs). Les champs confirm posés par le modèle ne valent jamais
  confirmation humaine.
- **Référence** : directives-outils.md (les 66 rôles et prérequis :
  provider_id, E.164, mobileOnly, liens temporaires, cascades),
  pieges-verifies.md, conformite-prospection.md (« à faire valider par un
  juriste », renvoi aux formations Academy conformite et rgpd),
  outils-sensibles.json (5 familles versionnées).
- **KB** : gabarit rapido-kb-template/prospection.md (quotas, fenêtre,
  identité d'expéditeur, désinscription/STOP, liste d'opposition,
  activation des appels automatisés) — bloc machine lu par les hooks ;
  sans KB, défauts prudents et appels à 0.
- CI : catalogue fail-closed `prospect` (66, min 60) + périmètre OUTILS
  strict pour `rapido-prospector/` (Prospect + RapidoCRM uniquement).
