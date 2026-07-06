---
name: studio-templates
description: Utiliser quand l'utilisateur veut créer un template dans l'éditeur RapidoCRM — newsletter, landing page, site web, carte de visite, email marketing ou brochure — à partir d'un design HTML/CSS.
---

# Studio de templates (éditeur RapidoCRM)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (règles communes)
et `${CLAUDE_PLUGIN_ROOT}/reference/charte-graphique.md` — la charte est
IMPOSÉE dans le HTML/CSS produit. KB : `./rapido-kb/charte-graphique.md`
(prioritaire) + `ton-et-accroches.md` si `./rapido-kb/` existe.

## Règle d'appel — IMPORTANTE

Appeler `create_editor_template` DIRECTEMENT avec le HTML généré — ne JAMAIS
créer de widget, bouton ou artifact JavaScript intermédiaire pour injecter le
HTML. L'outil retourne l'URL directe d'édition dans l'éditeur RapidoCRM :
la transmettre à l'utilisateur.

## Workflow

1. **Brief** — type de template (`newsletter` | `site_web` | `landing_page` |
   `carte_visite` | `email_marketing` | `brochure`), objectif, contenu clé
   (titres, sections, CTA).
2. **Charger la charte** — couleurs hex, typos, logo (URLs), ton : KB
   prioritaire, sinon charte générique du plugin (en signalant les sections
   marquées `### À COMPLÉTER` : demander les valeurs manquantes plutôt
   qu'inventer).
3. **Générer le HTML/CSS** aux contraintes du type :
   - newsletter / email_marketing : HTML email-safe (tables ou hybrid, CSS
     INLINE, largeur ~600 px, pile de polices web-safe en secours, un seul
     CTA — règles de `redaction-commerciale`) ;
   - landing_page / site_web : responsive, hiérarchie claire, un objectif de
     conversion par page ;
   - carte_visite / brochure : dimensions print, coordonnées PROFESSIONNELLES
     fournies par l'utilisateur ;
   - partout : codes hex EXACTS de la charte, logo par URL publique, ton de la
     marque dans les textes.
4. **Faire valider le rendu** (structure + textes) par l'utilisateur.
5. **Créer** — `create_editor_template` (`name` explicite ex. « Newsletter
   Été 2026 », `type`, `html` complet, `css` séparé optionnel,
   `description`). Transmettre l'URL d'édition retournée.
6. **Boucler** — le template est réutilisable par les autres skills :
   newsletters (`communication-client`), campagnes (`campagne-marketing`).

## Garde-fous

- Charte imposée : aucune couleur hors palette, aucune police hors typo de
  marque sans demande explicite (et alors mentionnée au récapitulatif).
- Contenu : arguments de `propositions-valeur.md` (source citée), pas de
  promesses inventées ; coordonnées fournies, jamais supposées.
- `delete_editor_template` : confirmation explicite (hook ask).
