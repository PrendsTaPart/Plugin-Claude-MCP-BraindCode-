# ACA — le contact chaud qui ne braque personne

> **Idées** : Alex Hormozi, *$100M Leads* (2023). **Distillation source** :
> founder-playbook (MIT © 2026 AgentSeal). Reformulation FR — voir `NOTICE.md`.

## Le framework ACA

Pour le **contact chaud** (1-à-1, audience qui vous connaît), l'ouverture suit
trois temps : **A**cknowledge — **C**ompliment — **A**sk (Reconnaître —
Complimenter — Demander).

```
Bonjour [Prénom],
[Reconnaître — référence à quelque chose de précis chez la personne]
[Complimenter — éloge sincère sur son travail/sa réussite]
Je travaille sur [chose] et j'ai pensé à toi parce que [raison précise].
Serais-tu ouvert à [petite demande] ?
```

> Note de la source : l'ordre exact des lettres ACA est à revérifier selon
> l'édition du livre ; le motif constant est **reconnaître → complimenter →
> demander** (donner/valoriser avant de demander).

## Les 10 étapes du contact chaud

1. Constituer sa liste (contacts tél., email, abonnés). 2. Choisir la plateforme
où l'on a le plus de contacts. 3. Personnaliser. 4. Contacter **un par un** (pas
de blast). 5. Apporter de la valeur avant de demander. 6. Demander des mises en
relation. 7. Faire l'offre la plus facile possible (gratuit, sans risque).
8. Commencer par les relations les plus proches. 9. Passer au payant après
résultats. 10. Garder la liste au chaud (continuer à donner de la valeur).

## Les mots magiques du référencement (referral)
« Tu connais quelqu'un qui… ? » · « Qui est la personne la plus [trait
pertinent] que tu connais ? » · « À ma place, à qui parlerais-tu ? »

## Bon vs mauvais contact chaud

| Mauvais | Bon |
|---|---|
| « Salut, ça fait longtemps ! Regarde mon nouveau truc » | « Vu ton post sur X, bravo ! Petite question… » |
| Message de masse | Personnalisé, un par un |
| Attaquer par le pitch | Attaquer par la valeur / la curiosité |

## Exemple Rapido / FoodEatUp
Un restaurateur relance ses habitués pour la nouvelle carte : message perso par
client (reconnaît sa dernière visite, complimente, propose une dégustation) —
pas un SMS groupé impersonnel.

## Outils MCP Rapido pressentis

| Besoin | Outils MCP Rapido |
|---|---|
| Liste chaude segmentée | rapidocrm `list_contacts`, `get_contacts_segment`, `create_segment` ; foodeatup `list_clients` |
| Message 1-à-1 personnalisé | rapidocrm `send_email`/`send_sms` (unitaire), `create_template_email` ; Gmail `create_draft` |
| Demander des référencements | rapidocrm `log_activity`, `create_task` (relance), programme via `07-lead-getters.md` |
| Garder la liste au chaud | rapidocrm `schedule_email`, newsletters ; loyalty `get_loyalty_points` |

> Envoi = action visible par le client : brouillon d'abord, envoi après accord
> (gouvernance des skills rapidocrm).

## Frontières
- **Transformer** ces conversations en programme de référencement →
  `07-lead-getters.md`.
- **Contact FROID** (inconnus) → autre canal du Core Four (`01-core-four.md`).
