# Rapport — export marketplace de prompts

**Total : 816 entrées** (cible : 1000).
> ⚠️ **184 sous la cible.** Voir « Ce qui manque » ci-dessous — aucune entrée n'a été gonflée artificiellement.

## Par type

| Type | Entrées |
|---|---|
| skill | 633 |
| agent | 114 |
| routine | 52 |
| orchestration | 15 |
| session | 2 |

## Par profil

| Profil | Entrées |
|---|---|
| tous | 496 |
| fondateur | 226 |
| restaurateur | 48 |
| editeur-saas | 46 |

## Par niveau d'autonomie

| Niveau | Entrées |
|---|---|
| 0 | 459 |
| 1 | 174 |
| 2 | 183 |

## Par MCP requis

| MCP | Entrées citant ce MCP |
|---|---|
| rapidocrm | 697 |
| rapidocms | 637 |
| rapidorh | 447 |
| foodeatup | 286 |
| lovable | 189 |
| facebook-ads | 115 |
| n8n | 97 |
| google-calendar | 92 |
| canva | 80 |
| gmail | 61 |
| huggsfield | 45 |
| hyperframes | 45 |
| dataforseo | 32 |
| analytics | 32 |
| stripe | 32 |
| gsc | 25 |
| google-drive | 9 |
| google-ads | 7 |
| tiktok-ads | 6 |
| web | 2 |
| fireflies | 1 |

## Détail de la moisson

- Skills — phrases entre guillemets : **257**
- Skills — prompt « besoin » synthétisé : **278**
- Skills — repli générique (ni guillemet ni clause) : **71**
- Agents moissonnés (×3 prompts) : **38**
- Routines moissonnées (×2 prompts) : **25**
- **Fusion sources écrites main** → 46 entrée(s) ajoutée(s) :
    - `orchestrations-main` : **absent** → 0
    - `collection:vente-saas` : **chargé** → 46

## Ce qui manque pour atteindre 1000 (à produire côté source, pas à gonfler)

- **`data/prompts-orchestrations.json` non fourni.** C'est la brique « orchestrations + sessions » écrite à la main (§4 de la mission). Elle apportera un complément une fois rédigée : scénarios multi-skills, playbooks de session, parcours guidés par profil.
- **Collections restantes** : 1 collection(s) fournie(s) (vente-saas). Les 3 autres annoncées (routines, boucles, sessions-loop) restent à déposer dans `data/prompts-collections/` pour compléter les 139 attendues.
- **Skills sans phrase déclencheuse explicite** : sur les 385 skills, seuls 257 déclencheurs « … » ont été trouvés dans les frontmatters. Ajouter 2–3 exemples de formulation utilisateur « … » dans le `description` des skills qui n'en ont pas multiplierait la moisson.
- **Variantes par profil** : chaque prompt pourrait être décliné restaurateur / fondateur / marketeur (×2–3) une fois les KB de profil définies — non fait ici car ce serait une duplication mécanique, pas du contenu réel.
- **Orchestrations inter-plugins** : les enchaînements documentés (routines → skills → agents) peuvent devenir des prompts « parcours », à écrire explicitement dans le fichier de fusion.

