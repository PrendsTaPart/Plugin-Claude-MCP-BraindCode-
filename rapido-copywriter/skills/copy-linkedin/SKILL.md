---
name: copy-linkedin
description: Utiliser quand l'utilisateur veut de la copy LinkedIn pour une PAGE de marque — « post LinkedIn pour la page », « carrousel LinkedIn », « copy LinkedIn de [marque/produit] ». Produit 3 variantes selon la grammaire LinkedIn, passe anti-voix-IA + gate marque, brouillon CMS. À NE PAS utiliser pour le profil PERSO du fondateur (social-selling-linkedin) ni un autre réseau (copy-meta, copy-tiktok).
---

# Copy LinkedIn (pages de marque)

**Frontière (à lire d'abord).** Ce skill écrit pour les **pages de MARQUE**. Le **profil
PERSO** du fondateur (Mo qui poste en son nom) → `rapido-marketing:social-selling-linkedin`.

## Étape 0 — contexte

Lire `reference/grammaires-reseaux.md` (fiche **LinkedIn**), `reference/banque-hooks.md`
(**piocher les hooks `GAGNANT` d'abord**, sinon NEUTRE), `reference/anti-voix-ia.md`,
`reference/articulations.md`. Charte : `get_brand` + `rapido-kb/`. Si campagne : **pilier**
du `rapidocms:calendrier-editorial`.

## 1. Brief

Objectif **funnel** (TOFU/MOFU/BOFU — cf. `rapidocms:funnel-tofu-mofu-bofu`), **cible**,
**preuve réelle** (chiffre/témoignage **du CRM/CMS uniquement — jamais inventé**). Format :
post texte ou **carrousel PDF**.

## 2. Trois variantes (hooks différents, même fond)

Écrire **3 variantes** selon la grammaire LinkedIn (hook 1-2 lignes avant « …voir plus »,
900-1 300 car., une idée par ligne, **pas de lien dans le corps** → commentaire, 3-5
hashtags en fin, CTA conversationnel). Hooks **différents** (piochés/adaptés de la banque),
même message de fond.

## 3. Passe anti-voix-IA (OBLIGATOIRE)

Appliquer `reference/anti-voix-ia.md` sur chaque variante (≥ 2 tics → réécrire). Personne
ne doit sentir la machine.

## 4. Gate voix de marque

`rapidocms:brand-review` sur le lot → conforme charte/ton avant livraison.

## 5. Livraison

`create_draft_tool` (brouillon CMS) rattaché à la **campagne**, sur le **compte page
marque** (`list_connected_accounts` pour l'account_id LinkedIn). **Jamais de publication
directe.** Consigner les **hooks utilisés** (incrémenter le compteur dans
`reference/banque-hooks.md`).

**Carrousel** : livrer la **structure slide par slide** (1 idée/slide, 6-10 slides) →
visuel délégué à `rapidocms:studio-visuel-marque` (ou Canva).

## Passerelles

Profil perso → `rapido-marketing:social-selling-linkedin`. Autres réseaux → `copy-meta`,
`copy-tiktok`. Décliner sur les 4 → `declinaison-multi-reseaux`.

## Règles

- **Pages marque uniquement** (perso = social-selling). **Brouillon**, jamais de publication.
- **Preuves réelles** (CRM/CMS) ; **anti-clickbait** (promesse tenue) ; hooks **re-dérivés**.
- Anti-voix-IA + gate brand-review **avant** livraison ; hooks consignés au compteur.
