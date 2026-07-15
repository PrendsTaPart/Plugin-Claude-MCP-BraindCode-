# Changelog — plugin rapido-leadmagnet

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
