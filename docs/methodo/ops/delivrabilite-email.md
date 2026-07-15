# Délivrabilité email — audit, warmup, incidents

> **Source distillée** : growthenginenowoslawski/coldoutboundskills (MIT © 2026
> GrowthEngineX) — skills `email-deliverability-audit`,
> `deliverability-incident-response`, `spam-word-checker`,
> `smartlead-inbox-manager`. Reformulé FR, non-verbatim (voir `NOTICE.md`).
> Complète `docs/methodo/etat-de-lart-2026.md` §4.

## Audit de délivrabilité (avant d'envoyer)
- **Authentification** : SPF, DKIM, DMARC configurés et valides (côté client).
- **Santé de l'inbox** : réputation du domaine, âge, historique de bounce.
- **Test spam** : passer la copy au crible des mots déclencheurs (voir plus bas).

## Warmup & volumes (rappel état de l'art)
Domaine neuf : 5-10/jour, montée sur 4-6 semaines ; 20-50/boîte/jour ; plafonds
~500/j Gmail, ~300/j Outlook ; **rotation de boîtes** au-delà.

## Mots à risque spam (garde-fou always-on)
Éviter/mesurer : « gratuit », « garanti », « urgent », « 100 % », excès de
majuscules/points d'exclamation, liens raccourcis. Un score de risque avant envoi.

## Réponse à incident (délivrabilité qui casse)
Arbre : taux de bounce en hausse ? → pause envois, vérifier auth, purger la liste
(emails invalides), réduire le volume, ré-échauffer. Ne pas « pousser plus » sur
un domaine qui décroche.

## Mapping Rapido
- Envoi/planification : **RapidoCRM** (`send_email`, `schedule_email`,
  `send_newsletter`). Désinscription honorée immédiatement (RGPD).
- ⚠️ **MCP manquant** : warmup, rotation de domaines/inboxes, mesure de placement
  (équivalents Smartlead/Zapmail) — **à remonter au backend Tunis**. En attendant,
  la partie **audit + méthode + garde-fous** est applicable ; l'infra warmup se
  fait via un outil externe.

→ Cible : **nouveau skill `delivrabilite-email`** (M-suivant), en dépendance
partielle d'un MCP infra email.
