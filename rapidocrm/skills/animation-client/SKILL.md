---
name: animation-client
description: Utiliser quand l'utilisateur veut lancer un sondage, un jeu concours, consulter des résultats de sondage, animer ou fidéliser ses clients, ou parle de points de fidélité.
---

# Animation client — sondages, jeux concours, fidélité

Anime et fidélise la base clients avec les outils Marketing de RapidoCRM.
**Un lancement est VISIBLE PAR LES CLIENTS : confirmation explicite avant
tout `lancer_*` (niveau 2 — le hook garde-destructif la force aussi).**

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`. Ton et
vocabulaire depuis `./rapido-kb/ton-et-accroches.md` si elle existe ; cibles
depuis `cibles-personas.md`. Jamais d'ID inventé : tout part d'un `list_*`.

## Sondages

1. **Modèles d'abord** : `list_sondages` (avec leurs statistiques de
   participation) pour repérer le MODÈLE à utiliser — ne JAMAIS inventer un
   `modele_sondage_id` (c'est l'ID `sondage_companie.id` renvoyé par la
   liste). Aucun modèle adapté → le dire, proposer d'en créer un côté
   interface RapidoCRM (pas d'outil de création de modèle exposé).
2. **Lancer** — `lancer_sondage_entreprise` (`modele_sondage_id` +
   `entreprise_id`, vérifié via `get_entreprise`/`list_entreprises`) —
   APRÈS confirmation avec récapitulatif : modèle, entreprise cible, ce que
   les clients verront.
3. **Résultats** — `get_sondage_resultats` (par `sondage_id` ou
   `sondage_nom` ; `type` = `companie` par défaut, `client` pour un sondage
   client) : restituer taux de participation, scores PAR QUESTION, et une
   **synthèse des verbatims en 3 enseignements** (citations courtes
   anonymisées — jamais de PII étalée dans la conversation).

## Jeux concours

1. `list_jeux_concours` (filtres `q`, `statut`, `periode`
   today/week/month/quarter/year) pour trouver le modèle (`modele_jeu_id` =
   `companies_games.id`) et éviter un doublon en cours.
2. `lancer_jeu_concours_entreprise` (`modele_jeu_id` + `entreprise_id`) —
   après confirmation. **Rappel systématique, en une ligne, du cadre FR :
   règlement déposé/accessible, participation gratuite sans obligation
   d'achat, mentions RGPD sur la collecte des données des participants** —
   sans jouer au juriste : pour le règlement lui-même, renvoyer vers un
   professionnel du droit.

## Fidélité

1. `get_loyalty_points` — points par client (`q` pour cibler un client,
   `periode` pour une fenêtre, `limit`).
2. **Croiser avec `get_top_clients`** (même `periode`) et proposer
   **3 actions de rétention ciblées** :
   - **relance douce des points dormants** (points élevés, aucune activité
     récente) ;
   - **récompense des top clients** (gros CA — reconnaissance avant qu'ils
     ne la demandent) ;
   - **réactivation** (CA en baisse ou client silencieux — offre de retour).
   Chiffres cités avec leur période.

## Envoi des invitations — TOUJOURS délégué

L'envoi (email/SMS) des invitations à un sondage, un jeu ou une opération de
fidélité passe par le skill `communication-client` (fiche entreprise, choix
du canal, template, confirmation d'envoi) — **jamais d'envoi en direct
depuis ce skill**. Pour une opération de masse : skill `campagne-marketing`
(segment recalculé + confirmation).

## Garde-fous

- Confirmation AVANT tout `lancer_*` (action visible par les clients) — le
  hook garde-destructif force l'ask en filet.
- Jamais deux animations identiques simultanées sur la même cible : vérifier
  les `list_*` avant de lancer.
- Résultats : synthèse fidèle aux données (taux réels, verbatims réels) —
  pas d'embellissement ; participation faible = dite et expliquée.
- Cas d'usage croisé : pour la VALIDATION TERRAIN d'une idée (Mom Test), un
  sondage RapidoCRM peut compléter les entretiens — voir le skill
  `mom-test` ; garder des questions sur le passé et le concret, pas des
  intentions.
- Boucle growth : la routine R6 GROWTH-LOOP (plugin rapido-startup) lit les
  sondages en cours en phase SENSE (`list_sondages` →
  `get_sondage_resultats`) — les animations lancées ici alimentent son
  signal qualitatif.
