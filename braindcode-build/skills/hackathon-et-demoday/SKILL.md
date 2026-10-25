---
name: hackathon-et-demoday
description: Utiliser quand l'utilisateur parle hackathon ou demoday Build — « inscris le projet au hackathon », « où en est le demoday ? », « prépare mon pitch », « montre l'arène ». Dates vérifiées avant toute inscription, pitch répété avec l'Academy, arène en lecture.
---

# Hackathon et demoday

## Étape 0
- `${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md` — braindcode-2026
  était encore marqué « ouvert » après sa fin (14 octobre, jury le 16) :
  les DATES de la fiche font foi, pas le statut seul.

## Démarche
1. **Lire** : `list_hackathons`, puis `get_hackathon` — VÉRIFIER les
   dates (inscriptions, fin, jury) avant de proposer quoi que ce soit ;
   un hackathon terminé mais marqué ouvert se SIGNALE à l'utilisateur,
   on ne s'y inscrit pas.
2. **S'inscrire** : `join_hackathon` SUR ACCORD (hook garde-build) —
   rattache le projet au hackathon.
3. **Le demoday** : `get_demoday` — format, créneaux, attendus du jury.
4. **Le pitch** : `register_pitch` SUR ACCORD après aperçu du contenu ;
   la répétition passe par `get_pitch_training` de l'Academy quand elle
   est connectée (structure, minutage, questions du jury).
5. **L'arène** : `get_clash_arena` — le score humains vs Claude Code et
   les votes du public, restitués tels quels.

## Pièges
- Un pitch qui promet ce que l'app ne fait pas encore : le pitch suit le
  rapport de test, pas l'inverse.

## Dégradation propre
Aucun hackathon ouvert aux dates valides : le dire, et préparer le pitch
quand même si l'utilisateur le veut (il resservira).
