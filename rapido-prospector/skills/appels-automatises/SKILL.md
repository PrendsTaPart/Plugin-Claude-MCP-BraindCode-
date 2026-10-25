---
name: appels-automatises
description: Utiliser quand l'utilisateur demande des appels automatisés Prospector Hub — « lance les appels Twilio sur ce segment », « fais passer le message vocal ». DÉSACTIVÉ par défaut - ne s'active que si ./rapido-kb/prospection.md le déclare avec sa base légale validée.
---

# Appels automatisés (place_call) — désactivé par défaut

## Étape 0 — bloquante
- `${CLAUDE_PLUGIN_ROOT}/reference/conformite-prospection.md` (régime le
  plus strict) ;
- `./rapido-kb/prospection.md` : si `appels_automatises.actives` n'est pas
  `true` (avec base légale documentée, périmètre professionnels,
  consentement recueilli), S'ARRÊTER ICI et le dire — le hook
  garde-conformite refuse de toute façon, et le quota par défaut est 0.

## Démarche (si et seulement si activé dans la KB)
1. **Cibles** : `list_clients` mobileOnly + segment, numéros vérifiés
   E.164 (`scripts/normaliser_telephone.py`), liste d'opposition écartée.
2. **Texte lu** : modèle `kind: call` (`list_message_templates`) — il
   IDENTIFIE l'expéditeur dès les premières secondes et offre un moyen de
   refuser. Contrôle : `scripts/conformite.py --canal appel`.
3. **Lot réduit** : plafond KB (défaut 5, serveur 100 max), fenêtre
   horaire stricte, quota du jour (`scripts/quotas.py`).
4. **Accord explicite** sur la liste finale et le texte exact (synthèse
   vocale française : relire à voix haute mentalement — pas de sigle
   imprononçable).
5. **Lancer** : `place_call` (targets, message).
6. **Lire les résultats** : `list_calls` (statuts), `add_log`, et toute
   demande de refus va dans la liste d'opposition le jour même.

## Pièges
- C'est l'outil le plus risqué juridiquement du serveur : en cas de doute,
  NE PAS APPELER et renvoyer vers le juriste (le document de conformité
  est marqué « à faire valider »).
- L'appel vocal IA conversationnel du CRM est un autre chemin
  (`appeler_entreprise_vocal`, plugin rapidocrm) : ne pas confondre avec
  ce message lu non interactif.

## Dégradation propre
KB absente ou `actives: false` : refus expliqué + ce qu'il faudrait pour
activer (validation juridique écrite). Jamais de « juste un test » sur un
vrai numéro.
