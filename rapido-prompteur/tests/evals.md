# Évals — plugin rapido-prompteur (0.3.0)

## Anti-déclenchements (le directeur ne s'invite pas partout)

| Phrase | NE doit PAS router vers | Route correcte |
|---|---|---|
| « Écris un post LinkedIn » | `directeur-prompts` (ce n'est pas un prompt de génération média) | `rapidocms:pipeline-contenu-social` |
| « Génère l'image » avec un **brief net** (produit, angle, format connus) | `directeur-prompts` (pas de détour : le brief est déjà clair) | skill exécutant direct (`rapidocms:prompt-engineering-visuel` ou `rapido-higgsfield:studio-image-pro`) |
| « Corrige la faute de texte dans ce visuel » | `directeur-prompts` | `rapidocms:prompts-visuels-pro` (protocole zéro faute) |

> Le directeur `directeur-prompts` s'active pour **cadrer un besoin flou / multi-moteurs**
> ou obtenir des **variantes comparées** — pas pour un brief déjà net ni pour du copy.

## agent directeur-prompts + boucle d'apprentissage

| # | Phrase | Attendu |
|---|---|---|
| DP1 | « J'ai un besoin flou, transforme-le en prompt » | `directeur-prompts` : étape 0 (grammaire-des-moteurs + regles-de-construction + patterns + **`list_prompts` GAGNANT d'abord**) → charte `get_brand` → **moteur choisi + grammaire lue en direct** (`models_explore`) → **3 variantes** (prompt complet affiché + paramètres réels + coût + références) → **délègue au skill exécutant** (jamais de génération payante en direct) → **propose la capitalisation** (`add_prompt`) |
| BA1 | « Ces prompts ont tourné, mets à jour ce qui marche » | boucle : métriques **réelles** (`post_insights`, virality, réutilisations) → `scripts/score_prompts.py` → tags **GAGNANT/NEUTRE** (`edit_prompt`) + journal `apprentissages.md` ; **INSUFFISANT** si aucune métrique (jamais de score inventé) ; l'agent **pioche les GAGNANT d'abord** ensuite |


## prompt-lovable

| # | Phrase | Attendu |
|---|---|---|
| PL1 | « Fais-moi un prompt Lovable pour ma landing » | `prompt-lovable` : étape 0 marque (`get_brand`/KB, hex+police+logo) → doc Lovable lue en direct → **brief 6 sections affiché en bloc** (rôle/objectif → pages/sections → design system charte → données & **mode B** form → CRM `enregistrer_prospect` → interdits (`localStorage`, clé serveur, parse par nom, données réelles) → **critères d'acceptation testables**) → propose `create_project`/`plan_mode` |
| PL2 (routage) | « Aide-moi à explorer l'idée de mon site (parcours idéation) » | **renvoie** vers `rapido-forge:ideation-lovable-prompt` (idéation StartupsForge) — `prompt-lovable` = version outillée marque+CRM, déclencheurs distincts ; « construis/déploie » → `rapido-lovable:usine-a-landing`/`site-restaurant` |

## prompt-personnage

| # | Phrase | Attendu |
|---|---|---|
| PP1 | « Donne-moi des prompts cohérents pour ma mascotte dans 3 scènes » | `prompt-personnage` : lit `personnages.json` (canon) + banque `traits-personnages.md` → **verrouille les traits de canon** (morphologie/tenue/style) → **combine** les axes variables (pose × expression × éclairage × décor × cadrage) → 3 prompts 6 blocs **affichés en bloc**, tous cohérents ; négatif délégué à `rapidocms:prompts-visuels-pro` |
| PP2 (routage média + boucle) | « Je veux la mascotte en version réaliste/vidéo » vs « visuel réseau brandé » | réaliste/vidéo/Elements/Soul → `rapido-higgsfield:personnages-univers` (`element_id`/`soul_id`) ; image brandée courante depuis un portrait canon → `rapidocms:coherence-personnage` (`images_to_image`) ; combinaison validée → **enrichit la banque** + `add_prompt` (`rapidocms:bibliotheque-prompts`) |

## Garde-fous (rappel)

- `PreToolUse anti-ip.py` : un prompt sortant nommant une IP/marque/artiste (liste
  `reference/ip-a-risque.md`) ou une formule « style de [artiste] » → **confirmation
  avec avertissement**. Personnage 100 % original imposé.
- `Stop` : récap des prompts produits (moteur, grammaire lue en live, prompt
  affiché, négatif, contrôle anti-IP).
