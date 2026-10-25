---
description: Audit des manques du catalogue de tutoriels (production)
argument-hint: "[slug de module, ou vide pour l'audit global]"
---

Dérouler le skill `studio-production-tutos`, étapes audit et priorisation :
`audit_formation` (limité au `moduleSlug` de l'argument s'il y en a un)
croisé avec `lister_modules` (`videosEnLigne` vs `videosPrevues`).

Restituer : les manques connus, les modules annoncés mais vides, et une
proposition d'ordre de tournage argumentée. Proposer ensuite les briefs
officiels (`brief_video_client`, `brief_video_partenaire`) pour les sujets
retenus — sans jamais promettre une vidéo non tournée.
