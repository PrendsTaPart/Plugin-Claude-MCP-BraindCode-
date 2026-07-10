# R9 — VIDEO-FACTORY (l'épisode vidéo du jour)

```yaml
# CONFIG — interchangeable par client (les valeurs de ./rapido-kb/ PRIMENT)
routine: R9-VIDEO-FACTORY
cadence: quotidienne (jours ouvrés) — ou au rythme éditorial de la KB
perimetre: [rapidocms]                # + hyperframes via le skill video-marketing
depot_production: PrendsTaPart/Video  # dépôt Git des compositions/scripts d'épisodes
serie: rapido-kb/ton-et-accroches.md  # format, ton, durée cible des épisodes
autonomie: niveau 1 max — TOUT est préparé ; le RENDU (payant) et la
           PUBLICATION restent des accords explicites — reference/autonomie.md
silence_si_vert: false
```

> Routine rédigée depuis la spec (nom et déclencheurs fournis, contenu détaillé
> du master plan non fourni — à réconcilier s'il diverge).

## Sense (lecture seule)

1. **Épisode du jour** : sujet depuis le calendrier éditorial
   (`calendrier-editorial`, plugin rapidocms) ou la série définie dans la KB ;
   vérifier ce qui est déjà sorti (`list_scheduled_posts`) pour ne pas
   doubler un épisode.
2. **Marque cible et assets** : résoudre la marque (agent
   `gestionnaire-marques` si multi-marques), charger `get_brand` + les logos
   depuis les ASSETS de marque (`list_all_files` search `"<Marque> — logo"`)
   — jamais un logo improvisé.
3. **Matière** : performances des épisodes précédents (`post_insights`, lots
   de 10) — quel angle/format a marché.

## Plan

4. Écrire le BRIEF de l'épisode : accroche, structure (hook 3 s → corps →
   CTA), texte incrusté éventuel (protocole zéro faute :
   `prompts-visuels-pro`), durée cible et déclinaisons par réseau.
5. Le scénario/composition de l'épisode vit dans le **dépôt de production
   `PrendsTaPart/Video`** (CONFIG `depot_production`) : partir du gabarit
   d'épisode existant du dépôt, produire la nouvelle composition/le nouveau
   script d'épisode, et le COMMITTER dans ce dépôt (pas dans la marketplace) —
   c'est la mémoire de la série.

## Act (niveau 1 max — préparation)

6. Déléguer la fabrication au skill `video-marketing` (plugin rapidocms) :
   compose → get_project_status (polling au rythme `retry_after_seconds`) →
   PREVIEW soumise à validation. **Le RENDU (`render_video`) est PAYANT :
   niveau 3, jamais lancé par la routine** — il attend l'accord explicite
   sur la preview.
7. Préparer le post d'accompagnement (brouillon `create_draft_tool` par
   réseau, caption depuis la KB) — PLANIFIÉ seulement après accord
   (`schedule_draft_tool`).

## Feed

8. Journal `./rapido-kb/startup/routines-journal.md` (date, épisode, statut :
   brief / preview / rendu / publié) + registre de série
   `./rapido-kb/startup/videos-episodes.md` (une ligne par épisode : sujet,
   angle, lien preview, verdict perfs à J+7). Commit de la composition dans
   `PrendsTaPart/Video` avec le numéro d'épisode.

## Report

9. Une page : l'épisode du jour (sujet, angle, où en est la chaîne
   brief → preview → rendu → publication), ce qui attend un accord (preview
   à valider, rendu à payer, planification), et la perf J+7 de l'épisode
   précédent (chiffres via `post_insights`, formule affichée si calcul).
