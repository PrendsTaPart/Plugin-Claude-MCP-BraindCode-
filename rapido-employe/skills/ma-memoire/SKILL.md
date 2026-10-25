---
name: ma-memoire
description: Utiliser quand quelque chose mérite d'être retenu ou retrouvé, que l'utilisateur dit « retiens cette méthode », « qu'avais-tu noté sur les relances », « oublie cette vieille procédure ». Range méthodes, préférences et corrections dans la mémoire Academy, les retrouve, et archive ce qui ne sert plus — jamais un secret ni une donnée client.
---

# Ma mémoire (retenir la méthode, jamais la coordonnée)

Famille engagée : **configurer** (Confirmé — écritures Academy avec aperçu
serveur).

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`.

## Workflow

1. **Retenir** : **`remember`** quand une préférence durable s'exprime,
   qu'une correction tombe, ou qu'une explication a vraiment marché — typée
   (méthode, préférence, correction), une idée par entrée, datée par le
   serveur. Un savoir utile à toute l'équipe se propose en portée
   « equipe » : le responsable le valide (pas nous).
2. **Retrouver** : **`recall`** avant d'agir sur un sujet déjà rencontré —
   la procédure retenue bat la réinvention. `get_claude_brief` relit déjà
   l'essentiel chaque matin.
3. **Archiver** : **`archive_memory`** quand une entrée ne sert plus ou a
   été corrigée — la mémoire reste courte et vraie. (Rien ne se supprime :
   l'archivage est le geste maximal.)

KPI : `routines-en-service` (les méthodes retenues nourrissent les
routines). Formations : `rituels`.

## Garde-fous

- **JAMAIS** de secret, de coordonnée bancaire, d'e-mail, de téléphone ni de
  donnée client nominative dans une entrée (hook garde-memoire : deny) — la
  fiche client vit dans le CRM, le jeton dans le coffre.
- La mémoire note des méthodes, pas des jugements sur des personnes.
- Une entrée d'équipe proposée reste un BROUILLON tant que le responsable ne
  l'a pas validée — on ne la cite pas comme règle avant.
