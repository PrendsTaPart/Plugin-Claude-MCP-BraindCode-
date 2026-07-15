---
name: lead-magnet-machine
description: Utiliser quand l'utilisateur veut créer un aimant à prospects, un lead magnet, une ressource ou un cadeau gratuit pour capter des emails, ou améliorer le nom d'une offre gratuite. Conçoit le lead magnet en 7 étapes (problème, type, format, nom, consommation, qualité, next step) et délègue la production et la capture.
---

# Lead Magnet Machine — concevoir un aimant à prospects

> **Idées** : Alex Hormozi, *$100M Leads* (2023). **Distillation** :
> `docs/methodo/100m-leads/02-lead-magnet-7-etapes.md` (source MIT
> founder-playbook). Reformulé, citations < 15 mots.

## Étape 0 — Charger (obligatoire)
- Fiche `docs/methodo/100m-leads/02-lead-magnet-7-etapes.md`.
- `./rapido-kb/marketing/` si présent (offres, cibles, ton) — sinon
  `produits-services.md` + `cibles-personas.md` + `ton-et-accroches.md`.
- `${CLAUDE_PLUGIN_ROOT}/reference/garde-fous-marketing.md`.

## Méthode (les 7 étapes, avec décisions)

1. **Problème** : étroit, réel, qui mène à l'offre principale (le tirer de la KB,
   jamais inventé).
2. **Type** (règle de décision) : *révéler un problème* (diagnostic) /
   *échantillon* (essai) / *une étape d'un process* (modèle, calculateur) —
   choisir selon l'offre à révéler ensuite.
3. **Format** : PDF, vidéo, outil, essai — le plus rapide à consommer (< 10 min).
4. **Nom** (levier n°1) : promettre **résultat + délai + public** précis ;
   proposer 3 noms, garder le plus spécifique.
5. **Consommation facile** ; 6. **Qualité** (assez bon pour être vendu) ;
   7. **Next step** évident vers l'offre.
8. **Distribution** : le placer PARTOUT (signatures, CTA de posts, bio, bas
   d'article) — le goulot est la distribution, pas la qualité.

## Livrable type
Un **brief de lead magnet** : problème visé, type + format, **nom testé**,
plan de consommation, CTA vers l'offre, liste des points de distribution.

## Délégation de l'exécution
- **Visuel / couverture** → skill `studio-visuel-marque` ou
  `prompt-engineering-visuel` (rapidocms).
- **Hébergement + capture** → `create_editor_template` type `landing_page`
  (rapidocrm) + `list_formulaires`/`list_cta`. *(exécuteur `tunnel-de-vente-360`
  — à livrer.)*
- **Diffusion** → skill `pipeline-contenu-social` (rapidocms) ; emails →
  skill `campagne-marketing` (rapidocrm), envoi **confirmé**.
- **Exécution complète de bout en bout** (fabrication → page → campagne → projet
  RH → mesure) → l'usine `rapido-leadmagnet:chef-usine-leadmagnet`. **Ce skill
  CONÇOIT** (7 étapes) ; **l'usine EXÉCUTE** ce qui est conçu.

## Cas d'usage croisés
- L'offre que le magnet révèle → skill `hundred-million-offers`.
- Où placer le magnet dans le funnel → skill `funnel-tofu-mofu-bofu` (TOFU).
- Nom / promesse mémorable → skill `storybrand-messaging`.

## Garde-fous
Données (problème, offre, cible) issues de la KB, **jamais inventées** ;
capture d'emails = **consentement RGPD** (garde-fous-marketing) ; envoi confirmé.
