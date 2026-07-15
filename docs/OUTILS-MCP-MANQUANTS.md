# Outils MCP manquants — specs pour le backend (Tunis)

> Registre des capacités MCP nécessaires aux skills mais **non exposées
> aujourd'hui** par les serveurs Rapido. Chaque entrée = spec courte (endpoint
> souhaité, champs, cas d'usage, priorité) pour l'équipe backend. Vérifié contre
> l'audit M0 (`docs/MATRICE-COUVERTURE.md`) et les schémas live. Aucune donnée
> inventée : tant qu'un outil n'existe pas, le skill fonctionne en **mode
> dégradé** documenté.

## 1. Télémétrie de délivrabilité (bounces / plaintes / échecs par destinataire)
- **Constat (live, audit M0)** : `get_stats_campagne` renvoie
  `{success, total, par_statut[]}` — des totaux par statut, **pas** de taux de
  bounce/plainte ni de motif d'échec par destinataire exploitable pour la
  délivrabilité.
- **Cas d'usage** : suivi post-envoi et runbook incident de `delivrabilite-email`
  (détecter un pic d'échecs, purger les invalides, décider une pause).
- **Endpoint souhaité** : `get_delivrabilite_campagne(campagne_id, periode)` →
  `{envoyes, delivres, bounces_hard, bounces_soft, plaintes, desabonnements,
  taux_bounce, taux_plainte, echecs: [{email_hash, motif, date}]}`.
- **Priorité** : haute (garde-fou d'envoi).

## 2. Infra warmup / rotation de boîtes / mesure de placement inbox
- **Constat** : aucun outil Rapido de warmup, de rotation de domaines/boîtes, ou
  de mesure de placement inbox↔spam (équivalents Smartlead/Instantly).
- **Cas d'usage** : montée en charge d'un domaine neuf ; envois froids à volume.
- **Souhait** : un MCP infra email dédié, ou une intégration externe documentée.
- **Priorité** : moyenne (contournable par la méthode + un outil externe en
  attendant ; la partie audit/méthode/garde-fous reste applicable).

## 3. Annulation d'un envoi planifié
- **Constat** : `schedule_email` / `schedule_sms` existent, mais **aucun outil
  d'annulation** d'un envoi déjà planifié n'est exposé côté CRM (RapidoCMS a son
  équivalent pour les posts).
- **Cas d'usage** : étape PAUSE du runbook incident (annuler les lots restants).
- **Endpoint souhaité** : `cancel_scheduled_email(id)` (analogue au tool
  d'annulation de posts planifiés de RapidoCMS).
- **Priorité** : haute (sécurité d'envoi).

## 4. Données d'intent tierces (enrichissement compte)
- **Constat** : pas de provider d'intent externe (ZoomInfo / Bombora / 6sense —
  techno installée, intent tiers, signaux d'achat marché) exposé côté Rapido.
- **Cas d'usage** : enrichir l'axe **intention** du skill `lead-scoring` au-delà
  des signaux first-party + actualité `account-research`.
- **Souhait** : un MCP d'enrichissement compte, ou une intégration documentée.
- **Priorité** : basse (les signaux first-party + `account-research` couvrent le
  besoin courant ; l'intent tiers est un bonus).
