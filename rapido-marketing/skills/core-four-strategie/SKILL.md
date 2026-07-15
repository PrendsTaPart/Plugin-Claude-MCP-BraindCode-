---
name: core-four-strategie
description: Utiliser quand l'utilisateur se demande par où commencer pour trouver des clients, quel canal d'acquisition choisir, combien de prospection faire par jour, ou comment scaler un canal qui marche. Diagnostique les ressources, recommande UN canal, fixe la cadence et le critère de maîtrise avant d'en ajouter un autre.
---

# Stratégie Core Four — choisir, cadencer, scaler l'acquisition

> **Idées** : Alex Hormozi, *$100M Leads* (2023). **Distillation** :
> `docs/methodo/100m-leads/` (source MIT founder-playbook). Reformulé, citations
> < 15 mots. Ce skill **décide** ; l'exécution est déléguée (voir plus bas).

## Étape 0 — Charger (obligatoire)
- Fiches `docs/methodo/100m-leads/01-core-four.md`, `03-regle-des-100.md`,
  `05-more-better-new.md`, `08-arbres-de-decision.md` (au **marketplace root**).
- `./rapido-kb/marketing/` **si présent** (seuils, canaux, historique client) —
  sinon `./rapido-kb/processus-internes.md`.
- `${CLAUDE_PLUGIN_ROOT}/reference/garde-fous-marketing.md` et `priorite-mcp.md`.

## Méthode

1. **Diagnostic ressources** (arbre 1, fiche 08) : combien de clients payants ?
   du temps / de l'argent ? → **règle de décision** :
   - < 10 clients → **contact chaud** (rien d'autre) ;
   - temps sans argent → contact froid OU contenu ;
   - argent sans temps → pub payante ;
   - les deux → contact froid + contenu.
   Recommander **UN** canal, jamais quatre en parallèle.
2. **Cadence** (règle des 100) : selon le canal, fixer le minimum quotidien
   (100 contacts / 100 min contenu / 100 min pub / 100 € pub) tenu **100 jours**.
3. **Critère de maîtrise** (checklist fiche 08) : coût/lead et conversion
   prévisibles à ~30 %, playbook documenté, économie sans le fondateur, scalable
   ×10. **Tant que faux → ne pas ajouter de canal.**
4. **Scaling** (More Better New, fiche 05) : d'abord *plus*, puis *mieux* quand
   ça casse, puis *nouveau* seulement après.

## Livrable type
Un **plan d'acquisition une page** : canal choisi + pourquoi, cadence
quotidienne, seuils de maîtrise à atteindre, prochaine étape (scaler ou ajouter).
Consigner dans `./rapido-kb/marketing/` via `mise-a-jour-kb` si l'utilisateur veut.

## Délégation de l'exécution (ne rien dupliquer)
- **Contact chaud / froid** → skills `redaction-commerciale` et
  `prospection-pipeline` (rapidocrm). *(exécuteur transverse `machine-outbound`
  du plugin — à livrer.)*
- **Contenu** → skills `pipeline-contenu-social` et `calendrier-editorial`
  (rapidocms). *(exécuteur transverse `machine-inbound` — à livrer.)*
- **Pub payante** → skill `lancement-campagne-meta` (rapido-meta-ads), budget
  confirmé, entités PAUSED.
- **Calcul des seuils** (coût/lead, ×10) → skill `catalogue-kpi` (jamais de tête).

## Cas d'usage croisés
- Offre pas prête à convertir → skill `hundred-million-offers` **avant** de
  générer du trafic.
- Machine outbound B2B structurée → skill `predictable-revenue`.
- Plan marketing global (cible, USP, canaux) → skill `one-page-marketing`.

## Garde-fous
Tout envoi/publication/activation reste **confirmé** (garde-fous-marketing) ;
priorité aux serveurs Rapido (priorite-mcp) ; aucun chiffre estimé de tête.
