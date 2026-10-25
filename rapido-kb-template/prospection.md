# Prospection — quotas, conformité, identité d'expéditeur

> Dernière mise à jour : AAAA-MM-JJ — gabarit du plugin rapido-prospector.
> Les hooks du plugin lisent le bloc JSON ci-dessous. Sans ce fichier, des
> valeurs PRUDENTES par défaut s'appliquent et les appels automatisés restent
> désactivés. Ce fichier abaisse ou précise les règles ; il ne les contourne
> jamais (les plafonds du serveur et les ask systématiques restent).

## Bloc machine (lu par les hooks — garder un JSON valide)

```json
{
  "quotas_jour": {
    "email": 50,
    "sms": 20,
    "appels": 0,
    "linkedin_invitations": 10,
    "linkedin_messages": 20
  },
  "plafonds_lot": {
    "email": 25,
    "sms": 10,
    "appels": 5
  },
  "fenetre_horaire": {
    "debut": "09:00",
    "fin": "18:00",
    "jours": ["lun", "mar", "mer", "jeu", "ven"],
    "fuseau": "Europe/Paris"
  },
  "expediteur": {
    "identite": "### À COMPLÉTER — nom de l'entreprise et de la personne qui signe",
    "email": "### À COMPLÉTER",
    "desinscription": "### À COMPLÉTER — phrase de désinscription insérée dans chaque e-mail",
    "mention_stop": "STOP au ### À COMPLÉTER (numéro court ou réponse STOP)"
  },
  "liste_opposition": [],
  "appels_automatises": {
    "actives": false,
    "base_legale": "### À COMPLÉTER — base légale validée par un juriste avant toute activation",
    "perimetre": "professionnels uniquement, consentement recueilli"
  }
}
```

## Comment remplir

- **quotas_jour** : plafond d'envois par canal et par jour civil (Europe/Paris).
  `appels: 0` tant que les appels automatisés ne sont pas activés.
- **plafonds_lot** : taille maximale d'UN envoi groupé. Le serveur impose en
  plus 200 cibles par SMS et 100 par appel ; le plus petit gagne.
- **fenetre_horaire** : aucun envoi réel hors de cette fenêtre.
- **expediteur** : l'identité apparaît dans chaque message ; la phrase de
  désinscription est obligatoire dans chaque e-mail, la mention STOP dans
  chaque SMS.
- **liste_opposition** : e-mails, numéros E.164 ou identifiants de connexion
  LinkedIn des personnes qui ont demandé à ne plus être contactées. Un
  destinataire de cette liste bloque l'envoi entier (deny).
- **appels_automatises** : `actives` ne passe à `true` qu'après validation
  juridique écrite (voir reference/conformite-prospection.md du plugin).

## Articulation avec rapido-employe

Si le plugin rapido-employe est installé et que son cadre
`.claude/state/cadre-employe.json` existe, le quota appliqué à chaque canal
est le PLUS PETIT des deux (cadre Academy d'abord : 20 envois/jour au
relevé d'octobre 2026).
