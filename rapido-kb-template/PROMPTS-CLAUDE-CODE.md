# Prompts Claude Code — Plugin Rapido Suite

> Copiez-collez ces phrases dans Claude Code (ou l'app Claude connectée aux MCP).
> Les skills se déclenchent au langage naturel : ces formulations sont testées pour
> toucher le bon workflow. Adaptez les valeurs entre [crochets].

---

## 0. Premier lancement (bootstrap)

- « Configure le plugin et apprends à connaître mon entreprise. »
  → lance l'onboarding : pré-remplit `rapido-kb/` depuis les MCP, puis interview.
- « Teste ma connexion : vérifie que RapidoCRM, RapidoCMS, RapidoRH et FoodEatUp répondent. »
- « Quel est mon establishment_id FoodEatUp ? » (si vous avez un restaurant)

## 1. Base de connaissance (rapido-kb/)

- « Construis ma base de connaissance rapido-kb. »
- « Mets à jour ma base de connaissance : [le prix de X passe à Y / nouveau concurrent Z / nouvelle offre]. »
- « Relis ma charte et applique-la à tout ce que tu produis. »

## 2. Direction / pilotage quotidien

- « Prépare ma journée. » (briefing : mails, agenda, business, alertes, 3 priorités)
- « Fais-moi le brief du lundi matin. »
- « Comment va la boîte ? Donne-moi un snapshot une page. »
- « Trie ma boîte mail et prépare des brouillons de réponse. »
- « Prépare une prévision de trésorerie sur 30/60/90 jours. »
- « Qui me doit de l'argent ? Prépare les relances au ton adapté. »
- « Prépare le comité de direction. »

## 3. CRM / Ventes (RapidoCRM)

- « Où en sont mes deals ? Qu'est-ce que je dois relancer ? »
- « Fais une revue de pipeline complète cette semaine. »
- « Prospecte [secteur] à [ville] et ajoute les meilleures au pipeline. »
- « Écris un cold email à [entreprise/prospect]. »
- « Recherche des renseignements sur [entreprise]. »
- « Crée un devis pour [client] : [lignes]. »
- « Relance les factures impayées. »
- « Fais-moi un forecast de ventes pour le trimestre. »
- « Donne-moi la performance de l'équipe commerciale. »

## 4. Marketing / Contenu (RapidoCMS)

- « Prépare mon calendrier éditorial du mois. »
- « Crée une campagne de [N] posts sur [réseau] pour [sujet]. »
- « Génère un visuel pour [sujet] aux couleurs de ma charte. »
- « Programme ce post sur [compte] le [date] à [heure]. »
- « Quels posts ont le mieux marché ? Donne 3 recommandations. »
- « Vérifie ce texte contre ma voix de marque avant publication. »
- « Crée une séquence d'emails de [onboarding / nurture / win-back]. »

## 5. RH / Projets (RapidoRH)

- « Où en est le projet [nom] ? Revue hebdo. »
- « Aide-moi à recruter un(e) [poste] : fiche, annonce, questions, grille. »
- « Prépare l'onboarding de [prénom] : comptes, rôle, permissions, plan 30/60/90. »
- « Qui est surchargé dans l'équipe ? »
- « Crée une tâche [titre] dans le projet [nom] et assigne-la à [personne]. »
- « Fais-moi un rapport RH (effectifs, turnover, organisation). »

## 6. Restauration (FoodEatUp) — si applicable

- « Donne-moi le briefing du jour du restaurant. »
- « Fais le point HACCP du jour. »
- « Analyse la rentabilité de ma carte. »
- « Crée la recette [nom] et calcule sa marge. »
- « Quels stocks sont bas ? Prépare une commande fournisseur. »
- « Prépare le service : réservations, plan de salle, staffing. »
- « Construis / mets à jour ma carte en ligne (vitrine). »

## 7. Publicité Meta (rapido-meta-ads) — si applicable

- « Lance une campagne Facebook/Instagram pour [objectif]. » (créée en PAUSED, activée après votre accord)
- « Comment performent mes pubs ? Donne 3 constats + 3 actions. »
- « Que font mes concurrents en pub ? »
- « Crée une audience de mes clients + un lookalike 1 %. »

## 8. Automatisations (rapido-n8n) — si applicable

- « Automatise : à chaque [événement], fais [action]. »
- « Est-ce que mes automatisations tournent ? Cherche les erreurs. »

## 9. Design & sites (Canva / Lovable) — si applicable

- « Crée un visuel Canva pour [réseau] et enchaîne-le dans le pipeline CMS. »
- « Génère la présentation du CODIR. »
- « Construis un site pour mon restaurant avec réservation connectée. »
- « Crée une landing page pour la campagne [nom]. »

---

## Bonnes pratiques
- Les actions destructrices (suppression, publication, activation de pub) demandent
  toujours une confirmation explicite. Rien n'est envoyé sans votre accord.
- Un visuel généré vous est toujours montré avant planification.
- Si un ID de tenant est faux, le serveur renvoie « Resource not found » :
  renseignez les bons IDs dans `entreprise.md`.
