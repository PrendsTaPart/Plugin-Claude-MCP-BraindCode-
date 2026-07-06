# Évals — marketplace Rapido

Cas de test manuels à dérouler après `/plugin marketplace add` + install +
`/reload-plugins`. Chaque cas se joue DEUX fois : avec et sans `./rapido-kb/`
dans le répertoire de travail. Critère global : avec KB, les valeurs MAISON
sont utilisées ET citées ; sans KB, les défauts secteur sont utilisés ET
signalés (« valeur par défaut — lancez l'onboarding pour personnaliser »).

## Éval 1 — Seuil food cost maison (foodeatup / analyse-rentabilite-carte)

**Setup KB** : créer `./rapido-kb/processus-internes.md` contenant :
```
## Seuils financiers
- Food cost cible maximum : 28 %
```

**Prompt** : « Analyse la rentabilité de ma carte. »

| | Attendu |
|---|---|
| **Avec KB** | Le skill lit le seuil 28 %, le passe en 2e argument à `menu_matrix.py` ; la sortie affiche `source_seuil_food_cost: "maison (rapido-kb)"` ; un plat à 29 % de food cost est EN ALERTE ; la restitution cite « votre food cost cible est 28 % — processus-internes.md ». |
| **Sans KB** | Le script tourne sans 2e argument (seuil 30 %, `"défaut secteur"`) ; un plat à 29 % n'est PAS en alerte ; la restitution signale « valeur par défaut — lancez l'onboarding pour personnaliser ». |
| **Échec si** | seuil calculé de tête sans le script ; seuil maison ignoré ; défaut utilisé sans le signaler. |

## Éval 2 — Cadence de relance maison (rapidocrm / directeur-commercial + coaching-pipeline)

**Setup KB** : créer `./rapido-kb/processus-internes.md` contenant :
```
## Cadences de relance
- Devis sans réponse : J+2, J+5, J+10
```

**Prompt** : « Le devis de la société X est parti hier sans réponse, programme les relances. »

| | Attendu |
|---|---|
| **Avec KB** | Les 3 `schedule_email` proposés tombent à J+2 / J+5 / J+10 de l'envoi du devis, avec la citation « votre cadence est J+2/J+5/J+10 — processus-internes.md » ; demande de confirmation avant programmation. |
| **Sans KB** | Cadence par défaut J+3 / J+7 / J+15, explicitement annoncée comme valeur par défaut avec suggestion d'onboarding. |
| **Échec si** | cadence maison ignorée ; cadence par défaut présentée comme si elle venait du client ; envois programmés sans confirmation. |

## Éval 3 — Arguments et ton maison (rapidocrm / redaction-commerciale + rapidocms / community-manager)

**Setup KB** : créer `./rapido-kb/propositions-valeur.md` :
```
## Différenciateurs
- Seul traiteur de la région certifié bio ET halal
- Livraison garantie en 45 min sinon remboursé (preuve : 99,2 % de tenue en 2025)
```
et `./rapido-kb/ton-et-accroches.md` :
```
## Ton
Complice, direct, tutoiement. Mots interdits : « leader », « révolutionnaire ».
## Accroches validées
- « Le bio qui arrive avant ta faim. »
```

**Prompt** : « Écris un email de prospection pour un restaurant d'entreprise » puis « Fais un post Instagram pour l'offre du midi ».

| | Attendu |
|---|---|
| **Avec KB** | L'email argumente sur les différenciateurs de `propositions-valeur.md` (certification, garantie 45 min avec la preuve chiffrée) en citant la source ; le post Instagram tutoie, réutilise ou décline l'accroche validée, et ne contient NI « leader » NI « révolutionnaire ». |
| **Sans KB** | Arguments limités aux données CRM réelles avec signalement que le message serait plus percutant après onboarding ; post au ton générique du réseau, signalé comme tel. |
| **Échec si** | différenciateurs inventés ; mots interdits présents malgré la KB ; accroches maison ignorées ; aucune citation de source. |

## Éval 4 — Installation vierge (portabilité)

**Setup** : simuler un NOUVEAU client — répertoire de travail propre, AUCUNE
KB (`./rapido-kb/` absent), aucun MCP optionnel connecté (pas de Canva, pas
de Lovable, pas de Meta, `N8N_MCP_URL` non définie, compte Google non
autorisé). Seuls les serveurs Rapido du client répondent.

**Prompts à dérouler** (un par plugin concerné) :

| Prompt | Attendu |
|---|---|
| démarrage de session | hooks SessionStart : rapido-suite suggère l'onboarding (KB absente) ; rapido-n8n affiche le message guidé `N8N_MCP_URL` |
| « analyse ma carte » | fonctionne (serveur foodeatup présent) ; seuil food cost 30 % annoncé « valeur par défaut — lancez l'onboarding » |
| « crée mon menu imprimable » | pas d'erreur brute : une phrase expliquant que Canva n'est pas connecté + marche à suivre + préparation du contenu (plats réels) en attendant |
| « fais-moi une landing page » | idem pour Lovable : explication + initial_message préparé |
| « lance une pub » | idem pour Meta : explication + plan de campagne préparé, plafond par défaut 50/jour mentionné |
| « automatise les relances » | explication `N8N_MCP_URL` + renvoi vers `rapido-n8n/README-installation.md`, sans planter |
| « ma journée » | briefing DÉGRADÉ : volets emails/agenda Google sautés EN LE DISANT, volets CRM/FoodEatUp livrés |
| « configure le plugin » | l'onboarding démarre : collecte auto sur les serveurs disponibles, blocs de questions (dont le bloc réglages techniques : fuseau, devise, establishment_id, plafond pub, rappel n8n) |

**Échec si** : une seule de ces demandes produit une erreur brute, invente
une donnée pour combler l'absence d'un MCP, ou référence une URL/un compte
qui n'appartient pas au client.

## Notes d'exécution

- Jouer chaque éval dans un dossier de travail propre ; pour le cas « sans
  KB », supprimer ou renommer `./rapido-kb/`.
- Le hook SessionStart de rapido-suite doit annoncer la KB (présente → liste
  des fichiers ; absente → suggestion d'onboarding) : le vérifier en début de
  session.
- Consigner tout écart dans le CHANGELOG du plugin concerné avant correction.
