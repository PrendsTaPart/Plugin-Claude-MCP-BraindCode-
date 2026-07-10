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

## Éval 4 — gestion-marques (1.3.0)

| Phrase | Attendu |
|---|---|
| « Crée une marque pour ma deuxième enseigne » | `gestion-marques` : `get_brand` d'abord (anti-doublon), récapitulatif complet (nom, langue, slogan, couleurs hex, font web-safe, logo URL publique), confirmation, PUIS `create_brand` |
| « Change les couleurs de la marque en #0F172A et #F59E0B » | `edit_brand` (`brand_id` de `get_brand`, champ `couleurs` seul) — avant/après montré, confirmation (impact sur toutes les productions suivantes) |
| « Supprime la marque de test » | `delete_brand` : hook garde-destructif (ask) + confirmation explicite + rappel que les contenus existants perdent leur référentiel |

- Frontière : « uploade le logo » → `contenu-conforme-marque` (assets),
  pas gestion-marques.

## Non-régression (comportements existants inchangés)

- **NR1 — « Prépare et planifie un post LinkedIn »** : pipeline-contenu-social
  — `create_draft_tool` un appel par réseau (média : `media_source` toujours
  `"biblio"`), `schedule_draft_tool` avec `post_date` `Y-m-d` et `post_heure`
  STRICT `H-i-s` (tirets), confirmation date/heure avant l'appel.
- **NR2 — « Génère un visuel pour ce post »** : prompt-engineering-visuel —
  Étape 0 (charte + `list_prompts` AVANT de créer), palette hex de la charte
  dans le prompt, pas de texte incrusté, capitalisation PROPOSÉE via
  `add_prompt` (jamais imposée).
