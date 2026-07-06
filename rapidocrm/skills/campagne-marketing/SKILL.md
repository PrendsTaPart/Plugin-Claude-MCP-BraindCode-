---
name: campagne-marketing
description: Utiliser quand l'utilisateur parle de campagne, de segment, d'envoi de masse ou de newsletter marketing. Construit le segment cible, crée la campagne, la lance et suit ses résultats.
---

# Campagne marketing

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (règles communes)
et `${CLAUDE_PLUGIN_ROOT}/reference/charte-graphique.md` — ce skill produit du
contenu visible (templates, contenus de campagne).

## Workflow

1. **Créer le segment cible** — `create_segment` (`nom` requis ; filtres
   `domaine_contient`, `ville_contient` ; `description` ; `recalculer: true` pour
   calculer immédiatement).
2. **Recalculer et vérifier la taille** — `recalculer_segment` (`segment_id` ou
   `segment_nom`) : annoncer le nombre de contacts/entreprises trouvés à
   l'utilisateur. Si le segment est vide, ajuster les filtres avant de continuer.
3. **Créer la campagne** — `create_campagne` (`nom`, `canal` ∈ email | sms |
   newsletter | multicanal | evenement, `segment_id`, `objectif`, `date_debut`,
   `date_fin`, `budget` ; `statut` initial : `brouillon` ou `planifiee`).
4. **Attacher un template** — choisir selon le canal via `list_templates_email` ou
   `list_templates_sms` (détail avec `get_template`). Si aucun template ne convient,
   en créer un avec `create_template_email` / `create_template_sms` après validation
   du contenu par l'utilisateur.
5. **Lancer** — `lancer_campagne` (`id` de la campagne) : passe le statut à
   `en_cours`. Demander une confirmation explicite AVANT le lancement (envoi de
   masse irréversible), en rappelant la taille du segment.
6. **Suivre les résultats** — `get_stats_campagne` (`id`, `periode` ∈ today | week |
   month | quarter | year) ; compléter avec `get_conversion_par_canal` si
   l'utilisateur compare les canaux.

## Garde-fous

- Cycle de statuts : `brouillon → planifiee → en_cours → terminee → archivee` ;
  ne pas lancer une campagne déjà `en_cours` ou `terminee`.
- Jamais de lancement sans : segment recalculé non vide + template/contenu validé +
  confirmation explicite de l'utilisateur.
- Ajouter des posts à une campagne existante : `add_post_campagne` est côté
  RapidoCMS — hors périmètre de ce skill (le signaler si demandé).
