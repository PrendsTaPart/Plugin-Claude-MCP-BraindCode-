---
name: maquettes-figma
description: Utiliser quand l'utilisateur veut les maquettes d'une extension Build — « écris les prompts Figma », « maquette les écrans avec la charte », « prépare le fichier Figma ». Charte par get_brand_guidelines, prompts kind figma, Figma en serveur de session, adresses gardées pour la vitrine.
---

# Maquettes Figma

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/regles-lovable.md` (section charte) ;
- Figma est un serveur MCP de SESSION (non déclaré dans le .mcp.json —
  précédent rapido-design) : s'il n'est pas branché, produire les prompts
  et le dire.

## Démarche
1. **La charte** : `get_brand_guidelines` — avec `product` pour un produit
   (foodeatup : palette hexadécimale, typographie, règles du logo, motif),
   sans produit pour la charte BraindCode. Et l'identité du PROJET :
   image officielle, accroche, punchline (`get_project_context`).
2. **Les prompts** : `get_project_prompts` avec kind figma — le brief
   officiel de l'idée ; le compléter avec les écrans du cahier des
   charges.
3. **Dans Figma (session)** : création du fichier, écrans, états
   (vide/chargement/erreur), composants réutilisables, variables de la
   charte ; contrôle par capture à chaque écran.
4. **Garder les adresses** : les URL Figma vont dans
   `save_project_progress` et serviront à la vitrine (figma_urls).
5. **Critique UX** : déléguée au plugin rapido-design (skill
   `studio-maquette`) s'il est installé — pas de double critique maison.

## Pièges
- La charte se LIT (get_brand_guidelines), elle ne se devine pas depuis
  une capture — et celle du produit prime sur les goûts.
- Des maquettes sans états d'erreur donnent des prompts Lovable
  incomplets : les trois états par écran.

## Dégradation propre
Figma absent de la session : livrer les prompts Figma complets, prêts à
coller, et le dire — ne pas simuler des URL de fichier.
