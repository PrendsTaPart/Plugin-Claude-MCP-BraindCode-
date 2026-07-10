---
name: gestion-depenses
description: Utiliser quand l'utilisateur veut saisir une dépense, enregistrer un achat ou un abonnement, consulter ses dépenses, suivre ses coûts ou vérifier un montant TTC/HT/TVA côté CRM. Saisie contrôlée par script (TTC = HT + TVA), confirmation avant toute écriture.
---

# Gestion des dépenses (CRM)

La source de vérité des DÉPENSES de l'entreprise côté RapidoCRM — lue par les
routines finance R4 CFO-WEEKLY et R7 CASH-SENTINEL (plugin rapido-startup).

Outils serveur (vérifiés live) : `list_depenses` et `create_depense`
UNIQUEMENT — il n'existe PAS d'outil de détail (`get_…`) ni de suppression de
dépense sur ce serveur : le détail vient de `list_depenses` (filtres), toute
correction se fait dans l'interface RapidoCRM (le dire, ne pas contourner).

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-outils.md`. Seuils et catégories
maison : `./rapido-kb/processus-internes.md` si présent.

## Workflow

1. **Consulter** — `list_depenses` (`statut` ∈ en_attente, payee ; `periode`
   ∈ today, week, month, quarter, year ; `entreprise_id`, `limit`) : toujours
   citer la période avec les chiffres.
2. **Contrôler AVANT de saisir — par script, jamais de tête** :
   construire le JSON d'entrée et exécuter
   `python3 "${CLAUDE_PLUGIN_ROOT}/skills/gestion-depenses/scripts/controle_depense.py" <fichier.json>`
   — entrées `{total_ht, taux_tva, total_ttc?, total_tva?}` ; le script
   calcule TVA et TTC attendus (TTC = HT × (1 + taux/100)), vérifie la
   cohérence à 1 centime près et renvoie
   `{coherent, ttc_attendu, tva_attendue, ecart, formule_appliquee}`.
   Incohérence → la montrer à l'utilisateur et corriger AVANT l'appel ;
   afficher la formule appliquée dans la réponse.
3. **Saisir** — `create_depense` (`entreprise_id` + `total_ht` REQUIS ;
   `taux_tva` en % — TTC/TVA auto-calculés par le serveur si omis ;
   `mode_paiement` ∈ Espèce, Carte bleu, Virement, Chèque ; `statut` ∈
   en_attente, payee ; pièce jointe via `file`/`filename`).
   **Confirmation obligatoire avant l'appel** (hook garde-destructif en
   filet) : récapituler entreprise, HT, taux, TTC contrôlé par le script,
   mode de paiement, statut — une dépense enregistre de l'argent sorti.
4. **Restituer** — après écriture : ID de la dépense, montants (HT/TVA/TTC),
   statut. En lecture : total par statut et par période, gros postes.

## Frontières

- **Dépenses RESTAURANT** (achats fournisseurs avec lignes détaillées) :
  plugin foodeatup, skill `reappro-fournisseurs` — le détail d'une dépense
  resto y est accessible, pas ici.
- **Analyse finance complète** (burn, runway) : routines R4/R7 du plugin
  rapido-startup, qui LISENT ce skill comme source primaire des dépenses
  (calculs délégués à catalogue-kpi).
- **Vue pilotage** (dépenses parmi les KPI commerciaux) :
  `performance-commerciale`.

## Garde-fous

- Aucun montant calculé de tête : le script contrôle, le serveur calcule —
  et si les deux divergent, le serveur fait foi (le signaler).
- Jamais de `create_depense` sans confirmation explicite (hook en filet).
- Ni détail unitaire ni suppression côté serveur : l'annoncer honnêtement,
  renvoyer vers l'interface RapidoCRM.
- Chiffres toujours cités avec leur période et leur statut.
