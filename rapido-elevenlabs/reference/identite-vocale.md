# Identité vocale — une voix par marque (et par personnage)

> La marque a des couleurs, un logo… et une **voix**. Symétrie avec
> `brand_id` / `element_id` / `soul_id` : le `voice_id` est l'identité audio.
> Le registre réel vit côté client (`./rapido-kb/`), **jamais dans ce dépôt**.

## Modèle de fiche voix (à stocker dans la charte du client)

```
Voix : [nom de la voix]
- voice_id : [id ElevenLabs]
- marque : [slug marque]           (ou personnage : [nom], à côté d'element_id/soul_id)
- source : [voice design | clonage | voix de bibliothèque]
- modèle recommandé : [Multilingual v2/v3 (final) | Flash (brouillon)]
- params : stability [0-1], similarity [0-1], style [0-1]  (valeurs figées après tests)
- usages autorisés : [voix off, posts audio, narration épisodes, agent vocal…]
- consentement (si clonage) : [chemin du document écrit archivé]  ← OBLIGATOIRE
- date / version : [AAAA-MM-JJ vN]
```

## Où vit le `voice_id`

- **Marque** → section « Identité vocale » de `charte-graphique.md` (patch rapidocms) :
  aux côtés des couleurs hex, police, logo. Toute narration d'une marque utilise **SA** voix.
- **Personnage** (narrateur PronoClip, mascotte) → `rapido-kb/personnages.json`, à côté
  d'`element_id` / `soul_id` (dimension vocale du canon — patch `coherence-personnage` /
  `personnages-univers` en E3). Chaque épisode garde la même voix.

## Règles

- **Cohérence vocale = cohérence de marque** : ne pas changer de voix d'un contenu
  à l'autre pour une même marque/personnage.
- **Voice design est LENT** (piège 3) : prévenir, ne pas conclure à l'échec.
- **Clonage** : uniquement voix propres/consenties ; consentement écrit archivé et
  son chemin consigné dans la fiche (garde-voix force la confirmation).
- Paramètres (`stability`/`similarity`/`style`) **figés après tests** puis réutilisés —
  pas de réglage au hasard à chaque génération.
