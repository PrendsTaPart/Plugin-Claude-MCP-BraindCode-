---
name: pitch
description: Utiliser quand on répète ou fabrique le pitch, que l'utilisateur dit « entraîne-moi au pitch téléphone », « on répète le pitch salon », « monte le pitch deck pour la démo de jeudi ». Sert l'entraînement par situation (téléphone, terrain, salon, démonstration, webinaire, apporteur), corrige la répétition, et construit le deck depuis les gabarits maison.
---

# Pitch (répéter, corriger, monter le deck)

Familles engagées : **apprendre** (entraînement) + **configurer**
(`create_pitch_deck`/`edit_pitch_deck`, Confirmé avec aperçu serveur).

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow — s'entraîner

1. **`get_pitch_training`** sur la situation (téléphone, terrain, salon,
   démonstration, webinaire, apporteur) — le pitch cible et ses critères.
2. **Répéter** : l'utilisateur dit son pitch, la correction se fait CONTRE
   les critères renvoyés (durée, accroche, preuve, appel à l'action) — point
   par point, jamais une réécriture complète d'un coup.
3. Recommencer jusqu'au critère tenu ; noter le progrès (formation
   `entrainement-pitch`, skill `chemin-de-formation` pour les missions).

## Workflow — le deck

4. **`list_pitch_templates`** — les gabarits maison ; choisir avec
   l'utilisateur.
5. **`create_pitch_deck`** depuis le gabarit (ou `edit_pitch_deck` sur
   l'existant via `list_pitch_decks`/`get_pitch_deck`) — contenus tirés du
   business plan (`get_business_plan`), des onglets (argumentaire, tarifs
   publics) et des faits réels ; aperçu serveur → accord → confirm.
6. Livrer le deck et sa note d'usage (quelle diapo pour quelle objection).

KPI : `demos`, `taux-signature`, `webinaire-presence`.
Formations : `pitch-deck` (8 missions), `entrainement-pitch` (6),
`demo-certifiee`.

## Garde-fous

- Aucune promesse de revenus ni chiffre non sourcé dans un pitch — chaque
  chiffre du deck porte sa source (onglet, plan, outil daté).
- Le deck se crée depuis les gabarits maison, pas depuis une esthétique
  improvisée ; la charte vient de `get_brand_guidelines` (skill
  `visuels-de-marque`).
