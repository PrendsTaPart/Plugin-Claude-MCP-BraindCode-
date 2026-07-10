# Évals — plugin rapido-startup

À remplir avec les skills (mêmes conventions que `tests/evals.md` racine :
scénario avec KB vs sans KB, vérification que les seuils maison priment sur
`reference/seuils-defaut.md` et que Stripe reste en lecture seule dans les
routines).

## Éval 0 — squelette (structure)

- `python3 scripts/valider-plugins.py` et `python3 scripts/tester-skills.py`
  passent avec le plugin présent.
- Le hook `garde-stripe-write` répond `ask` à
  `{"tool_name":"mcp__stripe__stripe_api_write"}` sur stdin.
