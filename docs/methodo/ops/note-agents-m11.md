# Note M11 — architecture d'agents (synthèse hormozi-skills)

> **Source** : alexsmedile/hormozi-skills, `agents/` (MIT © 2026 Alessandro
> Smedile). Synthèse du **pattern**, pas du contenu. Reformulé FR.

## Le pattern observé : hub-and-spoke stateless
Un **orchestrateur** est le seul point de contact utilisateur ; il pilote des
**sous-agents workers sans mémoire** qui écrivent chacun leur livrable dans
`output/*.md`.

### Orchestrateur — 5 phases
1. **Intake** : accepte tout input, lit les fichiers cités, reformule en 3-5 puces.
2. **Interview** : une question à la fois, avec **réponse recommandée pré-remplie** ;
   s'arrête quand 8 signaux sont capturés (cible, douleur, résultat, stade,
   livraison, contraintes, objectif, preuve).
3. **Détection de stade** : classe la situation (idée seule / offre non
   convertissante / assets seuls / service à scaler / mixte) → décide **quels
   sous-agents** lancer.
4. **Délégation** : spawn via Task avec un **brief complet** (les workers n'ont
   AUCUNE mémoire → tout le contexte est passé) ; gère les dépendances.
5. **Synthèse** : lit tous les `output/*.md` → `SUMMARY.md`.

### Dépendances imposées
Séquentiel : marché → offre → valeur → vente ; le pricing peut chevaucher la
valeur.

## Ce qu'on en retient pour rapido-marketing (M11)
- Notre **équipe d'agents** (directeur-marketing → managers → skills) suit **déjà**
  ce pattern hub-and-spoke, avec en plus nos garde-fous (confirmations, RGPD,
  KPI par script) et la **délégation sans doublon** vers les rôles existants.
- Idée à emprunter : le **brief complet et structuré** passé à chaque délégation
  (nos handoffs « brief une page » le formalisent déjà) et l'**interview avec
  réponse recommandée pré-remplie** (à réutiliser dans `icp-generator` /
  `directeur-marketing`).
- Différence à conserver : nos sous-traitants sont des **skills réels branchés
  MCP** (pas des workers qui écrivent des .md), et l'exécution est **Rapido-first**.

→ Note pour M11 : ne pas recréer un orchestrateur générique — enrichir l'existant
avec l'interview « réponse pré-remplie » et le brief de délégation structuré.
