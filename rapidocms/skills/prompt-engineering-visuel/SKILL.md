---
name: prompt-engineering-visuel
description: Utiliser quand l'utilisateur veut générer une image, créer un visuel ou améliorer un prompt image. Méthode de construction de prompts pour generate_image, avec variantes, critique vs charte et itération. Pour un visuel avec du texte incrusté ou la correction d'une faute dans un rendu, utiliser prompts-visuels-pro.
---

# Prompt engineering visuel

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (règles communes)
et `${CLAUDE_PLUGIN_ROOT}/reference/charte-graphique.md` — la palette du prompt
vient de la charte (valeurs live `get_brand` prioritaires). Consulter aussi la
bibliothèque de prompts gagnants (skill `bibliotheque-prompts`) : un prompt
proche déjà validé sert de base et économise les itérations.

## Structure de prompt — les 6 blocs, dans l'ordre

Construire chaque prompt `generate_image` avec :

1. **[Sujet précis]** — quoi exactement, pas « une belle image » : objet, scène,
   personnage, contexte métier.
2. **[Style]** — photo réaliste / illustration / flat design / 3D / aquarelle… ;
   un seul style par prompt.
3. **[Composition et cadrage]** — gros plan / plan large, angle, règle des
   tiers, espace négatif pour du texte éventuel (ajouté APRÈS, pas dans
   l'image).
4. **[Palette]** — les couleurs de la CHARTE, nommées explicitement (« tons
   #hex primaire, accents #hex accent ») — jamais une palette laissée au
   hasard. Source par ordre de priorité : `./rapido-kb/charte-graphique.md`
   (version complétée par le client) si elle existe, puis `get_brand` en
   vérification (signaler tout écart), puis la charte générique du plugin en
   dernier repli — citer la source retenue.
5. **[Ambiance lumière]** — lumière naturelle / studio / golden hour /
   contrasté doux…
6. **[Négatif — ce qu'il ne faut PAS]** — toujours exclure : texte incrusté
   dans l'image, logos (déformés ou non — le logo s'ajoute en post-prod),
   mains/doigts malformés, filigranes.
   Pour les prompts négatifs détaillés par type de visuel et le protocole
   zéro faute sur le texte incrusté, utiliser le skill `prompts-visuels-pro`.

`size` : `hd` pour publication, `standard` pour itérer vite.

## Workflow

1. **Brief** : sujet, réseau/format de destination, objectif du visuel.
2. **Consulter la bibliothèque AVANT de créer** — `list_prompts`
   (`type: "visuel"`, `search` par mot-clé du sujet) : si un prompt gagnant
   existe, le réutiliser en remplaçant ses placeholders `[entre crochets]`
   par les valeurs du brief — ne réinventer que s'il n'y a rien d'adapté.
3. **Proposer 2-3 VARIANTES de prompt** (angles ou styles différents), les
   soumettre à l'utilisateur avant génération.
3. **Générer** — `generate_image` (`prompt`, `size`).
4. **Critiquer le résultat VS la charte** — checklist du
   `directeur-artistique` : contraste, lisibilité, hiérarchie, couleurs exactes,
   point focal. Verdict honnête : conforme / à itérer (et pourquoi).
5. **Itérer** : ajuster le bloc fautif du prompt (pas tout réécrire), 2-3
   itérations max avant de changer d'approche.
6. **Uploader le visuel retenu** — `upload_file_tool` (`type: "image"`, `name`
   descriptif, `file_url`) pour la bibliothèque, prêt pour `create_draft_tool`.
7. **Capitaliser — bibliothèque de prompts vivante** : quand un prompt a donné
   un visuel VALIDÉ par l'utilisateur, le sauvegarder avec `add_prompt`
   (`title` descriptif ex. « Visuel plat signature — photo chaude »,
   `content` = le prompt gagnant en GÉNÉRALISANT les valeurs spécifiques en
   placeholders `[entre crochets]` — ex. `[nom du plat]`, `[couleur primaire]` —,
   `type: "visuel"`). Vérifier d'abord via `list_prompts` qu'un prompt
   équivalent n'existe pas déjà (sinon proposer `edit_prompt` pour l'améliorer).
   PROPOSER la sauvegarde à l'utilisateur, jamais l'imposer — titre normalisé
   « type — sujet — style » et gestion complète : skill `bibliotheque-prompts`.

## Garde-fous

- Jamais de génération sans palette de charte dans le prompt.
- Le visuel final est montré/décrit à l'utilisateur pour validation avant tout
  usage dans un post.
- Pas de texte dans l'image générée (typographie non fiable) : le texte vit
  dans la caption ou est ajouté par un outil dédié.
