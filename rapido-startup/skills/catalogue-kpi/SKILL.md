---
name: catalogue-kpi
description: Utiliser quand l'utilisateur demande un KPI, une métrique, une formule (MRR, CAC, LTV, churn, runway, burn, NRR, Rule of 40, DSO, point mort, vélocité pipeline, food cost…), « comment se porte ma boîte en chiffres », ou quand une routine Loop Engine a besoin d'un calcul.
---

# Catalogue KPI — formules, données réelles, calcul par script

Un KPI = une formule exacte + des données MCP réelles + un calcul par script.
Jamais de calcul de tête, jamais de chiffre sans formule affichée.

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md`,
`references/formules-kpi.md` (LE catalogue : formule, outils MCP, fréquence,
seuil, pièges par KPI) et les seuils : `./rapido-kb/processus-internes.md`
PRIME, sinon `${CLAUDE_PLUGIN_ROOT}/reference/seuils-defaut.md` (le dire :
« défaut secteur »).

## RÈGLE ABSOLUE — le script calcule, pas le modèle

Pour CHAQUE KPI demandé, dans cet ordre :

1. **Collecter les données via MCP** (outils exacts listés par KPI dans
   `references/formules-kpi.md`) — lecture seule ; montants Stripe convertis
   des CENTIMES vers l'unité AVANT d'écrire les entrées, conversion annoncée.
2. **Écrire le JSON d'entrées** : `{"kpi": "...", "entrees": {...}, "seuil":
   {...}, "source_seuil": "rapido-kb | seuils-defaut"}` — chaque entrée
   tracée (outil source + période).
3. **Exécuter** `python3 ${CLAUDE_PLUGIN_ROOT}/skills/catalogue-kpi/scripts/calcul_kpi.py`
   avec ce JSON sur stdin.
4. **Afficher TOUJOURS la formule avec les valeurs** (champ
   `formule_appliquee` de la sortie), la valeur, le seuil retenu et sa
   source, et le statut (ok / attention / alerte).

Un hook `Stop` (`garde-calcul-script`) BLOQUE toute réponse qui annonce un
KPI chiffré sans exécution du script dans le tour — ne pas le contourner :
si le script ne couvre pas un cas, le dire et proposer d'étendre le
catalogue, pas calculer de tête.

## Workflow type

1. **Comprendre la demande** : un KPI précis, ou un panorama (« comment se
   porte ma boîte en chiffres » → les 5-8 KPI pertinents selon l'activité :
   SaaS → MRR/churn/NRR/runway ; restaurant → food cost/ticket moyen/marge ;
   services → charge vs contrat/coût de revient/DSO ; commercial →
   vélocité/coverage).
2. **Même période partout** dans un panorama multi-serveurs.
3. Collecte MCP → JSON → script → restitution (formule visible, source des
   données, source du seuil).
4. **Routine Loop Engine** : mêmes étapes, sortie JSON du script reprise
   telle quelle ; la fréquence de calcul par KPI est dans le catalogue.
5. Proposer d'enregistrer les valeurs marquantes dans
   `./rapido-kb/startup/business-plan/hypotheses.md` (source + date) si un
   business plan est en cours (skill `interview-business-plan`).

## Pièges (rappel — détail par KPI dans formules-kpi.md)

- **Churn annuel = composé** : `1 − (1 − churn_mensuel)^12`, JAMAIS ×12.
- **Montants Stripe en centimes** : convertir avant le JSON d'entrées.
- **Contrat annuel dans le MRR** : montant annuel ÷ 12, pas compté le mois
  de signature.
- Un KPI sans seuil comparable (KB ou défaut) se restitue « sans seuil » —
  pas de verdict inventé.
- Données partielles (serveur absent, période incomplète) : le dire, ne pas
  extrapoler.

## Source unique des formules (anti-divergence)
Ce skill est la **source de vérité des formules KPI** du marketplace. Tout autre
skill qui a besoin d'un CAC, LTV, ratio, coverage, runway, DSO… **reprend la formule
d'ici** (mêmes définitions), jamais une variante locale :
- `rapido-marketing:attribution-kpi-marketing` : son CAC par canal = `dépense/clients`
  (**même formule**) ; ce qui lui est propre = la **répartition/attribution par canal**
  (que ce skill ne fait pas) + `LTGP`/`ROI` marketing (≠ LTV).
- `rapido-marketing:money-math-acquisition` : **délègue** tout calcul ici.
- `rapidocrm:pilotage-commercial`, routines `VENTE-*`, Loop Engine : coverage et
  ratios **calculés ici**, jamais de tête.

Le **Registre des KPIs** (`reference/registre-routines.md`) liste chaque KPI, sa
formule canonique, son script propriétaire et les skills autorisés à le citer.
