# Pattern — Web / app (brief Lovable, mode B)

**Usage** : brief structuré pour générer une landing / app via Lovable
(usine-à-landing, mode B).
**Média** : web / app.

## Pattern (à compléter aux [placeholders])

```
Rôle : [ce que l'app accomplit], pour [audience]. Objectif principal : [action
visée : capter un lead / vendre / réserver].
Pages :
- [Accueil] : [héros + proposition de valeur + CTA].
- [Page 2] : [rôle].
- [Page 3] : [rôle].
Design system : couleurs [hex charte], police [police], ton [sobre / premium /
chaleureux], style visuel [ambiance décrite — pas de nom de marque tierce].
Data / logique : [entités], [source des données], [connecteurs : formulaire →
CRM, paiement, e-mail].
Contraintes : responsive, accessible, [SEO de base].
```

## Moteurs compatibles

- **Lovable** — `create_project(initial_message=…)` puis `send_message` en langage
  naturel ; `plan_mode=true` pour cadrer avant code. **Lire la doc Lovable en live**
  (stack par défaut, connecteurs). Recoupe **`rapido-forge:ideation-lovable-prompt`**
  (le prompteur cadre le brief ; l'idéation produit reste dans forge).
- **Canva** pour les visuels de la page (brand kit + format d'export réels).

## Rappels

- Décrire le style en **générique** (« minimalisme premium, beaucoup de blanc »),
  jamais « façon [site/marque connue] ».
- Données réelles ou marquées « à confirmer » — pas de faux témoignages/chiffres.

---
*Source : structure « 1 brief = rôle / pages / design / data » distillée de
`KingLeoJr/prompts` (MIT) et de la structure `prompt-engineer` de `wshobson/agents`
(MIT) — francisé, aucun texte verbatim. Voir `NOTICE.md`. Aucune IP tierce.*
