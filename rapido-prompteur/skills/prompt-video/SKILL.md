---
name: prompt-video
description: >-
  Utiliser quand l'utilisateur veut un PROMPT vidéo (pas la vidéo elle-même) — « prompt
  vidéo », « prompt pour une pub produit », « prompt explainer », « prompt scène
  personnage », « prompt UGC ». Construit un prompt vidéo PAR USAGE (pub / explainer /
  personnage) + un brief de production, impose le préflight coût, puis ROUTE vers
  l'exécution. Le prompteur prompte, il ne dépense pas. Pour produire : rapido-higgsfield:
  usine-video-marketing ou videos-explicatives. Pour un prompt image : prompt-image.
---

# Prompt vidéo — par usage, coût d'abord, jamais de génération

Ce skill **écrit le prompt vidéo + le brief de production** et **route** vers
l'exécution ; il **ne génère jamais** (« le prompteur prompte, il ne dépense pas »).

## Étape 0 — charte, patterns, garde-fous (obligatoire)

- **Charte** : `get_brand` + `./rapido-kb/charte-graphique.md` (couleurs, ton). Manque →
  le signaler, ne rien inventer.
- `${CLAUDE_PLUGIN_ROOT}/reference/grammaire-des-moteurs.md`, `reference/ip-a-risque.md`
  (aucune IP tierce, aucun artiste/réalisateur vivant nommé dans le prompt),
  `reference/regles-de-construction.md`.

## 1. Choisir l'usage → le pattern

| Usage | Pattern (`assets/patterns/`) |
|---|---|
| Pub produit / UGC | `ugc-ad.md` + budget du hook `hooks-viraux.md` |
| Explainer / pédagogique | structure « format × objectif » (`cinematique.md`) |
| Scène personnage cohérent | `personnage.md` → déléguer au skill `prompt-personnage` |

Construire le prompt par **plans** (accroche, corps, CTA), avec durée du hook, ambiance
= **charte**, et **négatifs**. Zéro IP tierce (`ip-a-risque.md`).

## 2. Préflight coût — OBLIGATOIRE (jamais de dépense ici)

Avant toute production, **estimer le coût** via `rapido-higgsfield:gouvernance-credits`
(marqueur préflight). Le prompteur **affiche le coût chiffré**, il ne le **dépense pas** :
la décision et l'appel payant appartiennent au skill exécutant, sur confirmation.

## 3. Sortie = prompt + brief de production, puis router

Livrable : le **prompt** + un **brief de production** (plans, durée, format, voix/musique
si besoin — musique = registre autorisé, cf. `rapido-video`). Router :

| Besoin | Route (exécution, coût confirmé) |
|---|---|
| Pub / UGC / vidéo de marque | `rapido-higgsfield:usine-video-marketing` |
| Explainer / pédagogique | `rapido-higgsfield:videos-explicatives` |
| Montage libre / sous-titres | `rapido-video:montage-express` |
| Personnage récurrent | `prompt-personnage` |

## Articulation

`prompt-video` = **écrit le prompt + le brief** et impose le coût ; les skills d'exécution
de rapido-higgsfield (`usine-video-marketing`, `videos-explicatives`) **produisent**
(dépense confirmée). Aucun doublon : ici on **cadre**, là-bas on **exécute**.

## Sources

Patterns francisés (`assets/patterns/`) distillés du dépôt **MIT** rediumvex (découpe
format × objectif, budget du hook) — **structures uniquement**, aucun texte (cf. `NOTICE.md`).

## Pièges

- **Ne jamais générer ici** ni décider la dépense : préflight coût **obligatoire**, appel
  payant délégué.
- **Zéro IP tierce / réalisateur ou artiste vivant** dans le prompt (`ip-a-risque.md`).
- **Charte avant tout** ; musique = **registre autorisé** uniquement.
