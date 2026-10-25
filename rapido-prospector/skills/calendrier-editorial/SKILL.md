---
name: calendrier-editorial
description: Utiliser quand l'utilisateur planifie ses publications dans Prospector Hub — « cale les posts de la semaine dans Prospect », « quels trous dans mon calendrier Prospector ? ». Planification add/update_calendar_post par réseau et format ; la publication réelle reste côté rapidocms.
---

# Calendrier éditorial (planifier, pas publier)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (section
  contenus).

## Démarche
1. **Lire** : `list_calendar_posts` (période, réseau) — réseaux servis :
   linkedin, linkedin_profile, facebook, instagram, tiktok.
2. **Trous par script** : comparer les dates servies à la cadence voulue
   (jours sans post par réseau) — calcul montré, pas de « trou » décrété
   sans la liste.
3. **Planifier** : `add_calendar_post` (networks, format, subject, visual,
   scheduled_at, status brouillon) ; ajuster par `update_calendar_post`.
   Le statut « publie » déclenche l'ask du hook garde-publication.
4. **Supprimer** : `delete_calendar_post` sur confirmation.
5. **Semaine en un écran** : widget calendrier-editorial-semaine (posts,
   articles `list_blog_posts`, vidéos `list_video_posts`, webinaires
   `list_webinars`).

## Délégation (ne pas recopier)
Ce calendrier PLANIFIE dans Prospector Hub. La publication réelle sur les
réseaux (comptes connectés, brouillons, programmation effective) passe par
le plugin rapidocms (skill `pipeline-contenu-social`) ; la stratégie
éditoriale d'ensemble aussi. En cas de double calendrier, celui de
rapidocms fait foi pour ce qui PART réellement.

## Pièges
- `scheduled_at` ici n'envoie rien nulle part : c'est un plan de travail.
  Le dire pour éviter la fausse impression de « posts programmés ».
- Un visuel se fabrique côté rapido-design / rapidocms ; `visual` stocke
  la référence.

## Dégradation propre
Calendrier vide : le dire et proposer un cadencement réaliste (pas de
promesse de volume).
