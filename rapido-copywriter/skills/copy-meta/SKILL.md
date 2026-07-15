---
name: copy-meta
description: Utiliser quand l'utilisateur veut de la copy Facebook ou Instagram pour une page de marque — « post Facebook », « post Instagram », « caption », « carrousel Insta », « copy du Reel ». Grammaires distinctes FB et IG, 3 variantes, passe anti-voix-IA + gate marque, brouillon CMS par compte. À NE PAS utiliser pour LinkedIn (copy-linkedin), TikTok (copy-tiktok) ni le profil perso (social-selling-linkedin).
---

# Copy Meta — Facebook + Instagram

Deux grammaires **distinctes** (FB ≠ IG) dans un seul skill. Pages de **marque**.

## Étape 0 — contexte

Lire `reference/grammaires-reseaux.md` (fiches **Facebook** et **Instagram**),
`reference/banque-hooks.md` (**GAGNANT d'abord**), `reference/anti-voix-ia.md`,
`reference/articulations.md`. Charte : `get_brand` + `rapido-kb/`. Pilier du
`rapidocms:calendrier-editorial` si campagne.

## 1. Brief

Objectif funnel, cible, **preuve réelle** (CRM/CMS — jamais inventée), réseau(x) et
format(s) : **post FB**, **caption IG**, **carrousel IG**, **Reel**, **Stories**.

## 2. Écriture par format (grammaire native)

- **Post Facebook** : **40-120 mots**, natif > lien, **angle local** (résonne pour les
  restaurateurs FoodEatUp), CTA clic doux. 3 variantes (hooks différents).
- **Caption Instagram** : **hook dans les 125 premiers caractères**, **3-8 hashtags
  mixtes** (niche + volume), CTA (enregistrer/partager). 3 variantes.
- **Carrousel IG** : **6-10 slides** à valeur (1 idée/slide) → structure livrée, visuel
  délégué à `rapidocms:studio-visuel-marque` (ou Canva).
- **Reel** : **caption courte** + **texte à l'écran fourni** → au monteur
  (`rapido-video:montage-express` / `rapido-higgsfield:usine-video-marketing`).
- **Stories** : angle + interaction (sondage/question) → visuel délégué.

## 3. Passe anti-voix-IA (OBLIGATOIRE) + gate marque

`reference/anti-voix-ia.md` sur chaque variante, puis `rapidocms:brand-review`.

## 4. Livraison

`create_draft_tool` (brouillon CMS) **par compte** (`list_connected_accounts` → account_id
Facebook / Instagram), rattaché à la campagne. **Jamais de publication directe.** Hooks
utilisés **consignés** (compteur `banque-hooks.md`).

## Passerelles

LinkedIn → `copy-linkedin`. TikTok → `copy-tiktok`. Décliner sur les 4 →
`declinaison-multi-reseaux`. Profil perso → `rapido-marketing:social-selling-linkedin`.

## Règles

- **Grammaires distinctes** FB/IG respectées ; **brouillon** uniquement.
- **Preuves réelles**, anti-clickbait, hooks re-dérivés ; anti-voix-IA + brand-review avant.
