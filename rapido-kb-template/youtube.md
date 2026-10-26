# YouTube — seuils de dépense et préférences de chaîne

> Dernière mise à jour : AAAA-MM-JJ — gabarit du plugin rapido-youtube.
> Le hook garde-credits lit le bloc JSON ci-dessous. Sans ce fichier, un
> seuil PRUDENT par défaut s'applique (25 crédits par session). Ce fichier
> ajuste les seuils ; il ne désactive jamais les gardes.

## Bloc machine (lu par les hooks — garder un JSON valide)

```json
{
  "seuil_credits_session": 25,
  "variations_max_sans_question": 1,
  "chaine_de_travail_habituelle": "### À COMPLÉTER — nom de la chaîne (jamais un identifiant codé en dur)",
  "fenetre_publication": {
    "fuseau": "Europe/Paris",
    "jours_exclus": [],
    "heures_exclues": []
  }
}
```

## Comment remplir

- **seuil_credits_session** : au-delà de ce cumul estimé de crédits
  dépensés dans la session, chaque génération supplémentaire repasse par
  une question.
- **variations_max_sans_question** : nombre de variations de miniature
  généré sans demander (1 par défaut — l'analyse est gratuite, la
  génération ne l'est pas).
- **chaine_de_travail_habituelle** : un NOM de chaîne, à titre indicatif —
  la règle du channel_id explicite s'applique quand même.
- **fenetre_publication** : reprise par le skill autopilote
  (yt_set_autopilot) comme jours et heures exclus par défaut.
