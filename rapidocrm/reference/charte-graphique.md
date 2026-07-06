# Charte graphique (rapidocrm)

Ce plugin n'a PAS accès au `get_brand` du serveur CMS : ce fichier est donc LA
source de vérité pour tout contenu visible produit depuis le CRM — templates
email (`create_template_email`, `create_editor_template`), templates SMS
(`create_template_sms`), newsletters (`send_newsletter`), contenus de campagnes.

## Couleurs (codes hex)

### À COMPLÉTER
- Primaire : `#______`
- Secondaire : `#______`
- Accent (boutons / liens) : `#______`
- Neutres : fond clair `#______`, fond foncé `#______`, texte `#______`,
  texte secondaire `#______`

Règle : utiliser les codes EXACTS — jamais d'approximation ni de couleur proche.

## Typographies

### À COMPLÉTER
- Titres : ______ (graisse : ______)
- Corps : ______ (graisse : ______)
- Emails HTML : prévoir une pile de secours web-safe (ex. Arial, Helvetica,
  sans-serif) — ### À COMPLÉTER.

## Logos

### À COMPLÉTER
- Logo principal (couleur) : URL ______
- Variante monochrome : URL ______
- Variante fond clair : URL ______
- Variante fond foncé : URL ______

Règles d'usage :
- Marge de protection : ### À COMPLÉTER.
- En-tête d'email/newsletter : variante adaptée au fond ; toujours une URL
  publique accessible.
- Usages INTERDITS : déformer, recolorer, pivoter, appliquer des effets.
  ### À COMPLÉTER (interdits spécifiques).

## Ton de voix

### À COMPLÉTER — décrire le ton (ex. « professionnel et direct, vouvoiement,
orienté bénéfice client »).

### Do
- ### À COMPLÉTER (ex. objet d'email < 60 caractères, un seul appel à l'action,
  signature complète avec coordonnées)

### Don't
- ### À COMPLÉTER (ex. majuscules dans l'objet, pièces jointes lourdes, jargon
  interne, relances agressives avant le calendrier d'escalade)

## Application par outil

- `create_template_email` / `create_editor_template` / `send_newsletter` :
  HTML aux couleurs et typos ci-dessus, logo en en-tête, appel à l'action à la
  couleur accent.
- `create_template_sms` / `send_sms` : ton de voix, pas de mise en forme —
  signature courte de la marque.
- `send_email` (relances comprises) : appliquer ton + do/don't ; pour les
  relances d'impayés, rester factuel et courtois (voir devis-facture-relance).
