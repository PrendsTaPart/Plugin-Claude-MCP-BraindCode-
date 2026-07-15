# Garde-fous marketing

Règles **non négociables** de tout skill/agent de ce plugin. Les hooks
déterministes (`hooks/`) en appliquent une partie ; le reste est contractuel.

## (a) Tout envoi = confirmation humaine explicite

Aucun **envoi ou action visible de l'extérieur** ne part sans accord explicite :
email, SMS, newsletter, **lancement de campagne**, **publication/planification**
de post, **activation** de pub. Le contenu part **en brouillon** ; un
récapitulatif est présenté (destinataires, contenu, date/heure, coût), puis
l'utilisateur valide **en une fois**. Hook en filet : `garde-envois`
(confirmation forcée — voir `hooks/hooks.json`).

## (b) RGPD — consentement et effacement

- **Consentement vérifié AVANT** d'ajouter une personne à une séquence, une
  newsletter ou une audience publicitaire (patron du skill
  `rapido-meta-ads:audiences-crm` : données hashées, consentement rappelé).
- **Droit à l'effacement** respecté : une demande de suppression est honorée
  dans tous les systèmes concernés (CRM, séquences, audiences) et **jamais
  contournée**.
- Pas de donnée personnelle **inventée** ni enrichie hors cadre légal.

## (c) Délivrabilité et acquisition propre

- **Volumes progressifs** (warmup) sur les envois froids ; ne pas saturer un
  domaine neuf (cf. `docs/methodo/etat-de-lart-2026.md`).
- **Lien de désinscription présent** sur tout envoi de masse.
- **Pas d'achat de listes**, **pas de scraping** hors des **workflows de
  prospection officiels du CRM** (`prospecter_maps`/`prospecter_entreprise`/
  `prospecter_prospect`).

## (d) Budgets publicitaires

- **Plafond confirmé AVANT activation** ; toute entité pub naît en **PAUSED**
  (patron `rapido-meta-ads`) ; activation = accord explicite. Hooks du plugin
  rapido-meta-ads (`plafond-budget`, `garde-argent-reel`) en filet quand ce
  plugin est présent.

## (e) Jamais de KPI/score « de tête »

Tout **score** (lead scoring) ou **KPI** (taux de conversion, CAC, LTGP:CAC,
runway…) est calculé par un **script Python stdlib** avec **formule affichée** —
jamais estimé par le modèle. Réutiliser le skill `rapido-startup:catalogue-kpi`
(`calcul_kpi.py`) ; un futur script de scoring suivra le même principe.

## Renvois
- Priorité des serveurs : `reference/priorite-mcp.md`.
- Pièges par outil : `reference/pieges-outils.md`.
