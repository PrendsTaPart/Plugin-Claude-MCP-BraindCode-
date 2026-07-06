# Sécurité

## Ce qu'installe réellement un plugin

Un plugin de cette marketplace **exécute du code** (hooks, scripts de calcul)
et **appelle des outils MCP avec les privilèges du compte connecté**
(FoodEatUp, RapidoCRM, RapidoCMS, RapidoRh, Canva, Lovable, Meta Ads, n8n,
Google). Installer un plugin, c'est lui confier ces accès : n'installez que
depuis ce dépôt (ou votre fork audité), et relisez le diff à chaque mise à
jour si vous êtes votre propre distributeur.

## Les hooks de garde ne se contournent JAMAIS

Les garde-fous déterministes du dépôt (`<plugin>/hooks/`) sont la dernière
ligne de défense, indépendante du modèle : `garde-destructif` (suppressions,
transitions de facture hors DGFiP), `anti-donnee-inventee` (valeurs
invraisemblables), `garde-argent-reel` et `plafond-budget` (dépenses Meta
Ads), `garde-production` (workflows n8n), `garde-irreversible` (Gmail, Drive,
Calendar).

- Ne désactivez pas un hook, ne l'éditez pas pour « faire passer » un cas, ne
  demandez pas au modèle de le contourner : si un hook bloque à tort, ouvrez
  une issue.
- Toute pull request qui affaiblit un hook (pattern retiré, `deny` transformé
  en `allow`, plafond ignoré) est refusée — voir
  [CONTRIBUTING.md](CONTRIBUTING.md).
- Les hooks sont sans appel réseau et testés : toute modification doit le
  rester et fournir ses cas de test.

## Données et secrets

- **Jamais de secrets dans le dépôt** (skills, `reference/`, hooks — tout est
  distribué avec le plugin). Les authentifications passent par les connecteurs
  MCP et OAuth individuels.
- `./rapido-kb/` (données du client) vit dans le répertoire de travail du
  client et n'est **jamais versionnée ici** (voir `.gitignore`).

## Signaler une vulnérabilité

Écrivez en privé à **contact@braindcode.com** (objet : `[SECURITY] …`) —
n'ouvrez PAS d'issue publique pour une faille exploitable. Décrivez le
scénario (plugin, skill/hook concerné, étapes de reproduction, impact) ; nous
accusons réception et vous tenons informé de la correction. Merci de laisser
un délai raisonnable de correction avant toute divulgation publique.
