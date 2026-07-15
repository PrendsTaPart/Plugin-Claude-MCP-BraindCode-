# Sales intelligence — transcripts d'appels & objections (Fireflies)

> **Source distillée** : gtm-flywheel (`sales-intelligence/transcript-analysis`,
> `objection-mining`) MIT © 2026 ColdIQ. Reformulé FR, non-verbatim
> (voir `NOTICE.md`).

## L'idée
Miner les **transcripts d'appels** commerciaux pour en extraire : objections
récurrentes, formulations qui convertissent, signaux de closed-won/lost, prochaines
étapes. Une mine d'apprentissages pour la copy et la qualification.

## Méthode
1. Récupérer les transcripts (réunions commerciales).
2. **Extraire les objections** et les classer (prix, timing, autorité, besoin…).
3. Croiser gagné/perdu pour repérer les patterns.
4. **Réinjecter** : objections → `redaction-commerciale` (traitement) et
   `scale-bant-qualification` ; formulations gagnantes → templates.
5. Leçons datées → `rapido-kb/marketing/apprentissages.md`.

## Mapping Rapido
- **MCP Fireflies déjà disponible** dans l'environnement → source des transcripts
  (Gong/Otter/Chorus des dépôts s'y remplacent).
- Écriture des enseignements : `log_activity` / `create_task` (CRM) après
  confirmation ; jamais de contenu envoyé automatiquement.

→ Cible : **nouveau skill `sales-intelligence-fireflies`** (branché MCP Fireflies).
