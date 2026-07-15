# Évals — plugin rapidocrm

## Éval 1 — animation-client (déclenchement)

| Phrase | Attendu |
|---|---|
| « Lance un sondage de satisfaction chez Dupont SA » | `animation-client` (sondage) |
| « Les résultats de mon dernier sondage ? » | `animation-client` (résultats + verbatims) |
| « Organise un jeu concours pour mes clients » | `animation-client` (concours + rappel légal FR) |
| « Combien de points de fidélité a Martin ? » | `animation-client` (fidélité) |
| « Envoie l'invitation au sondage par email » | délégué au skill `communication-client` |
| « Sondage à tout mon segment restaurateurs » | envoi de masse → `campagne-marketing` |

## Éval 2 — animation-client (comportement)

- ATTENDU : `list_sondages` / `list_jeux_concours` AVANT tout lancement
  (jamais de `modele_sondage_id` / `modele_jeu_id` inventé) ; entreprise
  vérifiée ; CONFIRMATION explicite avant `lancer_*` (visible clients) — le
  hook garde-destructif force l'ask en filet (matcher étendu, testé stdin :
  `lancer_sondage_entreprise` → ask).
- ATTENDU concours : rappel une ligne du cadre légal FR (règlement,
  gratuité, RGPD).
- ATTENDU résultats : questions, scores, participation réelle + synthèse
  des verbatims en 3-5 thèmes, citations anonymisées, pas d'embellissement.
- ATTENDU fidélité : `get_loyalty_points` croisé `get_top_clients` MÊME
  période → 2-3 actions de rétention ciblées et nommées.
- ATTENDU : aucun envoi direct — invitations via `communication-client`.
- Croisement Mom Test : « je veux valider mon idée à plus grande échelle »
  → sondage via animation-client avec questions passé/concret (description
  de `mom-test` mise à jour, corps du skill Wondel inchangé).

## Non-régression 1.2.0 (comportements existants inchangés)

- **NR1 — « Relance mes factures en retard »** : devis-facture-relance —
  transitions CRM strictes (brouillon → en_attente → payee ;
  en_attente → en_retard → payee, sinon avoir), relance `send_email` avec
  numéro/montant/échéance, `log_activity` pour tracer. Le nouvel enum
  élargi ne concerne QUE update_invoice_status côté FoodEatUp.
- **NR2 — « Lance un sondage chez Dupont SA »** : animation-client —
  `list_sondages` d'abord (jamais d'ID inventé), confirmation niveau 2
  avant `lancer_sondage_entreprise` (hook en filet), invitations déléguées
  à communication-client (jamais d'envoi direct).

## Éval — gestion-depenses (1.3.0)

- **Phrase** : « Enregistre une dépense de 100 € HT à 20 % de TVA. »
- **Attendu** : `gestion-depenses` — le script controle_depense.py tourne
  AVANT la saisie (TTC attendu 120,00, formule affichée) ; récapitulatif +
  confirmation ; PUIS `create_depense` (hook garde-destructif → ask en
  filet, testé stdin) ; ID et montants restitués.
- **Incohérence** : « … le ticket dit 125 € TTC » → écart 5,00 montré,
  correction demandée AVANT tout appel.
- **Honnêteté serveur** : « montre le détail de la dépense 12 » → pas
  d'outil de détail côté CRM : `list_depenses` filtré, sinon renvoi
  interface (jamais de contournement).

## Éval — capture de leads (1.4.0)

- **Phrase** : « Comment convertit mon formulaire de contact ? » →
  `campagne-marketing` étape 8 : funnel vues → clics CTA → soumissions →
  prospects, taux PAR ÉTAPE via `taux_conversion_etape` (formule affichée).
- **Phrase** : « Traite les nouvelles soumissions du formulaire démo » →
  `prospection-pipeline` : `get_formulaire_soumissions`, dédoublonnage
  email puis nom (`rechercher_prospects`, `list_contacts`) AVANT
  `enregistrer_prospect` ; contact déjà connu → `log_activity`, pas de
  doublon.

## Éval — gate délivrabilité (1.4.3)

- **CM-GATE** (campagne bloquée par le gate, mode newsletter) : « Lance ma
  newsletter à ce segment » **avec rapido-marketing installé** →
  `campagne-marketing` étape 5 invoque `delivrabilite-email` en mode `newsletter` ;
  liste sale ou **lien de désinscription absent** → note sous le seuil → **PAS
  D'ENVOI**, actions correctives listées, rejouer après correction ; hook
  `garde-envois` inchangé.
- **CM-DEGRADE** (rapido-marketing absent → checklist minimale) : même demande
  **sans** le plugin → checklist intégrée déroulée : `recalculer_segment`
  (dédoublonnage + taille), lien de désinscription présent dans le template,
  taille du lot confirmée explicitement ; signale que le **gate complet** vient de
  rapido-marketing ; envoi **confirmé** (`garde-envois`) puis `lancer_campagne`.

## Éval — pilotage-commercial (1.5.0)

**5 phrases déclenchantes** (→ `pilotage-commercial`) :
1. « Pilote mon commercial »
2. « Fais le point ventes / la boucle commerciale »
3. « Sense → Plan → Report sur mes ventes »
4. « Où en est ma conversion, qu'est-ce que je relance en priorité cette semaine »
5. « Lance la revue commerciale du lundi » (VENTE-REVUE)

**3 contre-exemples** (NE doivent PAS déclencher `pilotage-commercial`) :
- « Où en sont mes deals ? » (revue ponctuelle) → **`coaching-pipeline`** (pas la boucle orchestrée).
- « Génère-moi des leads / remplis le haut du tunnel » → **`rapido-marketing:pilotage-marketing`** (génération, pas conversion).
- « Fais le point global de la boîte » → **`rapido-suite:pilotage-entreprise`** (transverse ; il invoque pilotage-commercial pour le volet ventes, sans le dupliquer).

> Frontière : `coaching-pipeline` = revue ponctuelle des deals ; `pilotage-commercial`
> = la boucle complète (hygiène → relances → revue → capitalisation, routines VENTE-*).
> `pilotage-marketing` génère, `pilotage-commercial` convertit.

## Éval — expansion-clients (1.6.0)

**5 phrases** (→ `expansion-clients`) :
1. « Fais monter mes clients en gamme / upsell »
2. « Qui est prêt à passer de Studio à Agence ? »
3. « Mes projets agence bientôt livrés à qui proposer le SaaS »
4. « Quels clients SaaS actifs peuvent monter de palier »
5. « Pilote le tunnel Studio → Agence → SaaS »

**3 contre-exemples** :
- « Transforme mes bons clients en apporteurs » → **`programme-ambassadeurs`** (parrainage, pas montée en gamme).
- « Quel type de programme de parrainage mettre en place » → **`rapido-marketing:lead-getters-systeme`** (choix stratégique du type).
- « Relance mes devis qui expirent » → **`devis-facture-relance`** / routine VENTE-RELANCES.

## Éval — programme-ambassadeurs (1.6.0)

**5 phrases** (→ `programme-ambassadeurs`) :
1. « Opère mon programme ambassadeurs »
2. « Qui est éligible au parrainage 10/20 »
3. « Suis les commissions de mes apporteurs »
4. « Relance mes ambassadeurs »
5. « Transforme mes clients satisfaits en apporteurs BraindCode »

**3 contre-exemples** :
- « Quel type de programme d'affiliation choisir » → **`rapido-marketing:lead-getters-systeme`** (stratégie/type).
- « Fais monter ce client au palier supérieur » → **`expansion-clients`** (montée en gamme).
- « Envoie la newsletter aux ambassadeurs » → **`campagne-marketing`** + gate délivrabilité (envoi de masse).

## Éval — vente terrain opérationnelle (1.7.0)

**preparation-rdv** — 5 : « prépare mon RDV avec X », « je vois ce client demain »,
« profil SONCAS de ce contact », « fiche de prépa entretien », « mon argumentaire pour X ».
Contre-ex : « où en sont mes deals » → `coaching-pipeline` ; « écris-lui un email » →
`redaction-commerciale` ; « teste mon idée business » → `mom-test`.

**qualification-deals** — 5 : « qualifie mon pipeline », « ce deal est-il solide »,
« BANT de mes deals », « quels deals sont fragiles », « lesquels je pousse/sors ».
Contre-ex : « quoi relancer / deals dormants » → `coaching-pipeline` ; « la boucle
commerciale complète » → `pilotage-commercial` ; « méthode de revue de pipeline » →
`pipeline-review-methodo`.

**coach-de-vente** — 5 : « comment vendre à ce prospect », « quelle approche de vente »,
« il ne répond plus je fais quoi », « coach de vente », « quelle méthode pour ce deal ».
Contre-ex : « négocie le prix / il dit trop cher, je négocie » → `negotiation` (Voss) ;
« quels leviers de persuasion » → `rapido-meta-ads:influence-psychology` ; « rédige l'email
de vente » → `redaction-commerciale`.

**playbook-objections-vivant** — 5 : « playbook d'objections », « quelles objections
reviennent », « comment répondre à c'est trop cher », « objections par produit »,
« mets à jour mes réponses aux objections ». Contre-ex : « refais mon offre face à trop
cher » → `rapido-meta-ads:hundred-million-offers` (redessine l'OFFRE) ; « négocie ce
prix » → `negotiation` ; « écris la réponse » → `redaction-commerciale`.

**funnel-aarrr-reel** — 5 : « mon funnel AARRR », « métriques pirates », « où fuit mon
funnel », « taux d'activation/rétention réels », « mon funnel chiffré ». Contre-ex :
« conçois mon funnel AARRR (exercice) » → `rapido-forge:scale-funnel-aarrr` ; « donne-moi
une formule KPT » → `catalogue-kpi` ; « pilote mon marketing » → `pilotage-marketing`.
