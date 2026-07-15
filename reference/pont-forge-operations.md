# Pont forge → opérations — la règle de pontage

> `rapido-forge` contient 181 skills d'**EXERCICES** (méthodologie) qui produisent des
> **livrables** dans `./rapido-kb/startup/forge/`. Les plugins métier contiennent les
> skills **OPÉRATIONNELS** branchés aux MCP. Ces deux couches doivent se **parler** :
> l'opérationnel **lit** le livrable forge au lieu de refaire l'exercice, et forge
> **redirige** vers l'opérationnel quand l'utilisateur veut agir sur données réelles.

## (a) Côté opérationnel — lire le livrable forge d'abord
Tout skill opérationnel qui applique une **méthode couverte par forge** commence par
**chercher le livrable forge correspondant** dans `./rapido-kb/startup/forge/` :
- **s'il existe** → le **charger comme base** (profil SONCAS des personas, définition
  des étapes AARRR, règles du programme de parrainage…) ;
- **s'il n'existe pas** → **proposer de faire l'exercice forge d'abord** OU **continuer
  avec les défauts en le disant** (jamais en silence).

Le livrable forge est la **source de connaissance** ; les **données MCP réelles** sont
la matière ; le skill opérationnel **applique** l'une à l'autre.

## (b) Côté forge — pointer vers l'opérationnel
Chaque skill forge d'une méthode « actionnable » ajoute en fin de `SKILL.md` une
section **« Passer à l'opérationnel »** pointant vers le skill métier qui applique la
méthode aux **données réelles**.

## Table de pontage (forge ↔ opérationnel)
| Skill forge (exercice) | Skill opérationnel (données réelles) |
|---|---|
| `scale-soncas` | `rapidocrm:preparation-rdv` |
| `scale-funnel-aarrr` | `rapidocrm:funnel-aarrr-reel` |
| `scale-bant-qualification` | `rapidocrm:qualification-deals` |
| `scale-spin-selling` | `rapidocrm:coach-de-vente` |
| `scale-sales-call-script` | `rapidocrm:coach-de-vente` |
| `scale-objections-playbook` | `rapidocrm:playbook-objections-vivant` |
| `scale-customer-success` | `rapido-relation-client:pilotage-service-client` |
| `scale-nps-survey` | `rapido-relation-client:boucle-nps` |
| `scale-customer-journey` | `rapido-relation-client:cent-premiers-jours` |
| `scale-referral-program` | `rapidocrm:programme-ambassadeurs` |
| `scale-upsell-crosssell` | `rapidocrm:expansion-clients` |
| `scale-influencer-marketing` | `rapido-marketing:operations-influenceurs` |

> La boucle se ferme : **100 premiers jours → NPS promoteur → ambassadeur → nouveaux
> leads → preparation-rdv → …** Chaque skill opérationnel cite le livrable forge lu (ou
> son absence), jamais un profil/segment inventé.
