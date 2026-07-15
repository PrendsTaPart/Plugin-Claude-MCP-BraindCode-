# Gate sécurité — apps « agent + clés MCP » (bloquant avant livraison)

**Kit v1 · 2026-07-15.** Checklist adaptée de `BehiSecc/VibeSec-Skill` (**Apache-2.0** —
attribution + notice de modification obligatoires, voir `NOTICE.md`), **spécialisée** pour
les sites Lovable qui embarquent un agent IA connecté à un MCP (donc porteurs de clés).
**À passer sur chaque app avant livraison** — un point rouge bloque la mise en ligne.

## 1. Secrets & exposition (critique)

- [ ] **Aucune clé/URL MCP dans le bundle client** (`grep` du build : `ANTHROPIC_API_KEY`,
  `*_MCP_URL`, `*_MCP_TOKEN`, `SERVICE_ROLE` → 0 résultat côté front).
- [ ] Secrets **uniquement** en env Lovable/Supabase (edge). Pas de secret dans le code,
  les logs, les messages d'erreur renvoyés au front.
- [ ] Clé **du client** (jamais une clé BraindCode maîtresse).

## 2. Appels serveur uniquement

- [ ] Le navigateur n'appelle **jamais** `api.anthropic.com` ni une URL MCP directement —
  uniquement l'edge function du projet.
- [ ] CORS de l'edge function restreint autant que possible (origine du site en prod ;
  éviter `*` en production si faisable).

## 3. Contrôle d'accès & scope (multi-tenant)

- [ ] **Scope serveur** : `SCOPE_ID` (établissement/société) vient de l'**env**, jamais
  d'un paramètre du front. Un message tentant de changer de scope → refusé.
- [ ] Autorisation par utilisateur pour les portails internes (RH) : session authentifiée
  requise (Supabase auth), pas d'accès anonyme aux données internes.
- [ ] Pas de **mass assignment** : l'edge function ne relaie que les champs attendus.

## 4. Écritures confirmées

- [ ] Toute action d'**écriture** (créer/modifier/supprimer) est **proposée** puis exécutée
  seulement après **confirmation UI** (`approved:true`). Aucune écriture silencieuse.
- [ ] Familles d'outils **restreintes** par le system prompt (l'agent ne peut pas appeler
  un outil hors périmètre de la fiche MCP).

## 5. Entrées & injection

- [ ] Filtre d'injection de prompt actif (patterns « ignore previous instructions »,
  « print api key »…) + `sanitize` (caractères de contrôle) + **longueur bornée**.
- [ ] Rate-limiting (burst + horaire) sur l'edge function.
- [ ] Validation serveur de **toutes** les entrées ; échec = **fail-closed** (refus).

## 6. Web classiques (rappel VibeSec)

- [ ] **XSS** : pas d'injection HTML non échappée ; contenu de l'agent rendu comme texte/
  markdown sûr, pas `dangerouslySetInnerHTML` sur du non-assaini.
- [ ] **Open redirect** / **SSRF** : pas de redirection ni de fetch serveur vers une URL
  fournie par l'utilisateur sans allow-list.
- [ ] **Upload** (si présent) : type/taille validés serveur, pas d'exécution.
- [ ] **En-têtes de sécurité** raisonnables (CSP si possible, `X-Content-Type-Options`).

## 7. RGPD & journal

- [ ] **Journal des actions** de l'agent (lecture/écriture, horodaté) accessible.
- [ ] Mentions (traitement, finalité) présentes ; **purge paramétrable** des logs de
  conversation ; pas de PII inutile stockée.

## Verdict

- **Tous les points critiques (1-4) verts** → livraison possible.
- Un seul rouge sur 1-4 → **blocage**, correction avant mise en ligne.
- Points 5-7 : à traiter ; un manquant documenté = dette explicite, pas silencieuse.

---
*Adapté de [BehiSecc/VibeSec-Skill](https://github.com/BehiSecc/VibeSec-Skill)
(Apache-2.0), **modifié** et spécialisé « agent + MCP » — voir `NOTICE.md`.*
