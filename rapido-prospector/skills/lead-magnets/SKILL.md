---
name: lead-magnets
description: Utiliser quand l'utilisateur gère ses lead magnets Prospector Hub — « téléverse ce PDF en lead magnet », « liste mes documents », « remplace la description ». Téléversement base64 ou URL, liens temporaires jamais collés en dur ; la fabrication se délègue à rapido-leadmagnet.
---

# Lead magnets (documents à télécharger)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md` (liens
  temporaires).

## Démarche
1. **Lire** : `list_lead_magnets` (nom, description, fichier) — les liens
   renvoyés sont TEMPORAIRES : bons pour une vérification immédiate,
   jamais pour un contenu durable.
2. **Fabriquer** : le document lui-même (contenu, maquette, page de
   capture) se construit avec le plugin rapido-leadmagnet (skill
   `fabrication-lead-magnet`) quand il est installé — ce skill-ci STOCKE
   et distribue côté Prospect.
3. **Téléverser** : `add_lead_magnet` — `content_base64` pour un fichier
   local, ou `source_url` PUBLIQUE réelle ; name, description, file_name,
   mime_type exacts.
4. **Retoucher** : `update_lead_magnet` (nom, description).
5. **Supprimer** : `delete_lead_magnet` sur confirmation — le FICHIER
   stocké part avec (cascade annoncée).

## Pièges
- Dans un e-mail, un article ou une page : pointer la page de capture (qui
  régénère un lien frais), pas le lien signé du jour.
- Un gros fichier en base64 gonfle l'appel : préférer `source_url` quand
  le document est déjà hébergé publiquement.

## Dégradation propre
Téléversement en erreur : restituer le message serveur ; ne pas re-tenter
en boucle ; vérifier mime_type et taille d'abord.
