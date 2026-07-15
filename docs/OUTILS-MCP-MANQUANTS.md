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

## 5. Clé de ré-scrape stable sur une fiche (place_id / cid Google Maps)
- **Constat** : aucun champ CRM dédié pour stocker `place_id` / `cid` / `data_id`
  d'une fiche Google Maps (identifiants stables d'un établissement).
- **Cas d'usage** : `rapido-gmaps:enrichissement-fiches` — re-scraper une fiche
  existante par son `place_id` pour compléter/rafraîchir ses coordonnées, sans
  re-chercher par nom (ambigu).
- **Endpoint souhaité** : champ `place_id` (+ `cid`) sur l'entreprise, ou
  `set_external_ref(entreprise_id, source, ref)` / `get_by_external_ref(source, ref)`.
- **Contournement actuel** : stocké en note `log_activity` + tag (non requêtable).
- **Priorité** : moyenne (débloque l'enrichissement fiable ; contourné en note).

## 6. Score de priorité prospect structuré
- **Constat** : pas de champ « score » structuré sur une fiche prospect ; le
  score `rating × log(review_count+1) × signal_opportunite` de `rapido-gmaps` ne
  peut être ni stocké ni filtré côté CRM.
- **Cas d'usage** : trier/segmenter les leads sourcés par score ; entraîner
  `rapido-marketing:icp-generator` sur « quels scores convertissent ».
- **Endpoint souhaité** : champ numérique `score` (ou `set_lead_score(id, valeur,
  source)`), filtrable par `rechercher_prospects`.
- **Contournement actuel** : note + tag de priorité (non requêtable finement).
- **Priorité** : moyenne.

## 7. Attributs structurés de fiche (popular_times / horaires / répartition avis)
- **Constat** : pas de réceptacle structuré pour `popular_times`,
  `reviews_per_rating`, `open_hours`, `about[]` d'une fiche Google Maps.
- **Cas d'usage** : recommander la **fenêtre d'appel** optimale (affluence),
  croiser avec `foodeatup:reservation_availability`.
- **Endpoint souhaité** : bloc `attributs` JSON sur l'entreprise, ou
  `set_entreprise_attributs(id, {...})`.
- **Contournement actuel** : note `log_activity` (lecture humaine seulement).
- **Priorité** : basse (la note libre suffit au premier usage).
