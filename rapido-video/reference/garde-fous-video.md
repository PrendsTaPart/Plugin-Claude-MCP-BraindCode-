# Garde-fous montage vidéo (rapido-video)

Règles **non négociables** de tout skill du plugin.

## (a) Musique & médias — droits obligatoires
- **Aucune musique/piste audio ajoutée sans droits** : la source doit être libre de
  droits (banque autorisée), fournie par l'utilisateur avec accord, ou sous licence.
  À défaut → **refus** du mix, en expliquant. Jamais de piste « trouvée » injectée.
- Idem pour toute image/vidéo tierce incrustée (logo, footage) : provenance vérifiée
  (assets de marque RapidoCMS, ou fournis avec accord).

## (b) Dépendances & installation — zéro action utilisateur
- ffmpeg/Whisper **auto-installés** par l'agent (`scripts/bootstrap_video.py`), après
  **annonce des tailles + une confirmation**. **Aucun guide manuel** ; ne jamais
  demander à l'utilisateur d'installer un binaire.

## (c) Providers externes (voie optionnelle avancée)
- Pour toute voie s'appuyant sur un **provider externe** (OpenMontage, TTS/gen
  tiers…) : **vérifier la présence des variables d'environnement AVANT lancement**.
  Absente → le dire et proposer la voie 100 % libre ou distante.
- **Jamais** de clé/secret **demandé en clair** dans la conversation ni **écrit dans
  le dépôt** ; les clés vivent dans l'environnement de l'utilisateur uniquement.

## (d) Temps de rendu selon l'environnement
- La durée de rendu **dépend de la machine** : l'annoncer comme telle (à mesurer
  localement), **jamais** un chiffre présenté comme absolu.

## (e) Sortie — jamais de publication directe
- Les rendus sont **rapatriés** en bibliothèque (RapidoCMS `upload_file_tool`) et
  **proposés en brouillon** ; la publication/planification reste sous le garde-fou
  d'envoi du plugin concerné. **Aucune diffusion automatique.**
- Nommage : `{marque}-{contenu}-{format}-vN`.

## (f) Calculs & recettes
- Le modèle **n'écrit jamais** une commande ffmpeg de tête : il passe par les
  **recettes** de `scripts/monter.py` / `scripts/sous_titres.py` (auditables).
