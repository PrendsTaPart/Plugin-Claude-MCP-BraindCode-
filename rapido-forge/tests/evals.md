# Évals — plugin rapido-forge (1.0.0)

Scénarios de déclenchement et de routage. À rejouer manuellement (ou via un
futur harnais) : la phrase doit router vers l'agent/skill attendu.

## 12 cas positifs (3 par agent)

| # | Phrase | Attendu |
|---|---|---|
| P1 | « Par où je commence avec mon idée ? » | `directeur-programme` (diagnostic de maturité → routage parcours) |
| P2 | « Quel est mon prochain exercice ? » | `directeur-programme` (lecture du journal `./rapido-kb/startup/forge/parcours.md` → prochain skill) |
| P3 | « Fais le point sur mon parcours forge » | `directeur-programme` (bilan : exercices faits/restants par parcours) |
| P4 | « On démarre le bootcamp » | `mentor-bootcamp` (jour 1, timeboxé) |
| P5 | « Jour 3 du bootcamp : mon business model » | `mentor-bootcamp` → `bootcamp-bmc-complete` |
| P6 | « Prépare ma certification de fin de bootcamp » | `mentor-bootcamp` → `bootcamp-certification-b5` |
| P7 | « J'ai une idée mais rien validé » | `mentor-ideation` (début de roadmap idéation) |
| P8 | « Comment tester mon idée sans produit ? » | `mentor-ideation` → skills de validation (`ideation-*`) |
| P9 | « Mon landing page d'idéation est prête, la suite ? » | `mentor-ideation` (exercice suivant de la roadmap) |
| P10 | « On a des clients payants, on passe à l'échelle » | `mentor-scale` (roadmap scale) |
| P11 | « Prépare ma levée » | `mentor-scale` → skills financement (`scale-*`) |
| P12 | « Structure mon équipe design pour scaler » | `mentor-scale` → `scale-design-system` (renvoi `rapido-lovable:frontend-design`) |

## 8 cas négatifs (doivent router vers un AUTRE plugin)

| # | Phrase | Attendu (PAS rapido-forge) |
|---|---|---|
| N1 | « Crée un post LinkedIn » | rapidocms (`pipeline-contenu-social`) |
| N2 | « Relance mes impayés » | rapidocrm (`devis-facture-relance`) |
| N3 | « Lance R4 » | rapido-startup (`loop-engine-v2`) |
| N4 | « Mon briefing du matin » | foodeatup (`briefing-du-jour`) |
| N5 | « Rédige mon business plan pour la banque » | rapido-startup (`interview-business-plan`) — forge = exercices, pas le document financeur |
| N6 | « Qui est surchargé dans l'équipe ? » | rapidorh (`detection-surcharge`) |
| N7 | « Calcule mon MRR » | rapido-startup (`catalogue-kpi`) |
| N8 | « Automatise l'envoi du récap hebdo » | rapido-n8n (`usine-automatisations`) |

## 5 cas de routage inter-parcours (directeur-programme)

| # | Contexte + phrase | Attendu |
|---|---|---|
| I1 | Fondateur AVEC revenus récurrents : « on démarre le bootcamp » | `directeur-programme` PROPOSE le parcours scale (diagnostic > demande brute) — bootcamp seulement s'il confirme |
| I2 | Aucune validation terrain : « prépare ma levée » | Redirection vers idéation/validation d'abord (lever sans traction = prématuré), expliqué factuellement |
| I3 | Bootcamp terminé (journal à jour) : « et maintenant ? » | Proposition roadmap idéation ou scale selon les revenus consignés dans la KB |
| I4 | Milieu de roadmap idéation : « je veux faire l'exercice de pricing scale » | Autorisé mais SIGNALÉ (hors séquence) ; le journal note le saut |
| I5 | Projet inconnu (pas de `./rapido-kb/startup/forge/`) : « quel est mon prochain exercice ? » | `directeur-programme` lance le diagnostic AVANT de répondre — jamais de recommandation sans état des lieux |

## Garde-fous (testés stdin par scripts/tester-skills.py)

- `garde-ecriture-kb.py` : Write `./rapido-kb/startup/forge/...` → allow ;
  Write dans le dépôt → deny ; Write `/tmp/...` → allow.
- `rappel-argent-reel.py` : `ads_create_campaign` → ask (création PAUSED,
  activation après accord explicite).
