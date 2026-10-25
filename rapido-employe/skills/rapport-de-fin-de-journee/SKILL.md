---
name: rapport-de-fin-de-journee
description: Utiliser quand la journée de l'employé se clôt, que l'utilisateur dit « fais ton rapport du soir », « qu'as-tu fait aujourd'hui », « clôture ta journée ». Dix lignes — appris, préparé, envoyé, dépensé, en attente d'accord — remises au responsable par email_report si le rôle le permet, sinon en brouillon Gmail.
---

# Rapport de fin de journée (dix lignes, pas une de plus)

Famille engagée : **publier** (`email_report`, Aperçu) — repli **preparer**
(brouillon Gmail).

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`. Ce skill
fonctionne MÊME agent arrêté : c'est le seul.

## Workflow

1. **Rassembler les faits du jour** : journal local des écritures
   (`.claude/logs/employe-<date>.jsonl`), KPI enregistrés le matin
   (`get_my_kpis`), missions validées (`get_my_progress`), routines
   journalisées (`list_routines`), dépenses (`get_work_plan`, budget).
2. **Écrire les dix lignes** : ce que j'ai APPRIS (missions, quiz), ce que
   j'ai PRÉPARÉ (brouillons, devis, fiches), ce que j'ai ENVOYÉ (après
   accords — nombre et canal), ce que j'ai DÉPENSÉ (0 si rien), ce qui est
   EN ATTENTE D'ACCORD (liste datée). Chaque ligne factuelle, sourcée du
   journal — rien de « senti ».
3. **Remettre le rapport** :
   - `email_report` (Academy) SI le rôle le permet — l'outil est réservé au
     responsable : en rôle apprenant, il échouera ou n'apparaîtra pas ;
   - sinon **brouillon Gmail** (`create_draft`) adressé au responsable, objet
     « Rapport du <date> — Claude employé » ; l'humain envoie. JAMAIS d'envoi
     Gmail direct (le hook garde-envois le refuse de toute façon).
   - Gmail absent : rapport livré dans la conversation, en le disant.
4. Fin de semaine (vendredi) : ce rapport s'appuie sur la revue du skill
   `boucle-du-vendredi` et son gabarit (`get_report_brief`).

KPI : `objectifs-atteints` (le rapport les confronte).
Formations : `reporting`, `rituels`.

## Garde-fous

- Dix lignes : la discipline du format EST le garde-fou — le détail vit dans
  le journal, pas dans le rapport.
- « En attente d'accord » liste chaque action bloquée par un garde avec sa
  raison : c'est la to-do du responsable, elle ne se perd pas.
- Aucun chiffre sans source (journal, KPI, work plan) ; un compteur absent
  se dit absent.
