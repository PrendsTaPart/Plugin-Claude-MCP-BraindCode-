---
name: presentation-codir
description: Utiliser quand l'utilisateur veut la présentation du CODIR ou des slides pour le comité de direction. Collecte les données des 4 serveurs Rapido, construit l'outline (1 slide par domaine + arbitrages), le fait valider, puis génère la présentation Canva et l'exporte.
---

# Présentation CODIR (Rapido-Suite × Canva)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`,
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-canva.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/CONFORMITE.md`.

## Workflow

1. **Données (lecture seule, même période partout)** — si le plugin
   rapido-suite est installé, dérouler son skill `comite-de-direction` ;
   sinon collecter directement : CRM (`get_dashboard_general_stats`,
   `get_revenue_summary`, `get_stats_pipeline_global`), CMS
   (`list_scheduled_posts` + `post_insights` par lots de 10), RH
   (`get-projects-list-tool`, `get-dailies-tool`), FoodEatUp
   (`finance_summary`, `establishment_id` requis). Chaque chiffre garde sa
   source.
2. **Construire l'outline** — 1 slide par domaine + ouverture et arbitrages :
   - Slide 1 : synthèse exécutive (période, 3 chiffres clés) ;
   - Slides 2-5 : Commercial / Contenu & marque / Équipe & projets /
     Restaurant — chacune : chiffre clé, tendance, alerte, décision proposée ;
   - Slide 6 : arbitrages inter-domaines (diagnostics croisés + décisions,
     3 max).
   Descriptions en puces markdown à TIRETS (`- Item\n- Item`), jamais « • ».
   Sauter un domaine non disponible (le dire).
3. **FLUX OUTLINE OBLIGATOIRE** — `request-outline-review` (`topic` ≤ 150
   caractères, `audience: "professional"`, `length: "balanced"` si 6 slides,
   `pages` = l'outline ci-dessus, `brand_kit_id` si choisi via
   `list-brand-kits`). Attendre la VALIDATION de l'utilisateur dans le widget.
   Toute demande de modification (retirer une slide, réordonner…) = re-appeler
   `request-outline-review` avec l'outline modifié.
4. **Générer** — `generate-design-structured` (`topic`, `audience`, `style`,
   `length`, `design_type: "presentation"`, `presentation_outlines` = outline
   approuvé). JAMAIS `generate-design` pour cette présentation.
5. **Export** — `get-export-formats` puis `export-design`
   (`format.type: "pptx"` ou `"pdf"` selon le choix de l'utilisateur) ;
   afficher l'URL de téléchargement.

## Garde-fous

- Chaque chiffre de slide a une SOURCE (outil MCP ou KB) mentionnée dans la
  restitution — aucun chiffre inventé (CONFORMITE.md).
- Données agrégées uniquement : pas de données personnelles clients ni de
  salaires individuels dans les slides (les sujets RH se formulent en charge
  d'équipe, pas en personnes).
- Le CODIR reste en lecture seule : la présentation restitue et propose, elle
  ne déclenche aucune écriture dans les serveurs.
