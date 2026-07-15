# Mémoire — sur primitives existantes uniquement

**Aucun nouveau système de mémoire.** Tout repose sur ce qui existe déjà :
`./rapido-kb/` (fichiers versionnés côté client) et les **tables n8n** (skill
`memoire-operationnelle`). Ce document mappe les périmètres et documente l'usage.

## Les 5 périmètres de mémoire

| Périmètre | Support (primitive existante) | Contenu |
|---|---|---|
| **Longue durée** | `./rapido-kb/marketing/` | ICP, scoring, offres, tunnels, benchmarks, apprentissages |
| **Travail** (session) | contexte de session + **projet RH Kanban** (RapidoRH) | tâches en cours, colonnes/étapes du travail |
| **Projet** | `tunnels.md` + **projet RapidoRH** dédié | un tunnel = un projet, IDs et statut |
| **Client** | **fiches CRM** (RapidoCRM) — **source de vérité** | contacts, entreprises, historique, pipeline |
| **Entreprise** | `./rapido-kb/` (racine) | identité, charte, offres, processus |

**RAG** = chargement de la KB en **Étape 0** de chaque skill/agent (les leçons de
`apprentissages.md` et les taux de `benchmarks.md` **priment** sur les défauts).
Les **agents citent leurs sources mémoire** (ex. « d'après `benchmarks.md`
(2026-07), cold email réf. 5 % »).

## Fichiers longue durée (modèles → `reference/kb-templates/`)
Créés dans `./rapido-kb/marketing/` **à la première exécution** (copie du modèle
si le fichier est absent — ne jamais écraser un fichier existant) :
`icp.md`, `scoring.md`, `offres.md`, `tunnels.md`, `benchmarks.md`,
`apprentissages.md`.

## Mémoire d'exécution — tables n8n (`memoire-operationnelle`)
Pour la version **automatisée** des séquences. **Une table par usage**, schéma
documenté (créées via le skill `memoire-operationnelle`, plugin rapido-n8n) :

### 1. `mkt_sequences_etat` — état des séquences
| Colonne | Type | Rôle |
|---|---|---|
| `prospect_id` | string | prospect CRM |
| `sequence` | string | nom de la séquence |
| `etape_courante` | string | J0/J3/J7/J14 |
| `statut` | string | active / en_pause / sortie |
| `prochaine_action_date` | date | quand relancer |

### 2. `mkt_relances_antidoublon` — anti-doublon des relances
| Colonne | Type | Rôle |
|---|---|---|
| `prospect_id` | string | prospect |
| `type_relance` | string | email / sms / linkedin |
| `date_envoi` | datetime | horodatage |

> Clé logique **(prospect_id + type_relance + jour)** : avant d'envoyer, vérifier
> l'absence de ligne du jour → **jamais deux relances identiques** le même jour.

### 3. `mkt_historique_envois` — historique des envois
| Colonne | Type | Rôle |
|---|---|---|
| `destinataire` | string | email/numéro |
| `canal` | string | email / sms / newsletter |
| `sujet` | string | objet |
| `date_envoi` | datetime | horodatage |
| `statut` | string | envoyé / répondu / désinscrit |

> Le statut `désinscrit` est **honoré immédiatement** (retrait de séquence +
> étape/tag CRM) — garde-fou RGPD.

## Renvois
- Priorité des serveurs : `reference/priorite-mcp.md`.
- Garde-fous (RGPD, confirmations) : `reference/garde-fous-marketing.md`.
