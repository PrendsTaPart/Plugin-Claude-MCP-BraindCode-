# Pièges des outils Canva — règles OBLIGATOIRES

À charger avant tout usage des outils Canva. Ces règles viennent des schémas
réels du serveur ; les enfreindre = échec d'appel ou perte de travail.

## 1. PRÉSENTATIONS — flux imposé, sans exception

1. `request-outline-review` D'ABORD (l'appeler directement, sans poser de
   questions préalables) : construire l'outline complet — `pages` =
   `[{title, description}]`, descriptions en puces markdown à TIRETS
   (`- Item\n- Item`), JAMAIS de caractère « • » ; `length` défaut `short`
   (1-5 slides — chaque slide ajoute de la latence) ; `topic` ≤ 150 caractères.
2. VALIDATION UTILISATEUR de l'outline dans le widget. Toute demande de
   modification (ajouter/retirer/réordonner des slides) = RE-appeler
   `request-outline-review` avec l'outline modifié, jamais générer directement.
3. PUIS SEULEMENT `generate-design-structured` (exige : `topic`, `audience`,
   `style`, `length`, `design_type: "presentation"`, `presentation_outlines`).
- INTERDIT : `generate-design` avec `design_type: "presentation"` après un flux
  d'outline, ou `generate-design-structured` sans outline approuvé.
- Note : certains clients exposent un outil `prepare-design-generation` à
  utiliser en premier ; il n'est PAS disponible sur cette connexion — le flux
  ci-dessus est le bon ici.

## 2. EXPORTS

- TOUJOURS `get-export-formats` (`design_id`) AVANT `export-design` : les
  formats supportés varient par design et par page — ne jamais deviner, même
  si l'utilisateur a nommé le format.
- `design_id` : 11 caractères, commence par « D » (les IDs dans les URLs de
  candidats n'en sont PAS).
- TOUJOURS afficher l'URL de téléchargement à l'utilisateur après l'export.
- PDF : `size` a4/a3/letter/legal ; PNG : `transparent_background`,
  `as_single_image` pour fusionner un multi-pages.

## 3. ÉDITION — transaction ou perte des modifications

1. `start-editing-transaction` (`design_id`) → mémoriser le `transaction_id`
   ET le tableau `pages` retourné.
2. `perform-editing-operations` (`transaction_id`, `operations` EN BLOC,
   `page_index`, `pages` = le tableau retourné par l'appel précédent).
   - Pages `is_responsive: true` : SEULES opérations permises `update_title`,
     `replace_text`, `update_fill`, `delete_element`, `find_and_replace_text` —
     sinon alerter l'utilisateur au lieu d'appeler.
   - Remplacement d'un mot présent à plusieurs endroits : confirmer les
     occurrences visées avant.
3. `commit-editing-transaction` — les modifications sont en BROUILLON et
   PERDUES sans commit. TOUJOURS montrer la preview (thumbnails de chaque
   réponse) et obtenir l'accord explicite de l'utilisateur AVANT le commit ;
   après commit, donner le lien d'ouverture du design. `cancel-editing-transaction`
   pour abandonner. Un `transaction_id` committé est invalide.
- Ne JAMAIS dire « c'est enregistré » avant un commit réussi.

## 4. GÉNÉRATION

- `generate-design` produit des CANDIDATS : présenter les candidats, faire
  choisir, puis `create-design-from-candidate` (`job_id` + `candidate_id`)
  OBLIGATOIRE avant toute édition ou export du candidat choisi.
- L'outil est SANS MÉMOIRE : requête `query` détaillée avec TOUT le contexte
  à CHAQUE itération (reprendre les détails des requêtes précédentes).
- Erreur « Common queries will not be generated » = requête trop vague :
  demander des précisions et enrichir la query.
- `user_intent` : à renseigner à chaque appel (description concise du but).

## 5. CHARTE / MARQUE

- Demander à l'utilisateur s'il veut un design « on-brand » ; si oui,
  `list-brand-kits` et faire choisir le `brand_kit_id` AVANT de générer.
- Si l'API renvoie « Missing scopes: [brandkit:read] » : demander de
  déconnecter/reconnecter le connecteur Canva.
- Sans brand kit : injecter la palette et le ton de
  `./rapido-kb/charte-graphique.md` (sinon la charte générique du plugin)
  directement dans la `query`.

## 6. TEMPLATES RÉCURRENTS (autofill)

- `search-brand-templates` avec `dataset: "non_empty"` pour trouver les
  templates auto-remplissables ; `get-brand-template-dataset` pour connaître
  les champs.
- L'outil `autofill-design` mentionné par la doc Canva n'est PAS exposé sur
  cette connexion : pour remplir un template, passer par
  `create-design-from-brand-template` (`brand_template_id` commence par
  « BTM ») puis une transaction d'édition (§3) pour injecter les valeurs — ou
  signaler la limite à l'utilisateur.
- Dataset vide = template non auto-remplissable : proposer le `create_url` du
  template pour une création manuelle.
