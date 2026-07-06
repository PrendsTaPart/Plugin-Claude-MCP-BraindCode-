# Charte graphique (rapidocms)

PRIORITÉ DES SOURCES : sur ce plugin, toujours privilégier les valeurs LIVE via
`get_brand` + `get_company` + `get_profile` (couleurs, logo, infos société).
Ce fichier sert de REPLI si l'API ne renvoie pas une valeur, et de référence pour
les règles NON exposées par l'API (marges de protection, usages interdits, ton).
En cas de conflit : la valeur API gagne, sauf mention contraire de l'utilisateur.

## Couleurs (codes hex)

### À COMPLÉTER
- Primaire : `#______`
- Secondaire : `#______`
- Accent : `#______`
- Neutres : fond clair `#______`, fond foncé `#______`, texte `#______`,
  texte secondaire `#______`

Règle : utiliser les codes EXACTS — jamais d'approximation ni de couleur proche.

## Typographies

### À COMPLÉTER
- Titres : ______ (graisse : ______)
- Corps : ______ (graisse : ______)
- Tailles minimales : titres ______ px, corps ______ px

## Logos

### À COMPLÉTER
- Logo principal (couleur) : URL ______
- Variante monochrome : URL ______
- Variante fond clair : URL ______
- Variante fond foncé : URL ______

Règles d'usage :
- Marge de protection : ### À COMPLÉTER (ex. hauteur du logo × 0,5 sur chaque côté).
- Choisir la variante selon le fond : monochrome/fond foncé sur images sombres,
  couleur/fond clair sur fonds clairs.
- Usages INTERDITS : déformer, recolorer, pivoter, appliquer une ombre ou un
  contour, placer sur un fond à faible contraste. ### À COMPLÉTER (interdits
  spécifiques).

## Ton de voix

### À COMPLÉTER — décrire le ton en une phrase (ex. « expert mais accessible,
tutoiement, énergique sans superlatifs »).

### Do
- ### À COMPLÉTER (ex. phrases courtes, un appel à l'action par post, emojis sobres)

### Don't
- ### À COMPLÉTER (ex. jargon technique, promesses chiffrées non vérifiées,
  majuscules criardes)

## Application par outil

- `generate_image` : intégrer les couleurs primaire/secondaire dans le `prompt` ;
  ne jamais laisser la palette au hasard.
- `create_draft_tool` (captions) : appliquer le ton de voix et les do/don't.
- `edit_card_page` : `background` et styles CSS inline aux codes hex exacts ;
  logo via `image_url` (variante adaptée au fond).
- `create_post_template` : mêmes contraintes que les posts.
