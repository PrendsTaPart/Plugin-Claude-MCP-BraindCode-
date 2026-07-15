---
name: campagne-lead-magnet
description: Utiliser quand l'utilisateur veut diffuser un lead magnet déjà en ligne — « lance la campagne du lead magnet », « fais connaître le guide », « diffuse le lead magnet », « campagne de téléchargement ». Diffusion complète : organique (posts + LinkedIn semi-auto), payant (vidéo + Meta PAUSED), nurturing (séquence gated) et mesure (par script). À NE PAS utiliser tant que la page n'est pas live (page-et-capture).
---

# Campagne lead magnet — diffusion complète

Organique + payant + nurturing + mesure. La **page doit être live** ; on fait
**connaître** le lead magnet et on **mesure**.

## Étape 0 — contexte

Lire `reference/parcours-lead-magnet.md`, `reference/garde-fous-leadmagnet.md`, le
registre `rapido-kb/marketing/lead-magnets.md` (**page live exigée** — sinon renvoyer
`page-et-capture`), `rapido-kb/marketing/icp.md` et `benchmarks.md`.

## 1. Organique — campagne CMS + LinkedIn semi-auto

- `create_campagne` (CMS) « LM {nom} » + **série de posts** (déléguer
  `rapidocms:pipeline-contenu-social` et `rapidocms:calendrier-editorial`) : **annonce**,
  **carrousel valeur**, **preuve**, **rappel** — chaque post avec le **lien de la
  landing**. Visuels délégués à `rapidocms:studio-visuel-marque`.
- **LinkedIn « commente pour recevoir »** (décision LM0 : GO **semi-auto**) : post dédié ;
  à chaque relève, **préparer les réponses aux commentaires et les DM** (avec le lien)
  **EN BROUILLONS** — l'**envoi est humain**. **Dédup** des commentaires traités dans
  une **table n8n** (`rapido-n8n` `memoire-operationnelle`). **Jamais** d'Unipile ni
  d'automatisation d'envoi (CGU). Cohérent avec `rapido-marketing:social-selling-linkedin`.

## 2. Payant — vidéo + visuels + Meta PAUSED

- **Vidéo** : déléguer `rapido-higgsfield:usine-video-marketing` (9:16, hook « guide
  gratuit », **`self_ai_disclosure` activé**) + `rapido-video:montage-express` pour
  l'habillage.
- **Visuels ads** : `rapido-meta-ads:creatifs-publicitaires`.
- **Campagne Meta** : `rapido-meta-ads:lancement-campagne-meta` (objectif conversions
  vers la landing, pixel via `rapido-meta-ads:pixel-et-retargeting`) — **TOUT EN
  PAUSED**, **coût max récapitulé**, **activation sur confirmation écrite séparée**
  (hook `garde-budget-ads`).

## 3. Nurturing — séquence gated

Séquence **J0** (livraison, déjà envoyée par `page-et-capture`) / **J2** (valeur
bonus) / **J5** (cas client + CTA RDV) — déléguer `rapido-marketing:machine-inbound`.
**Gate `rapido-marketing:delivrabilite-email` (mode newsletter) OBLIGATOIRE avant
chaque lot** ; envois **confirmés** (hook `garde-envois`). Désinscription honorée
immédiatement (retrait de séquence + tag).

## 4. Mesure — par script

Collecter : soumissions (`get_formulaire_soumissions`), clics CTA (`list_cta`),
téléchargements si disponibles, **dépense ads**. Calculer avec
`scripts/stats_leadmagnet.py` (stdlib, **jamais de calcul de tête**) :

```
python3 "${CLAUDE_PLUGIN_ROOT}/skills/campagne-lead-magnet/scripts/stats_leadmagnet.py" \
  --input docs/campagnes/{slug}/stats.json
```

→ **CPL**, **taux de conversion landing**, **taux de clic CTA**, **conversion vers
RDV** (formules affichées ; dénominateur nul = « — », jamais inventé). Consigner dans
`rapido-kb/marketing/benchmarks.md` + `apprentissages.md`. **Rapport une page** à
**J+7** et **J+30** (proposer la routine n8n récurrente).

## Passerelles

Page pas live → `page-et-capture`. Tuyauterie inbound → `rapido-marketing:machine-inbound`.
Projet/tâches de campagne → `projet-rh-lead-magnet`.

## Règles

- **Meta en PAUSED**, activation confirmée séparément ; **gate délivrabilité** avant
  chaque lot ; LinkedIn **semi-auto** (brouillons).
- **Mesure par script**, formules affichées, **rien d'inventé**.
- `self_ai_disclosure` sur toute vidéo IA diffusée sur Meta.
