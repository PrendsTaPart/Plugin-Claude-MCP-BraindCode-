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
5. **Gate délivrabilité** — OBLIGATOIRE avant tout envoi de masse
   (`lancer_campagne`, `send_newsletter`, ou tout envoi) :
   - **Si le plugin rapido-marketing est installé** : invoquer OBLIGATOIREMENT le
     skill `delivrabilite-email` en mode **`newsletter`** (scorecard d'hygiène :
     doublons/formats/emails de rôle + contrôle spam de la copy + **présence du
     lien de désinscription** + taille du lot vs plafond). **Lot refusé (note sous
     le seuil) = PAS D'ENVOI**, aucune dérogation ; corriger la liste/le template,
     puis rejouer.
   - **Sinon (mode dégradé, rapidocrm autonome)** : dérouler la **checklist
     minimale intégrée** — (a) `recalculer_segment` pour **dédoublonner** et
     vérifier la taille ; (b) **lien de désinscription présent** dans le template ;
     (c) **taille du lot confirmée explicitement** par l'utilisateur. Signaler que
     le **gate complet** (liste notée + contrôle spam) vient du plugin
     **rapido-marketing** (`delivrabilite-email`) — l'installer pour la version complète.
   - Le hook `garde-envois` (confirmation) reste **inchangé** dans les deux cas.
6. **Lancer** — `lancer_campagne` (`id` de la campagne) : passe le statut à
   `en_cours`. Demander une confirmation explicite AVANT le lancement (envoi de
   masse irréversible), en rappelant la taille du segment.
7. **Suivre les résultats** — `get_stats_campagne` (`id`, `periode` ∈ today | week |
   month | quarter | year) ; compléter avec `get_conversion_par_canal` si
   l'utilisateur compare les canaux.
8. **Lire le funnel complet de capture** (schémas vérifiés serveur) —
   `list_formulaires` (stats principales par formulaire),
   `get_formulaire_soumissions` (`formulaire_id` ou `formulaire_nom` :
   vues, clics, taux de conversion, segment lié) et `list_cta` (clics par
   CTA) : restituer la chaîne **vues → clics CTA → soumissions →
   prospects**, avec le taux de conversion PAR ÉTAPE calculé par script
   (`taux_conversion_etape` du skill `catalogue-kpi`, plugin rapido-startup
   — formule affichée, jamais de tête). Un formulaire qui ne convertit
   plus = signalé avec une proposition (revoir le CTA, la page, l'offre).

## Garde-fous

- Cycle de statuts : `brouillon → planifiee → en_cours → terminee → archivee` ;
  ne pas lancer une campagne déjà `en_cours` ou `terminee`.
- **Gate délivrabilité obligatoire avant tout envoi de masse** : mode `newsletter`
  du skill `delivrabilite-email` si rapido-marketing est présent, sinon checklist
  minimale intégrée — **lot refusé = pas d'envoi**, aucune dérogation.
- Jamais de lancement sans : segment recalculé non vide + template/contenu validé +
  confirmation explicite de l'utilisateur.
- Ajouter des posts à une campagne existante se fait côté RapidoCMS : pour le
  volet réseaux sociaux, utiliser le plugin rapidocms (skill
  orchestration-campagne) — hors périmètre de ce skill (le signaler si
  demandé).
