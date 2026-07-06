---
name: contenu-conforme-marque
description: Utiliser quand l'utilisateur demande de respecter la charte, le ton de la marque ou les couleurs de la marque — et en amont de toute génération de contenu ou de template. Charge l'identité de marque et l'impose partout.
---

# Contenu conforme à la marque

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (règles communes)
et `${CLAUDE_PLUGIN_ROOT}/reference/charte-graphique.md` — la charte complète les
valeurs live de l'API (marges de protection, usages interdits, do/don't) et sert
de repli si `get_brand` ne renvoie pas une valeur.

## Workflow

1. **Charger l'identité** (aucun paramètre requis) :
   - `get_brand` → couleurs, logo, éléments visuels de la marque ;
   - `get_company` → informations société (nom, activité, coordonnées) ;
   - `get_profile` → profil utilisateur.
2. **Imposer ces éléments dans TOUT contenu produit ensuite** :
   - visuels `generate_image` : intégrer les couleurs de la marque dans le
     `prompt` ; ne pas laisser le générateur choisir une palette arbitraire ;
   - captions et textes de posts (`create_draft_tool`) : respecter le ton de la
     marque (le déduire de `get_brand`/`get_company` ; si le ton n'y figure pas,
     le demander une fois et le réutiliser) ;
   - pages de cartes digitales (`edit_card_page`) : `background` et styles CSS
     inline aux couleurs exactes de la marque, logo via `image_url` ;
   - templates de posts (`create_post_template`) : mêmes contraintes.
3. **Vérifier avant livraison** : couleurs exactes (codes hex de `get_brand`, pas
   d'approximation), logo présent quand pertinent, ton homogène.

## Garde-fous

- Appeler `get_brand` UNE fois par session et réutiliser le résultat — pas besoin
  de le rappeler à chaque contenu.
- Si un élément de marque manque (pas de logo, pas de couleurs définies), le
  signaler à l'utilisateur et lui demander l'élément plutôt que d'inventer.
- Ne jamais écraser la charte : si l'utilisateur demande explicitement de s'en
  écarter, le faire mais le mentionner dans le récapitulatif.
