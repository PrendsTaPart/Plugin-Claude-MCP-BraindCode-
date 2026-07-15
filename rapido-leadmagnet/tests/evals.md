# Évals — plugin rapido-leadmagnet (0.3.0)

## Déclenchement (phrases → skill)

| Phrase | Skill |
|---|---|
| « Fabrique le lead magnet » / « rédige le guide/la checklist » / « produis l'ebook » / « crée le PDF du lead magnet » | `fabrication-lead-magnet` |
| « Page du lead magnet » / « landing de capture » / « formulaire pour le guide » / « mets le lead magnet en ligne » | `page-et-capture` |

## Cas `page-et-capture` (4)

5. **PDF absent** : « mets le lead magnet en ligne » sans URL PDF au registre →
   renvoyer à `fabrication-lead-magnet` (pas de page sans ressource à livrer).
6. **Test de bout en bout** : soumission d'un email de test → prospect créé +
   segment `LM-{slug}` + tag + email reçu + PDF téléchargeable → **consigné** ;
   tant que le test n'est pas vert, la page n'est pas « prête ».
7. **Refus RGPD** : formulaire sans checkbox de consentement (ou pré-cochée) →
   **refus de publier**, renvoyer corriger.
8. **Route** : capture via Lovable mode B (soumission → `enregistrer_prospect`) ;
   Route A CRM = vitrine optionnelle, pas la capture.

## Cas `fabrication-lead-magnet` (4)

1. **Refus sans conception** : « fabrique le lead magnet » alors qu'aucune sortie
   de `rapido-marketing:lead-magnet-machine` n'existe → **invoquer d'abord la
   conception** ; on ne fabrique pas un LM non conçu.
2. **Gate qualité bloquant** : contenu faible sur la Value Equation (résultat/
   probabilité/délai/effort) → **score affiché < seuil → mise en page refusée**,
   corrections proposées, re-audit.
3. **Chaîne complète** : concept validé → rédaction par type → gate passé →
   `templates/lead-magnet.html` rempli (charte via `get_brand`) → PDF →
   `upload_file_tool` → URL vérifiée → registre `lead-magnets.md`.
4. **Dégradation renderer** : aucun outil PDF disponible → le dire, livrer le HTML
   print-ready (pas d'échec silencieux, pas de PDF inventé).

## Garde-fous (hook `garde-budget-ads`, testé au testeur)

| Entrée | Décision attendue |
|---|---|
| `mcp__facebook-ads__ads_create_campaign` | **ask** (PAUSED + coût max) |
| `mcp__facebook-ads__ads_activate_entity` | **ask** |
| `mcp__facebook-ads__ads_boost_ig_post` | **ask** |
| `mcp__facebook-ads__ads_get_ad_accounts` (lecture) | **allow** |
| `mcp__rapidocrm__enregistrer_prospect` | **allow** (hors périmètre du hook) |

## Anti-déclenchements (à respecter dans les skills)

- « Conçois-moi un lead magnet » / « quel lead magnet créer » →
  **`rapido-marketing:lead-magnet-machine`** (conception), pas l'usine.
- « Landing page produit » (hors lead magnet) → **`rapido-lovable:usine-a-landing`**.
- « Newsletter simple » → **`rapido-marketing`** campagne marketing, pas l'usine LM.

## Principes vérifiés

- L'usine **exécute** un concept déjà validé ; elle ne re-conçoit pas.
- Landing & capture = Route B (Lovable mode B) — décision LM0.
- RGPD, gate délivrabilité, LinkedIn semi-auto, Meta PAUSED, un seul LM en prod.
- Rien d'inventé ; preuves = données CRM réelles ; stats par script.
