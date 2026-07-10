# Évals — plugin rapidocms

## Éval 1 — bibliotheque-prompts (déclenchement)

| Phrase | Attendu |
|---|---|
| « Sauvegarde ce prompt, il a super bien marché » | `bibliotheque-prompts` (add_prompt proposé) |
| « Réutilise le prompt gagnant du plat signature » | `bibliotheque-prompts` (list_prompts → base) |
| « Nettoie ma bibliothèque de prompts » | `bibliotheque-prompts` (edit/delete sur confirmation) |
| « Génère un visuel du burger » | prompt-engineering-visuel / prompts-visuels-pro, qui CONSULTENT la bibliothèque en Étape 0 |

## Éval 2 — bibliotheque-prompts (comportement)

- ATTENDU : list_prompts (type + search) AVANT toute génération d'image —
  prompt proche → proposé comme base avec placeholders remplacés.
- ATTENDU : sauvegarde PROPOSÉE (jamais imposée) après validation du
  visuel ; titre « type — sujet — style » ; content = positif + négatifs ;
  placeholders [entre crochets] ; anti-doublon via list_prompts.
- ATTENDU : type ∈ text | visuel UNIQUEMENT (piège serveur) — un prompt
  vidéo part en type visuel, titre préfixé « vidéo — ».
- ATTENDU : delete_prompt sur confirmation explicite (hook garde-destructif).

## Éval 3 — assets de marque (contenu-conforme-marque)

- « Ajoute ce logo comme logo officiel » → upload_file_tool (type image,
  fond transparent recommandé) → add_asset (brand_id de get_brand) →
  récapitulatif des IDs.
- « Retire l'ancien logo » → remove_asset APRÈS confirmation (matcher hook
  étendu — testé stdin : remove_asset → ask).
- ATTENDU : toute génération référence le logo des assets de marque — jamais
  d'URL improvisée, jamais de logo généré par IA.
- Pipeline vidéo (kit « Mika ») : les logos viennent des assets CMS, plus du
  repo GitHub — une mise à jour de logo = add_asset, le kit suit.
