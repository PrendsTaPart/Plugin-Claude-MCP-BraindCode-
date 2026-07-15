# VENTE-RELANCES — relances commerciales du jour (quotidien 14h)

```yaml
# CONFIG — interchangeable par client (les valeurs de ./rapido-kb/ PRIMENT)
routine: VENTE-RELANCES
cadence: quotidienne — 14h (fuseau : rapido-kb/entreprise.md)
perimetre: [rapidocrm]
seuil_devis_expirant_jours: 7
seuils: ./rapido-kb/commercial/seuils.md
table_memoire_n8n: vente_relances_journal   # anti-double-relance (obligatoire)
autonomie: niveau 1 max — relances PRÉPARÉES en brouillon, jamais envoyées seules — reference/autonomie.md
silence_si_vert: true
```

> **Version autonome (sans Claude)** : recette n8n à installer via
> `rapido-n8n:usine-automatisations` (préfixe `OPS-*` à venir) ; la **table mémoire
> `vente_relances_journal`** est obligatoire — sans elle, pas d'anti-double-relance,
> donc pas d'installation.

## Sense (lecture seule)

1. **Devis expirant sous 7 j** : `list_devis` → échéance dans `seuil_devis_expirant_jours`.
2. **Deals dormants** : `get_pipeline` → deals sans activité, avec leur valeur.
3. **Historique de relance** : lire la table `vente_relances_journal` — ne pas
   re-relancer un deal/devis déjà relancé récemment (fenêtre KB).

## Plan

4. Devis expirant → **1re relance** personnalisée (déléguer la rédaction à
   `redaction-commerciale`). Devis déjà relancé sans réponse → **2e relance** avec
   incitation (bonus onboarding, garantie — paramètres `./rapido-kb/commercial/offres.md`).
5. Deals dormants **classés par valeur**, **UNE prochaine action** chacun.

## Act (niveau 1 max — brouillons confirmés)

6. Préparer les relances en **brouillon** (`devis-facture-relance`) ; **rien ne part
   sans confirmation** (`garde-envois` + autonomie.md). Après envoi confirmé,
   **journaliser dans `vente_relances_journal`** (deal/devis, type de relance, date).

## Feed

7. Table `vente_relances_journal` tenue à jour (anti-double-relance) + leçons dans
   `./rapido-kb/commercial/apprentissages.md` (quelle incitation convertit).

## Report

8. Une page : devis expirants (client, montant, échéance, relance préparée), deals
   dormants top valeur avec leur prochaine action, ce qui attend une confirmation d'envoi.
