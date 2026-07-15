# Changelog — plugin rapido-leadmagnet

## 0.4.0 — 2026-07-15 — campagne-lead-magnet (organique + payant + nurturing + mesure)

- Skill **`campagne-lead-magnet`** — diffusion complète : **organique** (campagne CMS
  + série de posts via `pipeline-contenu-social`/`calendrier-editorial` ; LinkedIn
  « commente pour recevoir » **semi-auto** brouillons + dédup n8n), **payant** (vidéo
  `usine-video-marketing` self_ai_disclosure + `montage-express` ; visuels
  `creatifs-publicitaires` ; Meta `lancement-campagne-meta` + `pixel-et-retargeting`
  **TOUT PAUSED**), **nurturing** (J0/J2/J5 via `machine-inbound`, **gate
  `delivrabilite-email` obligatoire** avant chaque lot), **mesure** par script.
- `scripts/stats_leadmagnet.py` (stdlib) : CPL, taux de conversion landing, taux de
  clic CTA, conversion RDV — formules affichées, dénominateur nul = « — » (jamais
  inventé). Vérifié (210/140 → CPL 1.5 ; 140/1000 → 14 %).
- Évals : 4 cas (refus activation ads, gate délivrabilité, mesure par script,
  LinkedIn semi-auto).

## 0.3.0 — 2026-07-15 — page-et-capture (landing + formulaire + segment + pipeline)

- Skill **`page-et-capture`** — la landing (Route B Lovable mode B via
  `usine-a-landing`), le formulaire (consentement RGPD non pré-coché), le segment
  `LM-{slug}`, le pipeline (`enregistrer_prospect` → `ajouter_prospect_pipeline`
  étape « Lead entrant » + tag `leadmagnet:{slug}`), la livraison (email
  transactionnel `create_template_email`/`send_email` + page merci, double opt-in
  optionnel) et un **test de bout en bout obligatoire** avant « page prête ».
- Route A CRM (`create_editor_template` landing_page) documentée en option vitrine
  (capture reste Lovable tant que `create_formulaire` absent — LM0).
- Évals : 4 cas (PDF absent, test bout-en-bout, refus RGPD, route).

## 0.2.0 — 2026-07-15 — fabrication-lead-magnet (rédaction + PDF brandé + bibliothèque)

- Skill **`fabrication-lead-magnet`** — du concept validé (`lead-magnet-machine`) au
  PDF brandé publié dans la bibliothèque CMS : gate d'entrée (pas de fabrication sans
  conception), rédaction par type (frameworks content-vault francisés), **gate qualité
  bloquant** (forme d'audit hormozi + frameworks maison `hundred-million-offers`),
  mise en page (`templates/lead-magnet.html` rempli via `get_brand`) → PDF →
  `upload_file_tool` → URL vérifiée → registre `rapido-kb/marketing/lead-magnets.md`.
- `templates/lead-magnet.html` — template print-ready A4 paramétré par la charte
  (couleurs/police/logo), pattern charte→template→PDF réimplémenté maison (NOTICE).
- Évals : 4 cas (refus sans conception, gate qualité bloque, chaîne complète,
  dégradation renderer). Corrections de refs (machine-inbound, social-selling-linkedin,
  template au lieu d'un skill pdf inexistant).


## 0.1.0 — 2026-07-15 — Squelette (parcours 9 étapes)

- Nouveau plugin **rapido-leadmagnet** (23e du marketplace) — l'**usine d'exécution**
  des lead magnets (la conception reste à `rapido-marketing:lead-magnet-machine`).
- `.mcp.json` : rapidocrm, rapidocms, rapidorh, lovable, facebook-ads.
- `reference/parcours-lead-magnet.md` : pipeline canonique **9 étapes** (conception
  déléguée → fabrication → page → CRM → livraison → organique → payant → nurturing →
  mesure) avec skill responsable, outils, livrable et critère de done par étape.
- `reference/articulations.md` : frontières (conception vs exécution ; machine-inbound
  = tuyauterie ; usine-a-landing = Route B ; hundred-million-offers = frameworks
  maison ; forge = pédagogie).
- `reference/garde-fous-leadmagnet.md` : RGPD/double opt-in, gate délivrabilité,
  LinkedIn semi-auto, self_ai_disclosure, budget ads confirmé, attribution MIT,
  **un seul lead magnet en prod à la fois**.
- **Hook** `garde-budget-ads` (ask sur création/activation Meta : PAUSED + coût max) +
  `Stop` (récap assets/IDs/statuts/sources). Tests fonctionnels au testeur.
- `NOTICE.md` : 5 sources MIT (frameworks francisés, aucun corps copié ; GPL exclu).
- Fondé sur l'audit **LM0** (`docs/IMPORTS-LEADMAGNET.md`) : moisson MIT + inventaire
  MCP réel (pas de create_formulaire/create_cta ; agents IA = users RH). Skills à
  venir (LM2→LM5).
