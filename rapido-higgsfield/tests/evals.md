# Évals — plugin rapido-higgsfield (0.2.0)

## gouvernance-credits

| # | Phrase | Attendu |
|---|---|---|
| GC1 | « Combien de crédits me reste-t-il ? » | `gouvernance-credits` : `balance` → solde + plan ; `transactions` → consommation du mois ; reste vs plafond `budget-media.md` ; coûts des livrables courants cités depuis la grille H0 (jamais de tête) |
| GC2 | « Combien coûte cette vidéo Kling de 5 s ? » | `gouvernance-credits` : **préflight get_cost** (jamais d'estimation de tête) → `verifie_budget.py` → verdict ; rappelle qu'une vidéo (10-30 cr) dépasse un solde gratuit (~10 cr) |
| GC3 (blocage) | « Génère la pub vidéo 15 s » avec solde 8 crédits | `gouvernance-credits` : coût ~75 cr > solde → `verifie_budget.py` rend **BLOQUÉ** → **pas de génération**, propose top-up/plan payant ; aucun contournement (hook `garde-couts` en filet) |

## Hooks (tests fonctionnels dans le testeur)
- `garde-couts` : génération payante sans marqueur de coût → **deny** ; avec `get_cost`/`cout_confirme` → allow.
- `garde-voix` : create_voice/voice_change/dubbing → **ask** (droits) ; autre → allow.
