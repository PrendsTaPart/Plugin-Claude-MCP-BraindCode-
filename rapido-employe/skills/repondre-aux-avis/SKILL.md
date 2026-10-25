---
name: repondre-aux-avis
description: Utiliser quand les avis clients attendent une réponse, que l'utilisateur dit « réponds aux nouveaux avis », « il y a un avis négatif ce matin », « traite les avis de la semaine ». Lit les avis FoodEatUp, prépare chaque réponse en brouillon, et ne publie qu'après accord.
---

# Répondre aux avis (le brouillon, l'accord, la publication)

Familles engagées : **service-client** (Brouillon) — la PUBLICATION de la
réponse (`reply_review`) se montre et attend l'accord (garde-envois).

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow

1. **`list_reviews`** (FoodEatUp) — les nouveaux avis, du plus ancien au
   plus récent ; relever la note et le délai sans réponse.
2. **Préparer chaque réponse** : factuelle, calme, personnelle (le fait cité
   par le client, jamais un gabarit copié trois fois) ; un avis négatif
   reprend le problème, propose le geste réel (contact direct), ne promet
   rien que la maison ne tient pas.
3. **`reply_review`** — l'appel SE MONTRE (texte complet) et attend
   l'accord ; la publication est publique, donc famille service-client avec
   ask systématique du garde-envois. Quota `reponsesJour` compté.
4. **Mesurer** : note moyenne et délai de réponse (l'outil de statistiques
   d'avis côté RapidoCRM quand la source KPI le désigne — get_avis_client_stats
   vu en session mais absent de la liste live versionnée : vérifier avant
   usage) → `record_kpi`.
5. Un avis qui révèle un problème produit remonte au responsable et à la
   routine « demandes entrantes ».

KPI : `avis-note`, `avis-delai`.
Formations : `relation-client` (6 missions), `customer-success`.

## Garde-fous

- Jamais de réponse publiée sans accord humain — un avis est une vitrine.
- Pas de récompense promise contre modification d'avis, pas de débat
  public : au-delà d'un échange, on passe en privé.
- Les trois réponses types interdites : copie-collée, défensive, inventant
  un fait.
