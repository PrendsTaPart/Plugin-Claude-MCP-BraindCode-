# Délivrabilité — règles d'envoi (KB client)

> Copié depuis `reference/kb-templates/` dans `./rapido-kb/marketing/` à la 1re
> exécution. Le skill `delivrabilite-email` lit ce fichier en Étape 0 (gate
> pré-envoi + runbook). Ajuster aux domaines et boîtes réels du client.

## Plafonds
- Plafond quotidien par boîte : **40** (défaut prudent ; max Gmail ~500/j,
  Outlook ~300/j — ne jamais viser le max sur un domaine non établi).
- Boîtes en rotation : (à renseigner)
- **Plafond quotidien total** (taille de lot maximale, tous envois confondus) :
  (à renseigner)

## Calendrier de montée en charge (warmup — domaine/boîte neuf)
| Semaine | Volume/jour/boîte |
|---|---|
| S1 | 5-10 |
| S2 | 15-20 |
| S3 | 25-35 |
| S4 | 40-50 |
| S5+ | régime nominal (plafond ci-dessus) |

## Seuil de note minimale (scorecard de liste)
- **Seuil : C** — tout lot noté **D ou E est REFUSÉ**. Aucune dérogation sans
  **modifier explicitement ce fichier** (traçable).

## Pauses / incidents
- **Pause proposée** si : chute brutale des réponses **ou** pic d'échecs/bounces.
- **Reprise** : progressive — revenir 1-2 crans en arrière dans le calendrier.
- Journal des incidents et reprises : `./rapido-kb/marketing/apprentissages.md`
  (date | contexte | leçon | preuve | skill source).
