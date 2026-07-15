---
name: prompts-visuels-pro
description: Utiliser quand l'utilisateur veut un prompt de génération d'image professionnel, un prompt négatif, un visuel contenant du texte sans aucune faute, ou corriger une faute de texte dans un visuel déjà généré. Bibliothèque de négatifs par type de visuel, protocole zéro faute, charte et logo chargés depuis RapidoCMS.
---

# Prompts visuels pro — positif + négatif + zéro faute

Complète `prompt-engineering-visuel` (structure 6 blocs, workflow, capitalisation) :
ce skill ajoute les prompts NÉGATIFS structurés et le protocole texte-dans-l'image.
L'agent `prompt-designer` applique les deux.

## Étape 0 — Marque et bibliothèque (obligatoire, avant tout prompt)

Consulter la bibliothèque de prompts gagnants (skill `bibliotheque-prompts` :
`list_prompts` `type: "visuel"`, `search` par sujet) — un couple
positif/négatif déjà validé sert de base.

Ordre de priorité : `./rapido-kb/charte-graphique.md` → `get_brand` (couleurs
hex, logo, typos) + `get_company` en vérification (signaler tout écart) →
`${CLAUDE_PLUGIN_ROOT}/reference/charte-graphique.md` en repli. Citer la
source. Le logo réel s'ajoute TOUJOURS en post-production, depuis les ASSETS
de la marque (gérés par `gestion-marques` ; `list_all_files` search
`"<Marque> — logo"` → URL publique) : jamais demandé au générateur, jamais
tiré d'un repo GitHub.

## Prompt négatif — base commune

Toujours inclure, quel que soit le sujet :
blurry, low quality, low resolution, pixelated, jpeg artifacts, watermark,
signature, username, logo, brand mark, distorted text, misspelled text,
gibberish text, extra fingers, deformed hands, mutated limbs, duplicated
elements, cropped subject, out of frame, oversaturated, ugly, amateur

## Négatifs additionnels par type de visuel

- **Photo produit / plat** : `plastic look, fake food, unappetizing, messy
  background, harsh shadows, fluorescent lighting, dirty plate, steam overdone`
- **Portrait / équipe** : `asymmetric eyes, bad anatomy, extra teeth, waxy
  skin, dead eyes, uncanny valley, double head`
- **Illustration / flat design** : `photorealistic, 3D render, gradient mess,
  inconsistent style, sketchy lines, clip-art, stock illustration look`
- **Visuel avec texte incrusté** : `misspelled words, broken letters, fake
  alphabet, lorem ipsum, cut-off text, overlapping text, illegible font`
- **Architecture / lieu (restaurant, boutique)** : `warped perspective,
  impossible geometry, floating furniture, empty soulless space`

Le prompt négatif se passe dans le paramètre dédié de `generate_image` s'il
existe ; sinon l'ajouter en fin de prompt sous la forme
`--no <liste>` ou `Avoid: <liste>` selon le moteur.

## Protocole ZÉRO FAUTE (texte dans l'image)

1. **Texte exact entre guillemets** dans le prompt :
   `with the exact text "Menu du Jour" in bold sans-serif` — jamais « un texte
   qui dit à peu près… ».
2. **Validation orthographique AVANT génération** : épeler le texte à
   l'utilisateur (accents compris : Menu — M·e·n·u) et attendre son OK.
   Le texte vient des données réelles (MCP, KB, utilisateur) — jamais inventé.
3. **5 mots maximum incrustés.** Au-delà : générer l'image avec un
   `[espace négatif en haut/bas/gauche]` prévu dans la composition, poser le
   texte en post-production.
4. **Vérification APRÈS génération** : relire le rendu caractère par
   caractère. Une lettre déformée, un accent manquant = REJET.
5. **Correction chirurgicale du texte — protocole v2 (par défaut)** : NE PAS
   tout regénérer. Repasser **le rendu fautif lui-même en référence** via
   `images_to_image(images="<url du rendu fautif>", prompt=…)` avec une
   instruction ciblée sur le **texte seul** : « corrige uniquement le texte en
   `"Menu du Jour"` (orthographe exacte), **ne change RIEN d'autre** :
   composition, couleurs, logo, style identiques ». La charte reste inchangée
   (mêmes hex). C'est la même mécanique que la boucle corrective de
   `studio-visuel-marque`.
   - **Fallback** : si le serveur **refuse le rendu en référence** (erreur, ou
     `images_to_image` indisponible), revenir au protocole v1 — regénérer via
     `generate_image` en itérant sur le **bloc texte uniquement**.
6. **2 itérations max** sur le texte incrusté, puis bascule obligatoire en
   post-production. Ne jamais publier un « presque bon ».

## Livrable type (à produire pour chaque demande)

VARIANTE A — [nom de l'angle]
Prompt : [6 blocs, hex de la charte, texte exact "…" si applicable]
Négatif : [base commune + additionnels du type]
Format : [dimensions selon réseau — voir directeur-artistique]
Source charte : [rapido-kb / get_brand / générique]

2-3 variantes, validation utilisateur, génération, critique vs charte,
upload (`upload_file_tool`), puis PROPOSER la capitalisation (`add_prompt` —
le négatif fait partie du prompt sauvegardé ; titre « type — sujet — style »,
gestion : skill `bibliotheque-prompts`).

## Patterns & variante multi-moteurs

- **Patterns d'usage** : consulter les fiches `assets/patterns/` du plugin
  `rapido-prompteur` pour la structure positive de départ (le négatif et le
  protocole zéro faute restent gérés ici).
- **Variante multi-moteurs** : si la demande implique de **choisir le moteur** ou
  de comparer des **variantes** entre RapidoCMS / Higgsfield / Canva, déléguer à
  l'agent `rapido-prompteur:directeur-prompts` (grammaire lue en direct, 3
  variantes, délégation) — puis revenir ici pour le négatif et le zéro faute.

## Pièges

- Un négatif trop long dilue : 15-25 termes ciblés, pas 60.
- Négatif ≠ poubelle : n'y mettre que ce qui apparaît réellement dans les
  échecs constatés — itérer le négatif comme le positif.
- « no text » dans le négatif ET texte demandé dans le positif = conflit :
  choisir l'un ou l'autre.
- Les couleurs se nomment en hex dans le POSITIF ; le négatif exclut les
  dérives (`oversaturated, neon colors` si la charte est sobre).
