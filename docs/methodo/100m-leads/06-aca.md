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

## 🆕 Mise à jour marché 2026 (sourcée)

Le livre (2023) ne traite ni la délivrabilité ni le ciblage par signaux —
compléments 2025-2026 (détail + sources : `docs/methodo/etat-de-lart-2026.md`) :

- **Délivrabilité (email froid)** : chauffer un domaine neuf (**5-10 msg/jour**,
  montée sur 4-6 semaines), plafonner (~**500/j Gmail, 300/j Outlook**) et
  **répartir sur plusieurs boîtes** ; viser **≥ 85 % de placement en boîte de
  réception**. Le « 100 emails/jour » de la règle des 100 se répartit sur
  plusieurs boîtes chauffées, jamais une seule. Source :
  [instantly.ai](https://instantly.ai/blog/how-to-achieve-90-cold-email-deliverability-in-2025/) (2025),
  [lemlist](https://www.lemlist.com/blog/warm-up-email-account) (2025). Chiffres
  **INCERTAIN** (varient par secteur).
- **Signal-led outbound** : contacter au **bon moment** (changement de poste,
  visite site, actualité) plutôt qu'au volume aveugle ; enrichissement
  *waterfall*. Source : [clay.com](https://www.clay.com/blog/clay-apollo) (2025).
- **Speed-to-lead** : répondre à un lead entrant en **< 60 s** (patron GoHighLevel)
  renforce le « la vitesse gagne » du livre. Source :
  [grow-highlevel.com](https://grow-highlevel.com/post/gohighlevel-lead-nurturing-automation-workflows) (2026).
- **MCP Rapido** : le CRM (`schedule_email`) **n'a pas** de warmup/rotation
  (→ outil externe ou backend, cf. M0) ; le speed-to-lead se câble en **webhook
  n8n** sur `get_formulaire_soumissions`.

## Frontières
- **Transformer** ces conversations en programme de référencement →
  `07-lead-getters.md`.
- **Contact FROID** (inconnus) → autre canal du Core Four (`01-core-four.md`).
