# Changelog — plugin rapidocrm

## 1.7.0 — 2026-07-15 — vente terrain opérationnelle (pont forge → ops)

- **5 skills** appliquant les méthodes forge aux **données MCP réelles** (pont
  `reference/pont-forge-operations.md`) : `preparation-rdv` (SONCAS opérationnel :
  fiche CRM + profil SONCAS sourcé + SPIN + objectif de sortie, notes `log_activity`
  confirmées), `qualification-deals` (BANT/MEDDIC sur le pipeline, multi-threading ;
  anti-collision `coaching-pipeline`), `coach-de-vente` (routeur multi-livres SPIN/
  Challenger/Gap/Fanatical/Voss/Cialdini — **synthétise et route**, ne duplique pas
  `negotiation`/`influence-psychology`), `playbook-objections-vivant` (objections
  réelles Fireflies/CRM/deals perdus → `./rapido-kb/commercial/objections.md`
  incrémental ; frontière `hundred-million-offers`), `funnel-aarrr-reel` (AARRR sur
  données MCP, **formules `catalogue-kpi`**, étape fuyante + 3 actions routées).
- Évals 5+3 par skill. Chaque skill lit le livrable forge (ou dit son absence).

## 1.6.0 — 2026-07-15 — boucle d'expansion (upsell + ambassadeurs)

- Skill **`expansion-clients`** — le tunnel **Studio → Agence → SaaS** à 3 transitions
  à signaux réels : livrables Studio terminés (Kanban RapidoRH à Done), projet agence
  à J-15, client SaaS actif 3+ mois. Proposition déléguée à `redaction-commerciale`,
  `create_devis` après confirmation, relance J+7 — tout en brouillon ; fourchettes/
  paliers depuis `./rapido-kb/offres.md`.
- Skill **`programme-ambassadeurs`** — opère le programme **10 % client / 20 %
  apporteur** : éligibilité (6+ mois, factures payées, satisfaction), proposition
  convertible en crédits, suivi via `get_loyalty_points` (plafonds serveur ; aucun
  ajustement inventé), relance J+60. **Anti-collision** avec
  `rapido-marketing:lead-getters-systeme` (lui = choisit le TYPE ; moi = opère le
  programme existant) — documentée dans les deux SKILL.md.
- Routine **`VENTE-EXPANSION`** (hebdo jeudi) : scan des 3 signaux + éligibles
  ambassadeurs → opportunités de la semaine, propositions préparées. Enregistrée au
  registre unifié.
- Évals : 5 phrases + 3 contre-exemples par skill (non-collision).

## 1.5.0 — 2026-07-15 — pilotage-commercial (la boucle de vente)

- Skill **`pilotage-commercial`** — l'orchestrateur de la boucle commerciale
  (hygiène → relances → conversion → encaissement), sur le modèle EXACT de
  `rapido-marketing:pilotage-marketing` : cycle **Sense → Plan → Act → Feed →
  Report**, gouvernance `autonomie.md`, **calculs délégués à
  `rapido-startup:catalogue-kpi` (jamais de calcul local)**, priorisation
  valeur×probabilité×urgence, anti-doublon Kanban RapidoRH avant création. Envois en
  brouillon confirmé (`garde-envois`). **Anti-collision** explicite : sous-domaine de
  `rapido-suite:pilotage-entreprise` ; distinct de `coaching-pipeline` (revue
  ponctuelle) et de `pilotage-marketing` (génère les leads ; moi je convertis).
- **3 routines `VENTE-*`** au format CONFIG interchangeable de loop-engine
  (`references/routines/`) : **VENTE-HYGIENE** (hebdo lundi, score /100 pondéré
  40/30/20/10, niveau 0), **VENTE-RELANCES** (quotidien 14h, brouillons + table
  mémoire `vente_relances_journal` anti-double-relance), **VENTE-REVUE** (hebdo lundi,
  couverture = pipeline pondéré ÷ objectif via catalogue-kpi). Enregistrées au
  **registre unifié** `reference/registre-routines.md`.
- Évals : 5 phrases déclenchantes + 3 contre-exemples (non-collision coaching-pipeline
  / pilotage-marketing / pilotage-entreprise).

## 1.4.3 — 2026-07-15

- `campagne-marketing` : **gate délivrabilité conditionnel** avant tout envoi de
  masse (`lancer_campagne` / `send_newsletter`), nouvelle étape 5 (funnel et suivi
  décalés en 7/8).
  - **rapido-marketing présent** : invocation OBLIGATOIRE de `delivrabilite-email`
    en mode `newsletter` — **lot refusé = pas d'envoi**, aucune dérogation.
  - **Mode dégradé (rapidocrm autonome)** : checklist minimale intégrée —
    `recalculer_segment` (dédoublonnage + taille), lien de désinscription présent,
    taille du lot confirmée — + mention que le gate complet vient de rapido-marketing.
  - Hook `garde-envois` (confirmation) inchangé dans les deux cas.
  - Évals CM-GATE et CM-DEGRADE.

## 1.4.2 — 2026-07-15

- Enrichissement `mom-test` (founder-playbook, MIT © 2026 AgentSeal) : ajout du
  **Filter Test** — si le prospect n'a jamais cherché de solution par lui-même,
  la douleur ne justifie pas un achat, quel que soit son enthousiasme. Ajout
  seul, attribution en fin de section. Le type de mauvaise donnée
  « Idées/Fonctionnalités » n'est pas redupliqué (déjà couvert §3).

## 1.4.1 — 2026-07-11

- Vestige d'import retiré : la ligne « see CONNECTORS.md » (lien mort,
  le fichier n'a jamais été porté) supprimée de ticket-triage, draft-response, forecast et pipeline-review-methodo.

## 1.4.0 — 2026-07-11

- Capture de leads câblée côté CRM (schémas vérifiés serveur) :
  - `campagne-marketing` étape 7 : funnel complet vues → clics CTA →
    soumissions → prospects (`list_formulaires`,
    `get_formulaire_soumissions`, `list_cta`), taux PAR ÉTAPE calculé par
    script (`taux_conversion_etape`, catalogue-kpi) ; formulaire qui ne
    convertit plus = signalé avec proposition ;
  - `prospection-pipeline` : les soumissions de formulaires deviennent une
    SOURCE d'entrée du pipeline (leads chauds, à traiter en premier), avec
    dédoublonnage par email puis nom AVANT `enregistrer_prospect` — une
    soumission d'un contact connu = interaction tracée (`log_activity`),
    pas un nouveau prospect.

## 1.3.0 — 2026-07-10

- Nouveau skill `gestion-depenses` : source de vérité des dépenses CRM —
  `list_depenses` (chiffres cités avec période/statut), contrôle
  TTC = HT + TVA par script AVANT saisie
  (scripts/controle_depense.py, stdlib, tolérance 1 centime, formule
  affichée), `create_depense` après confirmation (hook garde-destructif
  étendu à create_depense, testé stdin → ask). Honnêteté serveur : PAS
  d'outil de détail (`get_…`) ni de suppression de dépense côté CRM — le
  détail resto relève du plugin foodeatup (reappro-fournisseurs).
- Câblé en SOURCE PRIMAIRE des dépenses dans les routines R4 CFO-WEEKLY et
  R7 CASH-SENTINEL (loop-engine-v2, plugin rapido-startup) ;
  performance-commerciale renvoie vers le skill dédié.

## 1.2.0 — 2026-07-10 (vague post-audit — consolidé)

- performance-commerciale (schémas vérifiés serveur) :
  - indicateurs complétés : `get_interaction_stats` (volume d'interactions),
    `list_depenses` (coûts) et SAISIE d'une dépense dictée `create_depense`
    (`entreprise_id` + `total_ht` requis, TTC/TVA auto-calculés,
    mode_paiement enum) après confirmation ;
  - section « Cycle de vie d'un commercial » (sur demande explicite
    uniquement) : `create_commercial` (nom/prenom/email + objectifs
    mensuels), `update_commercial_profil`, `delete_commercial` (`confirm:
    true` EXIGÉ par le serveur + hook garde-destructif) — proposer d'abord
    `set_commercial_status` inactif qui préserve l'historique.
- communication-client : `list_newsletters` consulté avant
  `send_newsletter` (anti-doublon d'envoi).
- contrats-clients : `update_contrat_template` (les contrats déjà émis ne
  changent pas) ; studio-templates : `list_editor_templates` (URLs
  d'édition directes, consulter avant de créer un doublon).
- tests/evals.md : non-régression (2 scénarios existants).

## 1.1.2 — 2026-07-10

- `animation-client` aligné sur la spécification détaillée (le skill
  existait depuis la 1.1.0 — écarts textuels uniquement, comportement
  inchangé) : description au mot près ; résultats de sondage = taux de
  participation + scores PAR QUESTION + synthèse des verbatims en
  3 ENSEIGNEMENTS ; cadre FR des jeux concours complété (règlement déposé,
  renvoi vers un professionnel du droit — jamais jouer au juriste) ;
  fidélité = 3 actions de rétention nommées (relance douce des points
  dormants, récompense des top clients, réactivation) ; renvoi croisé
  explicite vers la routine R6 GROWTH-LOOP (rapido-startup) qui lit les
  sondages en cours en phase SENSE.

## 1.1.1 — 2026-07-10

- Correction documentaire (audit) : note « FoodEatUp-only » de
  devis-facture-relance mise à jour — `update_invoice_status` (FoodEatUp) a
  désormais un enum élargi (brouillon, en_attente, envoyee, acceptee,
  refusee, litige, payee, annulee) et le serveur valide lui-même les
  transitions DGFiP (ne pas pré-filtrer, relayer l'erreur serveur). La
  logique CRM du skill est inchangée.

## 1.1.0 — 2026-07-10

- Skill `animation-client` : sondages (list_sondages → modèle existant →
  lancer_sondage_entreprise, résultats via get_sondage_resultats avec
  synthèse des verbatims), jeux concours (list_jeux_concours →
  lancer_jeu_concours_entreprise, rappel systématique du cadre légal FR :
  règlement, gratuité, RGPD), fidélité (get_loyalty_points croisé
  get_top_clients → actions de rétention ciblées). Envoi des invitations
  DÉLÉGUÉ à communication-client (masse : campagne-marketing). Schémas
  vérifiés sur le serveur live (modele_sondage_id = sondage_companie.id,
  get_sondage_resultats par id/nom + type companie/client).
- Hook garde-destructif : matcher étendu à lancer_sondage_entreprise et
  lancer_jeu_concours_entreprise (action visible par les clients =
  confirmation forcée, testé stdin).
- `mom-test` : cas d'usage croisé ajouté à la DESCRIPTION (validation
  terrain à l'échelle via animation-client) — corps du skill Wondel
  inchangé, conformément à la règle d'intégration.
- tests/evals.md : scénarios de déclenchement et de comportement.

## 1.0.0 — 2026-07-06

- Première version publique.

## 0.9.0 — 2026-07-06

- Intégration de 3 skills wondelai/skills (MIT, contenu non modifié — skills
  basés sur des livres ; LICENSE dans chaque dossier, provenance ajoutée à
  skills/ATTRIBUTIONS.md) : `predictable-revenue` (machine outbound B2B),
  `negotiation` (empathie tactique, questions calibrées, Ackerman),
  `mom-test` (interviews clients sans biais).

## 0.8.0 — 2026-07-06

- Intégration de 6 skills externes Apache 2.0 depuis
  anthropics/knowledge-work-plugins (commit 564d560c, LICENSE copiée dans
  chaque dossier, provenance tracée dans skills/ATTRIBUTIONS.md) :
  - vente : `pipeline-review-methodo` (renommé depuis pipeline-review pour ne
    pas confondre avec coaching-pipeline), `draft-outreach`,
    `account-research`, `forecast` ;
  - support : `ticket-triage`, `draft-response`.
- Chaque description se termine par « (utilise les données du MCP rapidocrm
  quand elles sont disponibles) » pour croiser la méthode avec les vraies
  données CRM.

## 0.7.0 — 2026-07-06

- Passe de portabilité : devise lue depuis la KB (défaut euros signalé).

## 0.6.0 — 2026-07-06

- Couverture des outils orphelins — 3 nouveaux skills :
  - `contrats-clients` : `create_contrat_template` → `create_contrat`
    (⚠️ send_email TRUE par défaut : validation du destinataire avant appel) →
    `update_contrat_status` (brouillon/en_attente/signe), relance des
    non-signés à la cadence maison ;
  - `agenda-rdv` : `create_rdv` (Visioconférence/Téléphonique/Présentiel avec
    champs conditionnels, mode_envoi SMS/Email confirmé avant),
    `get_today_schedule` (vérification de conflits), `create_evenement` ;
  - `studio-templates` : `create_editor_template` appelé DIRECTEMENT avec le
    HTML (jamais de widget intermédiaire), charte KB imposée dans le HTML/CSS,
    contraintes email-safe pour les newsletters.

## 0.5.0 — 2026-07-06

- Utilisation de la base de connaissance `./rapido-kb/` : règle de chargement
  dans les directives ; `directeur-commercial` : cadence de relance maison
  (processus-internes.md) sinon défaut J+3/J+7/J+15 signalé ;
  `coaching-pipeline` : seuil dormant et cadences maison ;
  `devis-facture-relance` : escalade d'impayés maison sinon J+7/J+21/J+45 ;
  `redaction-commerciale` : arguments depuis propositions-valeur.md,
  objections/parades depuis concurrents.md, ton depuis ton-et-accroches.md.

## 0.4.0 — 2026-07-06

- Script de calcul `skills/coaching-pipeline/scripts/funnel_metrics.py`
  (stdlib) : conversions par étape, maillon faible, deals dormants, valeur
  brute/pondérée — le skill impose « utiliser le script pour tout calcul ;
  ne jamais calculer de tête ».
- `reference/pieges-outils.md` : tableau des pièges (transitions DGFiP,
  company_id/user_id de session, confirm=true pour suppressions, formats de
  dates, message vs template SMS…), référencé par les directives.

## 0.3.0 — 2026-07-06

- Hooks déterministes (`hooks/hooks.json` + `hooks/scripts/`) :
  - PreToolUse `garde-destructif` : confirmation forcée (ask) sur `delete_*`,
    `update_contrat_status`, `close_opportunity` et `update_invoice_status` ;
    refus (deny) de toute transition de facture vers un statut non autorisé par
    la table DGFiP encodée dans le script (cibles valides : en_attente, payee,
    en_retard — jamais de retour à brouillon). `update_invoice_status` est
    matché défensivement (outil non exposé par le serveur à ce jour) ;
  - Stop `récap-actions` (hook prompt) : bloque la fin de tour si des écritures
    MCP ont eu lieu sans récapitulatif des IDs dans la réponse.

## 0.2.0 — 2026-07-06

- Ajout de la couche métier :
  - Agents : `directeur-commercial` (funnel, qualification BANT avant devis,
    relances J+3/J+7/J+15, pilotage par objectifs) et `sdr-prospection`
    (ciblage, personnalisation, cadence multicanal, qualification, passage de
    relais au closing).
  - Skills d'expertise : `coaching-pipeline` (revue de deals — dormants, devis
    expirants, étapes engorgées, une action par deal) et
    `redaction-commerciale` (AIDA/PAS, objet < 50 caractères, 1 CTA,
    personnalisation obligatoire, ton par étape du funnel).
- Les agents connaissent et invoquent les skills du plugin au bon moment.

## 0.1.0 — 2026-07-06

- Version initiale : `.mcp.json` (serveur rapidocrm), références
  `directives-outils.md` et `charte-graphique.md`, skills workflow
  `prospection-pipeline`, `campagne-marketing`, `devis-facture-relance`,
  `communication-client`, `performance-commerciale`.
