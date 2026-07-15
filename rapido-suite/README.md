# rapido-suite

La **suite transverse** Rapido : onboarding, pilotage d'entreprise et
synchronisation de la base de connaissance, par-dessus les serveurs Rapido
(CRM, CMS, RH, FoodEatUp) et les connecteurs de repli (Lovable, Meta Ads, n8n).

Skill phare : **`pilotage-entreprise`** — la boucle *Sense → Plan → Act → Feed →
Report* sur toute la boîte (finance, ventes, marketing, équipe, resto,
automatisations), gouvernée par `reference/autonomie.md` (lecture libre, écriture
confirmée par système, actions sensibles confirmées une par une).

## Anti-collision avec rapido-marketing

Le pilotage marketing détaillé vit dans le plugin **rapido-marketing**
(`pilotage-marketing`). Si les **deux plugins sont installés**,
`pilotage-entreprise` **invoque `rapido-marketing:pilotage-marketing`** pour son
volet marketing **au lieu de le dupliquer** — un seul moteur marketing, piloté
depuis la suite. Sans rapido-marketing, `pilotage-entreprise` traite le marketing
en lecture directe (posts, insights, campagnes, funnel). (Règle miroir dans le
README de rapido-marketing.)

## Gouvernance
`reference/autonomie.md` : lecture en autonomie totale ; **écriture confirmée par
système** (une validation par serveur, jamais deux serveurs sur un seul accord) ;
**actions destructrices/irréversibles confirmées une par une** ; en cas d'échec,
arrêt à l'étape + récapitulatif des IDs déjà créés. Les hooks du plugin forcent la
confirmation côté outillage.
