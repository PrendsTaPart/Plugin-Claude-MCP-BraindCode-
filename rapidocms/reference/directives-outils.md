# Directives communes d'utilisation des outils (rapidocms)

Règles applicables à TOUTE exécution de skill de ce plugin.

## 1. Résolution d'ID d'abord

- Ne JAMAIS deviner un ID : `account_id` (= `page_id`, `profile_id` ou `open_id`
  selon le réseau), `draft_id`, `post_id`, `campagne_id`, `card_id`, `page_id` de
  carte, `template_id`…
- Récupérer chaque ID via l'outil de liste correspondant
  (`list_connected_accounts`, `list_drafts_tool`, `list_scheduled_posts`,
  `list_campagnes`, `list_digital_card`, `list_card_page`,
  `list_card_templates`…) ou le demander à l'utilisateur, AVANT d'agir.
- Le contexte société/utilisateur est déduit de la session authentifiée.

## 2. Confirmation avant action destructrice ou irréversible

Récapituler l'action et obtenir un accord explicite de l'utilisateur avant :
- toute suppression (`delete_campagne`, `delete_digital_card`,
  `delete_card_page_link`, `delete_draft_tool`, `delete_prompt`,
  `remove_post_campagne`) ;
- toute planification/publication (`schedule_draft_tool`) et toute annulation de
  publication programmée (`cancel_schedules_post`) ;
- valider le contenu (texte + visuel) AVANT de planifier — jamais de visuel
  généré publié sans validation.

## 3. Ne jamais inventer de données

Dates/heures de publication, comptes cibles, textes validés : toujours fournis ou
confirmés par l'utilisateur. Couleurs et logos : valeurs exactes de la marque
(voir charte-graphique.md), pas d'approximation.

## 4. Locale et formats

- Dates ISO `YYYY-MM-DD` en général ; ATTENTION aux formats STRICTS de
  `schedule_draft_tool` : `post_date` = `Y-m-d`, `post_heure` = `H-i-s`
  (ex. `18-30-00`, avec tirets).
- `create_draft_tool` : tous les champs requis même en post texte ;
  `media_source` vaut toujours `"biblio"`.
- `post_insights` : 10 posts maximum par appel — découper au-delà.
- L'outil d'insights de campagne s'écrit `ingishts_campagne` (orthographe du
  serveur) — ne pas « corriger » son nom.

## 5. Gestion d'erreur

Si un outil échoue : expliquer clairement la cause probable, ne PAS boucler ni
réessayer aveuglément, proposer l'alternative manuelle (ex. planifier depuis
l'interface RapidoCMS).

## 6. Récapitulatif de fin de séquence

Terminer chaque séquence par la liste des objets créés/modifiés avec leurs IDs
(brouillons, posts programmés avec date/heure/réseau, campagnes, cartes, pages,
liens).
