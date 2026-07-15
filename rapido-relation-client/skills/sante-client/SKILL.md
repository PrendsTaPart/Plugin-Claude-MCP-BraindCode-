---
name: sante-client
description: Utiliser quand l'utilisateur veut un health score, savoir quels clients sont à risque, la santé de son portefeuille, ou qui va churner. Health score composite calculé sur données réelles (récence d'activité, régularité de paiement, tickets, NPS) via un script à formule affichée ; sortie = portefeuille trié vert/orange/rouge avec la prochaine action par client rouge.
---

# Santé client — le health score à la demande

Un score composite **explicable** par client, sur données réelles.

## Étape 0 — pondérations KB
- `./rapido-kb/relation-client/sante-client.md` : pondérations et seuils (jamais en dur).

## Sense (données réelles, selon le produit)
- **Récence d'activité** : campagnes CRM lancées, posts CMS publiés, commandes
  FoodEatUp — la source dépend du produit du client.
- **Régularité de paiement** : `list_factures` (retards ?).
- **Tickets ouverts** (support).
- **NPS individuel** si connu (`boucle-nps`).

## Plan (score par script)
- Calcul via `python3 "${CLAUDE_PLUGIN_ROOT}/skills/sante-client/scripts/health_score.py"`
  — **formule affichée** (Σ facteur normalisé × poids ÷ Σpoids). Facteur absent =
  exclu (poids renormalisés), jamais inventé.

## Report
- **Portefeuille trié** vert / orange / rouge, avec, pour **chaque client rouge**, **LA
  prochaine action** (et le facteur qui plombe le score).

## Frontière
- La **routine churn** (`OPS-ALERTE-CHURN` / loop-engineering) **ALERTE périodiquement** ;
  **moi = fournir le score à la demande** et son **explication** (quel facteur, pourquoi).
  Complémentaires.

## Garde-fous
Pondérations KB ; **score par script** (formule affichée), jamais de tête ; facteurs
**réels** (absent = exclu, pas inventé) ; une action concrète par client rouge.
