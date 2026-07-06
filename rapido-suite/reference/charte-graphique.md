# Charte graphique (rapido-suite)

> ⚠️ **CHARTE GÉNÉRIQUE DE REPLI** — ces valeurs ne représentent aucune
> marque. Ordre de priorité réel : `./rapido-kb/charte-graphique.md` →
> `get_brand` → ce fichier. Tout agent qui utilise ce repli doit le
> SIGNALER dans sa réponse.

Ce plugin embarque le serveur CMS : pour tout contenu visible créé pendant une
orchestration (posts, cartes digitales, campagnes de l'onboarding client),
privilégier les valeurs LIVE via `get_brand` + `get_company` + `get_profile`.
Si une base de connaissance `./rapido-kb/charte-graphique.md` existe dans le
répertoire de travail (version COMPLÉTÉE par l'onboarding entreprise), elle
prime sur ce fichier générique. Ordre : API live > KB > ce fichier.
En cas de conflit : la valeur API gagne, sauf mention contraire de l'utilisateur.

## Couleurs (codes hex) — palette neutre professionnelle (repli)

- Primaire : `#1E293B`
- Secondaire : `#64748B`
- Accent : `#3B82F6`
- Neutres : fond clair `#F8FAFC`, fond foncé `#0F172A`, texte `#0F172A`,
  texte secondaire `#64748B`

Règle : utiliser les codes EXACTS — jamais d'approximation ni de couleur proche.

## Typographies (repli : polices système sûres)

- Titres : Inter, repli `system-ui, sans-serif` (graisse : 600)
- Corps : Inter, repli `system-ui, sans-serif` (graisse : 400)

## Logos

- **Aucun logo par défaut** — utiliser le logo renvoyé par `get_brand`, ou le
  demander au client. Ne JAMAIS générer ni inventer un logo de substitution.

Règles d'usage :
- Marge de protection : hauteur du logo × 0,5 sur chaque côté (défaut).
- Choisir la variante selon le fond ; URL publique obligatoire.
- Usages INTERDITS : déformer, recolorer, pivoter, appliquer des effets.

## Ton de voix (repli)

Professionnel, clair et factuel — vouvoiement, orienté bénéfice client, sans
superlatifs. (Le ton réel du client vient de la KB ou de `get_brand`.)

### Do
- Phrases courtes, un seul appel à l'action, vocabulaire concret.

### Don't
- Jargon interne, promesses chiffrées non vérifiées, majuscules criardes.

## Application

Toute création de contenu pendant une orchestration (visuels `generate_image`,
captions `create_draft_tool`, pages de cartes `edit_card_page`, templates)
applique cette charte — mêmes règles que les plugins rapidocms et rapidocrm.
Mêmes valeurs de repli que rapidocms/rapidocrm, pour un comportement prévisible.
