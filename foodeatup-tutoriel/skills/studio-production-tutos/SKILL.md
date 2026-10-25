---
name: studio-production-tutos
description: Utiliser quand on produit le contenu pédagogique lui-même, que l'utilisateur dit « qu'est-ce qui n'est pas encore couvert », « quelles vidéos restent à tourner », « écris le script de la vidéo partenaire », « prépare le brief de tournage ». Audite les manques du catalogue, sert les briefs officiels (client et partenaire) et aide à écrire scripts et plans de tournage dans le ton imposé.
---

# Studio de production des tutos (les manques, puis les briefs)

## Étape 0 — Références (obligatoire)

Charger `${CLAUDE_PLUGIN_ROOT}/reference/directives-outils.md` et
`${CLAUDE_PLUGIN_ROOT}/reference/pieges-verifies.md`.

## Workflow

1. **L'état des manques** : `audit_formation` (global, ou `moduleSlug` ;
   `limite` pour borner les exemples) — sujets filmés, fiches sans vidéo,
   manques connus. Croiser avec `lister_modules` (`videosEnLigne` vs
   `videosPrevues`) pour prioriser : un module annoncé mais vide passe avant
   un module presque complet.
2. **Prioriser** : proposer un ordre de tournage argumenté (demande des
   apprenants rencontrée en séance, modules socles avant modules experts,
   parcours convive et partenaires encore sans vidéo).
3. **Les briefs officiels** :
   - parcours convive → `brief_video_client` (slug ou les dix briefs) :
     objectif, plan en cinq points, ton, durée visée, vignette déjà
     produite ;
   - réseau partenaires → `brief_video_partenaire` (`profil` ou `titre`) :
     objectif pédagogique, plan de tournage, durée cible, ton imposé.
4. **Écrire le script** à partir du brief, EN RESPECTANT le plan en cinq
   points, la durée cible et le ton. S'inspirer des fiches voisines
   (`transcription_tutoriel` d'une vidéo du même module donne le ton réel).
5. **Livrer** : script + plan de tournage + rappel de la vignette existante.
   La production vidéo elle-même (tournage, montage, publication) sort de ce
   plugin — les plugins `rapido-video`/`rapido-higgsfield` outillent le
   montage, et la PUBLICATION d'un tutoriel reste un geste humain côté
   serveur.

## Garde-fous

- **Aucun concurrent nommé, aucune promesse chiffrée** dans un script — ton
  imposé par les briefs, sans exception.
- Un manque se constate par `audit_formation`, il ne s'invente pas ; et un
  script ne comble jamais un manque dans la conversation (« voilà la marche
  à suivre que la vidéo aurait montrée ») — le sujet reste « à produire ».
- Les briefs convive décrivent des vidéos NON tournées : aucun lien vidéo
  annoncé (règle du skill `espace-convive`).
- Montants (coût de production, rémunération) : hors périmètre du serveur —
  aucun chiffre.
