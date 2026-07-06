# Politique d'autonomie (rapido-suite)

Ce plugin orchestre 4 serveurs MCP. Le niveau d'autonomie dépend du type
d'action, pas du contexte de la conversation.

## Lecture — autonomie totale

Les outils de lecture (`list_*`, `get_*`, `search_*`, insights, dashboards,
`finance_summary`, `floor_plan_status`…) s'appellent librement, sans demander :
c'est le carburant des diagnostics. Toujours la même période quand on compare
plusieurs serveurs.

## Écriture — confirmation PAR SYSTÈME

- Avant la PREMIÈRE écriture dans un serveur donné (CRM, CMS, RH ou FoodEatUp)
  au cours d'un workflow : récapituler ce qui va être créé/modifié dans CE
  serveur et obtenir l'accord de l'utilisateur.
- Un accord vaut pour le serveur concerné et le lot annoncé — pas pour le
  serveur suivant, pas pour un lot élargi.
- Jamais deux serveurs modifiés sur une seule validation globale.

## Actions destructrices ou irréversibles — confirmation UNITAIRE

Suppressions, annulations de publication, envois (email/SMS/newsletter),
lancements de campagne, changements de statut légal de facture : une
confirmation explicite PAR action, même si le serveur a déjà été validé.
(Les hooks du plugin forcent par ailleurs cette confirmation côté outillage.)

## En cas d'échec en cours de workflow transverse

S'arrêter à l'étape en échec. Lister ce qui a déjà été créé dans les serveurs
précédents (avec IDs). Ne jamais tenter de retour arrière silencieux ; proposer
les options à l'utilisateur.

## Fin de séquence

Récapitulatif PAR SERVEUR des objets créés/modifiés avec leurs IDs, plus ce qui
a été volontairement sauté et pourquoi.
