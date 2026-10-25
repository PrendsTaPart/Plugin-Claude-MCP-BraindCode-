---
name: modeles-de-messages
description: Utiliser quand l'utilisateur crée ou retouche ses modèles Prospector Hub — « crée un modèle d'e-mail de démo », « ajoute un modèle SMS », « modèle de message LinkedIn pour cette connexion ». Un modèle n'est enregistré qu'après le contrôle de conformité.
---

# Modèles de messages (e-mail, SMS, appel, LinkedIn)

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/conformite-prospection.md` ;
- `./rapido-kb/prospection.md` (identité d'expéditeur, désinscription,
  mention STOP) — sans elle, les modèles restent des brouillons locaux.

## Démarche
1. **Inventorier d'abord** : `list_email_templates`,
   `list_message_templates` (kind sms / call),
   `list_linkedin_templates` (par `connectionId`) — pas de doublon de
   modèle.
2. **Rédiger** : la copy se délègue au plugin rapido-copywriter quand il
   est installé (skill `copy-linkedin` pour LinkedIn) ; sinon rédaction
   sobre maison, variables entre {{double_accolades}} nommées.
3. **Contrôler AVANT d'enregistrer** :
   `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/conformite.py --canal email
   modele.txt` (ou sms / appel) — identité, désinscription ou STOP,
   longueurs. Un modèle NON CONFORME ne s'enregistre pas.
4. **Enregistrer** : `add_email_template` (name, subject, html),
   `add_message_template` (kind sms ou call), `add_linkedin_template`
   (connectionId, name, content). Modifier : `update_email_template`,
   `update_message_template`, `update_linkedin_template`.
5. **Supprimer** : `delete_email_template` / `delete_message_template` /
   `delete_linkedin_template` sur confirmation (définitif).

## Pièges
- Les modèles LinkedIn sont rattachés à UNE connexion (connectionId) : un
  « modèle LinkedIn global » n'existe pas côté serveur — garder le texte
  maître en local et le décliner.
- Un lien de lead magnet temporaire (`list_lead_magnets`) ne va JAMAIS
  dans un modèle : pointer la page de capture.

## Dégradation propre
KB sans identité d'expéditeur : produire le modèle en BROUILLON local et
dire ce qui manque pour l'enregistrer conforme.
