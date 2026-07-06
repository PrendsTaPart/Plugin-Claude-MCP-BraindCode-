---
name: usine-a-landing
description: Utiliser quand l'utilisateur veut une landing page, une page de campagne ou une page de capture. Construit la page depuis la campagne CRM et les arguments de la KB, le formulaire crée le prospect dans le CRM (mode B), et boucle les analytics avec les stats de campagne.
---

# Usine à landing pages (RapidoCRM × Lovable)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/architecture-lovable.md`. KB :
`propositions-valeur.md` (promesse, preuves), `cibles-personas.md`,
`charte-graphique.md`, `ton-et-accroches.md`.

## Workflow

1. **Partir de la campagne CRM** — `list_campagnes` / `get_stats_campagne` :
   objectif, segment cible (`get_contacts_segment`), offre. Une landing sans
   campagne : demander l'objectif et la cible.
2. **Assembler le contenu** — promesse et différenciateurs de
   `propositions-valeur.md` (source citée), pains du persona ciblé
   (`cibles-personas.md`), UN appel à l'action (règles de
   `redaction-commerciale` : un seul CTA). Faire valider le contenu avant de
   construire.
3. **Créer la page** — `get_workspace` (crédits) puis `create_project`
   (`initial_message` détaillé : landing UNE page — hero avec promesse,
   preuves/témoignages sourcés, offre, formulaire de capture nom/email/
   téléphone/consentement, palette hex KB, mobile-first, temps de chargement).
4. **Formulaire → prospect en MODE B** — faire construire l'edge function qui
   appelle l'API Anthropic avec `mcp_servers` = MCP RapidoCRM
   (`https://crm.rapidosoftware.com/mcp`) : à la soumission,
   `create_contact` puis `ajouter_prospect_pipeline` (étape d'entrée) — blocs
   parsés par type, clé API côté serveur, anti-doublon (rechercher avant de
   créer si l'email existe).
   - Alternative sans IA : POST direct du formulaire vers l'edge function qui
     appelle le CRM — proposer la plus simple selon le besoin.
5. **Déployer** — `deploy_project` (confirmation niveau 2, URL publique).
   Renseigner l'URL de la landing dans la campagne CRM (description/notes).
6. **Boucle de mesure** — après quelques jours : `get_project_analytics`
   (`start_date`/`end_date` RFC 3339, mêmes dates que la période de campagne)
   → visiteurs, conversion, sources — à rapprocher de `get_stats_campagne`
   (CRM) : le trafic vient-il des campagnes ? Les leads créés dans le pipeline
   correspondent-ils aux soumissions ?

## Garde-fous

- Promesses et preuves UNIQUEMENT depuis la KB ou des données vérifiables —
  pas de chiffre inventé sur une page publique.
- Formulaire : consentement explicite (RGPD), données envoyées au CRM
  uniquement — pas de stockage parallèle en clair dans la base Lovable sans
  raison (si base : `enable_database` une fois, écritures confirmées).
- Une landing par objectif : refuser la page fourre-tout (proposer d'en faire
  deux).
