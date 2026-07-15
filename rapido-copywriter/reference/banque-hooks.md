# Banque de hooks — vivante, par réseau

**Révisé le 2026-07-15.** Patterns **francisés et re-dérivés** (structures génériques à
`[placeholders]`) — inspirés de `hook-extractor`/`hook-writer` (MIT), **jamais** copiés
d'un post réel (cf. `NOTICE.md`). La **compréhension** (familles, contexte d'attention,
matrice) est dans `reference/mecanique-des-hooks.md`. Chaque hook porte : **famille**
(taxonomie), **contexte** (où vit le hook sur ce réseau), **contre-indication**, **tag**
(`NEUTRE` à l'init, passe `GAGNANT` via `score_hooks.py` sur les vrais insights),
**compteur d'usage**.

> **Règle** : piocher les `GAGNANT` d'abord (par réseau **et par famille**, cf. la synthèse
> en bas). Tag/Usage mis à jour **par script uniquement**. **Promesse du hook tenue** dans
> le contenu (sinon changer de famille — `mecanique-des-hooks.md` §d).

## LinkedIn — le hook se **lit** (1-2 lignes avant « …voir plus »)

| # | Structure [placeholder] | Famille | Funnel | Contre-indication | Tag | Usage |
|---|---|---|---|---|---|---|
| L1 | `Il y a [durée], je [situation]. Aujourd'hui, [résultat]. Voici ce que j'ai appris.` | Ouverture d'histoire | TOFU | trop longue avant le point | NEUTRE | 0 |
| L2 | `[Chiffre surprenant] sur [sujet]. La plupart l'ignorent.` | Chiffre-preuve | TOFU | chiffre invérifiable | NEUTRE | 0 |
| L3 | `Tout le monde dit [croyance]. C'est faux — voici pourquoi.` | Contrarien | TOFU | sans preuve → gratuit | NEUTRE | 0 |
| L4 | `[Erreur fréquente] m'a coûté [conséquence]. Ne la faites pas.` | Erreur coûteuse | MOFU | ton culpabilisant | NEUTRE | 0 |
| L5 | `3 choses que j'aurais aimé savoir sur [sujet] avant [étape].` | Liste à enjeu | MOFU | liste sans enjeu | NEUTRE | 0 |
| L6 | `On m'a demandé : « [question client] ? » Ma réponse en [N] points.` | Question miroir | MOFU | question banale | NEUTRE | 0 |
| L7 | `[Client] est passé de [avant] à [après] en [durée]. La méthode ↓` | Avant / après | BOFU | sans cas réel | NEUTRE | 0 |
| L8 | `Arrêtez de [pratique]. Faites [alternative] à la place.` | Négativité utile | TOFU | négativité gratuite | NEUTRE | 0 |
| L9 | `Le [métier] qui [action] gagne toujours contre celui qui [action opposée].` | Contrarien | TOFU | généralisation vide | NEUTRE | 0 |
| L10 | `Question pour les [cible] : comment gérez-vous [problème] ? (la mienne ↓)` | Question miroir | TOFU | question fermée | NEUTRE | 0 |

## Facebook — le hook est **court & local** (~1-2 s)

| # | Structure [placeholder] | Famille | Funnel | Contre-indication | Tag | Usage |
|---|---|---|---|---|---|---|
| F1 | `[Ville/quartier] : [nouveauté locale] 👇` | Écart de curiosité | TOFU | promesse non tenue | NEUTRE | 0 |
| F2 | `On a testé [chose] pour vous. Verdict :` | Écart de curiosité | TOFU | verdict décevant | NEUTRE | 0 |
| F3 | `[Jour], c'est [offre/événement]. Qui vient ?` | Question miroir | MOFU | pas d'enjeu | NEUTRE | 0 |
| F4 | `Petit rappel utile pour [cible locale] :` | Liste à enjeu | TOFU | rappel banal | NEUTRE | 0 |
| F5 | `Merci à [nombre] d'entre vous pour [action] — voici la suite.` | Autorité / coulisses | BOFU | fausse exclusivité | NEUTRE | 0 |
| F6 | `Avant / après : [transformation en une image].` | Avant / après | MOFU | sans photo réelle | NEUTRE | 0 |
| F7 | `[Question simple à réponse en commentaire] ?` | Question miroir | TOFU | engagement-bait | NEUTRE | 0 |
| F8 | `Nouveau chez [marque] : [bénéfice en 5 mots].` | Chiffre-preuve | MOFU | bénéfice vague | NEUTRE | 0 |

## Instagram — le hook est **visuel** (image/slide 1, caption ≤125 car.)

| # | Structure [placeholder] | Famille | Funnel | Contre-indication | Tag | Usage |
|---|---|---|---|---|---|---|
| I1 | `Enregistre ce post si tu [objectif].` | Liste à enjeu | MOFU | valeur faible | NEUTRE | 0 |
| I2 | `[N] façons de [résultat] (swipe →)` | Liste à enjeu | MOFU | liste creuse | NEUTRE | 0 |
| I3 | `Personne ne te dit ça sur [sujet].` | Écart de curiosité | TOFU | payoff absent | NEUTRE | 0 |
| I4 | `POV : tu viens de découvrir [astuce].` | Ouverture d'histoire | TOFU | cliché POV | NEUTRE | 0 |
| I5 | `Le secret de [résultat] tient en [N] slides.` | Écart de curiosité | MOFU | pas de secret réel | NEUTRE | 0 |
| I6 | `Arrête de faire ça ❌ → fais plutôt ça ✅` | Négativité utile | TOFU | négativité gratuite | NEUTRE | 0 |
| I7 | `[Chiffre] avant / [chiffre] après. Voici comment.` | Avant / après | BOFU | chiffre inventé | NEUTRE | 0 |
| I8 | `Sauvegarde pour plus tard : [ressource].` | Chiffre-preuve | MOFU | ressource vague | NEUTRE | 0 |

## TikTok — **triple hook** (verbal + visuel + texte à l'écran, < 3 s)

| # | Structure [placeholder] | Famille | Funnel | Contre-indication | Tag | Usage |
|---|---|---|---|---|---|---|
| T1 | `[Affirmation choc]. Reste, je t'explique.` | Écart de curiosité | TOFU | choc sans fond | NEUTRE | 0 |
| T2 | `Tu fais [action banale] ? Tu perds [conséquence].` | Erreur coûteuse | TOFU | anxiogène | NEUTRE | 0 |
| T3 | `Voici ce que personne ne montre sur [coulisses].` | Autorité / coulisses | TOFU | fausse exclusivité | NEUTRE | 0 |
| T4 | `3 secondes pour changer ta façon de [action].` | Liste à enjeu | TOFU | promesse creuse | NEUTRE | 0 |
| T5 | `J'ai testé [chose] pendant [durée]. Résultat inattendu.` | Ouverture d'histoire | MOFU | résultat plat | NEUTRE | 0 |
| T6 | `Si tu es [cible], arrête tout et regarde ça.` | Négativité utile | TOFU | racoleur | NEUTRE | 0 |
| T7 | `La vérité sur [sujet] que [autorité] ne dit pas.` | Contrarien | TOFU | complotiste | NEUTRE | 0 |
| T8 | `Étape 1 pour [résultat] (partie 1/[N]).` | Liste à enjeu | MOFU | série non tenue | NEUTRE | 0 |

## Synthèse — familles gagnantes par réseau (maj par script)

_Section écrite par `scripts/score_hooks.py` sur les vrais insights (liked/shares/comments/
views). Non éditée à la main._

- **Dernière mise à jour** : (aucune — lancer `score_hooks.py` après publication)
- LinkedIn : —
- Facebook : —
- Instagram : —
- TikTok : —

> Ajout de hooks : forme **[placeholder] générique** + **famille** (taxonomie
> `mecanique-des-hooks.md`) + **contre-indication** ; jamais un hook réel d'un créateur.
