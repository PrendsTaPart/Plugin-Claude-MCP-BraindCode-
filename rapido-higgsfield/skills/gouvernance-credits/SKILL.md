---
name: gouvernance-credits
description: Utiliser quand l'utilisateur parle de « combien de crédits », « budget média », « coût de cette vidéo », « consommation Higgsfield », ou en préflight par les autres skills du plugin avant toute production. Chiffre le coût réel d'une production (préflight get_cost, jamais de tête), le compare au solde et au plafond KB, rend un verdict OK / CONFIRMATION REQUISE / BLOQUÉ, et tient le compteur mensuel.
---

# Gouvernance des crédits Higgsfield

Tout est **payant en crédits**. Ce skill est le **gardien budgétaire** : il chiffre
avant, compare au plafond, tranche, et met à jour le compteur. Aucun chiffre n'est
estimé « de tête » — le coût vient du **préflight** (paramètre get_cost) ou de la
grille de l'audit.

## Règle transverse (écrite ici, applicable à tout le plugin)
**Tout skill de `rapido-higgsfield` invoque `gouvernance-credits` en préflight dès
que la production estimée dépasse le seuil KB** (`budget-media.md`). Le hook
`garde-couts` est le filet déterministe (refus sans marqueur de coût confirmé) ;
ce skill fournit le **chiffrage et le verdict** qui produisent ce marqueur.

## Étape 0 — Charger (obligatoire)
- `./rapido-kb/budget-media.md` (plafond mensuel, seuil de confirmation, compteur) —
  absent → le créer depuis `${CLAUDE_PLUGIN_ROOT}/reference/kb-templates/budget-media.md`.
- `docs/GRILLE-COUTS-HIGGSFIELD.md` et `docs/AUDIT-MCP-HIGGSFIELD.md` (coûts relevés
  en H0 : images ≤ 4 cr, **vidéo 10-75 cr, short 90 cr**).
- `${CLAUDE_PLUGIN_ROOT}/reference/garde-fous-media.md`.

## Workflow

1. **Solde** : `balance` → crédits disponibles + type de plan. (Rappel H0 : le plan
   par défaut est **gratuit, ~10 crédits** — toute vidéo épuise le solde.)
2. **Consommation de la période** : `transactions` (paginé, plus récent d'abord ;
   types spend/deduct/refund/grant) → sommer les dépenses du mois pour le compteur.
3. **Devis de la production** : préflight de coût (paramètre get_cost sur les outils
   de génération image / vidéo / audio / 3d, et sur shorts_studio_create).
   **Non préflightables** (dubbing, upscale_video, upscale_image sans id) : estimer
   via la **grille H0** et le signaler comme estimation, jamais un chiffre inventé.
4. **Verdict par script** (jamais de tête) :
   `python3 "${CLAUDE_PLUGIN_ROOT}/skills/gouvernance-credits/scripts/verifie_budget.py"`
   avec `{solde, cout_estime, plafond_mensuel, seuil_confirmation, deja_consomme|transactions}`
   → **OK** / **CONFIRMATION REQUISE** / **BLOQUÉ** (formule affichée) :
   - **BLOQUÉ** si coût > solde, ou coût > (plafond − déjà consommé) → **on ne génère pas**.
   - **CONFIRMATION REQUISE** si coût > seuil → présenter le coût, attendre l'accord.
   - **OK** sinon.
5. **Après une production validée** : mettre à jour le **compteur mensuel** de
   `budget-media.md` (via `rapido-suite:mise-a-jour-kb`) avec le coût réel relevé
   (`balance` avant/après, ou la transaction).

## Réponses types
- « Combien de crédits ? » → `balance` + reste vs plafond + coût des livrables courants
  (grille H0).
- « Coût de cette vidéo ? » → préflight get_cost du modèle/réglage visé + verdict.
- « Ma consommation ce mois ? » → somme des `transactions` spend/deduct de la période.

## Garde-fous
Coût **par préflight ou grille**, **jamais de tête** ; verdict **par script** ;
**BLOQUÉ = pas de génération** (ni contournement) ; plafond et solde réels priment ;
compteur KB tenu à jour ; cas non préflightables **signalés comme estimation**.
