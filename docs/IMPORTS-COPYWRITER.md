# Imports & audit — rapido-copywriter (CW0)

**Date** : 2026-07-15 · **Portée** : audit uniquement — aucune création de skill.
3 dépôts clonés (licences relues, **toutes MIT**), + relevé **live** des métriques
d'insights RapidoCMS (ce qui alimentera la boucle de scoring des hooks).

> **Anti-verbatim renforcé** : `linkedin-hook-extractor` et les skills de copy
> **partent de posts de créateurs/marques RÉELS**. On **re-dérive des templates
> génériques francisés** ; **aucun exemple citant un créateur/marque réel** n'est
> repris. Aucun corps de texte copié.

## 1. Moisson (3 dépôts MIT)

### 1.a `sergebulaev/linkedin-skills` (⭐383, MIT) — 🥇 ADAPTER (référence LinkedIn)
11 skills : `linkedin-humanizer`, `linkedin-hook-extractor`, `linkedin-post-writer`,
`linkedin-comment-drafter`, `linkedin-repurposer`, `linkedin-content-planner`,
`linkedin-profile-optimizer`, `linkedin-engager-analytics`, `linkedin-reply-handler`,
`linkedin-employee-advocacy`, `linkedin-thread-monitor`.

| Élément | Ce qu'on en tire | Verdict |
|---|---|---|
| **`linkedin-humanizer`** (V2, 3 tiers forensic/strict/aesthetic + mode audit ; basé « Signs of AI writing ») | Base de **`anti-voix-ia.md`** — **MAIS francisé/re-dérivé** : les tics LLM **français** diffèrent (« Dans un monde où… », « N'hésitez pas à… », « Plongeons dans… ») ; l'anglais n'est pas repris | **ADAPTER (FR)** |
| **`linkedin-hook-extractor`** (16 formules 2026 : anaphore, R.I.P., year-pivot, curiosity-gap, contrarian, comment-gate…) | **Mécanique de la banque de hooks** : structures à placeholders, **jamais** les posts réels analysés | **ADAPTER (templates génériques)** |
| `linkedin-post-writer` / `linkedin-repurposer` / `comment-drafter` | Structure post LinkedIn · repurpose · **commentaires semi-auto** (patch social-selling) | **S'INSPIRER** |
| `profile-optimizer` / `employee-advocacy` / `thread-monitor` | Hors périmètre (profil perso = `social-selling-linkedin` ; advocacy/veille = plus tard) | **BENCHMARK** |

### 1.b `blacktwist/social-media-skills` (⭐334, MIT) — 🥇 ADAPTER (ossature multi-réseaux)
14 skills `-sms` : `hook-writer`, `caption-writer`, `carousel-writer`, `thread-writer`,
`post-writer`, `content-repurposer`, `platform-strategy`, `performance-analyzer`,
`content-pattern-analyzer`, `optimization-advisor`, `content-calendar`,
`audience-growth-tracker`, `content-strategy`, `social-media-context`.

| Élément | Ce qu'on en tire | Verdict |
|---|---|---|
| **`platform-strategy` + `social-media-context`** | **Structure des fiches `grammaires-reseaux.md`** (par réseau : tactique, algo, différences) | **ADAPTER** |
| **`hook-writer`** | Écriture de hooks + variantes → `banque-hooks.md` | **ADAPTER** |
| **`caption-writer` / `carousel-writer` / `thread-writer`** | Grammaires **IG/FB** (caption, carrousel, thread) | **ADAPTER** |
| `content-pattern-analyzer` / `performance-analyzer` | Croisés avec **`rapidocms:analyse-performance-contenu`** (vrais insights) → « ce qui marche POUR TES comptes » | **S'INSPIRER** |
| `content-repurposer` | Moteur de **déclinaison** multi-réseaux | **ADAPTER** |
| ⚠️ Note : `platform-strategy` couvre LinkedIn/X/Threads/Bluesky ; **TikTok** vient des skills caption/carousel + notre grammaire maison | — | — |

### 1.c `rigarcia07/social-creative-director-skill` (⭐10, MIT) — ✅ S'INSPIRER (agent)
Skill « directeur de création senior » (creative director + designer + copywriter
direct-response, sortie agency-quality). → **squelette de l'agent `copywriter-social`**
(exigence, itérations, critique argumentée). Réécrit, pas copié.

### 1.d Compléments & benchmarks
- `timscheuerai/content-vault` (MIT, déjà cloné en LM0) : `linkedin-copywriter`,
  `x-copywriter`, `repurpose` → **compléments** de patterns.
- `aaaronmiller/create-viral-content` (**sans licence**) : concept de **banque de hooks**
  → 👁️ réimplémenté **maison**, jamais fusionné. `Othmane-Khadri/gtm-agent-playbook`
  (**sans licence**) : 👁️ benchmark. `azizaeffendi/ai-video-script-generator` (MIT) :
  🟡 **pattern** de structure de script vidéo court (TikTok/Reels).

## 2. Métriques d'insights RapidoCMS (live) — ce qui alimente le scoring

- `post_insights(post_ids[] ≤ 10)` → réponse **par réseau** (`tiktok`, `instagram`,
  `linkedin`, `facebook`), chaque post avec un tableau `insights` :
  **`liked`, `shares`, `views`, `comments`** (+ `post_id` = URN). Vérifié live sur des
  posts publiés (`statut:1`, `post_urn` présent) — company 321.
- `ingishts_campagne(campagne_id)` : insights agrégés d'une campagne. `list_scheduled_posts`
  filtrable par `social` (facebook|linkedin|instagram|tiktok), `statut` (0 planifié /
  1 publié), champ `post_urn`.
- **Conséquence pour `score_hooks.py` (CW4)** : l'engagement se calcule **uniquement**
  sur `liked`/`shares`/`comments`/`views` (les seules métriques exposées). Formule
  candidate : interactions = `liked + shares + comments` ; taux = interactions ÷ `views`
  (si views>0). Comparaison à la **médiane du compte sur 30 j**, **par réseau**. Aucun
  score inventé — ces 4 champs font foi.
- **Manque éventuel** (à porter si besoin en CW4) : pas de « reach/impressions » distinct
  des `views`, ni de breakdown par heure. Suffisant pour tagger GAGNANT/NEUTRE ; noté.

## 3. Croisement maison — qui fait quoi demain (le plugin ORCHESTRE)

| Existant | Rôle | Frontière avec rapido-copywriter |
|---|---|---|
| `rapidocms:funnel-tofu-mofu-bofu` | Frameworks funnel (AIDA/PAS/4U par étape) | **Référencé** pour la répartition TOFU/MOFU/BOFU par réseau ; pas copié |
| `rapidocms:content-creation-methodo` | Formats par canal | **Recouvrement partiel** → recentré sur **blog/email/landing** ; le **social** passe au nouveau plugin (renvoi ajouté en CW4) |
| `rapidocms:pipeline-contenu-social` | Brouillon → planification → insights | **Exécution** : le copywriter produit, le pipeline planifie ; patch « déclinaison multi-réseaux dispo » (CW4) |
| `rapidocms:calendrier-editorial` | Calendrier | Répartition des formats (grammaires référencées) |
| `rapidocms:analyse-performance-contenu` | Patterns gagnants | **Alimente la boucle** de scoring des hooks (vrais insights) |
| `rapidocms:brand-review` | Gate voix de marque | **Gate obligatoire** avant tout lot de copy |
| `rapido-marketing:social-selling-linkedin` | **Profil PERSO** du fondateur | **FRONTIÈRE STRICTE** : perso = ce skill ; **pages marque** = rapido-copywriter. Patch « commentaires semi-auto » (CW4) |
| `rapido-forge:ideation-linkedin-posts` (parcours) | Pédagogie | **Renvoi** (apprendre) ; le nouveau plugin **exécute** |
| `made-to-stick` / `contagious` / `storybrand` | Frameworks message | Référencés (fond du message), pas dupliqués |

## 4. Le trou que le plugin comble

Les **grammaires natives par réseau** (datées/versionnées, les algos bougent) + la
**production de copy plateforme par plateforme** + la **boucle d'apprentissage sur les
hooks** (banque vivante taguée par les vrais insights). Rien de tout cela n'existe
aujourd'hui de façon canonique.

## 5. STOP — validation avant CW1

1. **Anti-verbatim** : OK pour re-dériver des **templates génériques** de hooks (jamais
   les posts réels analysés par hook-extractor), et franciser l'humanizer en **liste de
   tics FR** (l'anglais ne s'applique pas) ?
2. **Métriques de scoring** : OK pour fonder `score_hooks.py` sur `liked/shares/comments/
   views` (les seules exposées), médiane 30 j par réseau — sans inventer reach/impressions ?
3. **Frontière `content-creation-methodo`** : OK pour **recentrer** ce skill sur
   blog/email/landing et déléguer le **social** au nouveau plugin (renvoi croisé) ?

*Sources : 3 dépôts clonés (LICENSE relus, MIT), sondes lecture seule RapidoCMS (live).
Aucune donnée inventée.*
