# Frameworks — interview business plan

Boîte à outils des phases. Chaque framework se remplit avec les réponses de
l'interview — jamais avec des généralités.

## Business Model Canvas (BMC) — 9 blocs

| Bloc | Question centrale | Phase source |
|---|---|---|
| 1. Segments clients | Pour qui crée-t-on de la valeur ? Qui PAIE ? | 3.2, 6.1 |
| 2. Proposition de valeur | Quel problème résout-on, 10× mieux ? | 3.5-3.7 |
| 3. Canaux | Comment atteint-on et livre-t-on le client ? | 6.4, 7.3 |
| 4. Relation client | Self-service, accompagné, grands comptes ? | 6.5 |
| 5. Flux de revenus | Qui paie quoi, combien, à quelle fréquence ? | 6.2-6.3 |
| 6. Ressources clés | Que doit-on posséder (équipe, techno, données) ? | 6.6 |
| 7. Activités clés | Que doit-on savoir faire mieux que tous ? | 6.6 |
| 8. Partenaires clés | De qui dépend-on ? | 6.7 |
| 9. Structure de coûts | Les 5 plus gros postes, fixes vs variables | 6.8 |

Restitution : un tableau 9 lignes dans `06-business-model.md`, chaque bloc en
2-3 phrases MAX, le bloc le plus fragile marqué ⚠️ (question 6.9).

## Lean Canvas (variante early-stage)

Remplace, pour un projet pré-revenu, 4 blocs du BMC : Partenaires → Problème
(top 3), Activités → Solution (top 3 features), Ressources → Indicateurs clés,
Relation → Avantage déloyal (ce qui ne se copie pas). Utiliser le Lean Canvas
si la phase 2 révèle un stade « idée/prototype », le BMC sinon.

## TAM / SAM / SOM

- **TAM** (Total Addressable Market) : la dépense annuelle totale du marché,
  SOURCÉE (étude datée, données publiques). Sert au récit, pas au prévisionnel.
- **SAM** (Serviceable Available Market) : la part que VOTRE offre peut
  servir (géographie, langue, segment, canal). Chaque restriction est écrite.
- **SOM** (Serviceable Obtainable Market) : ce que vous pouvez CAPTER en
  3 ans — TOUJOURS bottom-up :
  `SOM = clients atteignables/an × taux de conversion × panier annuel`
  chaque terme sourcé dans hypotheses.md. **Le top-down « 1 % du TAM » est
  refusé** : il ne dit rien de la capacité réelle d'exécution.
- Cohérence : le CA année 3 du prévisionnel (phase 9) doit être ≤ SOM —
  sinon l'un des deux ment.

## SWOT (synthèse, à remplir après les phases 2-8)

| | Interne | Externe |
|---|---|---|
| **Positif** | Forces : équipe, actifs, avantage déloyal (2.3, 5.5) | Opportunités : dynamique marché, « why now » (4.4) |
| **Négatif** | Faiblesses : trous d'équipe, dépendances (2.5, 8.7) | Menaces : concurrents entrants, réglementation (5.6, 8.5) |

Règle : 3-5 puces par case, chacune reliée à une réponse d'interview (pas de
SWOT générique). Chaque menace/faiblesse renvoie à une parade dans la section
Risques du business plan.

## Les 5 questions des investisseurs (et du banquier)

Le dossier final doit répondre à ces 5 questions en moins de 2 minutes de
lecture — les vérifier avant l'assemblage :

1. **Pourquoi ça, pourquoi vous, pourquoi maintenant ?** (problème vécu,
   équipe crédible, timing — phases 2-4)
2. **Le marché est-il assez grand et atteignable ?** (SOM bottom-up sourcé)
3. **Le modèle gagne-t-il de l'argent à l'unité ?** (LTV:CAC ≥ 3:1, payback
   5-12 mois — ou le plan pour y arriver)
4. **Qu'avez-vous PROUVÉ à date ?** (traction réelle : paiements, usage,
   engagements signés — pas des intentions)
5. **Que faites-vous de l'argent, et jusqu'où va-t-il ?** (usage des fonds
   ligne à ligne, runway visé 12-18 mois, jalons atteints avec cette enveloppe)

## Mom Test — rappels de conduite (toutes phases)

- Parler de LEUR vie, jamais de VOTRE idée ; du PASSÉ, jamais du futur.
- Les compliments sont des données nulles ; seuls comptent les engagements
  (argent, temps, réputation).
- Creuser le concret : « la dernière fois », « combien », « montrez-moi ».
- Détail complet : skill `mom-test` (plugin rapidocrm).
