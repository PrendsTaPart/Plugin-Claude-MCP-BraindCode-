# Cadence & séquences cold email

> **Sources distillées** : coldoutboundskills (`cold-email-weekly-rhythm`,
> `campaign-copywriting`, `campaign-strategy`) MIT © 2026 GrowthEngineX ;
> gtm-flywheel (`cold-email/sequence-architecture`, `copy-frameworks`,
> `personalization-engine`) MIT © 2026 ColdIQ. Reformulé FR, non-verbatim.

## Architecture de séquence (multi-touch)
Cadence de référence, ajustable via KB : **J0** email d'ouverture · **J3**
relance (« vous avez vu ? ») · **J7** nouvel angle/valeur · **J14** break-up.
Sortie de séquence dès **réponse** ou **RDV**.

## Copy (frameworks)
- 1 idée par email, court, une seule demande.
- Personnalisation **obligatoire** (1re ligne spécifique au prospect).
- Objet = curiosité/valeur, pas le pitch.

## Rythme opérationnel hebdo
Répartir sourcing / rédaction / envois / lecture des réponses sur la semaine
(pas tout d'un coup) ; tenir les plafonds de délivrabilité (voir
`delivrabilite-email.md`).

## Mapping Rapido
Rédaction → `redaction-commerciale` ; planification → `schedule_email` ;
personnalisation depuis `get_entreprise`/`account-research` ; anti-doublon des
relances via table n8n (`memoire-operationnelle`). Chaque lot **confirmé**
(`garde-envois`). Remplace Smartlead/Instantly par **RapidoCRM**.

→ Cible : **`machine-outbound` (M9)** — déjà livré ; ces éléments l'affinent.
