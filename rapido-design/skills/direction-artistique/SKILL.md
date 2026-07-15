---
name: direction-artistique
description: Utiliser quand l'utilisateur veut définir l'identité visuelle d'un projet — « direction artistique », « moodboard », « quel style pour [projet] », « définis l'identité visuelle du site », « charte du projet ». Propose 3 directions filtrées par le jugement design, formalise la retenue et synchronise la charte CMS. À NE PAS utiliser pour un simple choix de style (ui-ux-pro-max) ni un visuel de post (studio-visuel-marque).
---

# Direction artistique (DA ↔ charte CMS)

Définit l'**identité visuelle** d'un projet et la **synchronise avec la charte CMS**
(source de vérité). Le fil rouge des tokens démarre ici.

## Étape 0 — jugement + charte existante

Lire `reference/jugement-design.md` (anti-goût-IA, quand dire non),
`reference/passerelles.md`, `reference/pipeline-design.md`. **Charger la charte
existante** : `get_brand` (CMS) + `charte-graphique.md` (KB). **Si le projet/client a déjà
une charte, elle S'IMPOSE** — on la **décline**, on ne la réinvente pas (on ne propose de
nouvelles directions que pour une marque neuve ou une refonte assumée).

## 1. Exploration — 3 directions

Proposer **3 directions** via `rapido-lovable:ui-ux-pro-max` (styles + palettes + paires de
fonts), **filtrées par le jugement design** et le secteur (principe « la marque comme
input »). Chaque direction :
- **intention** en 2 lignes ;
- **palette** (5-6 tokens nommés, hex, contraste AA visé) ;
- **typo** (1-2 familles ; ⚠️ voir § police des passerelles — le CMS ne stocke que 9
  web-safe, la vraie police vit dans le DS) ;
- **un écran de principe** généré dans Figma (`figma-generate-design`) — pour **voir**,
  pas seulement lire.

## 2. Choix + formalisation

Direction retenue → **mini-charte projet** : tokens **nommés** (couleurs, typo, spacing),
règles d'usage, **do / don't**. Écrite dans le fichier Figma, page **« Fondations »**
(base du design system de `studio-maquette`).

## 3. Sync CMS (après confirmation — CMS = source de vérité)

- **Marque neuve** : `create_brand` (nom, langue, slogan, `couleurs` hex, `font_family`
  = la **plus proche des 9**) + `upload_file_tool` (logo/assets officiels).
- **Marque existante que la DA fait évoluer** : `edit_brand` (couleurs/logo/slogan)
  **après confirmation**.
- Toujours consigné dans `charte-graphique.md` (KB), avec la **vraie police** notée (celle
  du DS Figma/Lovable) et la correspondance CMS (9 web-safe).

## Passerelles

Maquettes/DS → `studio-maquette`. Sitemap/flows → `architecture-info`. Style seul →
`rapido-lovable:ui-ux-pro-max`. Visuel de post → `rapidocms:studio-visuel-marque`.

## Règles

- **Charte existante prime** (on décline, on ne réinvente pas).
- **CMS = source de vérité** ; écriture charte **confirmée**.
- **Jugement design** appliqué (anti-goût-IA) ; **tokens nommés** dès la DA (fil rouge).
- Rien d'inventé ; pas de copie de la langue de design d'une marque tierce.
