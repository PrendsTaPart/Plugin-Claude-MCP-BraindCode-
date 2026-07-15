# Banque de hooks — vivante, par réseau

**Révisé le 2026-07-15.** Patterns de hooks **francisés et re-dérivés** (structures
génériques à `[placeholders]`) — inspirés des formules de `hook-extractor`/`hook-writer`
(MIT), **jamais** copiés d'un post ou d'un créateur réel (cf. `NOTICE.md`). Chaque hook :
réseau, étape funnel, **tag** (`NEUTRE` à l'initialisation, passe `GAGNANT` via
`score_hooks.py` sur les vrais insights CMS), **compteur d'usage** (0).

> **Règle** : le copywriter **pioche les `GAGNANT` d'abord** (par réseau), puis complète.
> Le tag se met à jour **uniquement** sur les métriques réelles (liked/shares/comments/
> views), jamais à la main. La **promesse du hook est tenue** dans le contenu (anti-clickbait).

## LinkedIn

| # | Structure [placeholder] | Funnel | Tag | Usage |
|---|---|---|---|---|
| L1 | `Il y a [durée], je [situation initiale]. Aujourd'hui, [résultat]. Voici ce que j'ai appris.` | TOFU | NEUTRE | 0 |
| L2 | `[Chiffre surprenant] sur [sujet]. La plupart l'ignorent.` | TOFU | NEUTRE | 0 |
| L3 | `Tout le monde dit [croyance commune]. C'est faux — voici pourquoi.` (contrarian) | TOFU | NEUTRE | 0 |
| L4 | `[Erreur fréquente] m'a coûté [conséquence]. Ne la faites pas.` | MOFU | NEUTRE | 0 |
| L5 | `3 choses que j'aurais aimé savoir sur [sujet] avant [étape].` | MOFU | NEUTRE | 0 |
| L6 | `On m'a demandé : « [question réelle client] ? » Ma réponse en [N] points.` | MOFU | NEUTRE | 0 |
| L7 | `[Client/segment] est passé de [avant] à [après] en [durée]. La méthode ↓` | BOFU | NEUTRE | 0 |
| L8 | `Arrêtez de [pratique répandue]. Faites [alternative] à la place.` | TOFU | NEUTRE | 0 |
| L9 | `Le [métier] qui [action] gagne toujours contre celui qui [action opposée].` | TOFU | NEUTRE | 0 |
| L10 | `Question pour les [cible] : comment gérez-vous [problème] ? (je partage la mienne ↓)` | TOFU | NEUTRE | 0 |

## Facebook

| # | Structure [placeholder] | Funnel | Tag | Usage |
|---|---|---|---|---|
| F1 | `[Ville/quartier] : [nouveauté locale concrète] 👇` | TOFU | NEUTRE | 0 |
| F2 | `On a testé [chose] pour vous. Verdict :` | TOFU | NEUTRE | 0 |
| F3 | `[Jour], c'est [offre/événement]. Qui vient ?` | MOFU | NEUTRE | 0 |
| F4 | `Petit rappel utile pour [cible locale] :` | TOFU | NEUTRE | 0 |
| F5 | `Merci à [nombre] d'entre vous pour [action] — voici la suite.` | BOFU | NEUTRE | 0 |
| F6 | `Avant / après : [transformation en une image].` | MOFU | NEUTRE | 0 |
| F7 | `[Question simple à réponse en commentaire] ?` | TOFU | NEUTRE | 0 |
| F8 | `Nouveau chez [marque] : [bénéfice en 5 mots].` | MOFU | NEUTRE | 0 |

## Instagram

| # | Structure [placeholder] (≤125 car. pour le feed) | Funnel | Tag | Usage |
|---|---|---|---|---|
| I1 | `Enregistre ce post si tu [objectif].` | MOFU | NEUTRE | 0 |
| I2 | `[N] façons de [résultat] (swipe →)` | MOFU | NEUTRE | 0 |
| I3 | `Personne ne te dit ça sur [sujet].` | TOFU | NEUTRE | 0 |
| I4 | `POV : tu viens de découvrir [astuce].` | TOFU | NEUTRE | 0 |
| I5 | `Le secret de [résultat] tient en [N] slides.` | MOFU | NEUTRE | 0 |
| I6 | `Arrête de faire ça ❌ → fais plutôt ça ✅` | TOFU | NEUTRE | 0 |
| I7 | `[Chiffre] avant / [chiffre] après. Voici comment.` | BOFU | NEUTRE | 0 |
| I8 | `Sauvegarde pour plus tard : [ressource].` | MOFU | NEUTRE | 0 |

## TikTok (hook verbal + visuel < 3 s)

| # | Structure [placeholder] | Funnel | Tag | Usage |
|---|---|---|---|---|
| T1 | `[Affirmation choc]. Reste, je t'explique.` | TOFU | NEUTRE | 0 |
| T2 | `Tu fais [action banale] ? Tu perds [conséquence].` | TOFU | NEUTRE | 0 |
| T3 | `Voici ce que personne ne montre sur [coulisses].` | TOFU | NEUTRE | 0 |
| T4 | `3 secondes pour changer ta façon de [action].` | TOFU | NEUTRE | 0 |
| T5 | `J'ai testé [chose] pendant [durée]. Résultat inattendu.` | MOFU | NEUTRE | 0 |
| T6 | `Si tu es [cible], arrête tout et regarde ça.` | TOFU | NEUTRE | 0 |
| T7 | `La vérité sur [sujet] que [autorité] ne dit pas.` | TOFU | NEUTRE | 0 |
| T8 | `Étape 1 pour [résultat] (partie 1/[N]).` | MOFU | NEUTRE | 0 |

> Ajout de hooks : garder la forme **[placeholder] générique** ; ne jamais coller un hook
> réel d'un créateur. La colonne **Tag**/**Usage** est mise à jour par `score_hooks.py`
> (CW4) — ne pas éditer à la main les scores.
