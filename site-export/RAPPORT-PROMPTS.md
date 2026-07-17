# Rapport — export marketplace de prompts

**Total : 878 entrées** (cible : 1000).
> ⚠️ **122 sous la cible.** Voir « Ce qui manque » ci-dessous — aucune entrée n'a été gonflée artificiellement.

## Par type

| Type | Entrées |
|---|---|
| skill | 641 |
| agent | 114 |
| routine | 90 |
| boucle | 16 |
| orchestration | 15 |
| session | 2 |

## Par profil

| Profil | Entrées |
|---|---|
| tous | 500 |
| fondateur | 273 |
| restaurateur | 59 |
| editeur-saas | 46 |

## Par niveau d'autonomie

| Niveau | Entrées |
|---|---|
| 0 | 482 |
| 1 | 195 |
| 2 | 201 |

## Par MCP requis

| MCP | Entrées citant ce MCP |
|---|---|
| rapidocrm | 720 |
| rapidocms | 649 |
| rapidorh | 463 |
| foodeatup | 303 |
| lovable | 189 |
| facebook-ads | 119 |
| n8n | 98 |
| google-calendar | 96 |
| canva | 80 |
| gmail | 61 |
| huggsfield | 46 |
| hyperframes | 45 |
| stripe | 36 |
| dataforseo | 32 |
| analytics | 32 |
| gsc | 25 |
| google-ads | 10 |
| google-drive | 9 |
| tiktok-ads | 9 |
| web | 2 |
| fireflies | 1 |

## Détail de la moisson

- Skills — phrases entre guillemets : **264**
- Skills — prompt « besoin » synthétisé : **279**
- Skills — repli générique (ni guillemet ni clause) : **71**
- Agents moissonnés (×3 prompts) : **38**
- Routines moissonnées (×2 prompts) : **25**
- **Fusion sources écrites main** → 100 entrée(s) ajoutée(s) :
    - `orchestrations-main` : **absent** → 0
    - `collection:boucles` : **chargé** → 16
    - `collection:routines` : **chargé** → 38
    - `collection:vente-saas` : **chargé** → 46

## Ce qui manque pour atteindre 1000 (à produire côté source, pas à gonfler)

- **`data/prompts-orchestrations.json` non fourni.** C'est la brique « orchestrations + sessions » écrite à la main (§4 de la mission). Elle apportera un complément une fois rédigée : scénarios multi-skills, playbooks de session, parcours guidés par profil.
- **Collections restantes** : 3 collection(s) fournie(s) (boucles, routines, vente-saas). Les 3 autres annoncées (routines, boucles, sessions-loop) restent à déposer dans `data/prompts-collections/` pour compléter les 139 attendues.
- **Skills sans phrase déclencheuse explicite** : sur les 385 skills, seuls 264 déclencheurs « … » ont été trouvés dans les frontmatters. Ajouter 2–3 exemples de formulation utilisateur « … » dans le `description` des skills qui n'en ont pas multiplierait la moisson.
- **Variantes par profil** : chaque prompt pourrait être décliné restaurateur / fondateur / marketeur (×2–3) une fois les KB de profil définies — non fait ici car ce serait une duplication mécanique, pas du contenu réel.
- **Orchestrations inter-plugins** : les enchaînements documentés (routines → skills → agents) peuvent devenir des prompts « parcours », à écrire explicitement dans le fichier de fusion.

