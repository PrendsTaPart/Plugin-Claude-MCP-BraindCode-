# Les chaînes de l'écosystème — rôles et kits de marque

Relevé du propriétaire, 2026-10-25 : **4 chaînes connectées**. AUCUN
identifiant n'est codé en dur ici — `yt_list_channels` et
`yt_get_channel_status` font foi à chaque session, et chaque kit de marque
se lit en direct par `yt_list_brand_kits`. Il n'existe PAS de chaîne
RapidoRH : les vidéos de l'académie RapidoRH partent sur la chaîne que
l'humain désigne.

| Chaîne | Rôle éditorial | Sources de contenu | Kit de marque |
|---|---|---|---|
| **FoodEatUp** | Tutoriels du logiciel FoodEatUp, parcours métiers, offres | serveur foodeatup-tutoriel (fiches, transcriptions, vignettes, liens tutoriel.foodeatup.com) | kit FoodEatUp lu en direct + gabarit miniature tutos (reference/gabarit-miniatures-tutos-foodeatup.md) |
| **RapidoCMS** | Tutoriels et démos RapidoCMS | académie RapidoCMS (rapidocms-tuto) — les liens YouTube s'y enregistrent en retour avec enregistrer_youtube, sur accord | kit RapidoCMS lu en direct |
| **RapidoCRM** | Tutoriels et démos RapidoCRM | contenus CRM (l'académie RapidoRH tuto n'a pas de chaîne propre : affectation décidée par l'humain) | kit RapidoCRM lu en direct |
| **Formation Braindcode** | Formations, épisodes et BD verticales de l'Academy en Shorts | academy (get_formation_comic, list_media_resources) ; vidéos Plan'It via planit-tutoriel | kit Braindcode lu en direct |

Au relevé : **FoodEatUp est à la fois active et favorite** — c'est la
cible par défaut de toute publication sans channel_id. La règle du plugin
reste : channel_id EXPLICITE et nom de la chaîne annoncé avant chaque
écriture (hook garde-chaine).
