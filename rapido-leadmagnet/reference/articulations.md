# Articulations — qui fait quoi (l'usine ne duplique rien)

Le plugin **orchestre** des skills existants. Frontières claires pour ne jamais
réécrire ce qui existe.

## Conception vs exécution

- **`rapido-marketing:lead-magnet-machine`** = **CONCEPTION** (7 étapes : problème,
  type, format, nom, consommation, qualité, next step). L'usine **ne re-questionne
  pas** ce qu'elle a déjà validé — elle **lit sa sortie** et fabrique.
- **`rapido-leadmagnet`** (ce plugin) = **EXÉCUTION** : fabrication → page → campagne →
  RH → mesure.

## Tuyauterie inbound

- **`rapido-marketing:machine-inbound`** = la **tuyauterie générale** inbound
  (capture → nurturing → scoring → hand-off). L'usine **s'y branche** (le lead magnet
  est une **source de capture**), elle ne la réécrit pas.
- **`rapido-marketing:lead-scoring`** : le tag `leadmagnet:{slug}` = **signal
  d'engagement** pondéré (à intégrer côté lead-scoring, LM5).

## Landing & formulaire

- **`rapido-lovable:usine-a-landing`** = la **Route B** (défaut LM0) : landing +
  formulaire, soumission → `enregistrer_prospect`. On lui **délègue** la construction
  via un brief `rapido-prompteur:prompt-lovable` (mode B).

## Gate qualité & copy (frameworks maison prioritaires)

- **`rapido-meta-ads:hundred-million-offers`** = les frameworks Hormozi déjà distillés
  → **référence** du gate qualité `fabrication-lead-magnet` (ne pas re-copier les
  frameworks de la source hormozi-offer-audit ; en emprunter la **forme d'audit**).
- Copy de landing : frameworks direct-response (awareness/PAS/PASTOR) **francisés**
  depuis copy-thief, jamais de verbatim.

## Média

- Visuels : `rapidocms:studio-visuel-marque` / `rapido-higgsfield:studio-image-pro`
  via l'agent `rapido-prompteur:directeur-prompts`. Vidéo pub :
  `rapido-higgsfield:usine-video-marketing` (+ `rapido-video:montage-express`).
- PDF : **template HTML du plugin** (`templates/lead-magnet.html`) → rendu PDF
  (pattern charte→template réimplémenté maison, cf. NOTICE).

## Pédagogie (forge — renvois croisés, pas d'exécution)

- `rapido-forge:ideation-lead-magnet` et `rapido-forge:ideation-quiz-generator` =
  **parcours pédagogiques** (apprendre à concevoir). L'usine renvoie vers eux pour
  la théorie ; elle **exécute** sur les données réelles.

## Diffusion & ads

- Organique : `rapidocms:pipeline-contenu-social`, `rapidocms:calendrier-editorial`.
  Payant : `rapido-meta-ads:creatifs-publicitaires` + `lancement-campagne-meta` +
  `pixel-et-retargeting`. Nurturing : séquence via `rapido-marketing:machine-inbound` derrière le
  gate `rapido-marketing:delivrabilite-email`.

## RH

- `rapidorh` : `create-project-tool`, `create-task-list-tool`, `create-task-tool`.
  Suivi délégué à `rapidorh:revue-projet-hebdo`.
