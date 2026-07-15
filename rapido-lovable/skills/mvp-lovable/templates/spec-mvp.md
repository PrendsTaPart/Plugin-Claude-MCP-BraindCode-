# Spec MVP — {projet}

**Validée le : {date} par {qui}.** Aucun prompt Lovable n'est écrit avant validation
de cette spec (méthode spec-driven, cf. NOTICE — vibecode-pro-max-kit).

## 1. Cadrage

- **Cible / utilisateur** :
- **Promesse en une phrase** :
- **Périmètre (3-5 pages/features)** :
  - [ ] Page/feature 1 —
  - [ ] Page/feature 2 —
  - [ ] Page/feature 3 —
- **Hors périmètre (v1)** :

## 2. Données & intégrations

- **Données à afficher / saisir** :
- **Formulaires** (mode B → `enregistrer_prospect` si CRM) : oui / non — lesquels ?
- **Intégration MCP** (agent embarqué) : oui / non
  - Si oui : MCP(s) = foodeatup / crm / cms / rh ; périmètre (lecture / écritures
    confirmées) ; scope (établissement/société) → **délégué à `connecteur-mcp-lovable`**.

## 3. Design system

- **Charte** (couleurs hex, typos, logo) : depuis `get_brand` + `sync-marque-lovable`.
- **Style / références** : délégué à `ui-ux-pro-max` — figé ici :
- **Contraintes** : mobile-first, accessibilité (labels, contraste, focus).

## 4. Série de prompts prévue (P1…P8, cocher au fil)

- [ ] **P1** Fondations (structure, design system, règles de stack injectées)
- [ ] **P2** Page/feature 1 (critères de done)
- [ ] **P3** Page/feature 2
- [ ] **P4** Page/feature 3
- [ ] **P5** Données & formulaires (mode B)
- [ ] **P6** Agent embarqué (si MCP → `connecteur-mcp-lovable`)
- [ ] **P7** SEO / perfs / accessibilité
- [ ] **P8** Recette + gate sécurité + mise en ligne (sur confirmation)

## 5. Critères d'acceptation globaux

- États chargement / erreur / vide gérés partout.
- Aucune donnée inventée (contenu réel ou placeholder explicite).
- Si MCP : secrets hors bundle, appels serveur only, écritures confirmées, scope serveur.
- Gate sécurité (`reference/gate-securite.md`) **vert** avant mise en ligne.
