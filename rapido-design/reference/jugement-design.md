# Jugement design — le goût (anti-goût-IA)

**Révisé le 2026-07-15.** La couche qui évite le rendu « template IA ». Francisé de
`styleseed` et `qiaomu-design` (MIT, **réécrits maison** — cf. `NOTICE.md`) ; le pendant
design de `rapido-copywriter:anti-voix-ia`. À charger en **Étape 0** de tout skill design,
et à appliquer comme **gate de critique** avant livraison.

## Les principes de goût

- **Hiérarchie claire** : une seule chose domine chaque écran (taille, poids, couleur,
  position, densité). Si tout crie, rien ne ressort.
- **Respiration** : l'espace blanc est un choix, pas un vide. Marges généreuses, échelle
  d'espacement cohérente (4/8/12/16/24/32…).
- **Une idée par écran** : un objectif, un CTA principal. Le reste soutient.
- **Typographie qui travaille** : 2 familles max, une échelle de tailles nette, interligne
  1.4-1.7, `text-wrap: pretty` sur les titres. La typo porte la hiérarchie.
- **Couleur intentionnelle** : une couleur d'accent qui guide l'action ; le reste en
  neutres. Contraste **WCAG AA** (voir gate a11y).
- **Système, pas one-off** : tokens et composants réutilisables, pas des écrans peints à la
  main. Le fil rouge des tokens (charte → Figma → Lovable).

## Liste noire — le « goût IA » à bannir

- **Gradients violets/indigo par défaut** (le violet SaaS générique).
- **Glassmorphism partout** (flou + transparence sur chaque carte).
- **Emojis en puces** de liste / en début de chaque titre.
- **Cartes identiques à l'infini** (grille de cartes clonées sans hiérarchie).
- **Ombres portées « 2015 »** (drop-shadow lourde et uniforme).
- **Inter partout** par défaut (police par dépit).
- **Coins arrondis + bordure gauche colorée** (le cliché « carte d'alerte »).
- **Centrage systématique** de tout le texte ; **dégradés de texte** décoratifs.

## Quand dire NON (arbitrage)

- Le client demande **6 couleurs vives** → arbitrer avec la **charte** : une couleur
  d'accent + neutres ; proposer une palette qui respecte l'identité, expliquer pourquoi.
- « Mets plus d'animations / de la 3D / du parallax partout » → **sobriété motion** (une
  intention par animation, cf. `motifs-animation.md`) ; refuser le carnaval, argumenter.
- « Copie le style de [produit connu] » → s'**inspirer d'un pattern**, **jamais** recréer
  la langue de design d'une marque tierce (règle anti-verbatim).
- Structure non validée mais « fais-le joli » → **non** : wireframes validés d'abord
  (pipeline étape 4).

> Dire non se fait **avec un argument et une alternative**, jamais sèchement. 2 itérations
> max par étape (l'agent `directeur-ux` arbitre). Théorie de persuasion visuelle :
> `rapido-meta-ads:influence-psychology` (renvoyée, pas dupliquée).
