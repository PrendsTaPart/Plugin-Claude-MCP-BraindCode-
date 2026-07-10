---
name: journee-du-dirigeant
description: Utiliser quand l'utilisateur demande sa journée, un briefing complet ou « par quoi je commence ». Fusionne emails, agenda triple (Calendar + CRM + FoodEatUp), business et alertes d'automatisations en UNE page avec 3 priorités.
---

# Journée du dirigeant (le pilotage A→Z en une page)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/regles-direction.md` (agenda triple,
brouillons only, fuseau KB, dégradation propre).

## Collecte — EN PARALLÈLE (lancer des subagents pour les volets indépendants)

1. **Emails** — Gmail `search_threads` (`is:unread OR is:important`,
   48 dernières heures) : ce qui attend une réponse. Absent si compte Google
   non connecté — le mentionner, continuer.
2. **Agenda TRIPLE (toujours les trois)** — Calendar `list_events` (jour,
   fuseau de `rapido-kb/entreprise.md`) + `get_today_schedule` (CRM) +
   `list_reservations` (FoodEatUp, date du jour) → FUSIONNER
   chronologiquement ; signaler les conflits entre sources et les
   chevauchements.
3. **Business restaurant** — dérouler `briefing-du-jour` (plugin foodeatup)
   si un établissement est géré : notifications non lues
   (`list_notifications` — dont les alertes déposées par les routines Loop
   Engine), HACCP, salle, production, stocks.
4. **Alertes automatisations** — n8n `search_executions` (échecs récents) si
   `N8N_MCP_URL` est définie : un workflow en panne = un rôle non assuré.
5. **Signaux CRM** — devis expirants / deals dormants (aperçu rapide via
   `list_devis` + `get_pipeline`) ; funnel formulaires en un coup d'œil :
   `list_formulaires` (stats principales) + `list_cta` (clics) — un
   formulaire qui ne convertit plus est un signal du jour (détail :
   `get_formulaire_soumissions`, analyse complète : routine R6 du plugin
   rapido-startup).

## Restitution — UNE PAGE, pas plus

```
🌅 VOTRE JOURNÉE — {date}

🎯 3 PRIORITÉS (arbitrées : sécurité/légal > client > business)
1. …  2. …  3. …

📅 AGENDA FUSIONNÉ (Calendar + CRM + resto)
heure | quoi | source | préparation nécessaire ?

📧 EMAILS QUI ATTENDENT (Gmail, 48 h)
de | objet | enjeu | → brouillon proposé (oui/non)

🚨 SIGNAUX
resto (notifications non lues, HACCP/stocks) | CRM (devis, deals,
funnel formulaires/CTA) | automatisations (échecs)
```

- Pour chaque email actionnable : PROPOSER le brouillon (skill
  `tri-boite-mail`) — jamais d'envoi, rappeler que l'envoi reste au
  dirigeant.
- Terminer par : « on attaque la priorité 1 ? »

## Garde-fous

- Lecture seule (les actions — brouillons, RDV, correctifs — se lancent à la
  demande via les skills dédiés).
- Sources indisponibles : le volet est sauté EN LE DISANT (dégradation
  propre, README-installation pour reconnecter).
- 3 priorités maximum, arbitrées — pas une liste de 12 urgences.
