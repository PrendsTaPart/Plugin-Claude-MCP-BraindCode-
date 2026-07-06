# Notes de release — v1.0.0 (2026-07-06)

Première version publique de la **marketplace Rapido** : des plugins Claude
Code pour piloter une entreprise via les systèmes Rapido (FoodEatUp,
RapidoCRM, RapidoCMS, RapidoRh) et leurs outils satellites (Canva, Lovable,
Meta Ads, n8n, Google Workspace).

## En chiffres

- **10 plugins** (tous en 1.0.0), **108 skills**, **14 agents** (personas).
- **8 plugins avec hooks** déterministes — 13 scripts de garde testés
  fonctionnellement sur stdin, plus des hooks Stop (récapitulatif exigé) et
  SessionStart (détection de la KB).
- 40 des 108 skills importés de 4 dépôts open source, attribués et licenciés.
- 2 scripts de validation stdlib + une CI GitHub Actions qui les rejoue.

## Les 5 points forts

1. **Garde-fous déterministes** — indépendants du modèle : confirmation
   forcée sur le destructif et les dépenses réelles (Meta Ads), refus pur des
   patterns interdits (transitions de facture hors DGFiP, températures
   invraisemblables, budgets au-delà du plafond maison), mode production n8n
   verrouillé — y compris quand le paramètre est absent.
2. **Base de connaissance `./rapido-kb/`** — construite par l'onboarding dans
   le répertoire de travail du CLIENT (jamais dans les plugins) : seuils,
   charte, personas et ton PRIMENT partout sur les défauts secteur ; le dépôt
   reste un produit portable, sans aucune donnée client.
3. **Dossier startup 360** (`rapido-suite`) — la mémoire de l'entreprise en
   8 fichiers (vision, persona, marché, offre, identité, traction, pitch,
   roadmap) que tous les agents lisent avant de produire, avec chiffres
   sourcés MCP et publication CMS/RH.
4. **Skills tiers attribués** — 40 skills d'anthropics/knowledge-work-plugins,
   anthropics/skills, wondelai/skills et nextlevelbuilder : LICENSE dans
   chaque dossier, ATTRIBUTIONS.md par plugin, clé `source:` dans chaque
   frontmatter, descriptions francisées pour le déclenchement, corps
   originaux intacts.
5. **CI de validation** (`.github/workflows/validation.yml`) — à chaque push
   et pull request : validation structurelle, batterie de tests
   skills/agents/hooks (0 FAIL, 0 WARN exigés), compilation de tous les .py,
   `bash -n` de tous les .sh — sans aucune dépendance pip (100 % stdlib).

## Limites connues

- **`N8N_MCP_URL` requise** pour `rapido-n8n` et le volet automatisations de
  `rapido-direction` (URL du serveur MCP de votre instance n8n). Sans elle,
  dégradation propre. Les comptes tiers (Canva, Lovable, Meta Ads,
  HyperFrames, Google) s'authentifient via leurs connecteurs/OAuth.
- **Endpoints Google à confirmer** : les URLs des serveurs MCP Gmail /
  Calendar / Drive de `rapido-direction/.mcp.json`
  (`https://mcp.{gmail,calendar,drive}.googleapis.com/mcp`) restent à
  vérifier contre la documentation officielle des connecteurs — le
  README-installation du plugin le signale aussi.
- **67 outils MCP « à vérifier en ligne »** : les catalogues facebook-ads,
  n8n et Google vivent sur les serveurs distants — checklist manuelle avant
  usage intensif dans `tests/rapports/outils-a-verifier-en-ligne.md`.
- Le contenu des 40 skills tiers reste en anglais (seules leurs descriptions
  de déclenchement sont francisées).

## Contribuer

Conventions, structure d'un skill/plugin, principe anti-donnée-inventée et
validation obligatoire avant PR : voir [CONTRIBUTING.md](CONTRIBUTING.md).
Sécurité et signalement de vulnérabilité : [SECURITY.md](SECURITY.md).
Licence : [Apache 2.0](LICENSE).
