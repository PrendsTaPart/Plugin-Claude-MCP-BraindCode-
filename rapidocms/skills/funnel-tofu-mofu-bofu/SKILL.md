---
name: funnel-tofu-mofu-bofu
description: Utiliser quand l'utilisateur veut des posts par étape du funnel (TOFU, MOFU, BOFU), un équilibre découverte/considération/vente, une stratégie de contenu par niveau de maturité, ou appliquer AIDA, PAS ou 4U à un post. Répartition, frameworks copywriting et CTA par étape.
---

# Funnel de contenu — TOFU / MOFU / BOFU

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et la charte
(`./rapido-kb/charte-graphique.md` → `get_brand` → générique). Le ton de
marque s'applique à TOUTES les étapes du funnel. Les données citées dans les
posts (prix, chiffres, offres) viennent des MCP — jamais inventées.

## Les 3 étapes — définitions et répartition

- **TOFU (Top of Funnel — découverte)** : la cible ne connaît pas la marque.
  Objectif : attention et portée. Contenus : astuce métier, coulisses,
  tendance, storytelling, contenu divertissant. AUCUNE vente.
- **MOFU (Middle of Funnel — considération)** : la cible connaît, compare.
  Objectif : confiance et préférence. Contenus : preuve sociale (avis,
  témoignage client), cas concret avant/après, comparatif honnête, FAQ,
  démonstration du savoir-faire.
- **BOFU (Bottom of Funnel — décision)** : la cible est prête à acheter.
  Objectif : conversion. Contenus : offre claire, promotion datée, nouveauté
  produit, réservation/devis, urgence légitime (vraie date, vrai stock —
  jamais de fausse rareté).

**Répartition par défaut d'un calendrier : 60 % TOFU / 30 % MOFU / 10 % BOFU.**
Un compte qui ne publie que du BOFU épuise son audience ; que du TOFU ne vend
jamais. Adapter si l'utilisateur a un objectif ponctuel (lancement = +BOFU).

## Frameworks copywriting — lequel, quand

- **AIDA (Attention → Intérêt → Désir → Action)** : le couteau suisse, idéal
  MOFU/BOFU. Attention = 1re ligne qui stoppe le scroll ; Intérêt = le
  problème ou le fait ; Désir = bénéfice concret et sensoriel ; Action = UN
  CTA unique.
- **PAS (Problème → Agitation → Solution)** : puissant en MOFU quand la cible
  a une douleur identifiée. Agiter sans dramatiser artificiellement.
- **4U (Utile, Urgent, Unique, Ultra-spécifique)** : grille de validation des
  ACCROCHES et titres, toutes étapes. Une accroche doit cocher ≥ 2 U.
- **BAB (Before → After → Bridge)** : storytelling TOFU/MOFU — situation
  avant, résultat après, comment (la marque est le pont).

## CTA par étape — ne pas mélanger

- TOFU : engager, jamais vendre — « Et vous, plutôt X ou Y ? », « Enregistre
  ce post », « Partage à quelqu'un qui… ».
- MOFU : approfondir — « Découvre le cas complet », « Compare nos formules »,
  « Pose ta question en commentaire ».
- BOFU : convertir — « Réserve », « Commande », « Demande ton devis », avec
  le lien/moyen concret. Un seul CTA par post, toujours.

## Workflow

1. **Brief** : objectif, cible, réseau(x), période. Si un calendrier existe
   (`calendrier-editorial`), s'y insérer sans le contredire.
2. **Qualifier chaque idée de post** : étape du funnel + framework choisi —
   l'annoncer explicitement (« Post 3 — MOFU, framework PAS »).
3. **Rédiger** selon `redaction-commerciale` (rapidocrm) pour le fond et la
   charte pour le ton. Accroches passées au crible 4U. Zéro faute
   d'orthographe : relecture systématique avant toute création de brouillon.
4. **Visuel** : brief au skill `prompts-visuels-pro` (l'étape funnel influe :
   TOFU = lifestyle/émotion, BOFU = produit/offre lisible).
5. **Créer les brouillons** — `create_draft_tool`, un par réseau, puis
   planification via `pipeline-contenu-social`. Rattacher à une campagne
   (`orchestration-campagne`) si elle existe.
6. **Mesurer par étape** : lors de l'analyse (`analyse-performance-contenu`),
   comparer les posts PAR ÉTAPE de funnel (un TOFU se juge à la portée, un
   BOFU aux clics/conversions — jamais les mêmes KPI).

## Pièges

- Juger un post TOFU sur ses ventes ou un BOFU sur ses likes : mauvais KPI,
  mauvaises conclusions.
- Écrire « GOFU » ou d'autres variantes : les trois étapes sont TOFU, MOFU,
  BOFU (+ éventuellement la rétention post-achat, hors funnel d'acquisition).
- Empiler AIDA + PAS + BAB dans un même post : UN framework par post.
- Fausse urgence en BOFU (« plus que 2 places » inventé) : interdit — toute
  rareté annoncée doit être vérifiable dans les données MCP.
