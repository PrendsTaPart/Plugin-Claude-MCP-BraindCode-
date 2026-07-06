# Prompt Lovable — Site de présentation « Rapido Suite pour Claude »

> Copiez-collez le bloc ci-dessous dans Lovable pour générer un site vitrine +
> mini-documentation qui explique le plugin, l'écosystème et l'onboarding.
> Remplacez les [valeurs] par vos infos réelles avant de lancer.

---

## Prompt principal (à coller dans Lovable)

```
Crée un site vitrine moderne, une seule page (landing) avec ancres de navigation,
pour présenter « Rapido Suite pour Claude » : un plugin qui connecte l'IA Claude à
4 logiciels de gestion pour piloter une entreprise en langage naturel.

STACK & QUALITÉ
- React + Tailwind + shadcn/ui, responsive mobile-first, mode sombre par défaut.
- Design premium tech (façon SaaS AI) : fond bleu nuit, halos néon sobres, beaucoup
  d'espace, animations d'apparition discrètes au scroll. Pas de template générique.

CHARTE (couleurs exactes)
- Fond principal #0B1E3F, fond profond #060B1A
- Accent violet #7C3AED, accent cyan #22D3EE
- Texte #F5F7FA
- Dégradés violet→cyan pour les CTA et les titres clés.

SECTIONS (dans l'ordre)
1. HERO — titre « Pilotez toute votre entreprise en langage naturel »,
   sous-titre : « Claude connecté à vos 4 plateformes métier. 100+ compétences,
   sous votre contrôle. » Deux boutons : « Demander une démo » et « Voir comment ça marche ».
   Visuel : un noyau IA central relié à 4 modules (CRM, CMS, RH, Restauration).
2. LE PROBLÈME — « 6 outils, 47 onglets, 1 seule journée. » Illustrer la dispersion
   des outils. Ton empathique.
3. LA SOLUTION — « Une phrase suffit. » 3 exemples de commandes en langage naturel
   qui s'exécutent (Prépare mon briefing / Relance mes factures / Planifie ma campagne).
4. LES 4 PLATEFORMES — 4 cartes : RapidoCRM (ventes), RapidoCMS (marketing),
   RapidoRH (RH & projets), FoodEatUp (restauration), chacune avec 3 exemples d'actions.
5. LES 5 FAMILLES DE SKILLS — direction, CRM, marketing, RH, restauration :
   grille de 100+ compétences métier packagées.
6. SÉCURITÉ & CONTRÔLE — 3 points : confirmation des actions sensibles, contrôles
   automatiques (ex. HACCP), traçabilité des écritures. Rassurer : « rien n'est
   envoyé sans votre validation ».
7. LA BASE DE CONNAISSANCE — expliquer que le plugin apprend VOTRE entreprise
   (prix, charte, ton) via un dossier versionné qui reste chez vous ; les mises à
   jour du plugin ne l'écrasent jamais.
8. COMMENT DÉMARRER — 4 étapes : installer le plugin → poser rapido-kb/ →
   « Configure le plugin et apprends à connaître mon entreprise » → c'est parti.
9. FAQ — 4 questions : Mes données sont-elles en sécurité ? Faut-il coder ?
   Quels logiciels sont nécessaires ? Puis-je garder le contrôle des publications ?
10. CTA FINAL + pied de page (BraindCode / Rapido Software).

CONTENU & TON
- Français, vouvoiement, professionnel et direct, orienté bénéfice concret.
- Chaque section = un titre court + 1-2 phrases + éléments visuels/icônes (lucide-react).
- Pas de jargon inutile ; expliquer « MCP » simplement (« un pont sécurisé entre
  l'IA et vos logiciels »).

INTERACTIF (léger)
- Un petit "démo simulée" : champ où l'utilisateur tape une commande parmi des
  suggestions et voit une réponse pré-écrite s'afficher (pas d'appel API réel).
- Navigation sticky avec ancres, bouton « Demander une démo » qui ouvre un formulaire
  simple (nom, email, entreprise) — sans back-end, juste un état local + message de
  confirmation.

Livre un site prêt à publier, cohérent, sans texte Lorem ipsum.
```

---

## Variante « connectée » (mode avancé)

Si vous voulez que le formulaire de démo crée un vrai prospect dans RapidoCRM,
ajoutez à la fin du prompt :

```
Le formulaire de démo doit, à la soumission, appeler l'API Anthropic (modèle
claude-sonnet-4-6) avec le MCP RapidoCRM connecté, pour créer le prospect dans le
pipeline. Gère l'état de chargement et un message de succès/erreur. N'expose aucune
clé API côté client.
```

> Note : cette variante nécessite le connecteur RapidoCRM actif dans votre espace
> et relève du skill `agent-ia-produit` / `usine-a-landing`.
