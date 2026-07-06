# Conformité — publicité Meta

Règles applicables à TOUT usage des outils facebook-ads de ce plugin.

## Publicité — audiences et données clients

- **Consentement RGPD obligatoire** avant d'envoyer des données clients
  (emails, téléphones) dans une audience personnalisée : poser explicitement
  la question de la BASE LÉGALE à l'utilisateur (consentement marketing
  collecté ? intérêt légitime documenté ?). Pas de base légale claire = pas
  d'upload — proposer l'audience WEBSITE (pixel) à la place.
- Les clients concernés doivent avoir été informés (politique de
  confidentialité mentionnant le partage avec des partenaires publicitaires)
  et pouvoir s'opposer. En cas de doute, remonter à l'utilisateur.
- L'outil hashe lui-même les PII avant envoi — mais le hachage ne remplace
  pas la base légale.

## Catégories spéciales

Crédit, emploi, logement, politique/élections : si l'activité du client touche
l'une de ces catégories, la déclarer (`special_ad_categories`) — le demander
AVANT la création de campagne. Ne jamais tenter de contourner ces règles.

## Conservation des exports

- Les extractions CRM utilisées pour construire une audience (listes
  d'emails/téléphones) ne sont PAS conservées : ni fichier intermédiaire
  gardé, ni collage dans un document ; l'upload fait, la liste est oubliée.
- Ne jamais recopier des PII clients dans la conversation au-delà du strict
  nécessaire (compter plutôt que lister).

## Contenus publicitaires

- Pas de données personnelles de clients dans les créatifs (mêmes règles que
  la charte CONFORMITE du studio) ; témoignages uniquement avec accord.
- Tout chiffre affiché dans une pub (prix, promo, « -30 % ») a une source
  (CRM, FoodEatUp, KB) et est vérifié avant diffusion — une pub mensongère
  engage l'annonceur.
- Alcool et secteurs réglementés : respecter les règles Meta (ciblage d'âge)
  et le droit local (Loi Évin pour l'alcool en France) — signaler le sujet à
  l'utilisateur si sa pub concerne l'alcool.

## Argent réel

- Aucune activation, aucun boost confirmé, aucune étude payante sans
  confirmation explicite avec récapitulatif du coût maximum (les hooks du
  plugin forcent par ailleurs ces confirmations).
- Plafond de budget/jour : celui de `./rapido-kb/processus-internes.md`
  (défaut : 50 €/jour) — au-delà, validation écrite préalable exigée.
