# Audit README & hygiène du dépôt — 2026-07-15

Constat daté, **avant tout correctif**. Chiffres recomptés depuis les fichiers
(`marketplace.json`, `plugin.json`, arborescence), pas de mémoire.

## Méthode

- Inventaire : `.claude-plugin/marketplace.json` croisé avec chaque
  `*/.claude-plugin/plugin.json` et le comptage réel des dossiers
  (`skills/*/SKILL.md`, `agents/*.md`, `hooks/`, `scripts/`).
- Liens : cibles internes testées (le fichier existe), externes (format https).
- Secrets : `grep` du dépôt entier (`sk-…`, `api_key`, `Bearer …`, `password`,
  `AKIA…`, `ghp_…`).
- Hygiène : présence/qualité `.gitignore`, `LICENSE`, `CONTRIBUTING.md`,
  `SECURITY.md` ; tags vs versions.

## a. Inventaire réel vs README

- **25 plugins** dans `marketplace.json` = **25** sur le disque. Aucun plugin
  absent de la table du README, aucun plugin fantôme dans la table.
- **380 skills**, **37 agents** (recomptés). Les badges du README
  (`plugins-25`, `skills-380`, `agents-37`) sont **exacts**.
- Table des plugins : **25 lignes**, versions et comptes **tous alignés** sur
  les `plugin.json` réels (vérifié plugin par plugin — 0 dérive).

> **Constat clé** : la table est correcte **aujourd'hui** mais **maintenue à la
> main**. Rien ne garantit qu'elle le reste à la prochaine release. → étape 2
> (génération automatique entre marqueurs).

## b. Cohérence par plugin

| Plugin | README | CHANGELOG | Attribution | Tests |
|---|---|---|---|---|
| foodeatup | ❌ | ✅ | ATTRIBUTIONS.md | ✅ |
| rapidocrm | ❌ | ✅ | **❌ manquant (9 skills importés)** | ✅ |
| rapidocms | ❌ | ✅ | ATTRIBUTIONS.md | ✅ |
| rapidorh | ❌ | ✅ | ATTRIBUTIONS.md | ✅ |
| rapido-suite | ✅ | ✅ | ATTRIBUTIONS.md | ✅ |
| rapido-canva | ❌ | ✅ | ATTRIBUTIONS.md | ✅ |
| rapido-lovable | ❌ | ✅ | ATTRIBUTIONS.md + NOTICE.md | ✅ |
| rapido-meta-ads | ❌ | ✅ | ATTRIBUTIONS.md | ✅ |
| rapido-n8n | ❌ | ✅ | — (pas d'import) | ✅ |
| rapido-direction | ❌ | ✅ | — (pas d'import) | ✅ |
| rapido-startup | ❌ | ✅ | — (pas d'import) | ✅ |
| rapido-forge | ✅ | ✅ | — (skills maison) | ✅ |
| rapido-marketing | ✅ | ✅ | — (pas d'import) | ✅ |
| rapido-higgsfield | ✅ | ✅ | — | ✅ |
| rapido-video | ✅ | ✅ | NOTICE.md | ✅ |
| rapido-prompteur | ✅ | ✅ | NOTICE.md | ✅ |
| rapido-elevenlabs | ✅ | ✅ | NOTICE.md | ⚠️ squelette (0 skill) |
| rapido-seo | ✅ | ✅ | — | ✅ |
| rapido-google-ads | ✅ | ✅ | — | ✅ |
| rapido-tiktok-ads | ✅ | ✅ | — | ✅ |
| rapido-relation-client | ✅ | ✅ | — | ✅ |
| rapido-gmaps | ✅ | ✅ | — | ✅ |
| rapido-leadmagnet | ✅ | ✅ | NOTICE.md | ✅ |
| rapido-copywriter | ✅ | ✅ | NOTICE.md | ✅ |
| rapido-design | ✅ | ✅ | NOTICE.md | ✅ |

**Écarts relevés :**

1. **README de plugin manquant (10)** : `foodeatup`, `rapidocrm`, `rapidocms`,
   `rapidorh`, `rapido-canva`, `rapido-lovable`, `rapido-meta-ads`, `rapido-n8n`,
   `rapido-direction`, `rapido-startup`. → étape 4 (mini-template commun).
2. **Attribution manquante — `rapidocrm`** : 9 skills importés déclarent une
   `source:` (6 × `anthropics/knowledge-work-plugins`, **Apache 2.0** ; 3 ×
   `wondelai/skills`, **MIT**) mais le plugin n'a **ni `ATTRIBUTIONS.md` ni
   `NOTICE.md`**. Conformité licence à corriger (recommandé, hors périmètre
   « docs README » strict — à traiter en suivi).
3. **Convention d'attribution dédoublée** : `ATTRIBUTIONS.md` (7 plugins
   anciens) vs `NOTICE.md` (7 plugins récents) ; `rapido-lovable` a **les deux**.
   `CONTRIBUTING.md` ne cite qu'`ATTRIBUTIONS.md`. → uniformiser le vocabulaire
   (documentation, pas de suppression de fichier existant).
4. **CHANGELOG** : **25/25 à jour** — l'entrée de tête correspond exactement à la
   `version` du `plugin.json` pour **tous** les plugins.
5. **Tests** : présents partout sauf `rapido-elevenlabs` (squelette assumé, 0
   skill — acceptable, à documenter comme tel).

## c. Liens

- **Internes (README racine)** : `CONTRIBUTING.md`, `LICENSE`,
  `RELEASE-NOTES.md`, `rapido-kb-template/`, `reference/registre-routines.md` →
  **tous résolvent**. Aucun lien mort.
- **Externes** : badges shields.io, `code.claude.com/docs`, dépôts sources
  GitHub (anthropics/skills, anthropics/knowledge-work-plugins, wondelai/skills,
  nextlevelbuilder/ui-ux-pro-max-skill, AgriciDaniel/claude-blog) → **format
  valide**. `https://<instance>/mcp-server/http` est un **placeholder** dans un
  bloc d'exemple (pas un lien réel) — OK.

## d. Sécurité (bloquant si trouvaille)

`grep` du dépôt (`*.md`, `*.json`, `*.py`, `*.sh`, `*.js`, `*.cjs`) sur
`sk-…`, `api_key=…`, `Bearer …`, `password=…`, `AKIA…`, `ghp_…` →
**AUCUNE fuite**. Rien à retirer. **Pas de STOP.** Les seules URLs de serveurs
sont des URLs produit (`.mcp.json`) ou des variables d'environnement
(`${…_MCP_URL}`).

## e. Hygiène GitHub

- **`.gitignore`** (19 lignes) : couvre `__pycache__/`, `*.pyc`, `.coverage`,
  `node_modules/`, `.DS_Store`, `.env`, `rapido-kb/`, `.video-tools/`.
  **Manque** : `/repos` (dépôts clonés lors des audits d'import), sorties de
  tests éphémères. → étape 4 (complément additif).
- **`LICENSE`** : **Apache 2.0** (racine) ✅.
- **`CONTRIBUTING.md`** : présent (114 lignes), complet et fidèle aux conventions
  maison ✅. À aligner sur le vocabulaire d'attribution (point b.3).
- **`SECURITY.md`** : présent (44 lignes), couvre hooks/secrets/signalement ✅.
- **`NOTICE.md` racine** : **absent**. Apache 2.0 (§4) invite à propager un
  NOTICE quand on redistribue des œuvres Apache (les 6 skills `rapidocrm`
  importés d'`anthropics/knowledge-work-plugins`). → recommandé.
- **Tags / releases** : 7 tags (`v1.1.0`, `v1.2.0`, `v1.2.1`, `v1.3.0` +
  3 tags de vague datés). **En retard** sur l'état réel (le dépôt a 25 plugins,
  beaucoup au-delà de 1.3.0). → proposition de rattrapage en étape 5 (non
  exécutée).
- **Description / topics du dépôt** : `gh` indisponible dans l'environnement →
  proposition manuelle en étape 5.

## Synthèse des correctifs (ordre d'exécution)

1. **Script** `scripts/generate_readme_table.py` + marqueurs
   `<!-- TABLE-PLUGINS:START/END -->` (fiabilise la table).
2. **Refonte README racine** (structure imposée, chiffres issus de cet audit).
3. **Hygiène** : compléter `.gitignore` (`/repos`), aligner `CONTRIBUTING.md`
   (vocabulaire attribution), `SECURITY.md` (déjà bon — relire).
4. **README de plugin manquants (10)** — mini-template commun, un commit par
   plugin.
5. **Suivi hors périmètre README** (à planifier séparément) : attribution
   `rapidocrm`, NOTICE racine, rattrapage des tags/releases, description+topics
   GitHub.
