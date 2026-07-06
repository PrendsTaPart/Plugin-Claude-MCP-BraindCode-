# Charte graphique (rapido-suite)

Ce plugin embarque le serveur CMS : pour tout contenu visible créé pendant une
orchestration (posts, cartes digitales, campagnes de l'onboarding client),
privilégier les valeurs LIVE via `get_brand` + `get_company` + `get_profile`.
Si une base de connaissance `./rapido-kb/charte-graphique.md` existe dans le
répertoire de travail (version COMPLÉTÉE par l'onboarding entreprise), elle
prime sur ce fichier générique. Ordre : API live > KB > ce fichier.
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

## Logos

### À COMPLÉTER
- Logo principal (couleur) : URL ______
- Variante monochrome : URL ______
- Variante fond clair : URL ______
- Variante fond foncé : URL ______

Règles d'usage :
- Marge de protection : ### À COMPLÉTER.
- Choisir la variante selon le fond ; URL publique obligatoire.
- Usages INTERDITS : déformer, recolorer, pivoter, appliquer des effets.
  ### À COMPLÉTER (interdits spécifiques).

## Ton de voix

### À COMPLÉTER — décrire le ton.

### Do
- ### À COMPLÉTER

### Don't
- ### À COMPLÉTER

## Application

Toute création de contenu pendant une orchestration (visuels `generate_image`,
captions `create_draft_tool`, pages de cartes `edit_card_page`, templates)
applique cette charte — mêmes règles que les plugins rapidocms et rapidocrm.
