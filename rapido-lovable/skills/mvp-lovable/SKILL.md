---
name: mvp-lovable
description: Utiliser quand l'utilisateur veut un site/MVP multi-pages complet sur Lovable — « crée le MVP sur Lovable », « site complet pour [client] », « série de prompts Lovable pour l'app », « développe le produit sur Lovable ». Spec-driven : cadrage validé → série de prompts étagés P1-P8 avec critères d'acceptation. À NE PAS utiliser pour un brief one-shot (prompt-lovable), une landing seule (usine-a-landing) ou un site restaurant (site-restaurant).
---

# MVP Lovable — spec-driven, série P1-P8

Du **brief au MVP livré**. `rapido-prompteur:prompt-lovable` = **UN** brief one-shot
(landing, page simple) ; **ce skill** = la **SÉRIE COMPLÈTE** pour un site/MVP
multi-pages. `usine-a-landing` et `site-restaurant` = **cas verticaux** — y router si le
besoin correspond exactement.

## Étape 0 — contexte

Lire `reference/regles-stack-lovable.md`, `reference/gate-securite.md`, et
`reference/kit-connecteur-mcp/` si une intégration MCP est prévue. Charger la charte
(`get_brand` + `sync-marque-lovable`).

## 1. SPEC d'abord (validée AVANT tout prompt)

Mini-cadrage via `templates/spec-mvp.md` : cible, **3-5 pages/features**, données,
**intégration MCP oui/non**, design. Écrire dans `docs/specs/{projet}.md` → **validée par
l'utilisateur** avant d'écrire le moindre prompt Lovable (méthode spec-driven, cf.
`NOTICE.md`). Pas de spec validée → pas de prompt.

## 2. Design system

Charte du client (`get_brand` + `sync-marque-lovable`) + choix de style **délégué à
`ui-ux-pro-max`** → **figé dans la spec** (couleurs hex, typos, composants shadcn).

## 3. Générer la SÉRIE P1…P8 (adaptée au périmètre)

Chaque prompt : contexte minimal, **interdits** rappelés, **critères testables** de done.
Règles de stack (`regles-stack-lovable`) injectées.

- **P1** — Fondations : structure, design system, règles de stack.
- **P2-P4** — Pages/features par lot (une par prompt), critères de done.
- **P5** — Données & formulaires : **mode B** → soumission `enregistrer_prospect` si CRM.
- **P6** — Agent embarqué (si MCP) : **DÉLÉGUER à `connecteur-mcp-lovable`** (le kit fait
  foi ; on ne réimplémente pas le branchement ici).
- **P7** — SEO / performances / accessibilité.
- **P8** — Recette + **gate sécurité** (`gate-securite.md`) + mise en ligne **sur
  confirmation**.

## 4. Exécution assistée (optionnelle, confirmée)

`send_message` **étape par étape** (consomme des crédits — cadrer), **vérification entre
chaque** (`get_diff`, `read_file`), **jamais deux étapes sans contrôle**. Déploiement /
mise en ligne **uniquement sur confirmation explicite**.

## 5. Livraison & capitalisation

Spec + série archivées dans `rapido-kb/lovable/projets/{slug}.md`. **Apprentissages**
consignés (ce qui a demandé des itérations → améliore le kit / les règles de stack).

## Passerelles & anti-collisions

- Landing simple → `usine-a-landing`. Site restaurant → `site-restaurant`. Brief one-shot
  → `rapido-prompteur:prompt-lovable`. Artefact HTML → `web-artifacts-builder`.
- Branchement MCP → `connecteur-mcp-lovable` (jamais réimplémenté ici).

## Règles

- **Spec validée avant tout prompt** ; **rien d'inventé** (contenu réel ou placeholder
  explicite) ; gate sécurité **bloquant** ; mise en ligne **confirmée**.
