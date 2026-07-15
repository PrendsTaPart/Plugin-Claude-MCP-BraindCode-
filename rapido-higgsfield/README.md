# rapido-higgsfield

L'**usine média IA** de l'écosystème Rapido, branchée sur le MCP **Higgsfield**
(images 4K & packshots, vidéos génératives & pubs, personnages cohérents
Soul/Elements, voix & doublage, sites & jeux) et pontée avec RapidoCMS (marque,
bibliothèque d'assets), RapidoCRM, RapidoRH et FoodEatUp.

> **Version 0.1.0 — squelette.** Routage média, garde-fous et hooks de coûts/voix.
> Les **skills de production** arrivent en H2+, après l'audit live **H0**
> (`docs/AUDIT-MCP-HIGGSFIELD.md` + grille de coûts) qui conditionne leur GO/NO-GO.

## Socle livré (H1)

| Fichier | Rôle |
|---|---|
| `reference/routage-media.md` | arbre de décision unique : Canva / CMS / Higgsfield / HyperFrames / Lovable |
| `reference/pieges-outils.md` | 9 règles des schémas Higgsfield (medias=UUID, Kling+start_image, XOR hook/ad_reference, brand_kit, get_cost…) |
| `reference/garde-fous-media.md` | coûts (plafond KB, get_cost, confirmation), voix (droits), marque (charte), publication (OPT_IN, gate viral) |
| `hooks/` | `garde-couts` (refus si coût non confirmé), `garde-voix` (droits/consentement forcés), Stop récap job_ids/asset_ids |
| `reference/kb-templates/budget-media.md` | plafond mensuel, seuil de confirmation, compteur (copié dans `rapido-kb/`) |

## Skills prévus (H2+ — après H0)
`gouvernance-credits` (H2) · `studio-image-pro` (H3) · `usine-video-marketing` (H4)
· `personnages-univers` (H5, déblocage PronoClip) · `clips-et-shorts` +
`analyse-video-virale` (H6) · `voix-et-doublage` + `videos-explicatives` (H7) ·
`sites-et-jeux-express` (H8). Agent `producteur-studio` (H9).

## Connecteur requis
Le MCP Higgsfield est **requis** (le plugin existe pour lui). Il est déclaré dans
`.mcp.json` sous le namespace **`huggsfield`** via la variable
**`HIGGSFIELD_MCP_URL`** ; l'**URL et le transport exacts sont à figer en H0**
(audit live). Authentification à la charge de l'utilisateur (compte Higgsfield) —
**aucune clé ni secret dans le dépôt** (règle du marketplace).

## Garanties
Tout est **payant en crédits** → `get_cost` préflight + plafond KB + confirmation
au-delà du seuil ; **voix** clonées/doublées uniquement avec droits/consentement ;
**aucune publication directe** (brouillons), créatifs IA vers Meta en
`self_ai_disclosure: OPT_IN`, **gate viral avant tout boost**.
