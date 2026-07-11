---
name: lancement-projet-360
description: Utiliser quand l'utilisateur veut lancer un nouveau projet/produit/SaaS de A à Z, ou dit « accompagne-moi sur tout le cycle », « on part de zéro sur [idée] ». Orchestre méthodologie (rapido-forge) et exécution (CRM, CMS, Canva, Lovable, n8n, RH) en 5 actes, validation entre chaque acte.
---

# Lancement projet 360 — Forge pense, les plugins exécutent

Le scénario « je lance un nouveau SaaS » de bout en bout : chaque acte
enchaîne une phase MÉTHODO (rapido-forge — le livrable atterrit dans
`./rapido-kb/startup/forge/`) puis sa bascule EXÉCUTION (les systèmes
réels). **Jamais deux actes sans validation de l'utilisateur.**

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`. Si les
plugins cités ne sont pas tous installés : dérouler ce qui l'est, lister
honnêtement ce qui manque (`/plugin install <nom>@rapido`).

## Les 5 actes

1. **Penser** — routage par l'agent `directeur-programme` (rapido-forge) :
   vision, persona, BMC, pricing — chaque livrable ÉCRIT dans la KB avant
   d'avancer (journal `./rapido-kb/startup/forge/parcours.md`).
   ✋ Validation de l'acte, puis :
2. **Structurer** — projet RapidoRh via `rapidorh:setup-projet` (colonnes par
   phase, tâches issues du plan) ; prévisionnel chiffré via
   `rapido-startup:plan-financier-previsionnel` (scripts, 3 scénarios).
   ✋ Validation, puis :
3. **Construire** — landing `rapido-lovable:usine-a-landing` (brief cadré
   AVANT : les crédits Lovable se dépensent), identité
   `rapidocms:gestion-marques` (marque + assets, confirmation niveau 2),
   visuels `rapido-canva` (menu/supports selon le vertical).
   ✋ Validation, puis :
4. **Vendre & raconter** — pipeline `rapidocrm:prospection-pipeline`,
   contenus `rapidocms:calendrier-editorial`, séquences email
   (`rapidocrm:communication-client` — envois confirmés un par un).
   ✋ Validation, puis :
5. **Automatiser & mesurer** — workflows `rapido-n8n:recettes-metier`
   (validate avant create, production sous garde), KPI
   `rapido-startup:catalogue-kpi` (scripts, formules affichées), publicité
   `rapido-meta-ads` — **tout en PAUSED, activation après accord explicite
   uniquement : argent réel** (hooks plafond-budget + garde-argent-reel en
   filet).

## Règles d'orchestration

- **Ne JAMAIS dérouler deux actes sans validation** — chaque ✋ est un vrai
  arrêt : récapitulatif, accord, puis seulement l'acte suivant.
- **Tout livrable méthodo vit dans la KB AVANT son exécution** : pas de
  landing sans persona écrit, pas de campagne sans pricing validé.
- **Récapituler à chaque acte ce qui a été créé DANS les systèmes** — avec
  les IDs réels (projet RH, brand_id, campagne, workflows) ; les hooks
  Stop des plugins l'exigent aussi.
- Un acte peut être sauté à la demande (le dire au récapitulatif) ; l'état
  d'avancement se relit depuis la KB — relancer le skill reprend où on en
  était, sans doublonner.

## Garde-fous

- Ce skill n'invente aucun contenu : la méthode vient de rapido-forge, les
  données des MCP, le reste de l'utilisateur.
- Toute dépense (Lovable crédits, rendu vidéo, ads) = confirmation
  explicite au moment T — jamais « pré-accordée » par la validation d'un
  acte.
- Demande UNITAIRE (« crée un post ») → le plugin métier direct
  (rapidocms), pas l'orchestrateur.
