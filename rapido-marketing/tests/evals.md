# Évals — plugin rapido-marketing (0.5.0)

## machine-inbound

| # | Phrase | Attendu |
|---|---|---|
| MI1 | « Mets en place ma machine à leads entrants » | `machine-inbound` : Étape 0 exige `icp.md` (sinon `icp-generator` d'abord) → enchaîne contenu (`calendrier-editorial`/`generation-article-blog`/`geo-optimization`), lead magnet (`lead-magnet-machine` + landing), capture CRM, nurturing, `lead-scoring`, handoff `secretariat-commercial`, mesure une page, projet RH ; tout envoi confirmé |
| MI2 (mode dégradé) | « Fais l'inbound mais je n'ai pas Lovable » | `machine-inbound` : page de capture en **voie 1** `create_editor_template` type landing_page (RapidoCRM), signale l'absence de Lovable, **ne bloque pas** |
| MI3 (anti) | « Écris juste un article de blog » | PAS machine-inbound (orchestrateur) → skill `generation-article-blog` (tâche unitaire) |

## social-selling-linkedin

| # | Phrase | Attendu |
|---|---|---|
| SS1 | « Aide-moi à prospecter sur LinkedIn » | `social-selling-linkedin` : stratégie profil + cadence contenu (déléguée à `pipeline-contenu-social` sur compte perso confirmé) + **scripts DM prêts à copier** personnalisés (get_entreprise/`account-research`) — **jamais envoyés auto** ; suivi `enregistrer_prospect` confirmé |
| SS2 | « Optimise mon profil LinkedIn de fondateur » | `social-selling-linkedin` : headline/à-propos alignés ICP+KB, textes prêts à coller |
| SS3 (anti) | « Programme ce post LinkedIn pour demain » | PAS social-selling → skill `pipeline-contenu-social` (publication programmée) |

## geo-optimization

| # | Phrase | Attendu |
|---|---|---|
| GE1 | « Comment être cité par ChatGPT et Perplexity ? » | `geo-optimization` : checklist GEO sourcée (état de l'art) → audit via `audit_geo.py` → corrections + mise à jour CMS confirmée |
| GE2 | « Audite le GEO de mon article » | `geo-optimization` : `audit_geo.py` → score + critères ok/échec + corrections priorisées (jamais de score de tête) |
| GE3 (anti) | « Écris-moi un article de blog SEO » | PAS geo-optimization (audit) → skill `generation-article-blog` (production) |

## icp-generator

| # | Phrase | Attendu |
|---|---|---|
| IC1 | « Définis mon ICP » | `icp-generator` : analyse des clients gagnés (`list_entreprises`/`get_top_clients`) via `analyse_clients.py` (jamais de tête) → croise KB → `rapido-kb/marketing/icp.md` + critères prospection ; `create_segment` confirmé |
| IC2 | « Quelles entreprises cibler ? » | `icp-generator` : segments priorisés + signaux d'achat + critères de disqualification, fondés sur les données |
| IC3 (anti) | « Décris le persona de mon acheteur » | PAS icp-generator (= entreprise) → skill `bootcamp-persona-deep` / `ideation-persona-maker` (persona = individu) |

## lead-scoring

| # | Phrase | Attendu |
|---|---|---|
| LS1 | « Score mes leads » | `lead-scoring` : modèle 2 axes (fit×engagement) de `scoring.md` → `score_leads.py` sur données CRM réelles → tableau scoré + 3 actions/tranche ; écriture CRM confirmée |
| LS2 | « Quels prospects prioriser cette semaine ? » | `lead-scoring` : tranches chaud/tiède/froid, chaud → RDV via `secretariat-commercial`, froid → réactivation via `campagne-marketing` |
| LS3 (anti) | « Définis les critères de mon client idéal » | PAS lead-scoring → skill `icp-generator` (définit l'axe fit en amont) |

Chaque skill méthodo : 2 déclenchements + 1 anti-déclenchement.

## core-four-strategie

| # | Phrase | Attendu |
|---|---|---|
| CF1 | « Par où je commence pour trouver des clients ? » | `core-four-strategie` : Étape 0 (fiches 01/03/05/08 + garde-fous) → diagnostic ressources → recommande **UN** canal + cadence (règle des 100) ; délègue l'exécution |
| CF2 | « Ma pub marche, comment je scale ? » | `core-four-strategie` : More Better New (plus → mieux → nouveau) + critère de maîtrise avant d'ajouter un canal ; scaling pub délégué à `lancement-campagne-meta` |
| CF3 (anti) | « Écris-moi le cold email » | PAS core-four-strategie → skill d'exécution `redaction-commerciale` (rapidocrm) |

## lead-magnet-machine

| # | Phrase | Attendu |
|---|---|---|
| LM1 | « Je veux un cadeau gratuit pour capter des emails » | `lead-magnet-machine` : 7 étapes, type (révéler/échantillon/étape), **nom** résultat+délai+public ; capture déléguée (landing + formulaires) |
| LM2 | « Trouve un meilleur nom pour mon ebook gratuit » | `lead-magnet-machine` : formule de nommage, 3 propositions, plan de distribution |
| LM3 (anti) | « Génère le visuel de couverture » | PAS lead-magnet-machine → skill `studio-visuel-marque` (rapidocms) |

## money-math-acquisition

| # | Phrase | Attendu |
|---|---|---|
| MM1 | « Combien je peux dépenser pour acquérir un client ? » | `money-math-acquisition` : cadre LTGP/CAC/ratio ; **calcul délégué à `catalogue-kpi`** (jamais de tête) ; verdict scaler/corriger |
| MM2 | « Mon ratio LTGP:CAC est-il bon ? » | `money-math-acquisition` : seuils 3:1, données via `get_revenue_summary`/`list_depenses`, formule affichée |
| MM3 (anti) | « Fais ma prévision de trésorerie sur 90 jours » | PAS money-math → skill `cash-flow-snapshot` (rapido-suite) |

## lead-getters-systeme

| # | Phrase | Attendu |
|---|---|---|
| LG1 | « Je veux un programme de parrainage » | `lead-getters-systeme` : bienveillance d'abord, mécanique mutuelle traçable ; exécution déléguée à `animation-client` (rapidocrm) |
| LG2 | « Comment faire générer des leads par mes clients ? » | `lead-getters-systeme` : choix du type (clients→employés→affiliés→agences) selon maturité |
| LG3 (anti) | « Lance une pub Meta » | PAS lead-getters → skill `lancement-campagne-meta` (rapido-meta-ads) |

## Garde-fous transverses (rappel)
- Tout envoi/publication/activation → hook `garde-envois` (confirmation forcée).
- RGPD (consentement/effacement) avant séquence ou audience.
- KPI/score par script (`catalogue-kpi`), jamais de tête.
