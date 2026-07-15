# Grille de coûts Higgsfield (crédits)

> Relevé **live le 2026-07-15** via `get_cost: true` (préflight, aucune facturation)
> et **1 génération réelle** (image test). Workspace : **plan gratuit, 10 crédits**.
> `credits` = crédits facturés (arrondi) ; `credits_exact` = coût exact.
> ⚠️ Tous les coûts sont **par job** ; ils varient avec résolution/durée/audio.

## Images (bon marché)
| Livrable type | Modèle / réglage | Crédits |
|---|---|---|
| Portrait / UGC | `soul_2` (2k) | ~1 (exact 0.12) |
| Visuel pub image | `marketing_studio_image` (1k) | 2 |
| **Image standard 1k** | `nano_banana_pro` (1k) | **2** ✅ *(réel : balance 10→8)* |
| Packshot 4K / texte | `nano_banana_pro` (4k) | 4 |

## Vidéos (coûteuses)
| Livrable type | Modèle / réglage | Crédits |
|---|---|---|
| Clip vidéo 5s | `kling3_0` (5s, std) | 10 |
| Clip vidéo 10s | `kling3_0` (10s, std) | 20 |
| Clip 4K 5s | `kling3_0` (5s, mode 4k) | 30 |
| Vidéo réf 5s | `seedance_2_0` (5s, 720p, std) | 22.5 |
| **Pub vidéo 15s** | `marketing_studio_video` (15s déf., 720p, audio on) | **75** |

## Audio
| Livrable type | Modèle | Crédits |
|---|---|---|
| Voix off courte (TTS) | `seed_audio` (~1 phrase) | 0.4 |

## Montage / formats
| Livrable type | Outil / réglage | Crédits |
|---|---|---|
| Short restylé 30s | `shorts_studio_create` (30s) | 90 |

## Non préflightables (à mesurer à l'usage)
- **`upscale_image`** : `get_cost` exige un `image_id` résoluble (pas d'estimation à vide).
- **`upscale_video`** : pas de `get_cost` (schéma).
- **`dubbing`** : pas de `get_cost` (schéma) — coût à relever au 1er doublage réel.

## Lecture pour la gouvernance (H2)
- **Le plan actif est gratuit : 10 crédits.** Une **seule** vidéo Kling 5s (10 cr)
  épuise le solde ; une pub 15s (75 cr) ou un short (90 cr) sont **hors budget**.
- **Images et audio** sont abordables (≤ 4 cr) ; **toute vidéo/short** exige un
  **top-up / plan payant** avant exécution réelle.
- Le hook `garde-couts` (H1) impose déjà le marqueur `get_cost`/`cout_confirme` ;
  `budget-media.md` doit fixer un **plafond** cohérent avec le solde réel.
- Le coût facturé peut être **arrondi** au-dessus du coût exact (ex. `soul_2`
  exact 0.12 → 1 crédit) : toujours raisonner sur `credits` (arrondi), pas `credits_exact`.
