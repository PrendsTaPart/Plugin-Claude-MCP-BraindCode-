# Conformité de la prospection — règles appliquées par défaut

> **À faire valider par un juriste.** Ce document énonce les règles
> PRUDENTES que le plugin applique par défaut à la prospection B2B par
> e-mail, SMS et appel automatisé. Il ne constitue pas un avis juridique et
> n'invente aucune règle de droit : quand une obligation précise doit être
> citée (texte, seuil, sanction), elle se vérifie auprès d'un juriste ou de
> l'autorité compétente (en France : la CNIL) avant d'être affirmée. Quand
> le connecteur Academy (« FoodEatUp formation ») est branché, les
> formations `conformite` et `rgpd` du catalogue font référence :
> `get_formation` les sert avec leur date de mise à jour.

## Principes appliqués par les hooks, quel que soit le canal

1. **Identification de l'expéditeur** : chaque message dit qui écrit
   (entreprise + personne), avec un moyen de contact réel. Un envoi sans
   identité d'expéditeur dans ./rapido-kb/prospection.md est refusé.
2. **Droit d'opposition respecté AVANT l'envoi** : la liste d'opposition de
   la KB bloque l'envoi entier si un destinataire y figure ; toute demande
   « ne me contactez plus » y est ajoutée le jour même, tous canaux
   confondus.
3. **Moyen de refus dans chaque message** : phrase de désinscription dans
   chaque e-mail, mention STOP dans chaque SMS, formule de refus dans
   chaque texte d'appel.
4. **Fenêtre horaire et volumes** : envois en jours et heures ouvrés
   (fenêtre de la KB, Europe/Paris), par petits lots, sous les quotas du
   jour. La prudence sur les volumes protège aussi la délivrabilité.
5. **B2B ciblé** : la base vise des établissements professionnels,
   contactés à raison de leur activité (ciblage par zone et spécialité).
   La prospection de particuliers est HORS périmètre de ce plugin.
6. **Minimisation et exactitude** : on n'enregistre que les champs utiles
   à la prospection ; les corrections demandées (update_client) se font
   sans délai ; aucune donnée personnelle de prospect n'est versionnée
   dans le dépôt (widgets générés dans un dossier ignoré par git).

## Appels automatisés : régime le plus strict

`place_call` lance des appels robotisés (synthèse vocale). C'est le canal
le plus encadré juridiquement et le plus intrusif :

- **désactivé par défaut** : le hook garde-conformite refuse tout
  `place_call` tant que `appels_automatises.actives` n'est pas `true` dans
  ./rapido-kb/prospection.md ;
- l'activation exige une **base légale documentée dans la KB et validée
  par un juriste** (périmètre : professionnels, consentement recueilli) ;
- le texte lu **s'identifie dès les premières secondes** et offre un moyen
  de refus ;
- lots réduits (plafond KB, ≤ 100 côté serveur), fenêtre horaire stricte,
  journal systématique (`add_log`, `list_calls`).

## Ce que le plugin refuse de faire

- Envoyer à une adresse ou un numéro deviné, générique reconstruit, ou
  acheté hors de la base Prospect.
- Contourner un quota en fractionnant les lots sur plusieurs sessions.
- Retirer la mention de désinscription ou la mention STOP « pour gagner de
  la place ».
- Présenter un chiffre (MRR, taux de réponse) sans sa source ni son statut
  (mesuré ou estimé).
