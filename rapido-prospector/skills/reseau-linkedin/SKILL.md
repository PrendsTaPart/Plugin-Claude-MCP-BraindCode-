---
name: reseau-linkedin
description: Utiliser quand l'utilisateur gère son réseau LinkedIn Prospector Hub — « ajoute cette connexion », « enrichis ces profils », « retrouve mes contacts chez X ». Comptes, connexions, enrichissement provider_id par lot réduit et sur accord.
---

# Réseau LinkedIn (comptes, connexions, enrichissement)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (section
  LinkedIn : provider_id, cascades).

## Démarche
1. **Comptes d'envoi** : `list_linkedin_accounts` — la SEULE source des
   `account_id`. Ajouter/modifier un compte (`add_linkedin_account`,
   `update_linkedin_account`) = configuration : accord requis (hook).
2. **Chercher** : `list_linkedin_connections` (search, company,
   `enrichedOnly: true` pour les profils prêts à l'envoi), pagination.
   Détail : `get_linkedin_connection`.
3. **Créer / corriger** : `add_linkedin_connection` (prénom ou nom
   requis), `update_linkedin_connection` — données réelles uniquement.
4. **Enrichir** : `enrich_linkedin_profile` (id + account_id) — webhook
   facturé : par LOT RÉDUIT, sur accord, en annonçant le volume. C'est le
   prérequis (provider_id) de toute invitation ou message.
5. **Supprimer** : `delete_linkedin_connection` sur confirmation, en
   rappelant la CASCADE (modèles + historique + messages programmés).

## Pièges
- Un envoi vers une connexion non enrichie échoue : vérifier
  `enrichedOnly` avant de préparer une séquence.
- La stratégie social selling (profil, cadence, contenu) vit dans le
  plugin rapido-marketing (skill `social-selling-linkedin`) : ici on tient
  le CARNET et les prérequis techniques.

## Dégradation propre
Webhook d'enrichissement en erreur : restituer, consigner, ne pas
réessayer en boucle ; proposer de continuer avec les profils déjà
enrichis.
