---
name: tableau-de-bord-prospection
description: Utiliser quand l'utilisateur demande « où en est ma prospection ? », « fais le point commercial Prospector », « combien d'envois aujourd'hui ? » ou ouvre sa journée de prospection. Un écran — entonnoir, envois du jour vs quotas, LinkedIn du jour, MRR estimé — et trois priorités.
---

# Tableau de bord prospection

## Étape 0 — à lire avant tout
- `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` (les cinq lois) ;
- `./rapido-kb/prospection.md` s'il existe (quotas, fenêtre) — sinon le dire
  et appliquer les défauts prudents.

## Démarche
1. **Prospection** : `prospection_history` (dernières zones, volumes) et
   `list_logs` (dernières actions journalisées).
2. **Base** : `list_clients` — volumes globaux, puis par statut si le champ
   est servi. Aucun chiffre reconstruit : un champ absent s'affiche « — ».
3. **Envois récents** : `list_emails`, `list_sms`, `list_calls` (limites
   raisonnables), et la file du jour `list_linkedin_scheduled_day`
   (date du jour, heure de Paris).
4. **Quotas** : `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/quotas.py` —
   envoyés/quota par canal, formule affichée.
5. **Revenus** : `stripe_stats`, lu par
   `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/mrr.py` — MRR présenté comme
   ESTIMATION, agrégé, sans e-mail client.
6. **Restitution en UN écran** (widget tableau-de-bord-prospection si
   demandé) : l'entonnoir (scripts/entonnoir.py), les envois du jour vs
   quotas, la file LinkedIn, le MRR estimé — puis TROIS priorités
   argumentées (relances dues, zone à prospecter, contenu en retard),
   proposées, jamais exécutées d'office.

## Pièges
- Réponses et rendez-vous ne sont PAS mesurés par le serveur Prospect :
  ils s'affichent « — (côté CRM) », voir skill `synchroniser-vers-rapidocrm`.
- La file LinkedIn du jour n'envoie rien toute seule (calendrier
  d'enregistrement) : la traiter passe par le skill `linkedin-du-jour`.

## Dégradation propre
Serveur non connecté (OAuth refusé, 401) : le dire, ne rien inventer, et
proposer la connexion dans la session. KB absente : défauts prudents
annoncés.
