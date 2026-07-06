---
name: calendrier-editorial
description: Utiliser quand l'utilisateur veut un calendrier éditorial, planifier ses posts du mois ou un plan de contenu. Méthode piliers → répartition par réseau → formats variés → brouillons planifiés rattachés à une campagne.
---

# Calendrier éditorial

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (règles communes)
et `${CLAUDE_PLUGIN_ROOT}/reference/charte-graphique.md` — ton de marque sur
tous les posts.

## Méthode

1. **Objectif du mois** — notoriété / trafic / leads / ventes (le demander si
   absent — voir agent `responsable-marketing`). L'objectif pondère les piliers.
2. **Définir 3-4 PILIERS de contenu** — ex. : coulisses/équipe, expertise/
   conseils, offre/produit, preuve sociale/avis. Chaque post du mois appartient
   à UN pilier ; proposer la répartition (ex. 40/30/20/10) selon l'objectif.
3. **Répartir sur le mois PAR RÉSEAU** — vérifier les comptes disponibles
   (`list_connected_accounts`), fixer une fréquence TENABLE par réseau (mieux
   vaut 2 posts/semaine tenus que 5 abandonnés), utiliser les créneaux de
   l'agent `community-manager` (ou les données `post_insights` si disponibles).
   Étaler — jamais tous les posts le même jour.
4. **Varier les formats** — alterner image / vidéo / texte (`post_type` :
   media, text, mediatext) ; sur Instagram et TikTok le visuel est obligatoire.
   Visuels : skill `prompt-engineering-visuel`.
5. **Présenter le calendrier pour VALIDATION** — tableau : date | heure |
   réseau | pilier | format | accroche. Rien n'est créé avant l'accord de
   l'utilisateur.
6. **Créer et planifier** — pour chaque post validé : `create_draft_tool`
   (adaptation native par réseau — un appel par réseau, bon `account_id`) puis
   `schedule_draft_tool` (`post_date` `Y-m-d`, `post_heure` `H-i-s`).
7. **Rattacher à une campagne** — `create_campagne` (CMS) si besoin puis
   `add_post_campagne` (`campagne_id`, `post_id`) pour chaque post : le mois
   devient analysable d'un bloc via `ingishts_campagne`.

## Garde-fous

- Validation du calendrier complet AVANT la première création ; toute
  modification après coup passe par `list_scheduled_posts` +
  `cancel_schedules_post` (avec confirmation).
- Fréquence honnête : si l'utilisateur n'a pas les visuels/le temps, réduire le
  plan plutôt que planifier l'échec.
- Fin de mois : proposer le skill `analyse-performance-contenu` pour ajuster le
  calendrier suivant.
