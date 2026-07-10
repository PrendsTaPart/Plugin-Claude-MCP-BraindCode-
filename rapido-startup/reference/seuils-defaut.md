# Seuils par défaut — benchmarks finance & startup (rapido-startup)

**Règle d'usage** : ces valeurs ne servent QUE si le seuil est absent de
`./rapido-kb/` (en priorité `processus-internes.md`). Un seuil maison PRIME
toujours. Quand un défaut est utilisé, le SIGNALER dans la réponse :
« défaut secteur — personnalisable dans ./rapido-kb/processus-internes.md ».
Ne jamais présenter un benchmark comme la donnée réelle de l'entreprise.

| Indicateur | Seuil par défaut | Lecture |
|---|---|---|
| LTV:CAC | sain ≥ 3:1 | En dessous : acquisition trop chère ou rétention trop faible |
| CAC payback | 5–12 mois | Au-delà de 12 mois : la croissance consomme la trésorerie |
| Runway cible | 12–18 mois | Horizon confortable pour lever ou atteindre la rentabilité |
| **Alerte runway** | **< 6 mois** | Alerte prioritaire dans toute revue — à remonter en premier |
| Churn B2B annuel | sain 3–8 % | Au-delà : problème de rétention avant tout problème d'acquisition |
| Marge brute SaaS | 70–85 % | En dessous : coûts d'infra/support à examiner |
| Food cost (restaurant) | 28–35 % | Référence FoodEatUp — croiser avec analyse-rentabilite-carte |
| Rule of 40 | croissance % + marge % ≥ 40 % | Équilibre croissance/rentabilité |
| DSO (délai d'encaissement) | < 45 jours | Au-delà : relances d'impayés (devis-facture-relance / invoice-chase) |
| NRR (rétention nette de revenu) | > 100 % | Sous 100 % : la base installée se contracte |
| Croissance MRR post-seed | 10–15 % / mois | Ordre de grandeur, à contextualiser selon le secteur |
| Pipeline coverage | 3–4× l'objectif | Sous 3× : pipeline insuffisant pour l'objectif du trimestre |

Notes :
- Les montants Stripe sont en CENTIMES : convertir avant de comparer à ces
  seuils (voir `pieges-outils.md`).
- Tout calcul d'indicateur (LTV, CAC, runway, NRR…) passe par un script
  embarqué du skill concerné — jamais de calcul de tête.
- Chiffres datés et sourcés (serveur + période) dans toute restitution.
