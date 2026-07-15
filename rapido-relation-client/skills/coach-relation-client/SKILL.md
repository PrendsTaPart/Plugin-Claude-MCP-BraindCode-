---
name: coach-relation-client
description: Utiliser quand l'utilisateur demande comment fidéliser, améliorer l'expérience client, réduire le churn, activer ses utilisateurs SaaS, ou transformer des clients en ambassadeurs — sans savoir quelle approche. Routeur qui diagnostique le problème (onboarding / usage / churn / advocacy) puis route vers le bon skill/framework (100 jours, Hooked, Cialdini rétention, animation).
---

# Coach relation client — le routeur fidélité/expérience

Le pendant relation client du `rapidocrm:coach-de-vente` : diagnostique et **route**.
Il **synthétise et oriente** — il ne refait pas les skills dédiés.

## Diagnostic d'entrée → routage
| Problème | Approche (réécrite FR, aucun verbatim) | Où aller |
|---|---|---|
| **Onboarding** (nouveaux clients qui décrochent tôt) | *Never Lose a Customer Again* — les 100 premiers jours (8 phases) | **`cent-premiers-jours`** |
| **Usage / activation** (SaaS peu utilisés) | **Hooked** (Nir Eyal) — boucle **déclencheur → action → récompense variable → investissement** | ici (application) + produit |
| **Churn** (clients qui partent) | Health score + sauvetage ciblé | **`sante-client`** + **`boucle-nps`** (détracteurs) |
| **Advocacy** (transformer en promoteurs) | NPS promoteurs → ambassadeurs | **`boucle-nps`** + `rapidocrm:programme-ambassadeurs` |
| **Rétention par la relation** (habitudes, engagement) | Leviers **Cialdini** côté rétention (réciprocité, cohérence/engagement) | **`rapido-meta-ads:influence-psychology`** |
| **Animation** (sondages, jeux, points) | Mécaniques d'animation | **`rapidocrm:animation-client`** |

Pour l'approche retenue : **résumé opérationnel court** (réécrit FR, **jamais de texte
de livre verbatim**) + **application immédiate** à la situation + **renvoi au skill dédié**.

## Sortie
Le diagnostic (onboarding / usage / churn / advocacy), l'approche recommandée, les 3
prochains gestes, et le skill à enchaîner.

## Anti-collision
- **Ne duplique pas** `cent-premiers-jours`, `sante-client`, `boucle-nps`,
  `animation-client`, `influence-psychology` : il **route** vers eux.
- Pendant relation client de `rapidocrm:coach-de-vente` (lui = vente ; moi = fidélité).

## Garde-fous
Synthèse **réécrite** (aucun verbatim de livre) ; route vers les skills dédiés ;
diagnostic **avant** méthode ; données client réelles si un compte est nommé.
