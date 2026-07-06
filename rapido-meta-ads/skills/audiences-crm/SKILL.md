---
name: audiences-crm
description: Utiliser quand l'utilisateur veut une audience de ses clients, un lookalike ou du retargeting clients. Construit une audience personnalisée depuis le CRM (consentement RGPD vérifié), propose le lookalike 1 % et documente dans le CRM.
---

# Audiences CRM (CRM × Meta)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`,
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-meta-ads.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/CONFORMITE.md` — la section RGPD s'applique
en entier ici.

## Workflow

1. **Source CRM** — `list_clients` ou `get_contacts_segment` (segment
   existant via `list_segments`) : la liste cible. Annoncer le VOLUME, pas
   les identités (compter, ne pas lister les PII dans la conversation).
2. **CONSENTEMENT — question explicite et bloquante** : « Ces contacts
   ont-ils une base légale pour la publicité (consentement marketing collecté
   ou intérêt légitime documenté + information + droit d'opposition) ? »
   Pas de réponse claire = pas d'upload → proposer l'audience WEBSITE (pixel)
   à la place.
3. **Créer l'audience** — `ads_create_custom_audience` (type CUSTOM, nom
   explicite ex. « Clients CRM — {segment} — {date} », description avec la
   base légale).
4. **Charger les contacts** — `ads_update_custom_audience_users` : emails et
   téléphones BRUTS (l'outil hashe lui-même — pas de pré-hash, pas de
   normalisation maison). Ne conserver AUCUN fichier intermédiaire après
   l'upload (CONFORMITE.md).
5. **Lookalike (proposer)** — `ads_create_custom_audience` type LOOKALIKE :
   origine = l'audience CUSTOM créée (jamais une lookalike comme origine),
   ratio 1 % par défaut, ne pas demander de pays.
6. **Documenter dans le CRM** — `log_activity` (note : audience créée, source
   segment, volume, base légale, date) pour la traçabilité.
7. **Miroir WEBSITE** — proposer l'audience WEBSITE depuis le pixel des
   landings Lovable (skill `pixel-et-retargeting`) : retargeting sans PII.

## Garde-fous

- Suppression d'audience : `ads_get_custom_audience_adsets` d'abord + avertir
  que les ad sets liés seront mis en pause (hook ask).
- Une audience trop petite (< 100 contacts) matche mal : le dire, proposer
  d'élargir le segment.
- Jamais de PII listées dans la conversation ni conservées en fichier.
