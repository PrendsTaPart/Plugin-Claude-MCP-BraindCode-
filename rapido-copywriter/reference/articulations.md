# Articulations — qui fait quoi (le plugin ORCHESTRE, ne duplique pas)

## Frontière stricte : profil perso vs pages marque

- **Profil PERSO du fondateur** (Mo qui poste en son nom) → `rapido-marketing:social-selling-linkedin`.
- **Pages de MARQUE** (FoodEatUp, BraindCode, comptes clients) → **ce plugin**.
- **Ne jamais** produire de post pour le profil perso ici ; router vers social-selling.

## Chaîne de production

| Étape | Skill |
|---|---|
| Frameworks funnel (répartition TOFU/MOFU/BOFU) | `rapidocms:funnel-tofu-mofu-bofu` (référencé) |
| Grammaire par réseau + banque de hooks | `reference/grammaires-reseaux.md` + `banque-hooks.md` (ici) |
| Écriture de la copy par réseau | `copy-linkedin`, `copy-meta`, `copy-tiktok` (CW2-3) |
| Passe anti-voix-ia (finale) | `reference/anti-voix-ia.md` (ici) |
| Gate voix de marque | `rapidocms:brand-review` (**obligatoire avant tout lot**) |
| Brouillon + planification | `rapidocms:pipeline-contenu-social` + `calendrier-editorial` |
| Insights réels → scoring des hooks | `rapidocms:analyse-performance-contenu` → `scripts/score_hooks.py` (CW4) |

## Recouvrements à cadrer

- **`rapidocms:content-creation-methodo`** : recouvre le social → **recentré** sur
  **blog / email / landing** ; le **social** passe à ce plugin (renvoi croisé ajouté en CW4).
- **Frameworks message** (`made-to-stick`, `contagious`, `storybrand`) : **référencés**
  pour le fond du message, jamais dupliqués.
- **Pédagogie** : `rapido-forge:ideation-linkedin-posts` (apprendre) → **renvoi** ; ici on
  **exécute** sur les vraies données.

## Garde-fous (rappel)

Voix de marque obligatoire (gate) · **brouillons CMS uniquement, jamais de publication
directe** · anti-clickbait (promesse du hook tenue) · preuves/chiffres **réels**
(CRM/CMS, jamais inventés) · hooks **re-dérivés** (jamais copiés d'un créateur) · pas de
faux engagement (pods, achats).
