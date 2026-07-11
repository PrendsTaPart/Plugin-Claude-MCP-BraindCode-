---
name: ideation-contact-form
description: "Utiliser quand l'utilisateur veut créer un formulaire de contact optimisé pour la conversion (parcours idéation StartupsForge)."
---

# Contact Form

**Catégorie** : Idéation  
**Durée** : 20-30 min

## Pourquoi

Le formulaire de contact est ton point de conversion principal. Un formulaire bien conçu peut doubler le nombre de leads générés.

## Objectif

Créer un formulaire de contact optimisé pour la conversion.

## Livrable attendu

Formulaire de contact fonctionnel avec webhook de notification

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Définir les champs essentiels** — Minimum : email. Idéal : nom, email, message
2. **Créer le formulaire** — Utilise Tally, Typeform ou natif Lovable
3. **Configurer les notifications** — Email et/ou Slack à chaque soumission
4. **Créer la page de remerciement** — Confirme la réception + prochaines étapes
5. **Tester le flux complet** — Vérifie réception des notifications

## Pro tips

- Moins de champs = plus de conversions
- Affiche un message de confirmation clair
- Ajoute un délai de réponse attendu

## Erreurs fréquentes

- Trop de champs obligatoires
- Pas de confirmation après soumission
- Formulaire qui ne fonctionne pas sur mobile

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord
- **Lovable** (`lovable`, via le plugin `rapido-lovable`) pour la construction réelle

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/ideation/ideation-contact-form.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).
