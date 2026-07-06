---
name: orchestration-campagne
description: Utiliser quand l'utilisateur parle de campagne de contenu, de série de posts ou d'insights de campagne sur les réseaux sociaux. Regroupe des posts dans une campagne et en analyse les résultats.
---

# Orchestration de campagne de contenu

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et appliquer ses
règles pendant toute l'exécution (IDs, confirmations, données, formats, erreurs).

## Workflow

1. **Créer la campagne** — `create_campagne` (`name`, `description` requis ;
   réseaux ciblés via les drapeaux `facebook`, `instagram`, `linkedin`, `tiktok`
   à 1 ou 0). N'activer que les réseaux où un compte est réellement connecté
   (vérifier avec `list_connected_accounts`).
2. **Rattacher les posts** — pour chaque post de la série :
   `add_post_campagne` (`campagne_id`, `post_id`). Les posts sont créés au
   préalable via le skill pipeline-contenu-social (`create_draft_tool` puis
   `schedule_draft_tool`) ; retrouver leurs IDs avec `list_scheduled_posts` ou
   `list_posts_campagne` pour vérifier le contenu de la campagne.
3. **Analyser** — `ingishts_campagne` (`campagne_id`) — attention, le nom de
   l'outil s'écrit bien « ingishts » sur ce serveur. Restituer une synthèse :
   portée, engagement, meilleurs posts, recommandations pour la suite.

## Garde-fous

- Une série de posts cohérente : même campagne, ton adapté par réseau, calendrier
  étalé (pas tout le même jour) — proposer un planning avant de planifier.
- Retirer un post d'une campagne (`remove_post_campagne`) ou supprimer une
  campagne (`delete_campagne`) : confirmation explicite obligatoire.
- Consulter les campagnes existantes avec `list_campagnes` avant d'en créer une
  nouvelle (éviter les doublons).
