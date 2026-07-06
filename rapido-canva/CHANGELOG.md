# Changelog — plugin rapido-canva

## 0.4.0 — 2026-07-06

- Passe de portabilité : section « dégradation propre » dans les directives (Canva absent → explication + préparation du contenu, jamais d'erreur brute).

## 0.3.0 — 2026-07-06

- Agent `studio-creatif` : 5e canal « créatif publicitaire » (formats Meta,
  plugin rapido-meta-ads) — peu de texte incrusté, CTA lié à l'objectif ODAX,
  variantes A/B, avertissement argent réel.

## 0.2.0 — 2026-07-06

- Nouvel agent `studio-creatif` : arbitre les 4 canaux de création — image IA
  (rapide), Canva (support designé), vidéo (motion), Lovable (produit
  interactif, app, agent) — avec critères de choix par brief (interactivité,
  durée de vie, mouvement, délai/budget, données vivantes) et annonce des
  coûts avant de lancer.

## 0.1.0 — 2026-07-06

- Version initiale : `.mcp.json` (canva + foodeatup + rapidocms + rapidocrm +
  rapidorh).
- Références : `pieges-canva.md` (flux présentations outline → validation →
  generate-design-structured ; get-export-formats avant export ; transactions
  d'édition avec commit obligatoire ; candidats → create-design-from-candidate ;
  brand kits / palette KB ; autofill via create-design-from-brand-template,
  l'outil autofill-design n'étant pas exposé sur cette connexion),
  `CONFORMITE.md` (jamais de données personnelles clients dans les designs
  publics ; tout chiffre cite sa source), `directives-outils.md` (IDs, KB,
  confirmations, erreurs, récapitulatif).
- Skills : `menu-restaurant-design` (FoodEatUp × Canva, avec variante mise à
  jour de prix et option QR carte digitale), `visuels-sociaux-canva`
  (RapidoCMS × Canva, formats natifs par réseau + mode récurrent par brand
  templates), `supports-commerciaux` (RapidoCRM × Canva, proposal/présentation
  avec flux outline/business card, envoi CRM à double confirmation),
  `presentation-codir` (4 serveurs × Canva, outline validé puis
  generate-design-structured, export PPTX/PDF).
