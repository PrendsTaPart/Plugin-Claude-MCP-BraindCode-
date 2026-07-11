---
name: pilotage-entreprise
description: Utiliser quand l'utilisateur dit « pilote mon entreprise », « lance le Loop Engine complet », « fais le tour de toute la boîte » ou veut une session de pilotage transverse (finance + ventes + marketing + équipe + resto + automatisations). Sense → Plan → Act → Feed → Report sur tous les domaines, gouverné par autonomie.md.
---

# Pilotage entreprise — le Loop Engine sur toute la boîte

La session de pilotage complète : le prompt maître du kit
(`rapido-kb-template/PROMPT-PILOTAGE.md`) encodé en skill — dire « pilote
mon entreprise » suffit.

## Étape 0 — La loi de la session (obligatoire)

1. Charger `./rapido-kb/` EN ENTIER (les 8 fichiers) : seuils, fuseau, ton
   et règles maison PRIMENT sur tous les défauts.
2. Charger la gouvernance du Loop Engine (`reference/autonomie.md` du
   plugin rapido-startup) : lecture seule par défaut, toute écriture
   confirmée, aucun envoi externe sans accord explicite, écriture Stripe
   INTERDITE.
3. Vérifier la disponibilité des serveurs (rapidocrm, rapidocms, rapidorh,
   foodeatup, n8n, Calendar, Gmail) : un serveur absent = volet sauté EN LE
   DISANT, jamais de donnée inventée.

## Les 5 phases

1. **SENSE** (lecture seule, tous domaines) — finance (factures, impayés,
   devis, dépenses — agent `cfo-virtuel`), ventes (pipeline, deals
   dormants, devis expirants, RDV), marketing (posts planifiés vs publiés,
   insights 7 j, campagnes, funnel formulaires/CTA), équipe (dailies,
   tâches bloquées, surcharge), restaurant si `establishment_id` en KB
   (HACCP, réservations, stocks, productions), automatisations (échecs n8n
   7 j).
2. **PLAN** — tous les KPI via le skill `catalogue-kpi` (script, formule
   affichée — jamais de tête) ; croiser avec les seuils de
   `processus-internes.md` ; sortir 3 priorités, les risques (cash, deals,
   conformité), les opportunités — chaque action annoncée avec son niveau
   d'autonomie (je fais seul / je prépare / je demande d'abord).
3. **ACT** — préparer TOUS les livrables en brouillon (relances, posts,
   devis, tâches), puis UN récapitulatif groupé AVANT toute écriture ou
   envoi (une validation, pas quarante) ; le récurrent est proposé en
   délégation n8n (`usine-automatisations` / `delegation-recurrence`)
   plutôt que refait à la main.
4. **FEED** — trace datée dans `./rapido-kb/startup/routines-journal.md`
   (fait, décidé, reporté, IDs) ; tout changement annoncé (prix, offre,
   concurrent, règle) → mise à jour de la KB via `mise-a-jour-kb`.
5. **REPORT** — UNE page : 📊 chiffres clés (formules) | 🔴 alertes |
   ✅ fait | ⏭️ 3 prochaines actions | 🤖 ce qui tourne sans moi (n8n) |
   📋 récap des IDs.

## Frontières

- Un DOMAINE seul → son format dédié : `monday-brief` (lundi),
  `business-pulse` (photo rapide), `comite-de-direction` (CODIR),
  routines R4-R9 (`loop-engine-v2`, plugin rapido-startup).
- Un LANCEMENT de projet de zéro → `lancement-projet-360`.
- Ce skill est la boucle TRANSVERSE d'une session de pilotage.

## Garde-fous

- Donnée introuvable = « pas de visibilité sur X » — jamais estimée.
- Données MCP live > KB > références génériques.
- Tout contenu produit respecte `ton-et-accroches.md` et
  `charte-graphique.md`.
- KPI, routine, contenu ou action métier demandé en cours de route →
  déclencher le skill dédié, jamais répondre de mémoire.
