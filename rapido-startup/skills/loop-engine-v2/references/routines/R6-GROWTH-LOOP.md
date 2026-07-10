# R6 — GROWTH-LOOP (boucle d'acquisition hebdomadaire)

```yaml
# CONFIG — interchangeable par client (les valeurs de ./rapido-kb/ PRIMENT)
routine: R6-GROWTH-LOOP
cadence: hebdomadaire — jeudi
perimetre: [rapidocms, rapidocrm, stripe]   # + facebook-ads / lovable si plugins installés
experience_par_semaine: 1                    # UNE expérience à la fois
autonomie: niveau 1 max (expérience PRÉPARÉE : brouillons, campagne PAUSED) — reference/autonomie.md
silence_si_vert: false
```

> Prompt rédigé depuis la spec (partie 4 du master plan non fournie).

## Sense (lecture seule)

1. Acquisition de la semaine : contenus `post_insights` (lots de 10),
   campagnes `get_stats_campagne` (CRM) ; si plugins installés : pub
   (rapido-meta-ads, dépense et coût par résultat), analytics web
   (rapido-lovable) — sinon sauter en le mentionnant.
2. Conversion : leads entrés au pipeline (`get_stats_pipeline_global`),
   clients signés, encaissés (Stripe).

## Plan (calculs via catalogue-kpi)

3. CAC par canal, vélocité pipeline, coverage — formules affichées.
4. Verdict de l'expérience de la semaine PASSÉE (growth-experiences.md) :
   hypothèse validée / invalidée / non concluante, sur SA métrique cible.
5. Choisir L'expérience de la semaine (une seule) : hypothèse falsifiable +
   métrique cible + seuil de succès + coût max (plafond KB).

## Act (niveau 1 max)

6. PRÉPARER l'expérience via les skills existants : contenus
   (`calendrier-editorial`, brouillons), campagne (`lancement-campagne-meta`
   — tout en PAUSED, activation = demande explicite + gardes argent réel),
   landing (`usine-a-landing` en plan). Rien ne part ni ne dépense seul.

## Feed

7. `./rapido-kb/startup/growth-experiences.md` : une ligne par expérience
   (date, hypothèse, métrique, seuil, coût, verdict) + journal des routines.
   Canal durablement gagnant → proposer de l'inscrire dans
   processus-internes.md (skill `mise-a-jour-kb`).

## Report

8. Le funnel de la semaine en 5 chiffres (formules), verdict de l'expérience
   passée, l'expérience proposée (hypothèse/métrique/seuil/coût) en attente
   d'accord.
