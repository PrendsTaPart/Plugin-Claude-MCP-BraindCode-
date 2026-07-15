---
name: fabrication-lead-magnet
description: Utiliser quand l'utilisateur veut fabriquer un lead magnet déjà conçu — « fabrique le lead magnet », « rédige le guide/la checklist », « produis l'ebook », « crée le PDF du lead magnet ». Du concept validé (lead-magnet-machine) au PDF brandé publié dans la bibliothèque CMS, avec gate qualité. À NE PAS utiliser pour concevoir un lead magnet (lead-magnet-machine) ni pour la page de capture (page-et-capture).
---

# Fabrication du lead magnet

Du **concept validé** au **PDF brandé** dans la bibliothèque CMS. On **fabrique** ce
qui a été **conçu** — on ne conçoit pas ici.

## Étape 0 — contexte + concept

Lire `reference/parcours-lead-magnet.md`, `reference/garde-fous-leadmagnet.md`, et la
**sortie de `rapido-marketing:lead-magnet-machine`** (problème, type, format, nom,
consommation, qualité, next step). **Si cette sortie est absente → invoquer d'abord
`lead-magnet-machine`** : on ne fabrique pas un lead magnet non conçu. Charger la
charte : `get_brand` (CMS) + `rapido-kb/` (ton, charte).

## 1. Rédaction selon le TYPE choisi en conception

Frameworks de format francisés de content-vault (attribution `NOTICE.md`) — le
**format est une décision** prise en conception, pas ici :

- **checklist actionnable**, **guide court** (8-15 pages), **template/modèle à
  remplir**, **calculateur** (déléguer un artefact ou une page Lovable),
  **mini-cours email** (déléguer `rapido-marketing:machine-inbound`), **quiz**
  (déléguer `rapido-forge:ideation-quiz-generator`).

Règles maison : **français impeccable** ; **promesse du titre tenue dès la page 2** ;
**une action concrète par section** ; **CTA final** vers l'étape suivante du funnel
(RDV / démo / essai). Preuves/chiffres = **données réelles** uniquement, jamais
inventées.

## 2. GATE QUALITÉ (bloquant) — avant toute mise en page

Auditer le contenu avec la **forme d'audit** adaptée de hormozi-offer-audit, en
s'appuyant sur les frameworks **maison** `rapido-meta-ads:hundred-million-offers`
(ne pas re-copier les frameworks) : score sur la **Value Equation** (résultat rêvé,
probabilité perçue, délai, effort) + spécificité + rapidité de consommation.
**Afficher le score**, lister les corrections. **On ne met en page qu'un contenu qui
passe le gate** — sinon corriger et re-auditer.

## 3. Mise en page PDF brandée

Réimplémentation maison du pattern `charte → template → PDF` (cf. `NOTICE.md`) :

- Remplir `templates/lead-magnet.html` avec la charte (couleurs hex, police mappée,
  logo depuis `get_brand`) et le contenu (sections, CTA).
- Rendre en **PDF** depuis ce HTML (renderer local : chromium headless
  `--print-to-pdf`, weasyprint, ou l'outil PDF disponible). Le template est
  **print-ready** (A4, `@page`). Sans renderer disponible : le dire (dégradation
  propre) et livrer le HTML.
- **Couverture** : visuel/mockup 3D du document délégué à
  `rapidocms:studio-visuel-marque` (ou `rapido-higgsfield:studio-image-pro` via
  l'agent `rapido-prompteur:directeur-prompts`) — **aucun texte incrusté généré**
  (politique anti-IP prompteur).

## 4. Publication dans la bibliothèque

`upload_file_tool` (CMS) → bibliothèque de la marque → **vérifier l'URL publique**
(`file_url`) en testant le téléchargement (`list_all_files` type `doc`). Consigner
dans **`rapido-kb/marketing/lead-magnets.md`** (registre : slug, type, URL, date,
version). Cette URL est le **lien de livraison** utilisé par `page-et-capture`.

## Passerelles

Concept absent → `rapido-marketing:lead-magnet-machine`. PDF prêt → `page-et-capture`
(landing + capture). Visuels → `rapidocms:studio-visuel-marque`.

## Règles

- **On ne fabrique pas sans conception validée** (gate d'entrée).
- **Gate qualité bloquant** avant mise en page.
- Charte via `get_brand` + KB ; **rien d'inventé** ; attribution MIT (`NOTICE.md`).
- URL du PDF **vérifiée** avant de déclarer le livrable prêt.
