# Lead Getters — faire générer des leads par d'autres

> **Idées** : Alex Hormozi, *$100M Leads* (2023). **Distillation source** :
> founder-playbook (MIT © 2026 AgentSeal). Reformulation FR — voir `NOTICE.md`.

## Le principe
Une fois que **vous** savez générer des leads, faites-le faire par d'autres. Ça
dépasse votre capacité personnelle. **4 types** :

| Type | Qui | Comment |
|---|---|---|
| **Clients** | acheteurs actuels | programme de **référencement** |
| **Employés** | votre équipe | former + intéresser |
| **Agences** | prestataires marketing | payer au résultat |
| **Affiliés** | partenaires à audience | structure de commission |

## Type 1 — Clients (référencement)
Source la plus qualifiée (le client pré-qualifie). D'abord bâtir la **bienveillance**
(tenir ses promesses, expérience fluide, communication, rapidité, extras), PUIS
demander. **7 façons de demander** : après une grosse victoire ; au moment de
l'achat ; comme monnaie de négociation ; via des **événements** (« semaine
parrainage ») ; programme permanent ; bonus à débloquer ; carte cadeau à offrir.

**Un bon programme** : bénéfice **mutuel**, **facile** (partage en 1 clic),
récompense **claire**, **traçable**, **rapide** à verser.

## Type 2 — Employés (les 3D)
Former avec **Document → Démontrer → Dupliquer** : écrire exactement comment vous
faites (checklist) → le faire devant eux → ils le font devant vous en suivant la
checklist. **Test** : si vous disparaissiez demain, un inconnu obtiendrait-il vos
résultats avec la seule checklist ? Ne jamais recruter pour un canal que vous
n'avez pas maîtrisé vous-même.

## Type 3 — Agences
Quand un canal est profitable mais qu'il manque temps/expertise. Filtrer :
études de cas dans **votre** vertical, ancienneté client, SLA de réponse,
reporting, part de risque acceptée. Éviter le « bien lancé puis silence » (revue
mensuelle), le reporting boîte noire (exiger l'accès aux comptes pub).

## Type 4 — Affiliés
Partenaires à audience, rémunérés à la commission (souvent 20-40 % digital).
Essentiels : **matériel fourni** (sinon pas de participation), **attribution
fiable**, **paiement rapide**. Recrutement : clients superfans, créateurs du
secteur, réseaux d'affiliation, partenaires complémentaires non concurrents.

## Empilement
```
Vous (maîtrise Core Four) → Employés → Clients (référent) → Affiliés → Agences
```
Chaque couche compose ; l'entreprise mature a les cinq en simultané.

## Quand NE PAS ajouter de lead getters
Canal non maîtrisé soi-même ; unit economics insuffisantes ; pas de tracking ;
expérience client médiocre (les référents s'épuisent) ; offre qui ne convertit pas.

## Exemple Rapido / FoodEatUp
Restaurant : programme parrainage (« 10 € pour toi, 10 € pour ton ami ») via le
CRM + jeu concours pour amplifier ; carte de fidélité comme déclencheur.

## Outils MCP Rapido pressentis

| Type | Outils MCP Rapido |
|---|---|
| Clients / référencement | rapidocrm `list_jeux_concours`/`lancer_jeu_concours_entreprise`, `get_loyalty_points`, `create_campagne` ; foodeatup fidélité |
| Employés (3D, suivi) | rapidorh `create-project-tool`/`create-task-tool`, `get-dailies-tool` ; skill `detection-surcharge` |
| Agences (suivi perf) | rapido-meta-ads `ads_account_get_activity_logs`, `ads_insights_*` |
| Affiliés (segments, commissions) | rapidocrm `create_segment`, `list_commerciaux`, `update_commercial_objectifs` |

## Frontières
- **Générer** les leads soi-même d'abord → `01-core-four.md`.
- **Décider** quand déléguer → checklist « canal maîtrisé » de
  `08-arbres-de-decision.md`.
