# Rapport d'intégration — rapido-forge (2026-07-10)

## Procédure exécutée

1. `python3 scripts/valider-plugins.py` → **TOUT VALIDE**
   (12 plugins, 36 JSON, 322 frontmatters).
2. `python3 scripts/tester-skills.py` → **0 FAIL, 0 WARN, 0 INFO**
   (après 1 correctif : « lorem ipsum » hors code dans
   bootcamp-mvp-wireframes → backticks, convention du scanner).
3. Hooks testés fonctionnellement sur stdin (tests figés dans la batterie) :
   - `garde-ecriture-kb.py` : Write `./rapido-kb/...` → allow ;
     Write dans le dépôt → deny ; Write `/tmp/...` → allow ;
   - `rappel-argent-reel.py` : `ads_create_campaign` → ask (PAUSED,
     activation après accord explicite).

## Vérifications de contenu (184 fichiers)

- Frontmatters : 184/184 valides, `name` = dossier/fichier partout,
  descriptions « Utiliser quand » (guillemets doubles tolérés par le
  parseur du testeur).
- Portabilité : 0 écriture hors `./rapido-kb/`, 0 URL en dur, 0 ID client.
- Renvois `plugin:skill` : 146 vérifiés, 2 corrigés
  (`design:design-system` → `rapido-lovable:frontend-design` ;
  `design:user-research` → `rapidocrm:mom-test`).
- Unicité des `name` : 0 collision avec les 119 skills existants.

## Cas de test (rapido-forge/tests/evals.md)

12 déclenchements positifs (3 par agent), 8 négatifs (routage vers
d'autres plugins), 5 inter-parcours (le directeur-programme diagnostique
avant de router — fondateur avec revenus → scale proposé).
