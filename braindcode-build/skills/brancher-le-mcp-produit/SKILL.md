---
name: brancher-le-mcp-produit
description: Utiliser quand l'app Lovable doit parler au MCP produit — « branche FoodEatUp dans l'app », « connecte le MCP RapidoCRM côté serveur », « mets l'auth du connecteur ». Modèle « Connexion MCP + auth », lien profond du tableau de bord, audit du code - rien au navigateur.
---

# Brancher le MCP produit (côté serveur, rien au navigateur)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/regles-lovable.md` (règle n° 3) —
  critère Build n° 3 : AUCUN credential MCP n'atteint le navigateur.

## Démarche
1. **Le modèle officiel** : `list_prompt_templates` → le modèle
   « Connexion MCP + auth » (le lire avec include_body sur CE modèle
   seulement) — c'est lui qui cadre le prompt Lovable.
2. **Côté Lovable** : `list_custom_connectors` (ce qui existe déjà), puis
   `add_connector` — il renvoie un LIEN PROFOND vers le tableau de bord :
   c'est l'humain qui y finit la connexion. En parallèle,
   `request_human_validation` de kind oauth ou api_key côté Build, suivie
   dans `get_pending_validations`.
3. **Le prompt Lovable** (send_message, dans une carte ouverte) impose :
   appel du MCP côté serveur UNIQUEMENT (edge function ou connecteur),
   scope verrouillé aux outils du cahier des charges, journaux masqués,
   gestion du jeton expiré.
4. **Vérifier le code** : `get_diff` et `read_file` — aucun jeton, aucune
   clé de service, aucune variable d'environnement front porteuse de
   secret (le hook audit-credentials-front signale ; le correctif passe
   AVANT la clôture de la carte).
5. **Clore** : `complete_prompt_step` avec needs_review (étape sensible),
   `save_project_progress`.

## Délégation
Le kit connecteur MCP côté serveur du plugin rapido-lovable fait foi s'il
est installé : ce skill l'applique au chantier Build, il ne le réécrit pas.

## Pièges
- Un connecteur « ajouté » par add_connector n'est PAS connecté : sans le
  passage humain par le tableau de bord, les appels échoueront.
- Tester avec un vrai jeton collé dans le chat : jamais (hook anti-secret).

## Dégradation propre
Connexion refusée ou OAuth en échec : `report_blocker` factuel, et l'app
continue sur les écrans indépendants du MCP.
