---
name: page-et-capture
description: Utiliser quand l'utilisateur veut mettre un lead magnet en ligne — « page du lead magnet », « landing de capture », « formulaire pour le guide », « mets le lead magnet en ligne ». Construit la landing (Lovable mode B), le formulaire de capture, le segment et le pipeline CRM, la livraison par email, avec test de bout en bout. À NE PAS utiliser pour fabriquer le PDF (fabrication-lead-magnet) ni pour une landing produit hors lead magnet (usine-a-landing).
---

# Page & capture

La landing, le formulaire, le CTA, le segment, le pipeline et la livraison. **Route B
(Lovable mode B)** par défaut (décision LM0) : la capture est garantie via
`enregistrer_prospect`.

## Étape 0 — contexte + PDF

Lire `reference/parcours-lead-magnet.md`, `reference/garde-fous-leadmagnet.md`, et le
registre **`rapido-kb/marketing/lead-magnets.md`** : **l'URL du PDF est obligatoire**
— si elle manque, renvoyer à `fabrication-lead-magnet`. Charger les frameworks de copy
(structure de landing francisée de copy-thief, cf. `NOTICE.md`).

## 1. Copy de la page

Structure francisée (niveau de conscience du trafic) : **titre bénéfice**, **3 puces
de valeur**, **preuve** (chiffre/témoignage **réel du CRM uniquement — jamais
inventé**), **CTA unique** « Télécharger le guide », **mentions RGPD** (voir §RGPD).
Proposer la structure → validation avant d'écrire la copy complète.

## 2. Construction — Route B (Lovable mode B)

Déléguer à `rapido-lovable:usine-a-landing` via un brief `rapido-prompteur:prompt-lovable`
(**mode B** : la soumission du formulaire appelle `enregistrer_prospect`). Le CTA de
téléchargement pointe l'**URL bibliothèque** du PDF (livraison après capture).
Formulaire minimal (email requis ; nom/entreprise optionnels) + **checkbox de
consentement non pré-cochée**.

> **Route A (option vitrine, non défaut)** : `create_editor_template` type
> `landing_page` (HTML/CSS charte) pour une landing CRM. Les outils de création de
> formulaire et de CTA (create_formulaire / create_cta) **n'existent pas** côté CRM
> (LM0), donc la **capture reste sur Lovable** tant que le câblage natif n'est pas
> confirmé (`docs/OUTILS-MCP-MANQUANTS.md`).

## 3. Branchements CRM

- `create_segment` « **LM-{slug}** » (une fois).
- À **chaque soumission** : `enregistrer_prospect` → `ajouter_prospect_pipeline`
  (étape « Lead entrant ») → **tag `leadmagnet:{slug}`** → ajout au segment
  « LM-{slug} » → `log_activity` (« Lead magnet {slug} téléchargé le {date} »).

## 4. Livraison

Email transactionnel **immédiat** avec le **lien du PDF** : `create_template_email`
(expéditeur de la marque) puis `send_email` (soumis au hook `garde-envois`). Page de
**remerciement** avec le **next step** (RDV / démo). **Double opt-in** si activé en KB :
email de **confirmation AVANT** le lien (le lien n'est livré qu'après clic de
confirmation).

## 5. TEST DE BOUT EN BOUT (obligatoire avant « page prête »)

Soumettre un **email de test** → vérifier : **prospect créé** au bon endroit +
**segment** « LM-{slug} » + **tag** + **email reçu** + **PDF téléchargeable** depuis
l'URL. **Consigner le résultat** du test. Tant que ce test n'est pas vert, la page
n'est **pas** déclarée prête.

## RGPD (bloquant)

Pas de mise en ligne sans : **checkbox de consentement non pré-cochée**, mention claire
de l'échange (« recevez le guide + nos conseils »), lien de désinscription. Un
formulaire sans consentement explicite → **refus** de publier (renvoyer corriger).

## Passerelles

PDF/URL absent → `fabrication-lead-magnet`. Page live → `campagne-lead-magnet`
(diffusion). Tuyauterie inbound générale → `rapido-marketing:machine-inbound`.

## Règles

- Route B (Lovable) = capture garantie ; Route A = vitrine optionnelle.
- **Preuves = données CRM réelles** ; rien d'inventé.
- **Test de bout en bout** avant « prête » ; **RGPD** bloquant ; envois confirmés.
