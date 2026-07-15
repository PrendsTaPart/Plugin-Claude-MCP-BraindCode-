# EXEMPLE — sante-client.md (le vrai fichier vit dans ./rapido-kb/relation-client/)

> Copier dans `./rapido-kb/relation-client/sante-client.md`. Lu par `sante-client`
> (`scripts/health_score.py`). Pondérations **jamais en dur** dans le skill.

## Pondérations du health score (somme = 1)
| Facteur | Poids | Sens |
|---|---|---|
| recence | [0.35] | activité récente (campagnes CRM / posts CMS / commandes FoodEatUp) |
| paiement | [0.30] | régularité de paiement (factures) |
| tickets | [0.15] | charge de support (tickets ouverts) |
| nps | [0.20] | satisfaction individuelle si connue |

## Seuils
- `seuil_recence_jours` : [45] (au-delà = froid)
- `seuil_tickets` : [5]
- Couleurs : vert ≥ [70], orange ≥ [45], rouge < 45.
