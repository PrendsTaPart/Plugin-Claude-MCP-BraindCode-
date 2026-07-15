# Mécanique des hooks — la couche de COMPRÉHENSION

**Révisé le 2026-07-15.** Ceci n'est **pas un catalogue** (voir `banque-hooks.md` pour les
patterns) mais le **pourquoi** : pourquoi un même hook ne marche pas partout, quelles
**familles** existent, et **quelle famille sur quel réseau** (la matrice). Patterns
inspirés de `hook-extractor` (sergebulaev) et `hook-writer` (blacktwist) — **MIT, réécrits
maison, aucun verbatim** (cf. `NOTICE.md`). Théorie psychologique complète →
`rapido-meta-ads:influence-psychology` (renvoyée, jamais dupliquée).

## a. Le contexte d'attention par réseau (le hook ne vit pas au même endroit)

| Réseau | Contexte | Où vit le hook | Fenêtre |
|---|---|---|---|
| **LinkedIn** | Feed **pro**, lecture lente, statut & douleur métier | **Texte** : 1-2 lignes visibles avant « …voir plus » | quelques secondes de lecture |
| **Facebook** | Feed **relationnel/local**, défilement moyen, émotion simple | **Texte** court + visuel natif ; proximité | ~1-2 s |
| **Instagram** | **Visuel d'abord** ; caption ~**125 car.** avant « plus » | **Dans l'image / le 1ᵉʳ slide** (+ caption courte) | ~1 s |
| **TikTok** | **FYP**, décision **< 3 s**, le scroll est l'ennemi à chaque seconde | **Triple hook simultané** : verbal + visuel + texte à l'écran | < 3 s |

**Conséquence** : sur LinkedIn le hook se **lit** ; sur Instagram/TikTok il se **voit et
s'entend**. Traduire mot pour mot un hook LinkedIn en TikTok le tue.

## b. Les familles de hooks (mécanisme · quand · quand éviter)

Réécrites maison. Le **mécanisme** est résumé ; la théorie complète (biais, Cialdini,
émotions) est dans `rapido-meta-ads:influence-psychology`.

1. **Écart de curiosité** — ouvre une boucle que le cerveau veut fermer. *Quand* : TOFU,
   découverte. *Éviter* : si la réponse déçoit (clickbait).
2. **Contre-intuition / contrarien** — casse une croyance admise. *Quand* : TOFU, prise de
   position. *Éviter* : sans preuve derrière → paraît gratuit.
3. **Chiffre-preuve** — un nombre concret et vérifiable ancre la crédibilité. *Quand* :
   MOFU/BOFU. *Éviter* : chiffre inventé ou invérifiable (interdit ici).
4. **Erreur coûteuse** — nomme une faute fréquente et son prix. *Quand* : MOFU. *Éviter* :
   ton culpabilisant.
5. **Avant / après** — montre une transformation. *Quand* : BOFU, preuve. *Éviter* : sans
   cas réel.
6. **Question miroir** — renvoie au lecteur sa situation. *Quand* : TOFU, engagement.
   *Éviter* : question fermée/banale.
7. **Ouverture d'histoire** — démarre une scène (personnage, tension). *Quand* : TOFU
   storytelling. *Éviter* : trop longue avant le point.
8. **Liste à enjeu** — « N façons / erreurs / signes de… ». *Quand* : MOFU, valeur.
   *Éviter* : liste sans enjeu réel.
9. **Négativité utile** — « Arrête de… », ce qu'il ne faut **pas** faire. *Quand* : TOFU.
   *Éviter* : négativité gratuite / anxiogène.
10. **Autorité / coulisses** — « Ce que [métier] ne montre pas ». *Quand* : TOFU/MOFU.
    *Éviter* : fausse exclusivité.

## c. LA MATRICE famille × réseau (pièce centrale)

Déclinaison native de chaque famille : **format · dosage · où vit le hook** + un pattern
`[placeholder]`.

| Famille | LinkedIn (texte, 1-2 lignes) | Facebook (court, local) | Instagram (image/slide, ≤125 car.) | TikTok (verbal+visuel+texte, <3 s) |
|---|---|---|---|---|
| **Écart de curiosité** | `Personne ne parle de [sujet]. Voici pourquoi ça compte.` | `On a remarqué un truc sur [sujet local]…` | slide 1 : `Ce que personne ne te dit sur [X]` | verbal : `Reste, tu vas pas croire [X].` |
| **Contrarien** | `Tout le monde fait [X]. C'est une erreur.` | `Et si [croyance locale] était fausse ?` | image texte : `❌ [croyance] → ✅ [vérité]` | `Arrête [X]. Sérieux.` (visuel stop) |
| **Chiffre-preuve** | `[chiffre] % des [cible] ignorent [fait].` | `[chiffre] [unité] économisés ce mois.` | slide 1 : `[chiffre] avant / [chiffre] après` | texte à l'écran : `[chiffre] en [durée]` |
| **Erreur coûteuse** | `Cette erreur sur [X] coûte [conséquence].` | `Petite erreur, grosse addition :` | image : `L'erreur qui coûte [conséquence]` | `Tu fais [erreur] ? Tu perds [X].` |
| **Avant / après** | `[cas] : de [avant] à [après] en [durée].` | `Avant / après en une photo 👇` | carrousel : slide 1 avant, dernier après | montage split : `avant [X] / après [Y]` |
| **Question miroir** | `Comment gérez-vous [problème] ? (le mien ↓)` | `Ça vous arrive aussi, [situation] ?` | sticker question en Story | `Toi aussi tu [situation] ?` |
| **Ouverture d'histoire** | `Il y a [durée], [scène]. Voilà la leçon.` | `L'autre jour, [petite scène locale]…` | slide 1 = scène visuelle | `Hier, [scène]. Regarde ce qui s'est passé.` |
| **Liste à enjeu** | `3 signes que [problème] vous guette.` | `3 trucs utiles pour [cible locale] :` | carrousel `N façons de [résultat]` | `3 erreurs de [cible] (partie 1/N)` |
| **Négativité utile** | `Arrêtez de [pratique]. Faites [X].` | `À ne PAS faire quand [situation] :` | image : `Stop ❌ [pratique]` | `Arrête ça tout de suite.` (visuel) |
| **Autorité / coulisses** | `Ce que [métier] ne dit pas sur [X].` | `Dans les coulisses de [marque locale] :` | slide 1 : `Coulisses : [X]` | `La vérité sur [X] que [autorité] cache.` |

## d. Anti-clickbait (règle non négociable)

**La promesse du hook est TENUE dans le contenu.** Si le contenu ne délivre pas ce que le
hook promet, **la famille est mal choisie** — pas le contenu à gonfler. Le hook n'est pas
un **appât**, c'est un **contrat**. Un hook « curiosité » sans payoff = à remplacer par une
famille honnête (chiffre-preuve, avant/après).

---
*Patterns inspirés de [sergebulaev/linkedin-skills](https://github.com/sergebulaev/linkedin-skills)
et [blacktwist/social-media-skills](https://github.com/blacktwist/social-media-skills)
(MIT), **réécrits maison** — voir `NOTICE.md`. Psychologie : `rapido-meta-ads:influence-psychology`.*
