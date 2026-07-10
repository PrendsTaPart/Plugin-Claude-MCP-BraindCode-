# WBS startup France — référentiel ~120 tâches en 6 phases

À ADAPTER au business plan (vertical, équipe, budget, stade) avant toute
création — voir SKILL.md. Durées types en jours ouvrés (j) ou semaines (sem),
à titre indicatif. « Dépend de » = tâches à terminer avant. Les tâches
marquées ⚖️ touchent au légal : faire valider par un professionnel (ceci
n'est pas un conseil juridique). Les tâches « → skill X » s'exécutent en
invoquant le skill, pas en refaisant sa logique.

## Phase 1 — Juridique & admin (J)

| # | Tâche | Dépend de | Durée type |
|---|---|---|---|
| J1 | Choisir la forme juridique (SAS/SASU/SARL/EI…) selon associés, régime social, levée prévue ⚖️ | BP §2 | 3 j |
| J2 | Rédiger le pacte d'associés (vesting, sortie, non-concurrence) ⚖️ | J1 | 1 sem |
| J3 | Rédiger les statuts ⚖️ | J1 | 3 j |
| J4 | Choisir la domiciliation (siège social) | J1 | 2 j |
| J5 | Déposer le capital (attestation de dépôt) | J3, J4 | 3 j |
| J6 | Publier l'annonce légale | J3 | 1 j |
| J7 | Immatriculer via le Guichet unique (INPI) → Kbis/SIREN | J5, J6 | 1-2 sem |
| J8 | Ouvrir le compte bancaire professionnel définitif | J7 | 1 sem |
| J9 | Choisir l'expert-comptable et signer la lettre de mission | J1 | 1 sem |
| J10 | Souscrire la RC professionnelle | J7 | 3 j |
| J11 | Souscrire multirisque locaux / cyber selon activité | J7 | 3 j |
| J12 | Prévoyance / mutuelle dirigeant (madelin si TNS) ⚖️ | J7 | 1 sem |
| J13 | Déclarer aux caisses sociales (URSSAF, retraite) — souvent auto via Guichet | J7 | 1 j |
| J14 | Options fiscales : régime TVA, IS, exercice comptable ⚖️ | J9 | 2 j |
| J15 | Déposer la marque à l'INPI (classes pertinentes) | BP §3 | 3 j |
| J16 | Réserver domaines + boîte mail pro | — | 1 j |
| J17 | RGPD : registre des traitements | P/G premiers outils | 2 j |
| J18 | RGPD : politique de confidentialité + bandeau cookies | J17 | 2 j |
| J19 | Rédiger CGV/CGU ⚖️ | J1, BP §6 | 1 sem |
| J20 | Mentions légales du site | J7, J16 | 0,5 j |
| J21 | Contrats fournisseurs/sous-traitants critiques ⚖️ | BP §8 | 1 sem |
| J22 | Classer tous les documents fondateurs (coffre — plugin rapido-direction si installé) | J7 | 0,5 j |

## Phase 2 — Produit (P)

| # | Tâche | Dépend de | Durée type |
|---|---|---|---|
| P1 | Extraire les specs MVP du BP (périmètre MINIMAL qui teste la PVU) | BP §3, §6 | 2 j |
| P2 | Prioriser la roadmap depuis le BP (6 mois détaillés / 18 mois en blocs) | P1 | 2 j |
| P3 | Choisir la stack et les outils de dev | P1 | 2 j |
| P4 | Maquettes des parcours clés | P1 | 1 sem |
| P5 | Mettre en place repo, environnements, CI | P3 | 2 j |
| P6 | Développer le MVP — lot 1 (cœur de la PVU) | P4, P5 | 3-6 sem |
| P7 | Hébergement, nom de domaine produit, TLS | P3, J16 | 1 j |
| P8 | Sauvegardes + plan de reprise minimal | P7 | 1 j |
| P9 | Sécurité de base (authentification, secrets, accès) | P6 | 3 j |
| P10 | Analytics produit (événements d'activation) | P6 | 2 j |
| P11 | Recruter 5-10 beta-testeurs dans la cible (depuis persona BP §3) | P1 | 2 sem |
| P12 | Programme beta : accès, canal de feedback, cadence | P6, P11 | 3 j |
| P13 | Interviews beta (règles Mom Test — skill `mom-test`) | P12 | 2 sem |
| P14 | Itérations MVP depuis le feedback (lot 2) | P13 | 2-4 sem |
| P15 | CGU produit + conformité RGPD produit (données traitées) | J17, P6 | 3 j |
| P16 | Documentation d'aide / FAQ support | P14 | 3 j |
| P17 | Critères de sortie beta → v1 (chiffrés : activation, rétention) | P12 | 1 j |
| P18 | Go/no-go v1 avec les critères P17 | P14, P17 | 0,5 j |

## Phase 3 — Go-to-market (G)

| # | Tâche | Dépend de | Durée type |
|---|---|---|---|
| G1 | Figer positionnement et messages (PVU du BP §3, pitch §7) | BP | 2 j |
| G2 | Identité visuelle / charte → `./rapido-kb/charte-graphique.md` | G1 | 1 sem |
| G3 | Site vitrine ou landing de lancement → skill `usine-a-landing` (plugin rapido-lovable) | G1, G2, J20 | 3 j |
| G4 | SEO de base : titres, meta, plan du site, Search Console | G3 | 2 j |
| G5 | Créer les profils sociaux (comptes connectés RapidoCMS) | G2 | 1 j |
| G6 | Calendrier éditorial du lancement → skill `calendrier-editorial` (plugin rapidocms) | G1, G5 | 2 j |
| G7 | Produire les contenus du mois 1 (posts, visuels) → skills rapidocms | G6 | 1 sem |
| G8 | Construire la liste de prospection cible → skill `prospection-pipeline` (plugin rapidocrm) | BP §7 | 3 j |
| G9 | Séquence de premier contact → skill `redaction-commerciale` | G1, G8 | 2 j |
| G10 | Paramétrer le pipeline CRM (étapes, segments) | G8 | 1 j |
| G11 | Les 10 premiers clients : plan nominatif (BP question 7.2) | G8 | 1 j |
| G12 | Poser le pixel / tracking conversions → skill `pixel-et-retargeting` (plugin rapido-meta-ads) | G3 | 2 j |
| G13 | Première campagne payante (si budget) → skill `lancement-campagne-meta` — plafond KB respecté | G3, G7, G12 | 3 j |
| G14 | Offre de lancement (prix, durée, conditions — sourcées BP §6) | G1 | 1 j |
| G15 | Inscriptions annuaires/plateformes du secteur | G3 | 1 j |
| G16 | Kit presse + 5 médias/newsletters du secteur | G1, G3 | 3 j |
| G17 | Partenariats prescripteurs : 3 premiers contacts | BP §7 | 2 sem |
| G18 | Mesure d'acquisition : UTM, sources dans le CRM | G3, G10 | 1 j |
| G19 | Boucle avis clients / témoignages (dès les premiers clients) | G11 | continu |
| G20 | Bilan GTM mois 1 : CAC réel vs BP → skill `catalogue-kpi` | G13, G18 | 0,5 j |

## Phase 4 — Finance (F)

| # | Tâche | Dépend de | Durée type |
|---|---|---|---|
| F1 | Générer le prévisionnel 36 mois → skill `plan-financier-previsionnel` | BP §9 | 1 j |
| F2 | Ouvrir le compte Stripe (KYC, compte pro) | J7, J8 | 3 j |
| F3 | Configurer produits/prix dans Stripe (écritures = confirmation, hors routine) | F2, BP §6 | 1 j |
| F4 | Chaîne de facturation : devis → facture → relance (mentions légales FR) → skill `devis-facture-relance` | J14, F2 | 2 j |
| F5 | Templates devis/factures conformes ⚖️ | F4 | 1 j |
| F6 | Process de relance d'impayés (calendrier d'escalade → KB) | F4 | 1 j |
| F7 | Outil comptable connecté + flux vers l'expert-comptable | J9, F2 | 2 j |
| F8 | Dossier Bourse French Tech / BPI (si éligible — BP en pièce maîtresse) | BP, F1 | 2 sem |
| F9 | CII / CIR : qualification avec l'expert-comptable ⚖️ | J9, P6 | 1 sem |
| F10 | Statut JEI : vérifier l'éligibilité (R&D, âge, effectif) ⚖️ | J9 | 3 j |
| F11 | Aides régionales / concours : shortlist et calendrier | BP | 3 j |
| F12 | Prêt d'honneur (réseaux type Initiative/Entrepreneurs) : dossier | BP, F1 | 2 sem |
| F13 | Tableau de bord financier mensuel → skill `catalogue-kpi` (MRR, burn, runway, DSO) | F1, F2 | 1 j |
| F14 | Suivi de trésorerie hebdo (réel vs prévisionnel) | F13 | continu |
| F15 | Seuils maison dans `./rapido-kb/processus-internes.md` (plafonds, cibles) → skill `mise-a-jour-kb` | F1 | 0,5 j |
| F16 | Point mort : suivre le mois de croisement réel vs plan | F13 | mensuel |
| F17 | Mise à jour du prévisionnel à chaque jalon (document vivant) | F1 | à chaque jalon |
| F18 | Préparer la data room minimale (statuts, Kbis, BP, prévisionnel, contrats) | J22, F1 | 2 j |

## Phase 5 — RH (R)

| # | Tâche | Dépend de | Durée type |
|---|---|---|---|
| R1 | Organigramme cible 12 mois (depuis BP §2 et §8) | BP | 1 j |
| R2 | Grille salariale + budget masse salariale (chargée ×1,45) | R1, F1 | 2 j |
| R3 | Fiches de poste des recrutements prioritaires → skill `job-post-builder` (plugin rapidorh) | R1 | 1 j/poste |
| R4 | Diffuser les annonces + pipeline candidats → skill `recruiting-pipeline` | R3 | continu |
| R5 | Trames d'entretien → skill `interview-prep` | R3 | 1 j |
| R6 | Promesse d'embauche + contrat de travail ⚖️ | R4 | 3 j |
| R7 | DPAE avant chaque prise de poste ⚖️ | R6 | 0,5 j |
| R8 | Mutuelle + prévoyance collective ⚖️ | R6 | 1 sem |
| R9 | Registre unique du personnel | R7 | 0,5 j |
| R10 | Comptes et accès outils (offboarding prévu dès l'onboarding) | R6 | 0,5 j |
| R11 | Onboarding RapidoRH (permissions → rôle → département → utilisateur) → skill `onboarding-equipe` | R6 | 0,5 j |
| R12 | Plan d'accueil J1/S1/30-60-90 → skill `onboarding-rh-methodo` | R11 | 1 j |
| R13 | Rituels d'équipe : dailies (skill `daily-report`), revue hebdo projet | R11 | continu |
| R14 | BSPCE / intéressement : cadrer avec conseil si prévu au BP ⚖️ | J2 | 2 sem |
| R15 | Suivi de charge → skill `detection-surcharge` (dès 2 personnes) | R13 | hebdo |

## Phase 6 — Pilotage (C)

| # | Tâche | Dépend de | Durée type |
|---|---|---|---|
| C1 | Installer la revue hebdo business → skill `revue-hebdo-business` (plugin rapido-suite) | F13 | 0,5 j |
| C2 | Installer le CODIR mensuel → skill `comite-de-direction` | C1 | 0,5 j |
| C3 | Routine KPI (R4) : lecture hebdo du tableau de bord → skill `catalogue-kpi` | F13 | hebdo |
| C4 | Routine STARTUP-BUILDER (R5) : relire plan-execution.md, créer le delta | ce skill | hebdo |
| C5 | Routines R6-R8 (relances, veille, récap) : déployer via skill `recettes-metier` (plugin rapido-n8n, N8N_MCP_URL requise) | C1 | 2 j |
| C6 | Board mensuel : ordre du jour type (KPI, trésorerie, jalons, risques, décisions) | C2 | 1 j |
| C7 | Jalons du board dans Google Calendar (récurrence mensuelle) | C6 | 0,5 j |
| C8 | Mise à jour mensuelle de 06-traction et 08-roadmap → skill `mise-a-jour-kb` | C2 | mensuel |
| C9 | Revue trimestrielle du BP : hypothèses vs réel (hypotheses.md annotée) | C2, F17 | trimestriel |
| C10 | OKR du trimestre (3 objectifs max, reliés au BP) | C9 | 1 j |
| C11 | Registre des risques : relire la section Risques du BP, mettre à jour les parades | C9 | trimestriel |
| C12 | Rétrospective d'exécution : WBS réel vs prévu, ajuster les durées types | C4 | trimestriel |

**Ordre de déroulé recommandé** : J (bloquant légal) → P et G en parallèle
(G3+ dépend de J20) → F dès J7/J8 → R au rythme du plan de recrutement →
C dès que F13 existe. Total indicatif : 105 tâches cœur + variantes
verticales (restaurant : + carte/HACCP via plugin foodeatup ; services :
+ staffing) — le plan VALIDÉ par le client fait foi, tracé dans
`plan-execution.md`.
