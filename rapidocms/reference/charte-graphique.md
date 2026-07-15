# Charte graphique (rapidocms)

> ⚠️ **CHARTE GÉNÉRIQUE DE REPLI** — ces valeurs ne représentent aucune
> marque. Ordre de priorité réel : `./rapido-kb/charte-graphique.md` →
> `get_brand` → ce fichier. Tout agent qui utilise ce repli doit le
> SIGNALER dans sa réponse.

PRIORITÉ DES SOURCES : sur ce plugin, toujours privilégier les valeurs LIVE via
`get_brand` + `get_company` + `get_profile` (couleurs, logo, infos société).
Ce fichier sert de REPLI si l'API ne renvoie pas une valeur, et de référence pour
les règles NON exposées par l'API (marges de protection, usages interdits, ton).
En cas de conflit : la valeur API gagne, sauf mention contraire de l'utilisateur.

## Couleurs (codes hex) — palette neutre professionnelle (repli)

- Primaire : `#1E293B`
- Secondaire : `#64748B`
- Accent : `#3B82F6`
- Neutres : fond clair `#F8FAFC`, fond foncé `#0F172A`, texte `#0F172A`,
  texte secondaire `#64748B`

Règle : utiliser les codes EXACTS — jamais d'approximation ni de couleur proche.

## Typographies (repli : polices système sûres)

- Titres : Inter, repli `system-ui, sans-serif` (graisse : 600)
- Corps : Inter, repli `system-ui, sans-serif` (graisse : 400)
- Tailles minimales : titres 20 px, corps 14 px

## Logos

- **Aucun logo par défaut** — utiliser le logo renvoyé par `get_brand`, ou le
  demander au client. Ne JAMAIS générer ni inventer un logo de substitution.

Règles d'usage :
- Marge de protection : hauteur du logo × 0,5 sur chaque côté (défaut).
- Choisir la variante selon le fond : monochrome/fond foncé sur images sombres,
  couleur/fond clair sur fonds clairs.
- Usages INTERDITS : déformer, recolorer, pivoter, appliquer une ombre ou un
  contour, placer sur un fond à faible contraste.

## Ton de voix (repli)

Professionnel, clair et factuel — vouvoiement, orienté bénéfice client, sans
superlatifs. (Le ton réel du client vient de la KB ou de `get_brand`.)

### Do
- Phrases courtes, un seul appel à l'action par post, vocabulaire concret,
  emojis sobres.

### Don't
- Jargon interne, promesses chiffrées non vérifiées, majuscules criardes.

## Identité vocale (voix de marque)

La marque a des couleurs, un logo… et une **voix**. Symétrie avec `brand_id` :

- **`voice_id`** : [id ElevenLabs de la voix de la marque] (repli : aucune → à créer
  via `rapido-elevenlabs:identite-vocale-marque`).
- **params** : `stability` / `similarity` / `style` figés après tests.
- **modèle** : Multilingual v2/v3 (final) · Flash (brouillon).
- **usages** : voix off, posts audio, narration, agent vocal.
- **source / consentement** : voice design | clonage (consentement écrit archivé, chemin cité).

> Toute narration/voix off d'une marque utilise **SA** voix (cohérence vocale =
> cohérence de marque). Fiche complète : `rapido-elevenlabs/reference/identite-vocale.md`.
> Voix d'un **personnage** (narrateur PronoClip) → `rapido-kb/personnages.json`, à côté
> d'`element_id`/`soul_id`.

## Application par outil

- `generate_image` : intégrer les couleurs primaire/secondaire dans le `prompt` ;
  ne jamais laisser la palette au hasard.
- `create_draft_tool` (captions) : appliquer le ton de voix et les do/don't.
- `edit_card_page` : `background` et styles CSS inline aux codes hex exacts ;
  logo via `image_url` (variante adaptée au fond).
- `create_post_template` : mêmes contraintes que les posts.
