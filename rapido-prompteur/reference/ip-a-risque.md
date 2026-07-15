# Liste maison — IP / marques / artistes à risque (scan anti-IP)

> **Rôle** : source du garde `hooks/scripts/anti-ip.py`. Toute puce `- terme`
> de ce fichier est cherchée (frontière de mot, insensible à la casse) dans les
> prompts sortants vers un moteur de génération. Une correspondance → **demande
> de confirmation** avec avertissement (le garde ne bloque pas, il alerte).
>
> **Éditer ici, pas dans le code.** Le texte après `—` ou `(` est ignoré par le
> parseur (commentaire libre). Ajouter les IP/marques/artistes propres au
> secteur du client si besoin. Ne PAS mettre de mots trop génériques (risque de
> faux positif) — préférer les noms distinctifs.
>
> Cette liste n'est **pas** une base de données juridique exhaustive : c'est un
> filet de sécurité pédagogique. Le vrai garde-fou est la règle de construction
> (`reference/regles-de-construction.md`, section INTERDITS).

## Franchises & œuvres sous licence
- Star Wars
- Harry Potter
- Marvel
- Spider-Man
- Batman
- Superman
- Pokémon
- Mario — Nintendo
- Zelda
- Mickey Mouse
- Barbie
- Lego
- Studio Ghibli
- Ghibli
- Peppa Pig
- Minecraft
- Fortnite

## Marques (mode, produits, tech)
- Nike
- Adidas
- Coca-Cola
- Louis Vuitton
- Gucci
- Chanel
- Prada
- Rolex
- Ferrari
- Lamborghini
- iPhone
- Apple — (marque ; attention aux faux positifs « apple » fruit, laissé volontairement pour confirmation manuelle)
- Playstation
- Xbox
- Netflix
- Disney
- Pixar

## Artistes vivants / réalisateurs (style protégé de fait)
- Wes Anderson
- Christopher Nolan
- Quentin Tarantino
- Wong Kar-wai
- Park Chan-wook
- David Lynch
- Denis Villeneuve
- Hayao Miyazaki
- Greta Gerwig
- Banksy
- Yayoi Kusama
- Takashi Murakami
- Beeple
