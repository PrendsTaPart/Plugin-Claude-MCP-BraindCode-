# Rapport — export marketplace de prompts

**Total : 770 entrées** (cible : 1000).
> ⚠️ **230 sous la cible.** Voir « Ce qui manque » ci-dessous — aucune entrée n'a été gonflée artificiellement.

## Par type

| Type | Entrées |
|---|---|
| skill | 606 |
| agent | 114 |
| routine | 50 |

## Par profil

| Profil | Entrées |
|---|---|
| tous | 496 |
| fondateur | 226 |
| restaurateur | 48 |

## Par niveau d'autonomie

| Niveau | Entrées |
|---|---|
| 0 | 444 |
| 1 | 158 |
| 2 | 168 |

## Par MCP requis

| MCP | Entrées citant ce MCP |
|---|---|
| rapidocrm | 666 |
| rapidocms | 633 |
| rapidorh | 445 |
| foodeatup | 283 |
| lovable | 187 |
| facebook-ads | 113 |
| n8n | 96 |
| google-calendar | 92 |
| canva | 79 |
| gmail | 60 |
| hyperframes | 45 |
| huggsfield | 44 |
| dataforseo | 32 |
| analytics | 32 |
| stripe | 32 |
| gsc | 25 |
| google-drive | 9 |
| google-ads | 7 |
| tiktok-ads | 6 |

## Détail de la moisson

- Skills — phrases entre guillemets : **257**
- Skills — prompt « besoin » synthétisé : **278**
- Skills — repli générique (ni guillemet ni clause) : **71**
- Agents moissonnés (×3 prompts) : **38**
- Routines moissonnées (×2 prompts) : **25**
- Fusion `data/prompts-orchestrations.json` : **absent** → 0 entrée(s) ajoutée(s)

## Ce qui manque pour atteindre 1000 (à produire côté source, pas à gonfler)

- **`data/prompts-orchestrations.json` non fourni.** C'est la brique « orchestrations + sessions » écrite à la main (§4 de la mission). Elle doit apporter le complément (~230 entrées) : scénarios multi-skills, playbooks de session, parcours guidés par profil.
- **Skills sans phrase déclencheuse explicite** : sur les 385 skills, seuls 257 déclencheurs « … » ont été trouvés dans les frontmatters. Ajouter 2–3 exemples de formulation utilisateur « … » dans le `description` des skills qui n'en ont pas multiplierait la moisson.
- **Variantes par profil** : chaque prompt pourrait être décliné restaurateur / fondateur / marketeur (×2–3) une fois les KB de profil définies — non fait ici car ce serait une duplication mécanique, pas du contenu réel.
- **Orchestrations inter-plugins** : les enchaînements documentés (routines → skills → agents) peuvent devenir des prompts « parcours », à écrire explicitement dans le fichier de fusion.

