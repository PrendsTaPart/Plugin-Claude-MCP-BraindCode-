---
name: distribution-multi-plateformes
description: Utiliser quand l'utilisateur diffuse un Short ou une vidéo hors YouTube — « poste ce clip sur TikTok et Instagram », « programme la distribution », « où en sont mes cross-posts ? ». Comptes connectés vérifiés d'abord ; sans compte, renvoi vers l'application ou délégation rapidocms.
---

# Distribution multi-plateformes

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md` — au relevé du
  2026-10-25 : AUCUN compte de distribution connecté.

## Démarche
1. **Vérifier** : `yt_list_connected_accounts` — la distribution exige
   des comptes connectés (loi n° 11).
2. **Sans compte** : le dire et renvoyer vers la page Distribution de
   l'application ; pour les réseaux que rapidocms couvre déjà (comptes
   connectés côté CMS), DÉLÉGUER au plugin rapidocms plutôt que doubler.
3. **Avec comptes** : `yt_schedule_cross_post` — 6 posts AU PLUS par
   appel, avec par plateforme : légende adaptée, hashtags, premier
   commentaire. La copy multi-réseaux se travaille avec
   rapido-copywriter quand il est installé. (Hook garde-public : ask.)
4. **Suivre** : `yt_list_cross_posts` (états réels),
   `yt_cancel_cross_post` sur confirmation.

## Pièges
- Une même légende partout performe mal : l'appel accepte des champs PAR
  plateforme — les utiliser.
- Un cross-post annulé côté serveur ne retire pas un post déjà parti sur
  la plateforme : regarder l'état réel avant d'annoncer.

## Dégradation propre
Plateforme absente des comptes connectés : proposer l'ajout dans
l'application — jamais d'identifiant de compte deviné.
