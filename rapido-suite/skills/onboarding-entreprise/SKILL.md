---
name: onboarding-entreprise
description: Utiliser quand l'utilisateur parle d'onboarding, de configurer le plugin, de setup initial, ou demande d'apprendre à connaître son entreprise. Interviewe l'utilisateur et construit la base de connaissance ./rapido-kb/ (8 fichiers markdown) utilisée ensuite par tous les skills et agents.
---

# Onboarding entreprise (construction de la KB)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## RÈGLE CRITIQUE — emplacement de la KB

La KB s'écrit dans le RÉPERTOIRE DE TRAVAIL de l'utilisateur : `./rapido-kb/`.
JAMAIS dans le dossier du plugin installé (`${CLAUDE_PLUGIN_ROOT}` reste
générique et identique pour toute l'équipe). Ainsi la KB est versionnable dans
le git du client, éditable à la main, et survit aux mises à jour du plugin.
Si `./rapido-kb/` existe déjà : proposer `mise-a-jour-kb` plutôt qu'un
onboarding complet (ne pas écraser sans confirmation).

## Structure cible (8 fichiers)

| Fichier | Contenu |
|---|---|
| `entreprise.md` | identité, histoire, mission, implantations, équipe clé, fuseau horaire, devise, establishment_id FoodEatUp |
| `produits-services.md` | offres, prix, marges cibles, best-sellers, saisonnalité |
| `propositions-valeur.md` | promesse par cible, différenciateurs, preuves (chiffres, avis, labels), garanties |
| `cibles-personas.md` | segments clients, pains, déclencheurs d'achat, canaux |
| `charte-graphique.md` | hex, typos, logos (URLs), do/don't — version COMPLÉTÉE |
| `ton-et-accroches.md` | ton de voix, vocabulaire maison, mots interdits, accroches validées par canal, exemples de posts qui ont marché |
| `processus-internes.md` | règles métier maison : seuils (food cost, marges), cadences de relance, horaires, politique de remise, plafond budget pub/jour, registre des automatisations |
| `concurrents.md` | concurrents principaux, leur positionnement, nos parades |

## Phase 1 — COLLECTE AUTO (ne jamais demander ce que les MCP savent déjà)

Interroger les serveurs disponibles et pré-remplir :
- rapidocms : `get_brand`, `get_company`, `get_profile` → charte-graphique.md
  (couleurs, logo) + entreprise.md (identité) ;
- rapidocrm : `list_products`, `list_commerciaux`, `list_segments` →
  produits-services.md + entreprise.md (équipe) + cibles-personas.md (segments) ;
- foodeatup : `list_dishes`, `list_recipes` (avec `establishment_id`, le
  demander si l'utilisateur a un restaurant) → produits-services.md ;
- rapidorh : `get-users-list-tool`, `get-departments-list-tool` →
  entreprise.md (organisation).
Si un serveur est indisponible ou vide : le noter et passer — sans bloquer.
Annoncer à l'utilisateur ce qui a été pré-rempli automatiquement.

## Phase 2 — INTERVIEW GUIDÉE (uniquement les questions restantes)

Par blocs COURTS : max 3-4 questions à la fois, attendre les réponses avant le
bloc suivant. Sauter toute question dont la réponse est déjà connue (phase 1).

1. **Bloc identité** : mission en 1 phrase ? ce qui vous rend différent ?
   votre histoire en 2-3 phrases ?
2. **Bloc offre** : vos best-sellers ? marges cibles ? offres à pousser / à
   abandonner ? saisonnalité ?
3. **Bloc clients** : vos 2-3 types de clients ? leur problème n° 1 ?
   pourquoi ils vous choisissent vous et pas le concurrent ?
4. **Bloc marque** : 3 mots qui décrivent votre ton ? mots/sujets interdits ?
   accroches ou posts qui ont déjà bien marché (les citer) ?
5. **Bloc règles maison** : seuils financiers (food cost max, marge mini) ?
   cadence de relance ? politique de remise (qui peut, jusqu'à combien) ?
6. **Bloc concurrence** : 3 concurrents principaux ? leur force ? votre parade ?
7. **Bloc réglages techniques** (la personnalisation vit dans la KB, jamais
   dans les plugins) :
   - FUSEAU HORAIRE de l'entreprise ? → `entreprise.md` (utilisé par
     l'agenda, les planifications, les workflows) ;
   - DEVISE de travail (si autre qu'euros) ? → `entreprise.md` ;
   - `establishment_id` FoodEatUp (si restaurant — le retrouver ensemble via
     un premier appel FoodEatUp si inconnu) ? → `entreprise.md` ;
   - PLAFOND de budget publicitaire par jour (défaut 50 €/jour si non
     défini) ? → `processus-internes.md` (ligne « Plafond budget pub :
     X €/jour » — lue par le hook du plugin rapido-meta-ads) ;
   - instance n8n ? → rappel : l'URL se configure par variable
     d'environnement (`export N8N_MCP_URL=…` avant de lancer Claude Code,
     voir `rapido-n8n/README-installation.md`) — consigner dans
     `processus-internes.md` (registre des automatisations) QUE l'instance
     existe et qui l'administre, pas de secret dans la KB.

Règles d'interview :
- « je ne sais pas » / « passe » = accepté : insérer le marqueur
  `### À COMPLÉTER` dans le fichier, ne JAMAIS inventer pour combler ;
- reformuler les réponses orales en contenu structuré (listes, tableaux) — pas
  de verbatim brut ;
- une réponse qui contredit une donnée MCP : signaler l'écart et demander
  laquelle fait foi.

## Phase 3 — RÉDACTION ET VALIDATION

1. Générer les 8 fichiers dans `./rapido-kb/` (créer le dossier), chacun avec
   en tête : `> Dernière mise à jour : YYYY-MM-DD — onboarding initial`.
2. Montrer un RÉSUMÉ (par fichier : 2-3 lignes de ce qui y est + les sections
   encore marquées `### À COMPLÉTER`) — pas les 8 fichiers in extenso.
3. Demander validation ; corriger les fichiers concernés si besoin.

## Phase 3 bis — Miroir CMS de la marque (OPTIONNEL)

Une fois `charte-graphique.md` rempli et validé, proposer de créer la **marque
miroir dans RapidoCMS** (le CMS est le miroir d'exécution ; la KB reste la
source de vérité). Étapes :

1. **Vérifier la disponibilité** : plugin `rapidocms` installé et MCP joignable
   (`get_company`). **Absent/indisponible → le signaler et continuer sans
   bloquer** (l'onboarding n'échoue jamais là-dessus ; on pourra synchroniser
   plus tard via `mise-a-jour-kb`).
2. **Mapping validé par l'utilisateur** : montrer le mapping KB → marque avant
   d'écrire — `nom`, `langue`, `slogan`, `couleurs` (hex de la charte),
   `font_family` (pile web-safe la plus proche, expliquée), `logo` (URL
   publique). Déléguer la création au skill **`gestion-marques`** (plugin
   `rapidocms`, confirmation niveau 2, hook `valide-charte` en filet).
3. **Consigner la sync dans la KB** : écrire dans `charte-graphique.md` une
   ligne de pied — `> Miroir CMS : brand_id <id retourné par create_brand> —
   dernière sync <YYYY-MM-DD>`. C'est cette ligne que `mise-a-jour-kb` relira
   pour la sync descendante.
4. **Assets de base** : proposer d'importer le logo via `bibliotheque-assets`
   (rapidocms) et de le rattacher à la marque — optionnel, non bloquant.

## Phase 4 — CÂBLAGE

1. Confirmer que la KB est active : les skills et agents la chargent au besoin
   (le hook SessionStart du plugin la détecte à chaque session).
2. Expliquer la mise à jour : skill `mise-a-jour-kb`, ou édition directe des
   fichiers (markdown simple), ou versionnage dans le git du client.
3. Recommander de committer `./rapido-kb/` dans le dépôt du client.

## Garde-fous

- Jamais de données inventées pour combler un trou : insérer le marqueur
  `### À COMPLÉTER`.
- La KB appartient au client : ne jamais y écrire de secrets (tokens, mots de
  passe) ; les prix et marges y sont acceptés (c'est son dépôt).
- Priorité des sources pour les autres skills : données MCP live > KB >
  références génériques du plugin.
