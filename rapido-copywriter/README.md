# rapido-copywriter — le copywriter 4 réseaux

Il **connaît chaque réseau** (LinkedIn, Facebook, Instagram, TikTok) : grammaires natives
datées, banque de hooks **vivante** (taguée par les vrais insights CMS), passe
**anti-voix-IA** francisée, et une **boucle d'apprentissage** sur les hooks. Produit des
**brouillons CMS** par réseau — **jamais de publication directe**. Orchestre l'existant
(funnel, pipeline, brand-review) sans le dupliquer.

## État : squelette (0.1.0)

Fondations : `reference/grammaires-reseaux.md` (4 fiches datées), `banque-hooks.md`
(patterns par réseau, tag GAGNANT/NEUTRE), `anti-voix-ia.md` (tics FR + passe finale),
`articulations.md` (frontières), hook `garde-voix-marque`. Skills à venir : `copy-linkedin`,
`copy-meta`, `copy-tiktok`, `declinaison-multi-reseaux` (CW2-3) + agent `copywriter-social`
et boucle `score_hooks.py` (CW4). Audit fondateur : `docs/IMPORTS-COPYWRITER.md`.

## Frontières (à respecter)

- **Profil perso** du fondateur → `rapido-marketing:social-selling-linkedin`. **Pages
  marque** → ce plugin.
- **Blog/email/landing** → `rapidocms:content-creation-methodo` (recentré). **Social** →
  ce plugin.
- Frameworks funnel/message → `rapidocms:funnel-tofu-mofu-bofu`, made-to-stick…
  (référencés, pas copiés).

## Garde-fous

- **Gate voix de marque** (`rapidocms:brand-review`) + **passe anti-voix-IA** avant tout lot ;
  hook `garde-voix-marque` (confirmation à la création de brouillon).
- **Brouillons CMS uniquement, jamais de publication directe.**
- **Anti-clickbait** (promesse du hook tenue) ; preuves/chiffres **réels** (CRM/CMS) ;
  hooks **re-dérivés** (jamais copiés d'un créateur) ; pas de faux engagement.

## Boucle d'apprentissage

Après publication, `rapidocms:analyse-performance-contenu` + `post_insights`
(liked/shares/comments/views par réseau) → `scripts/score_hooks.py` tague les hooks
GAGNANT/NEUTRE → le copywriter pioche les gagnants d'abord. Grammaires **révisées
trimestriellement** via `rapido-seo:tendances-marche`.

## Attribution & portabilité

Frameworks francisés de dépôts **MIT** (aucun corps copié ; sans-licence exclus) :
`NOTICE.md`. Aucune donnée client dans le dépôt. Slug **immuable**.
