# Motifs d'animation — catalogue sobre

**Révisé le 2026-07-15.** Patterns d'animation web **génériques** (durées, easings —
savoir commun), **inspirés** de magicui / motion-primitives / animata (**motifs
référencés, aucun code embarqué** ; cf. `NOTICE.md`). Règle d'or (`jugement-design.md`) :
**une intention par animation**, jamais de carnaval. **`prefers-reduced-motion: reduce`
obligatoire** sur chaque motif.

## Barème transverse

- **Durées** : micro-interaction 120-200 ms · entrée/transition 200-400 ms · jamais > 500 ms.
- **Easing** : `ease-out` pour l'entrée (rapide puis pose), `ease-in-out` pour les
  transitions ; éviter le `linear` (mécanique).
- **Perf** : animer **`transform` et `opacity`** uniquement (GPU) ; **jamais** `width`/
  `height`/`top`/`left` (reflow) ni d'ombres animées en boucle. Viser **60 fps**.
- **Reduced-motion** : sous `@media (prefers-reduced-motion: reduce)`, remplacer par un
  fondu discret **ou** aucune animation (état final direct).

## Catalogue

| Motif | Intention | Durée · easing | Contre-indication |
|---|---|---|---|
| **Entrée de page** (fade + translate 8-16 px) | poser le contenu sans brusquer | 250-350 ms · ease-out | pas sur chaque élément → effet cascade lourd |
| **Scroll-reveal** (apparition au scroll) | rythmer la lecture, un bloc à la fois | 200-300 ms · ease-out | pas sur du texte long (gêne la lecture) ; `IntersectionObserver`, une fois |
| **Hover states** (CTA, cartes) | feedback d'affordance | 120-180 ms · ease-out | pas de scale > 1.03 ; jamais sur mobile (pas de hover) |
| **Micro-interaction formulaire** (focus, validation) | guider et rassurer | 120-200 ms · ease-out | pas d'animation d'erreur agressive (shake léger max) |
| **Transition de navigation** (page/onglet) | continuité spatiale | 250-400 ms · ease-in-out | pas de transition longue qui retarde l'action |
| **Compteur / chiffre animé** | souligner une preuve | 400-600 ms · ease-out | une seule fois, jamais en boucle |
| **Skeleton / loading** | occuper l'attente | pulsation 1-1.5 s | pas de spinner + skeleton en même temps |

## Règles de sobriété

- **Maximum 2-3 surfaces animées** par écran (hero, CTA, un feedback) — pas tout.
- Une animation qui n'a **pas d'intention** (juste « faire joli ») → **retirée**.
- Toute animation a son **fallback reduced-motion** testé.

---
*Motifs inspirés de [magicui](https://github.com/magicuidesign/magicui),
[motion-primitives](https://github.com/ibelick/motion-primitives),
[animata](https://github.com/animata-design/animata) — **licences à confirmer avant tout
emprunt de code** ; ici **aucun code embarqué**, seulement des motifs génériques réécrits.
Voir `NOTICE.md`.*
