---
name: gestion-marques
description: Utiliser quand l'utilisateur veut créer une marque, modifier l'identité d'une marque (couleurs, logo, slogan, typo), gérer plusieurs marques ou supprimer une marque dans RapidoCMS. Le CRUD complet de la marque — les assets (logos) et la conformité restent dans contenu-conforme-marque.
---

# Gestion des marques (multi-marques)

Le CRUD des MARQUES elles-mêmes (schémas vérifiés serveur le 2026-07-10).
La marque est la racine de toute production : couleurs, typo, logo, slogan —
toute écriture ici impacte TOUTES les générations suivantes.

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`. Si
`./rapido-kb/charte-graphique.md` existe, c'est la source des valeurs
(couleurs hex, typo, slogan) — la citer.

## Workflow

1. **Lire d'abord** — `get_brand` (sans paramètre : la marque par défaut ;
   `nom` pour cibler une marque précise en multi-marques). Toujours vérifier
   ce qui existe AVANT de créer : deux marques du même nom = confusion dans
   toutes les productions.
2. **Créer** — `create_brand` (requis : `nom`, `langue`, `slogan` ;
   fortement recommandés : `couleurs` = hex séparés par des VIRGULES ex.
   `#0F172A,#F59E0B`, `font_family` = une pile de l'ENUM web-safe (Arial,
   Verdana, Tahoma, Trebuchet MS, Georgia, Times New Roman, Garamond,
   Courier New, Lucida Console — telle quelle, avec son repli), `logo` = URL
   PUBLIQUE, `site_web` http(s)). Valeurs depuis la KB ou l'utilisateur —
   jamais inventées. Confirmation avant l'appel (récapitulatif complet).
3. **Modifier** — `edit_brand` (`brand_id` requis — celui de `get_brand` ;
   ne passer QUE les champs qui changent). Confirmation avec avant/après :
   un changement de couleurs ou de logo se propage à toutes les productions
   suivantes.
4. **Supprimer** — `delete_brand` (`brand_id`) : action IRRÉVERSIBLE sous
   hook garde-destructif — confirmation explicite, rappeler que les
   contenus existants perdent leur référentiel de marque. Jamais proposé
   spontanément.

## Frontières (renvois)

- **Assets (logos officiels)** : `add_asset`/`remove_asset` et le pipeline
  vidéo (kit « Mika ») → skill `contenu-conforme-marque`.
- **Application de la charte** aux contenus/visuels → `contenu-conforme-marque`
  et `prompt-engineering-visuel`.
- La marque par défaut du compte suffit à un mono-marque : ce skill sert
  surtout le MULTI-MARQUES (agences, groupes, marques blanches).

## Garde-fous

- Jamais d'écriture de marque sans confirmation — c'est le référentiel de
  TOUTES les productions.
- `couleurs` : toujours des hex valides séparés par des virgules ; refuser
  les noms de couleurs (« bleu ») — demander le code exact ou le lire dans
  la KB.
- `font_family` : uniquement une valeur de l'enum web-safe du serveur — une
  police custom se gère côté assets/production, pas ici.
- `logo` : URL publique uniquement (comme `upload_file_tool`) ; le logo
  lui-même vit dans les assets de marque.
- Récapituler chaque écriture avec le `brand_id` et les champs modifiés.
