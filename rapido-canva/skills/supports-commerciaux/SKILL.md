---
name: supports-commerciaux
description: Utiliser quand l'utilisateur veut une proposition commerciale, une présentation de vente ou une carte de visite. Croise les données du deal (RapidoCRM) et les arguments de la KB avec la génération Canva, puis lie le document au CRM.
---

# Supports commerciaux (RapidoCRM × Canva)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`,
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-canva.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/CONFORMITE.md`. KB : `propositions-valeur.md`
(arguments, preuves) + `concurrents.md` (parades) + `charte-graphique.md`.

## Workflow

1. **Données du deal (CRM)** — `get_entreprise` (contexte client),
   `get_devis`/`list_devis` (montants, prestations), `get_historique_prospect`
   (enjeux évoqués). Arguments et preuves depuis la KB (citer la source) —
   jamais de promesse inventée.
2. **Choisir le type de support** :
   - **Proposition commerciale** → `generate-design`
     (`design_type: "proposal"` — visuel ; ou `"doc"` si texte d'abord) ;
   - **Présentation de vente** → FLUX OUTLINE OBLIGATOIRE :
     `request-outline-review` (slides : contexte client → enjeu → solution →
     preuves → offre/prix → prochaines étapes ; descriptions en puces à
     tirets) → validation de l'outline par l'utilisateur →
     `generate-design-structured`. JAMAIS `generate-design` en type
     presentation.
   - **Carte de visite** → `generate-design` (`design_type: "business_card"`,
     coordonnées PROFESSIONNELLES fournies par l'utilisateur).
3. **Charte** — brand kit (`list-brand-kits`) ou palette KB dans la query.
4. **Candidats → design → retouches** — `create-design-from-candidate`, puis
   transaction d'édition si besoin (montants exacts du devis, nom du contact) —
   preview + accord avant commit.
5. **Export** — `get-export-formats` puis `export-design` (PDF pour une
   proposition, PPTX ou PDF pour une présentation) ; afficher l'URL.
6. **Lier au CRM** — envoyer le document au client via `send_email`
   (`entreprise_id`, `sujet`, `contenu` avec le lien du document).
   NIVEAU 2 DE CONFIRMATION : récapituler destinataire + objet + contenu +
   document joint et obtenir l'accord AVANT l'envoi. Tracer avec
   `log_activity`.

## Garde-fous

- Montants STRICTEMENT issus du devis CRM (`get_devis`) — pas de prix de tête.
- CONFORMITE.md : le support cite l'entreprise cliente et son contact pro
  (c'est son objet), mais JAMAIS de données d'autres clients, de prix
  consentis à d'autres, ni de données internes (marges, salaires).
- Qualification avant proposition : si le deal n'est pas qualifié (BANT), le
  signaler — un support soigné ne remplace pas la qualification
  (directeur-commercial).
