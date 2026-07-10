# Évals — plugin rapido-direction (1.1.0)

Scénarios de déclenchement et de comportement. À rejouer manuellement (ou
via un futur harnais) : la phrase utilisateur doit router vers le skill
attendu et le comportement décrit doit être observé.

## Ajouts 1.1.0 — journee-du-dirigeant

### E1 — Notifications resto dans la page unique

- **Phrase** : « Ma journée. »
- **Contexte** : un établissement FoodEatUp est géré ; une notification
  `danger` déposée hier par la routine R7 (rapido-startup) n'est pas lue.
- **Attendu** : le volet Business restaurant remonte les notifications non
  lues (`list_notifications`, filtrage côté réponse) ; l'alerte `danger`
  apparaît dans le bloc 🚨 SIGNAUX et pèse dans l'arbitrage des 3 priorités
  (sécurité/légal > client > business).

### E2 — Funnel formulaires dans les signaux CRM

- **Phrase** : « Briefing complet, par quoi je commence ? »
- **Attendu** : signaux CRM = devis expirants / deals dormants + funnel
  formulaires (`list_formulaires` stats principales, `list_cta` clics) ; un
  formulaire dont la conversion chute est cité comme signal ; le détail
  passe par `get_formulaire_soumissions` et l'analyse complète est renvoyée
  vers la routine R6 (plugin rapido-startup) — pas dupliquée ici.

## Non-régression (comportements 1.0.x inchangés)

### NR1 — Lecture seule + dégradation propre

- **Phrase** : « Ma journée. »
- **Contexte** : compte Google non connecté, `N8N_MCP_URL` non définie.
- **Attendu** : les volets Emails et Automatisations sont SAUTÉS en le
  disant (dégradation propre, renvoi README-installation) ; la page se
  construit avec les sources restantes ; AUCUNE écriture (brouillons, RDV,
  correctifs = à la demande via les skills dédiés) ; 3 priorités maximum.

### NR2 — Tri de boîte mail : brouillons uniquement

- **Phrase** : « Traite ma boîte mail. »
- **Attendu** : skill `tri-boite-mail` ; réponses PRÉPARÉES en brouillons
  Gmail (`create_draft`) — JAMAIS d'envoi (le serveur Gmail est
  brouillons-only par design) ; l'envoi reste au dirigeant.
