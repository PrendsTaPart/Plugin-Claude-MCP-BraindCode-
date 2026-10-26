---
name: commentaires
description: Utiliser quand l'utilisateur traite ses commentaires YouTube — « réponds aux commentaires sans réponse », « quelles questions en attente ? », « gère les négatifs ». Filtres réels, brouillon relu par l'humain, réponse publique sur accord - jamais d'automatique sur négatif ou spam.
---

# Commentaires

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/quota-et-credits.md` (50 unités par
  réponse).

## Démarche
1. **Lire** : `yt_list_comments` avec les filtres réels — sans réponse,
   questions, négatifs, spam, forte interaction, mot-clé. Le paramètre
   sync CONSOMME du quota : sur accord seulement.
2. **Rédiger** : `yt_draft_comment_reply` — un BROUILLON par
   commentaire, relu et ajusté par l'humain.
3. **Répondre SUR ACCORD** : `yt_reply_to_comment` (réponse PUBLIQUE au
   nom de la chaîne + 50 unités — hook garde-public) — un par un.
4. **Les cas sensibles** : AUCUNE réponse automatique à un commentaire
   négatif ou à un spam — le négatif se traite avec l'humain (ou
   s'ignore sur sa décision), le spam se signale dans l'application.
5. **File** : widget file-commentaires (sans réponse, par ancienneté).

## Pièges
- 20 réponses = 1 000 unités : compter la série dans le quota du jour
  AVANT de commencer.
- Une réponse publiée ne s'édite pas d'ici : relire AVANT.

## Dégradation propre
Flot trop gros : prioriser (questions > forte interaction > reste) avec
des volumes dits, plutôt que « tout traiter » mal.
