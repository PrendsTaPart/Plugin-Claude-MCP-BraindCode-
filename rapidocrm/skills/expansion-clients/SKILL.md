---
name: expansion-clients
description: Utiliser quand l'utilisateur veut faire monter ses clients en gamme, détecter les opportunités d'upsell, ou piloter le tunnel Studio → Agence → SaaS de BraindCode. Détecte 3 transitions à signaux réels dans les données (livrables Studio finis, projet agence à J-15, client SaaS actif 3+ mois), prépare la proposition (déléguée à redaction-commerciale), crée le devis après confirmation, planifie la relance J+7. Tout en brouillon.
---

# Expansion clients — la boucle Studio → Agence → SaaS

Détecte, dans les **données réelles**, les clients prêts à passer au palier suivant,
puis prépare la proposition. **Rien ne part sans confirmation** ; fourchettes et
paliers viennent de `./rapido-kb/offres.md` (jamais en dur — absent → le signaler).

## Les 3 transitions (signaux détectables)

### STUDIO → AGENCE
- **Signal** : incubé dont les **livrables Studio sont terminés** — projet RapidoRH
  dont les colonnes *Lean Canvas / BP / pitch deck* sont à **Done** (lecture du
  Kanban RapidoRH, en prose : liste des tâches du projet).
- **Argumentaire AIDA** : « votre projet est structuré, passons au MVP » —
  fourchette et paliers lus dans `./rapido-kb/offres.md`.

### AGENCE → SAAS
- **Signal** : **projet agence à J-15 de la livraison** (jalon Kanban RapidoRH /
  Calendar à 15 jours).
- **Pitch** : pack **RapidoSoftware** pour exploiter ce qui vient d'être construit,
  **essai 14 jours**.

### SAAS → PALIER SUPÉRIEUR
- **Signal** : **client actif 3+ mois avec usage soutenu** — campagnes CRM lancées
  (`list_campagnes`, `get_stats_campagne`) et posts CMS publiés (activité éditoriale,
  en prose). Ancienneté via `get_contact` / `get_entreprise`.
- **Pitch** : palier supérieur adapté à l'usage constaté (chiffres réels à l'appui).

## Pour chaque opportunité

1. **Préparer la proposition** — déléguer la rédaction à `redaction-commerciale`
   (argumentaire AIDA, valeur démontrée par les livrables/usage réels).
2. **Créer le devis** au CRM (`create_devis`) **après confirmation** — jamais d'office.
3. **Planifier la relance J+7** (`create_task` / `create_rdv`), en brouillon.
4. **Tout envoi = confirmation** (`garde-envois` + autonomie.md).

## Anti-collision
- **`programme-ambassadeurs`** (rapidocrm) : moi = faire **monter en gamme** un
  client ; lui = transformer un client satisfait en **apporteur** (10 %/20 %). Deux
  boucles distinctes, souvent enchaînées (un client au palier SaaS est aussi un bon ambassadeur).
- **`pilotage-commercial`** : m'**invoque** dans sa boucle (routine `VENTE-EXPANSION`).

## Garde-fous
Signaux **lus dans les données réelles** (Kanban, CRM, CMS), jamais supposés ;
fourchettes/paliers depuis `./rapido-kb/offres.md` ; devis créé **après
confirmation** ; tout envoi en **brouillon** ; pas de promesse chiffrée non sourcée.
