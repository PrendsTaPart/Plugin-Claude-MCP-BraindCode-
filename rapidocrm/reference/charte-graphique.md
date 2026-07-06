# Charte graphique (rapidocrm)

> ⚠️ **CHARTE GÉNÉRIQUE DE REPLI** — ces valeurs ne représentent aucune
> marque. Ordre de priorité réel : `./rapido-kb/charte-graphique.md` →
> `get_brand` → ce fichier. Tout agent qui utilise ce repli doit le
> SIGNALER dans sa réponse.

Ce plugin n'a PAS accès au `get_brand` du serveur CMS : sans
`./rapido-kb/charte-graphique.md`, ce fichier est donc le repli effectif pour
tout contenu visible produit depuis le CRM — templates email
(`create_template_email`, `create_editor_template`), templates SMS
(`create_template_sms`), newsletters (`send_newsletter`), contenus de campagnes.

## Couleurs (codes hex) — palette neutre professionnelle (repli)

- Primaire : `#1E293B`
- Secondaire : `#64748B`
- Accent (boutons / liens) : `#3B82F6`
- Neutres : fond clair `#F8FAFC`, fond foncé `#0F172A`, texte `#0F172A`,
  texte secondaire `#64748B`

Règle : utiliser les codes EXACTS — jamais d'approximation ni de couleur proche.

## Typographies (repli : polices système sûres)

- Titres : Inter, repli `system-ui, sans-serif` (graisse : 600)
- Corps : Inter, repli `system-ui, sans-serif` (graisse : 400)
- Emails HTML : pile de secours web-safe obligatoire —
  `Arial, Helvetica, sans-serif`.

## Logos

- **Aucun logo par défaut** — demander l'URL publique au client (ou la
  récupérer via le plugin rapidocms / `get_brand` si installé). Ne JAMAIS
  générer ni inventer un logo de substitution.

Règles d'usage :
- Marge de protection : hauteur du logo × 0,5 sur chaque côté (défaut).
- En-tête d'email/newsletter : variante adaptée au fond ; toujours une URL
  publique accessible.
- Usages INTERDITS : déformer, recolorer, pivoter, appliquer des effets.

## Ton de voix (repli)

Professionnel, clair et factuel — vouvoiement, orienté bénéfice client, sans
superlatifs. (Le ton réel du client vient de la KB.)

### Do
- Objet d'email < 60 caractères, un seul appel à l'action, signature complète
  avec coordonnées, vocabulaire concret.

### Don't
- Majuscules dans l'objet, pièces jointes lourdes, jargon interne, relances
  agressives avant le calendrier d'escalade.

## Application par outil

- `create_template_email` / `create_editor_template` / `send_newsletter` :
  HTML aux couleurs et typos ci-dessus, logo en en-tête, appel à l'action à la
  couleur accent.
- `create_template_sms` / `send_sms` : ton de voix, pas de mise en forme —
  signature courte de la marque.
- `send_email` (relances comprises) : appliquer ton + do/don't ; pour les
  relances d'impayés, rester factuel et courtois (voir devis-facture-relance).
