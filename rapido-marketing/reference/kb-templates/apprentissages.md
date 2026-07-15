# Apprentissages marketing

> Modèle. Copié dans `./rapido-kb/marketing/apprentissages.md`. Mémoire longue
> durée des leçons : **alimentée automatiquement** à chaque clôture de
> campagne/expérience par les skills (1 à 3 leçons datées et **sourcées par les
> chiffres du script**). Ces leçons **priment** sur les valeurs par défaut lors
> des plans futurs.

## Format (une ligne par leçon)
`date | contexte | leçon | preuve (chiffre + script) | skill source`

## Journal
| Date | Contexte | Leçon | Preuve | Skill source |
|---|---|---|---|---|
| (AAAA-MM-JJ) | (exemple : séquence cold email S1, segment resto/TPE) | (exemple : la relance J3 double les réponses) | (exemple : 7 % vs 3,4 %, `stats_outbound.py`) | `machine-outbound` |

## Règle
Pas de leçon sans **preuve chiffrée** issue d'un script (jamais « on a
l'impression que »). Une leçon qui change un taux de référence → mettre aussi à
jour `benchmarks.md`.
