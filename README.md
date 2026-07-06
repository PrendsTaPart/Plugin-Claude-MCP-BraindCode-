# Marketplace Rapido — Plugins Claude Code

Marketplace interne regroupant 7 plugins Claude Code qui packagent des skills
métier par-dessus les serveurs MCP Rapido (FoodEatUp, CRM, CMS, RH), Canva et
Lovable.

## Prérequis

- **Claude Code installé** (CLI, desktop ou web) — voir
  https://code.claude.com/docs
- **Accès aux 4 serveurs MCP** (comptes/session authentifiés) :
  FoodEatUp, RapidoCRM, RapidoCMS, RapidoRh.
- **Si le dépôt est privé** : définir la variable d'environnement `GITHUB_TOKEN`
  (token avec accès en lecture au dépôt) pour que les mises à jour automatiques
  de la marketplace fonctionnent.

## Installation

```
/plugin marketplace add <org>/rapido-plugins
/plugin install foodeatup@rapido
/plugin install rapidocrm@rapido
/plugin install rapidocms@rapido
/plugin install rapidorh@rapido
/plugin install rapido-suite@rapido
/plugin install rapido-canva@rapido
/plugin install rapido-lovable@rapido
/reload-plugins
```

Remplacer `<org>` par l'organisation GitHub qui héberge ce dépôt. Installer
uniquement les plugins dont vous avez besoin — `rapido-suite` suppose l'accès
aux 4 serveurs.

## Les 5 plugins

| Plugin | MCP | À quoi ça sert | Skills principales |
|---|---|---|---|
| `foodeatup` | foodeatup | Gestion restaurant : conformité HACCP, service en salle, recettes & marges, production, réapprovisionnement, carte en ligne, planning, commandes — agents `chef-restaurateur` et `chef-cuisine` | `haccp-conformite-quotidienne`, `service-salle`, `recette-cout-marge`, `production-stock`, `reappro-fournisseurs`, `analyse-rentabilite-carte`, `briefing-du-jour`, `carte-vitrine`, `planning-equipe`, `gestion-commandes` |
| `rapidocrm` | rapidocrm | CRM : prospection & pipeline, campagnes marketing, devis/factures/relances, contrats, agenda/RDV, templates éditeur, communication client, performance commerciale — agents `directeur-commercial` et `sdr-prospection` | `prospection-pipeline`, `campagne-marketing`, `devis-facture-relance`, `communication-client`, `performance-commerciale`, `coaching-pipeline`, `redaction-commerciale`, `contrats-clients`, `agenda-rdv`, `studio-templates` |
| `rapidocms` | rapidocms + hyperframes (HeyGen) | Contenu & réseaux sociaux (Facebook, Instagram, LinkedIn, TikTok), campagnes de posts, vidéos marketing, cartes digitales, conformité de marque — agents `responsable-marketing`, `community-manager`, `directeur-artistique` | `pipeline-contenu-social`, `orchestration-campagne`, `carte-digitale`, `contenu-conforme-marque`, `prompt-engineering-visuel`, `calendrier-editorial`, `analyse-performance-contenu`, `video-marketing` |
| `rapidorh` | rapidorh | RH & projets : setup de projets, Kanban, dailies (rapports journaliers), onboarding des employés — agents `chef-de-projet` et `responsable-rh` | `setup-projet`, `flux-kanban`, `daily-report`, `onboarding-equipe`, `revue-projet-hebdo`, `detection-surcharge` |
| `rapido-suite` | les 4 serveurs | Orchestration transverse : onboarding client de bout en bout (CRM→CMS→RH), revue business hebdomadaire unifiée, comité de direction, base de connaissance entreprise — agent `directeur-general` | `onboarding-client-360`, `revue-hebdo-business`, `comite-de-direction`, `onboarding-entreprise`, `mise-a-jour-kb` |
| `rapido-canva` | canva + les 4 serveurs | Design Canva alimenté par les données Rapido : menus imprimables, visuels sociaux aux formats natifs, propositions/présentations de vente, slides CODIR — agent `studio-creatif` (arbitre image IA / Canva / vidéo / Lovable), règles Canva encodées (`reference/pieges-canva.md`, `CONFORMITE.md`) | `menu-restaurant-design`, `visuels-sociaux-canva`, `supports-commerciaux`, `presentation-codir` |
| `rapido-lovable` | lovable + les 4 serveurs | Apps et agents IA Lovable alimentés par les données Rapido : site restaurant avec réservation connectée, landing pages de campagne, agent IA produit (API Anthropic + mcp_servers), marque synchronisée sur le workspace — architecture 2 modes encodée (`reference/architecture-lovable.md`) | `site-restaurant`, `usine-a-landing`, `agent-ia-produit`, `sync-marque-lovable` |

**Base de connaissance entreprise** : le skill `onboarding-entreprise`
(rapido-suite) interviewe l'utilisateur et construit `./rapido-kb/` (8 fichiers
markdown : entreprise, produits, propositions de valeur, personas, charte,
ton & accroches, processus internes, concurrents) dans le **répertoire de
travail du client** — jamais dans le plugin — donc versionnable dans son git,
éditable à la main, et conservée lors des mises à jour du plugin. Tous les
skills/agents des 5 plugins la chargent au besoin et **elle PRIME sur les
valeurs par défaut des skills** (seuils, cadences, arguments, piliers) ; sans
KB, les skills utilisent les standards du secteur en le signalant. Ordre des
sources : données opérationnelles (prix, stocks, stats) = MCP live d'abord ;
identité de marque = `./rapido-kb/charte-graphique.md` (client, complété,
PRIORITAIRE) > `get_brand` (vérification) > `reference/charte-graphique.md` du
plugin (générique, FALLBACK). Mise à jour via `mise-a-jour-kb`.

Chaque plugin embarque en plus un dossier `reference/` (directives communes
d'utilisation des outils ; `pieges-outils.md`, tableau des pièges par outil MCP ;
charte graphique pour les plugins à contenu visible), chargé par les skills en
« Étape 0 » — les règles voyagent avec le plugin. Les skills d'analyse
(`analyse-rentabilite-carte`, `coaching-pipeline`, `analyse-performance-contenu`,
`detection-surcharge`) délèguent leurs calculs à des scripts Python stdlib
embarqués (`skills/<skill>/scripts/`) : le modèle ne calcule jamais de tête.

## Test en local

Avant tout push GitHub, valider depuis le dossier parent du clone :

```
/plugin marketplace add ./rapido-plugins
/plugin install foodeatup@rapido
/reload-plugins
```

Puis dérouler les scénarios de test de déclenchement fournis pour chaque plugin
(une phrase déclencheuse + vérification des appels d'outils et des garde-fous).

## Versionner / contribuer

- **Le nom (slug) d'un plugin est IMMUABLE une fois publié.** Ne jamais renommer
  `foodeatup`, `rapidocrm`, `rapidocms`, `rapidorh` ou `rapido-suite` : cela
  casse toutes les installations existantes. Pour un changement de nom, créer un
  nouveau plugin et déprécier l'ancien.
- **Incrémenter `version`** (dans `<plugin>/.claude-plugin/plugin.json`) à chaque
  changement, même mineur — c'est ce qui déclenche la mise à jour chez les
  utilisateurs.
- **Tenir un CHANGELOG par plugin** (`<plugin>/CHANGELOG.md`) : une entrée par
  version, avec les skills ajoutés/modifiés et les changements de comportement.
- Toute modification de skill doit référencer des outils MCP existants (vérifier
  les noms exacts sur le serveur) et passer le test de déclenchement en local
  avant merge.

## Sécurité

- Un plugin **exécute du code et appelle des outils avec les privilèges de
  l'utilisateur** connecté (CRM, CMS, RH, FoodEatUp) : n'installer des plugins
  que depuis **cette source de confiance**.
- Les skills encodent des garde-fous : toute action destructrice ou irréversible
  (suppressions, envois d'emails/SMS, lancements de campagne, annulations)
  **demande une confirmation explicite** avant exécution — ne pas contourner ces
  confirmations dans les prompts.
- **Garde-fous déterministes (hooks)** : chaque plugin embarque
  `hooks/hooks.json` + `hooks/scripts/` (Python/bash, sans appel réseau, < 1 s) :
  - PreToolUse `garde-destructif` : confirmation utilisateur FORCÉE sur les
    outils destructifs du plugin, et refus pur des patterns interdits (ex.
    transition de facture hors table DGFiP côté CRM) — indépendant du modèle ;
  - PreToolUse `anti-donnee-inventee` (foodeatup, rapido-suite) : rejet des
    températures hors plage plausible (-30 °C à +90 °C) ;
  - Stop `récap-actions` : la fin de tour est bloquée si des écritures MCP ont
    eu lieu sans récapitulatif des IDs dans la réponse ;
  - SessionStart `contexte` (rapido-suite) : rappel de la politique
    d'autonomie (`reference/autonomie.md`) injecté à chaque session.
- Ne jamais mettre de secrets (tokens, mots de passe) dans les skills ou les
  fichiers `reference/` : ils sont distribués avec le plugin.

## À compléter avant publication

- `owner.name` dans `.claude-plugin/marketplace.json` et `author.name` dans
  chaque `plugin.json` (nom de la société).
- Les sections `### À COMPLÉTER` des `reference/charte-graphique.md`
  (codes hex, URLs de logo, typographies, ton de voix).
