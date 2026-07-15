# Séquences email — types & trames

> **Source distillée** : zubair-trabzada/ai-marketing-claude (`market-emails` +
> `templates/`) MIT © 2026 Zubair Trabzada. Reformulé FR, non-verbatim.
> Templates traduits : `docs/methodo/templates-email/`.

## 7 types de séquences (le skill source en définit 7, en fournit 3)
Bienvenue · Nurture · Lancement · Réengagement · Onboarding · Panier abandonné ·
Cold outreach. **3 templates** pré-écrits existent (bienvenue, nurture,
lancement) — traduits en français dans `templates-email/`.

## Trame réutilisable (commune à tous les emails)
**Objet** + **texte d'aperçu** + **corps** (framework numéroté) + **principe
clé / PS**. Un seul CTA par email.

## Les 3 séquences traduites
- **Bienvenue** (5 emails, J0→J8) : accueil + attentes → problème/agitation →
  mini cas client → objection « pas le temps » → check-in.
- **Nurture** (6 emails, J1→J12, ratio valeur/confiance/offre 70/20/10) :
  insight → framework → story → objection → stack de valeur → deadline.
- **Lancement** (8 emails, J-7→J+7, 3 phases pré/lancement/clôture) : teaser →
  pourquoi l'ancien marche mal → sneak peek → live → preuve sociale → FAQ →
  48 h → dernier appel.

## Mapping Rapido
Conception → skill `email-sequence` (existant) ; exécution → templates CRM
(`create_template_email`) + `schedule_email`/`send_newsletter`. **Chaque envoi
confirmé** (`garde-envois`), désinscription présente, consentement RGPD.

→ Cible : alimente `email-sequence` et `machine-inbound` (nurturing).
