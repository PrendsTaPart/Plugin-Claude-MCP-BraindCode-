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
2. Funnel formulaires & CTA (le haut du tunnel, vérifié serveur) :
   `list_formulaires` (stats principales par formulaire),
   `get_formulaire_soumissions` (`formulaire_id` ou `formulaire_nom` : vues,
   clics, taux de conversion, segment lié) pour les formulaires actifs,
   `list_cta` (clics par CTA) — le funnel complet se lit désormais
   vues → clics → soumissions → leads.
3. Sondages en cours : `list_sondages` (participation) puis
   `get_sondage_resultats` (`sondage_id` ou `sondage_nom`, `type` companie |
   client) sur ceux en cours — signal qualitatif à côté des chiffres
   d'acquisition (croiser avec le skill `animation-client`, plugin rapidocrm).
4. Conversion : leads entrés au pipeline (`get_stats_pipeline_global`),
   clients signés, encaissés (Stripe).

## Plan (calculs via catalogue-kpi)

5. CAC par canal, vélocité pipeline, coverage — formules affichées ; taux de
   conversion du funnel formulaires (vues → clics → soumissions) par canal.
6. Verdict de l'expérience de la semaine PASSÉE (growth-experiences.md) :
   hypothèse validée / invalidée / non concluante, sur SA métrique cible.
7. Choisir L'expérience de la semaine (une seule) : hypothèse falsifiable +
   métrique cible + seuil de succès + coût max (plafond KB).

## Act (niveau 1 max)

8. PRÉPARER l'expérience via les skills existants : contenus
   (`calendrier-editorial`, brouillons), campagne (`lancement-campagne-meta`
   — tout en PAUSED, activation = demande explicite + gardes argent réel),
   landing (`usine-a-landing` en plan). Rien ne part ni ne dépense seul.

## Feed

9. `./rapido-kb/startup/growth-experiences.md` : une ligne par expérience
   (date, hypothèse, métrique, seuil, coût, verdict) + journal des routines.
   Canal durablement gagnant → proposer de l'inscrire dans
   processus-internes.md (skill `mise-a-jour-kb`).

## Report

10. Le funnel de la semaine en 5 chiffres (formules — formulaires et CTA
    inclus), verdict de l'expérience passée, signal sondages s'il y en a,
    l'expérience proposée (hypothèse/métrique/seuil/coût) en attente
    d'accord.
