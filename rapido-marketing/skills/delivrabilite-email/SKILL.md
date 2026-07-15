---
name: delivrabilite-email
description: Utiliser quand l'utilisateur parle de « délivrabilité », dit « mes emails tombent en spam », « vérifie la liste avant envoi », « warmup », « on peut envoyer ? ». Gate OBLIGATOIRE avant tout lot d'envoi (scorecard de liste + contrôle spam de la copy) et runbook d'incident délivrabilité, en mode outbound (cold) ou newsletter (base opt-in). Exécution via RapidoCRM.
---

# Délivrabilité email — gate pré-envoi & runbook incident

Ce skill est le **GATE obligatoire** de tout envoi de masse : il **valide la
liste** et **contrôle la copy** AVANT qu'un lot parte, impose la **cadence** de
montée en charge, et fournit le **runbook** quand la délivrabilité casse.

Adapté des fiches `docs/methodo/ops/delivrabilite-email.md` et
`cold-email-cadence.md` (distillation coldoutboundskills, MIT © 2026
GrowthEngineX — voir `docs/methodo/ops/NOTICE.md`), exécution via RapidoCRM.

## Règle d'invocation OBLIGATOIRE
Ce skill est invoqué avant tout lot d'envoi. Un lot **sous le seuil KB est
REFUSÉ** — pas d'envoi tant que la liste n'est pas corrigée.
- `machine-outbound` → mode **`outbound`** (cold email).
- `rapidocrm:campagne-marketing` → mode **`newsletter`** (câblé, conditionnel à la
  présence du plugin rapido-marketing ; sinon checklist minimale côté rapidocrm).

## Modes (paramètre du contrat)
Le skill s'invoque avec un **mode** :
- **`outbound`** (défaut, cold email/prospection) — **tout** le gate : scorecard
  de liste + `spam_check` + **plafonds + cadence/warmup** de `delivrabilite.md`.
- **`newsletter`** (envoi à une base **opt-in** existante) — **scorecard
  d'hygiène** (doublons, formats invalides, emails de rôle) + `spam_check` du copy
  + **présence du lien de désinscription** (bloquante) + **taille du lot vs
  plafond** ; **PAS de règles de warmup/cadence** (base déjà consentante).

**Même seuil de refus, mêmes scripts** dans les deux modes — aucune duplication :
seule la couche warmup/cadence est retirée en `newsletter`, où l'absence de lien
de désinscription (`spam_check` → `controles.lien_desinscription: false`) est
**bloquante**.

## Étape 0 — Charger (obligatoire)
- `./rapido-kb/marketing/delivrabilite.md` — **plafond quotidien, calendrier de
  montée en charge, seuil de note minimale, règles de pause**. Absent → le créer
  depuis `${CLAUDE_PLUGIN_ROOT}/reference/kb-templates/delivrabilite.md`.
  (En mode `newsletter`, seuls plafond et seuil sont utilisés ; warmup/cadence ignorés.)
- `${CLAUDE_PLUGIN_ROOT}/reference/garde-fous-marketing.md` (§a envois confirmés,
  §b RGPD, §c délivrabilité) et `docs/methodo/etat-de-lart-2026.md` §4 (warmup,
  plafonds, rotation — chiffres de référence).
- `./rapido-kb/marketing/apprentissages.md` (incidents/leçons passés — priment).

## Gate pré-envoi (bloquant)

### 1. Scorecard de liste — REFUS si sous le seuil
- `python3 "${CLAUDE_PLUGIN_ROOT}/skills/delivrabilite-email/scripts/scorecard_liste.py" liste.json`
- Entrée : le segment/export (`contacts` avec `titre`, ou `emails`), le
  `plafond_quotidien` et le `seuil_note` **lus dans `delivrabilite.md`**.
- Sortie chiffrée (formule affichée) : doublons, emails de rôle (`info@`,
  `contact@`…), formats invalides, diversité des titres, concentration de
  domaines, taille du lot vs plafond → **note A-E** + actions correctives.
- **`refus: true` (note sous le seuil) ⇒ on n'envoie pas.** Aucune dérogation
  sans **modifier explicitement `delivrabilite.md`** (traçable). Appliquer les
  actions correctives, puis rejouer le scorecard.

### 2. Contrôle de la copy
- `python3 "${CLAUDE_PLUGIN_ROOT}/skills/delivrabilite-email/scripts/spam_check.py" copy.json`
  (objet + corps) → lexique à risque FR/EN, densité de liens, excès de
  majuscules, ponctuation agressive, promesses chiffrées → **signalements** +
  note de risque (faible/moyen/élevé).
- Le script **signale seulement** : la **réécriture est déléguée à
  `rapidocrm:redaction-commerciale`** (pas de doublon). Re-contrôler après réécriture.
- **Mode `newsletter`** : `controles.lien_desinscription` doit être **`true`** —
  sinon **REFUS** du lot (obligation légale d'un lien de désinscription).

### 3. Volumes & cadence
- **Plafond quotidien** (les deux modes) : **jamais au-delà** ; fractionner un lot
  trop gros sur plusieurs jours (taille du lot vs plafond de `delivrabilite.md`).
- **Cadence / warmup — mode `outbound` uniquement** : respecter le **calendrier de
  montée en charge** de `delivrabilite.md`. En `newsletter`, ces règles ne
  s'appliquent pas (base opt-in déjà consentante).
- **Chaque lot reste soumis au hook `garde-envois`** (confirmation humaine
  explicite) — ce gate ne remplace pas la confirmation, il la précède.
- Envoi/planification via RapidoCRM : `send_email`, `schedule_email`,
  `send_newsletter` (désinscription honorée immédiatement — RGPD).

## Suivi post-envoi
- Lire ce que le serveur expose réellement : `get_stats_campagne`
  (`{success, total, par_statut[]}` — audit M0) et `list_campagnes`.
- **Limite connue** : les **bounces/plaintes par destinataire** ne sont **pas**
  exposés comme signal de délivrabilité exploitable. C'est consigné comme **outil
  MCP manquant** avec spec dans `docs/OUTILS-MCP-MANQUANTS.md` (entrée 1) — à
  faire porter par le backend (Tunis). En attendant : suivi au niveau statut de
  campagne, sans taux de bounce fin.

## Runbook incident (délivrabilité qui casse)
1. **Signaux** : chute brutale des réponses **ou** pic d'échecs (au niveau des
   statuts de campagne, faute de taux de bounce fin).
2. **PAUSE** : suspendre les lots à venir (ne plus rien confirmer). L'**annulation
   des envois déjà planifiés** nécessite un outil d'annulation CRM **non exposé à
   ce jour** (voir `docs/OUTILS-MCP-MANQUANTS.md` entrée 3) — le signaler ; sinon
   documenter les planifications non annulables.
3. **Diagnostic** (checklist) : authentification SPF/DKIM/DMARC valide (côté
   client) ? liste récemment élargie ? copy modifiée ? volume monté trop vite ?
   → purger les emails invalides (rejouer le scorecard), vérifier l'auth.
4. **Reprise progressive** : revenir 1-2 crans en arrière dans le calendrier,
   **ne pas “pousser plus”** sur un domaine qui décroche.
5. **Capitalisation** : consigner l'incident et la reprise dans
   `./rapido-kb/marketing/apprentissages.md` (date | contexte | leçon | preuve |
   skill source), via `mise-a-jour-kb`. Pas de leçon sans preuve chiffrée.

## Modes dégradés
- **Infra warmup/rotation absente** (pas d'équivalent Smartlead) : audit +
  méthode + garde-fous restent applicables ; l'infra de montée en charge se fait
  via un outil externe → `docs/OUTILS-MCP-MANQUANTS.md` (entrée 2).
- **Bounces non exposés** : suivi au statut de campagne (ci-dessus).

## Cas d'usage croisés
- Réécriture de la copy signalée → `rapidocrm:redaction-commerciale`.
- Séquences & cadence outbound → `machine-outbound`.
- Campagnes CRM → `rapidocrm:campagne-marketing`.

## Garde-fous (rappel)
Gate **avant tout lot** ; **REFUS** si note < seuil KB (pas de dérogation sans
modifier `delivrabilite.md`) ; **jamais au-delà du plafond** ; chaque lot **confirmé**
(`garde-envois`) ; scores **par script** (jamais de tête) ; RGPD (désinscription
immédiate) ; capacités manquantes **consignées**, jamais inventées.
