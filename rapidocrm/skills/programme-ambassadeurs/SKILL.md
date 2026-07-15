---
name: programme-ambassadeurs
description: Utiliser quand l'utilisateur veut opérer le programme ambassadeurs BraindCode (10 % client / 20 % apporteur pro), identifier les clients éligibles au parrainage, suivre les commissions ou relancer les ambassadeurs. Opère le programme existant (exécution) ; le choix du TYPE de programme relève de rapido-marketing:lead-getters-systeme. Paramètres depuis ./rapido-kb/offres.md.
---

# Programme ambassadeurs — opérer le parrainage BraindCode

**OPÈRE** le programme ambassadeurs **existant** (10 % client / 20 % apporteur pro).
Paramètres (taux, plafonds, conversion en crédits) dans `./rapido-kb/offres.md` —
jamais en dur, absent → le signaler.

## Éligibilité (signaux réels)
- **Ancienneté 6+ mois** (`get_contact` / `get_entreprise`).
- **Factures payées sans retard** (`list_factures` — aucun `en_retard` historique).
- **Satisfaction élevée** si un sondage est disponible (`get_sondage_resultats`) —
  sinon ne pas inventer, le noter.

## Proposition
- **10 % client / 20 % apporteur pro**, **convertible en crédits** (paramètres
  `./rapido-kb/offres.md`). Préparer le message (déléguer à `redaction-commerciale`),
  **envoi confirmé** (brouillon par défaut).

## Suivi des commissions
- **Lecture** : `get_loyalty_points` (solde de points/commissions de l'ambassadeur).
- **Ajustement** : si un outil d'ajustement des points est exposé par le serveur,
  l'utiliser en **respectant les plafonds du serveur** ; **sinon consigner le montage
  et le signaler au backend** (aucun ajustement inventé).
- **Relance systématique J+60** post-signature (`create_task`) — réactiver l'ambassadeur.

## Anti-collision
- **`rapido-marketing:lead-getters-systeme`** : lui **choisit le TYPE** de programme
  (parrainage / affiliation / ambassadeurs…) selon la maturité — **stratégie**. Moi
  j'**OPÈRE** le programme BraindCode déjà défini — **exécution**. (Règle miroir
  documentée dans les deux SKILL.md.)
- **`expansion-clients`** : lui fait monter en gamme ; moi transforme en apporteur.

## Garde-fous
Éligibilité **sourcée** (ancienneté, paiement, satisfaction), jamais supposée ;
taux/plafonds depuis `./rapido-kb/offres.md` ; **plafonds serveur respectés** sur les
points ; aucun ajustement inventé ; tout envoi en **brouillon confirmé**.
