# planit

**Pilote Plan'It de bout en bout** depuis Claude Code : tâches, routines,
calendrier, boucles routine ↔ KPI (loop engineering), widgets de l'accueil,
alertes, crédits, connecteurs MCP, routines sur événement, prompts,
catalogue privé de plugins et vidéos courtes. Serveur :
`https://planit.braindcode.com/mcp` (63 outils relevés en live, dont 10
destructifs).

## Les règles de coût et de décision (le contrat du plugin)

- **Tout coût s'annonce AVANT** : `estimate_routine_cost` avant tout
  lancement, acceptation ou changement de fréquence ; `list_kpi_catalog`
  avant tout widget ; vidéo = max(5, ⌈durée/2⌉) crédits, calculée par
  script. Le hook garde-cout-annonce REFUSE une exécution sans estimation
  dans la session.
- **Propositions d'abord** : `propose_routine` et
  `propose_routine_improvement` enregistrent sans créer ; accept/apply
  n'arrivent qu'après l'accord explicite sur CETTE proposition ; un refus
  est définitif à l'identique.
- **Les 10 destructifs du serveur** (delete, pause/resume/run, accept/apply,
  remove, unsubscribe) + les payants + ceux qui tranchent (alerte, refus)
  passent par une confirmation humaine — les champs posés par le modèle ne
  valent jamais confirmation.
- **Vérité des données** : aucun effet annoncé sur `not_enough_data`
  (3 exécutions ET 14 jours minimum), une valeur `throttled` se dit « pas
  fraîche » avec son âge, flat_price/default ne sont pas des mesures —
  un hook PostToolUse le rappelle à chaque occurrence.
- **Jamais de pause de notre initiative** : une routine qui échoue ou coûte
  reçoit d'abord une proposition d'amélioration.

## Journée type

| Moment | Commande | Ce qui se passe |
|---|---|---|
| Ouverture | `/planit` | crédits, autonomie, widgets, boucles, alertes + 3 décisions à prendre |
| Planning | `/calendrier` | la plage demandée (≤ 62 j), états réels, chevauchements |
| Conception | `/routine-nouvelle` | la chaîne de l'Architecte jusqu'à la proposition |
| Mesure | `/boucles`, `/widgets` | verdicts des boucles, widgets posés au bon type |
| Comptes | `/credits` | consommation par routine, classement, jours d'autonomie (formules) |
| Écosystème | `/connecteurs`, `/evenements`, `/catalogue-prive` | état réel, abonnements, propositions privées |
| Vendredi | `/vendredi` puis `/audit-routines` | verdicts, une amélioration par routine qui stagne, décisions listées |

## Phrases d'exemple

« Où en est mon Plan'It ? » · « Mets en place une routine qui prépare mes
posts chaque lundi » · « Est-ce que ma routine veille sert à quelque
chose ? » · « Combien me coûtent mes routines, il me reste combien de
jours ? » · « Quand je reçois un e-mail de prospect, propose la routine de
réponse » · « Exporte le plugin rapidocrm vers Plan'It ».

## Articulation avec les autres plugins

`rapido-suite`, `rapido-startup` et `rapido-employe` CONÇOIVENT des routines
métier (Loop Engine, cadre Academy) ; **ce plugin est leur exécutant
Plan'It** : il les installe (`installer-une-routine-du-registre`), les
mesure (boucles KPI), les améliore (audit) — il ne recopie pas leurs skills.
`rapido-n8n` exécute côté n8n ; les vidéos partent en brouillon via
`rapidocms`.

## État des connecteurs (relevé du 2026-10-25 — à relire à chaque séance)

Connectés : Gmail (62 outils), Plan'It natif (63), RapidoCMS (45),
RapidoRH (22). **FoodEatUp : jeton expiré depuis juillet** ; **RapidoCRM :
déconnecté** — toute routine qui s'y appuie sera refusée par le serveur ;
reconnexion dans l'écran Connecteurs de l'application.

## Installation

```
/plugin marketplace add PrendsTaPart/Plugin-Claude-MCP-BraindCode-
/plugin install planit@rapido
```

Aucun secret dans le dépôt : l'authentification Plan'It est l'OAuth du
premier appel ; les connecteurs s'authentifient dans l'application.
