# Décision licences — chaîne montage vidéo

> Recherche du 2026-07-15. Sources vérifiées en direct : `remotion.dev/license`
> (→ LICENSE.md GitHub), `remotion.pro/license`, LICENSE d'OpenMontage (cloné).
> **STOP validation attendu — notamment la décision Remotion.**

## 1. Remotion (moteur de rendu React → vidéo)
**Modèle : gratuit sous seuil d'effectif, payant au-dessus.**
- **Gratuit** : individus, **organisations à but lucratif de ≤ 3 employés**,
  associations/non-profit, et évaluation. (Verbatim : *« a for-profit organization
  with up to 3 employees »*.)
- **Au-delà de 3 employés → licence Company payante** (`remotion.pro/license`) :
  - **Remotion for Creators** — **25 $/mois par siège** (1 siège = 1 utilisateur) ;
  - **Remotion for Automators** — **à partir de 100 $/mois** (modèle à l'usage) :
    c'est la formule pour le **rendu automatisé/programmatique** — exactement ce
    que fait un pipeline piloté par agent (bootstrap → render sans humain) ;
  - **Enterprise** — **à partir de 500 $/mois**, termes sur mesure.
- Le fichier LICENSE ne détaille ni « developer seat » ni clause Lambda spécifique
  (renvoi à remotion.pro).

### Recommandation chiffrée pour BraindCode
- **Si BraindCode ≤ 3 employés** : **0 €** — Remotion est gratuit, utilisable tout de suite.
- **Si BraindCode > 3 employés** : notre usage est **automatisé** (agent) →
  **Remotion for Automators, ~100 $/mois minimum**. Le tier « Creators » (25 $/siège)
  vise l'usage manuel dans un éditeur, pas le rendu piloté.
- **Reco d'architecture (économie)** : **ne PAS dépendre de Remotion pour le socle.**
  La chaîne de base (concat, xfade, sous-titres burn-in, 9:16, upscale) tient
  **100 % sur ffmpeg** (aucune redevance par siège) + **Higgsfield MCP** (déjà payé
  au crédit) pour le génératif. **Réserver Remotion** aux compositions React
  avancées (motion graphics data-driven, templates paramétrés) — et **n'acheter
  Automators (100 $/mois) que si/quand** le rendu Remotion programmatique devient
  réellement central. Décision à valider par toi.

## 2. OpenMontage — **AGPL-3.0** (copyleft fort)
Confirmé : `LICENSE` = *GNU AFFERO GENERAL PUBLIC LICENSE Version 3*.
- **Usage interne : OK** (exécuter l'outil pour produire nos vidéos).
- **Fusion de code INTERDITE** : on ne **copie/mélange pas** son code dans le
  plugin (MIT/propriétaire) — l'AGPL « contaminerait » l'ensemble.
- **Clause réseau (AGPL §13)** : si OpenMontage était **exposé comme service en
  ligne** (SaaS accessible à des tiers), il faudrait **offrir le code source
  (modifié inclus)** aux utilisateurs du service.
- **Décision** : OpenMontage reste un **outil OPTIONNEL, séparé** (dossier **frère**,
  jamais dans le dépôt), **invoqué en sous-processus/CLI** sur demande explicite —
  **jamais fusionné**, **jamais exposé en SaaS** sans conformité AGPL. Conforme au
  pivot (OpenMontage rétrogradé « optionnel avancé »).

## 3. ffmpeg / ffprobe — GPL/LGPL, **appelés en sous-processus**
Les builds statiques (johnvansickle via `imageio-ffmpeg` ; `ffmpeg-static`) sont
GPL. **Mais** : nous **appelons le binaire en sous-processus** (usage-outil), sans
**lier** de bibliothèque ffmpeg dans notre code → c'est de l'**agrégation**, pas du
« travail dérivé ». **→ Usage commercial OK**, sans imposer la GPL à notre code.
Obligation : ne pas redistribuer les binaires en prétendant un autre régime ; si on
**redistribuait** ffmpeg, joindre l'offre de source (les paquets amont s'en chargent).

## 4. Briques MIT (`jianshuo/claude-skills`, `video-recap-skills`, `auto-video-edit`)
**MIT = permissif** : usage commercial/fusion **autorisés**, **seule obligation =
conserver la mention de copyright + le texte de licence**. → Si on réutilise du code
ou une méthode de ces dépôts, **créer une entrée NOTICE** (dépôt, auteur, licence
MIT) comme pour les autres imports du marketplace. *(À vérifier repo par repo : le
texte MIT exact et le titulaire du copyright, avant toute réutilisation.)*

## Synthèse — matrice de décision
| Composant | Licence | Usage interne | Fusion code | SaaS / distribution | Coût |
|---|---|---|---|---|---|
| **ffmpeg** (imageio/static) | GPL/LGPL | ✅ | via sous-processus seult | joindre offre de source si redistribué | **0** |
| **Remotion** | Remotion License | ✅ ≤3 empl. | (biblio, usage normal) | licence si >3 empl. | 0 / **100 $/mois** (Automators) |
| **OpenMontage** | **AGPL-3.0** | ✅ (outil séparé) | ❌ interdit | ❌ sans conformité AGPL §13 | 0 (mais providers payants) |
| Briques MIT | MIT | ✅ | ✅ | ✅ | 0 (mention obligatoire) |

**À valider par toi** : (1) effectif BraindCode (≤3 ou >3) pour trancher Remotion ;
(2) accord sur « socle ffmpeg + Higgsfield, Remotion optionnel Automators si besoin » ;
(3) OpenMontage garde son statut optionnel/séparé.
