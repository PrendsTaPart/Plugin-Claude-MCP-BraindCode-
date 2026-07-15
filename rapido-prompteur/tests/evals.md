# Évals — plugin rapido-prompteur (0.2.0)

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
