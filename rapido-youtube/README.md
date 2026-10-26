# rapido-youtube

**Toute la vie des chaînes YouTube de l'écosystème depuis Claude Code**,
au-dessus du serveur MCP Rapido YouTube (« YouTube Publisher Bot ») :
veille et outliers, idées, mots-clés, titres, descriptions et SEO,
atelier de miniatures, publication et planification **sous contrôle du
quota**, autopilote, Shorts tirés des vidéos longues, distribution
multi-plateformes, tests A/B de miniatures, analytics et rapports,
corrections en lot, commentaires, bibliothèque de prompts. Serveur :
`https://youtube.rapidocms.com/mcp` (86 outils officiels `yt_`, OAuth au
premier appel — aucun jeton dans le dépôt). Quatre chaînes : FoodEatUp,
RapidoCMS, RapidoCRM, Formation Braindcode.

## La règle n° 1 : les noms d'outils

Le serveur expose chaque outil DEUX fois : le nom officiel `yt_…` et un
alias déprécié sans préfixe, **retiré le 2026-12-31**. Ce plugin n'utilise
que les noms `yt_` — la CI fait échouer toute citation d'un alias, et un
hook refuse leur appel en donnant le bon nom.

## Le contrat du plugin

- **Le quota se lit avant d'agir** : quota du jour, part réservée aux
  publications sous 24 h, DISPONIBLE RÉEL, risque — le hook garde-quota
  refuse tout envoi sans lecture < 30 min ou sur `will_fail`, et
  questionne sur `tight`.
- **La chaîne est toujours nommée** : channel_id explicite sur chaque
  écriture, bascules active/favorite sur accord.
- **Les crédits s'annoncent** : barème LU sur le serveur, 1 variation
  puis analyse gratuite, seuil de session dans `./rapido-kb/youtube.md`.
- **Le public attend l'accord** : privacy private par défaut, réponses
  aux commentaires une à une, A/B, cross-post, rapports partageables et
  prompts publics sous question.
- **Les lots s'aperçoivent d'abord** : preview_only / dry_run
  obligatoires (hook), mêmes vidéos, même recherche.
- **Les visages sont verrouillés** : uniquement les modèles de visage de
  l'utilisateur, relevés dans la session.
- **Les champs confirm et dry_run posés par le modèle ne valent jamais
  confirmation humaine.**

## Chaîne de travail complète

| Étape | Commande | Ce qui se passe |
|---|---|---|
| Point du jour | `/youtube`, `/quota` | chaîne, quota et risque, crédits, planning, échecs, 3 priorités |
| Inspiration | `/veille`, `/idees` | outliers filtrés, motifs, idées — on s'inspire, on ne copie pas |
| Contenu | `/miniature` + skill titre-description-seo | mots-clés FR, titres (estimations), description chaptée, SEO noté |
| Mise en ligne | `/publier`, `/planning`, `/autopilote` | quota lu, privacy prudente, idempotence, grille lue avant remplacement |
| Déclinaison | `/shorts`, `/distribuer` | clips asynchrones, rendu dans l'app, comptes connectés vérifiés |
| Mesure | `/ab-test`, `/stats` | verdicts exacts (95 % / 100 impressions), analytics tels que servis |
| Entretien | `/audit`, `/commentaires`, `/reprise` | lots après aperçu, réponses relues, réarmements respectés |
| Interconnexions | `/tutos-foodeatup` + skill academies-et-formations | tutoriels lus aux serveurs sources, liens rendus en tableau, Shorts Academy sur Formation Braindcode |

## Phrases d'exemple

« Où en sont mes chaînes YouTube ? » · « Trouve les outliers de la
semaine » · « Génère la miniature au gabarit FoodEatUp — annonce le
coût » · « Publie en non répertorié sur la chaîne RapidoCMS » · « Quels
clips dans ce tuto ? » · « Lance l'A/B sur cette vidéo » · « Corrige les
descriptions des 200 vidéos — montre l'aperçu d'abord ».

## Quota et crédits (l'état du relevé du 2026-10-25)

Risque **will_fail** : 6 400/10 000 unités consommées, 4 800 réservées
aux 3 publications sous 24 h (1 200 au-dessus du plafond), disponible à
la demande ZÉRO — le premier geste utile est la revue du planning
(`/quota` puis `yt_list_schedule`). Crédits : 9 981. Distribution : aucun
compte connecté (page Distribution de l'application).

## Délégations (jamais de recopie)

Montage et transcription → `rapido-video` ; génération média →
`rapido-higgsfield` ; copy multi-réseaux → `rapido-copywriter` ; direction
artistique → `rapido-design` ; publication sociale → `rapidocms` ;
routines → plugin `planit` (coût annoncé, jamais accepté d'office).

## Installation

```
/plugin marketplace add PrendsTaPart/Plugin-Claude-MCP-BraindCode-
/plugin install rapido-youtube@rapido
```

Puis copier `rapido-kb-template/youtube.md` dans `./rapido-kb/` (seuils de
crédits, fenêtre de publication). OAuth au premier appel ; les académies
tuto optionnelles se déclarent par `${RAPIDOCMS_TUTO_MCP_URL}`,
`${RAPIDORH_TUTO_MCP_URL}` et `${PLANIT_TUTORIEL_MCP_URL}`.
