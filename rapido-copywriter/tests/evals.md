# Évals — plugin rapido-copywriter (0.2.0)

## Déclenchement (phrases → skill)

| Phrase | Skill |
|---|---|
| « Post LinkedIn pour la page » / « carrousel LinkedIn » / « copy LinkedIn de [marque] » | `copy-linkedin` |
| « Post Facebook/Instagram » / « caption » / « carrousel Insta » / « copy du Reel » | `copy-meta` |
| « Script TikTok » / « vidéo TikTok pour [marque] » / « hook TikTok » | `copy-tiktok` |
| « Décline sur les 4 réseaux » / « adapte ce post pour » / « repurpose ce contenu » | `declinaison-multi-reseaux` |

## Cas `copy-linkedin` + `copy-meta` (4)

1. **Chaîne** : brief (funnel, cible, preuve réelle) → **3 variantes** (grammaire du
   réseau, hooks différents) → **passe anti-voix-IA** → **gate brand-review** →
   `create_draft_tool` (brouillon, bon compte) + hooks consignés au compteur.
2. **Renvoi profil perso** : « post LinkedIn sur MON profil » → renvoyer à
   `rapido-marketing:social-selling-linkedin` (pas ce skill = pages marque).
3. **Blocage anti-voix-IA** : une variante avec ≥ 2 tics FR (« Dans un monde où… »,
   « N'hésitez pas à… ») → **réécriture obligatoire** avant `brand-review`.
4. **Grammaires distinctes** : FB (40-120 mots, local) ≠ IG (hook < 125 car., 3-8
   hashtags) ; carrousel/Reel → structure + visuel/monteur délégués. Brouillon par compte.

## Cas `copy-tiktok` + `declinaison-multi-reseaux` (4)

5. **Script TikTok** : livrable = **script de tournage** (hook < 3 s, boucle→valeur→
   payoff→CTA, texte à l'écran horodaté, sous-titres) — **pas** une caption ; anti-voix-IA
   sur le parlé ; sortie double (génératif / tournage réel).
6. **Déclinaison complète** : une idée-noyau → 4 déclinaisons **natives** (délégation aux
   copy-*), lot de brouillons CMS même campagne + calendrier proposé — jamais un
   copier-coller raccourci.
7. **Anti-collision montage** : « monte cette vidéo » → `rapido-video:montage-express`
   (pas copy-tiktok, qui écrit le script).
8. **Publication** : aucun réseau publié directement — brouillon CMS (ou export du script
   si pas de compte TikTok connecté).

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
