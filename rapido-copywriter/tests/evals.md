# Évals — plugin rapido-copywriter (0.1.0, squelette)

Stade squelette : grammaires + banque de hooks + anti-voix-IA + garde-fous. Les évals de
déclenchement des skills arrivent avec eux (CW2→CW5).

## Garde-fous (hook `garde-voix-marque`, testé au testeur)

| Entrée | Décision attendue |
|---|---|
| `mcp__rapidocms__create_draft_tool` | **ask** (anti-voix-IA + brand-review passés ?) |
| `mcp__rapidocms__list_scheduled_posts` (lecture) | **allow** |
| `mcp__rapidocms__get_brand` | **allow** |

## Principes vérifiés

- **Brouillons uniquement** : aucune publication directe (pas d'outil de publication câblé).
- **Grammaires datées** + révision trimestrielle (`rapido-seo:tendances-marche`).
- **Hooks re-dérivés** (templates à placeholders), jamais copiés d'un créateur ; tags
  GAGNANT/NEUTRE mis à jour **par script** sur les vrais insights (liked/shares/comments/
  views), jamais à la main.
- **Anti-voix-IA** : tics FR ; ≥ 2 items → réécriture avant `brand-review`.
- **Frontière** : profil perso → `social-selling-linkedin` ; pages marque → ce plugin.

## Anti-déclenchements (à respecter dans les skills)

- « Post sur MON profil » → `rapido-marketing:social-selling-linkedin` (perso).
- « Article de blog » → `rapidocms:generation-article-blog`.
- « Campagne email » → `rapidocrm:campagne-marketing` / marketing.
