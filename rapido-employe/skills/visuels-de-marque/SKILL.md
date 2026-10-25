---
name: visuels-de-marque
description: Utiliser quand un support visuel se prépare, que l'utilisateur dit « fais le visuel du webinaire », « il me faut un flyer pour le salon », « récupère la charte et les logos ». Relit la charte et les assets, référence les sources Figma, et ne passe par Studio Print qu'après coût estimé et dépense acceptée.
---

# Visuels de marque (la charte d'abord, le crédit ensuite)

Familles engagées : **configurer** (assets Academy) + **preparer**
(créations Studio Print — PAYANTES : garde-depense).

## Étape 0 — Références (obligatoire)

1. Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.
2. Budget relu dans le cadre — il est à 0 € tant que le responsable ne l'a
   pas changé : toute création payante sera refusée, le dire d'emblée.

## Workflow

1. **`get_brand_guidelines`** — couleurs, logos EN FICHIER (jamais
   redessinés), formats. C'est la charte qui prime, toujours.
2. **`list_brand_assets`** — l'existant se réutilise avant de créer ;
   `get_figma_sources` pour les maquettes sources.
3. **Un asset manquant non payant** (texte, gabarit, déclinaison simple) :
   le préparer et le ranger avec **`add_brand_asset`** (aperçu → confirm).
4. **Une création Studio Print** (pack, QR, vidéo promo, newsletter — au
   crédit) : d'abord **`estimer_cout`**, puis **`record_expense`** (aperçu,
   accord) — ACCEPTÉE seulement, lancer `creer_pack` / `creer_qr` /
   `creer_video_promo` / `creer_newsletter`. Un refus arrête la dépense
   (hook garde-depense en filet). Studio Print absent : volet sauté en le
   disant.
5. Les visuels produits rejoignent les skills qui les servent
   (`communication-de-la-semaine`, `webinaire-du-mois`, `pitch`).

KPI : `posts-publies` (les supports servent la semaine de com).
Formations : `studio-print` (4 missions), `visuels`, `calendrier`.

## Garde-fous

- Jamais un logo redessiné ni une couleur « proche » : la charte est un
  fichier, pas un souvenir.
- Le coût s'affiche AVANT de lancer (règle Studio Print), la dépense
  s'inscrit AVANT d'être engagée, et le budget vient du cadre — trois
  verrous, aucun ne saute.
