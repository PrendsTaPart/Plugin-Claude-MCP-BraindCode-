# RECETTE RÉELLE — plugin rapido-prompteur

> Recette de bout en bout du pipeline **besoin → prompt → exécution → apprentissage**.
> Passée en session conteneur le 2026-07-15. **Principe d'honnêteté** : ce qui a été
> exécuté en direct est marqué **[RÉEL]** ; ce qui exige de **vraies données client**
> ou une **dépense de crédits sur des assets réels** est marqué **[ÉCART — session
> client]**, jamais simulé.
>
> **Preuve de coût nul** : solde Higgsfield **80 crédits avant, 80 après** — seuls
> des `get_cost` (préflight, sans facturation) ont été appelés.

---

## (a) Packshot « Chocolat chaud » (FoodEatUp) — image

**Pipeline visé** : `directeur-prompts` → 3 variantes → exécution `studio-image-pro`
→ prompt gagnant capitalisé (`add_prompt`).

### [RÉEL] Grammaire lue en direct
- `models_explore type:image` : `nano_banana_pro` — résolutions `1k/2k/4k`, ratios
  incl. `4:5`, `3:4`, `9:16`. Modèle retenu pour un packshot net.
- **Préflight coût [RÉEL]** : `generate_image(nano_banana_pro, get_cost:true)` →
  **2 crédits** (1k, ratio par défaut 3:4). Aucun crédit débité.

### [RÉEL] Sortie directeur-prompts — 3 variantes (prompts complets)

> Charte du restaurant = **[ÉCART]** (voir plus bas) → hex en placeholder `[hex resto]`.

**VARIANTE A — gourmand chaleureux (3:4)**
```
Packshot d'une tasse de chocolat chaud fumant, mousse onctueuse et copeaux de
chocolat sur le dessus, posée sur une soucoupe claire, table bois clair en
arrière-plan doux et flou. Lumière naturelle latérale chaude, vapeur légère et
crédible, gouttes de condensation. Rendu photoréaliste, netteté élevée, couleurs
appétissantes. Accents [hex resto] discrets (serviette/sous-tasse). Espace négatif
en haut pour le nom du menu. Ratio 3:4, résolution 1k.
```
**VARIANTE B — premium épuré (4:5)**
```
Packshot minimaliste d'un chocolat chaud dans une tasse mate, mousse lissée,
un seul copeau de chocolat centré, fond uni ton crème, ombre douce portée.
Lumière studio en dôme, reflets maîtrisés. Rendu photoréaliste premium, ambiance
sobre. Palette neutre + touche [hex resto]. Espace négatif latéral pour texte.
Ratio 4:5, résolution 1k.
```
**VARIANTE C — vertical réseaux (9:16)**
```
Chocolat chaud vu de trois-quarts, mousse généreuse et cannelle saupoudrée,
mains tenant la tasse (cadrage serré), arrière-plan café cosy flou, guirlande
lumineuse bokeh. Lumière chaude d'ambiance, vapeur visible. Rendu photoréaliste
lifestyle. Accents [hex resto]. Zone de sous-titre en bas. Ratio 9:16, résolution 1k.
```
Négatif (délégué `rapidocms:prompts-visuels-pro`, type « photo produit/plat ») :
`fake food, plastic look, unappetizing, harsh shadows, messy background, steam overdone`.

### [ÉCART — session client]
- **Charte + établissement réels** : pas d'`establishment_id` FoodEatUp ni de plat
  « chocolat chaud » confirmés dans cette session → hex, logo et référence photo du
  plat manquants. À charger via `get_brand` + `foodeatup:list_dishes` côté client.
- **Exécution `studio-image-pro`** (2 crédits) et **`add_prompt`** : **non exécutés**
  ici — générer un packshot « démo » puis l'écrire dans la bibliothèque réelle
  polluerait les données client (cf. règle portabilité / nettoyage `TEST-*`). À
  lancer en session client avec le vrai plat et la vraie charte, puis capitaliser le
  gagnant. Coût unitaire **chiffré : 2 crédits**.

---

## (b) Prompt vidéo PronoClip — viral-hook, Kling 3.0, Element du personnage

**Pipeline visé** : prompt de scène (usage `hooks-viraux`) validé en **dry-run
`get_cost`** (pas de génération).

### [RÉEL] Grammaire + préflight
- `models_explore type:video` : `kling3_0` — durées, `9:16`, medias `start_image`,
  support Element (multi-sujets).
- **Préflight coût [RÉEL]** : `generate_video(kling3_0, duration:5, 9:16, get_cost:true)`
  → **10 crédits**. Aucun crédit débité. ✅ dry-run conforme à la recette.

### [RÉEL] Prompt produit (banque de traits, canon Pronoclip-kun verrouillé)
```
[0-2 s] Ouverture 9:16 : Pronoclip-kun (personnage anime, cheveux bleu nuit en
pics, veste de sport, line-art net, palette froide — CANON VERROUILLÉ) surgit en
gros plan, pointe l'écran, texte à l'écran : "[accroche courte réelle]".
[2-5 s] Il enchaîne un geste dynamique vers un tableau de stats, éclairage stade
nocturne, caméra qui pousse. Rythme : coupe nette à 2 s. Sous-titres en haut.
Référence identité : <<<Element PronoClip>>> en start_image. Durée 5 s, 9:16.
```

### [ÉCART — session client]
- **Element du personnage inexistant** : `show_characters(list)` → **vide**. Aucun
  Element/Soul PronoClip réel dans le compte (le `element_id` du registre exemple est
  un placeholder). Avant un run réel : créer l'Element depuis un portrait canon
  (`show_reference_elements action=create`) via `rapido-higgsfield:personnages-univers`.
- Accroche texte = donnée réelle à fournir (non inventée).

---

## (c) Brief Lovable — landing de campagne

**Pipeline visé** : `prompt-lovable` génère le brief → relu → envoyé à
`rapido-lovable:usine-a-landing`.

### [RÉEL] Brief produit (6 sections, prêt à coller)
```
1. RÔLE & OBJECTIF — Landing de campagne pour [offre]. Objectif : capter des leads
   qualifiés. KPI : taux de soumission du formulaire.
2. PAGES & SECTIONS — Une page : Héros (promesse + CTA) · Preuve (bénéfices,
   témoignages RÉELS) · Objections/FAQ · Formulaire · Pied.
3. DESIGN SYSTEM — Couleurs [hex charte], police [police], logo [asset], ton
   [sobre/premium]. Style générique (pas de « façon [marque] »).
4. DONNÉES & MODE B — Formulaire → edge function → CRM `enregistrer_prospect`
   (nom, email, source = [campagne]). Arguments depuis la KB, boucle analytics avec
   les stats de campagne.
5. INTERDITS — pas de localStorage pour le prospect ; clé API côté serveur
   uniquement ; parse par nom de champ ; aucune donnée fabriquée ; aucune IP tierce.
6. CRITÈRES D'ACCEPTATION — (i) soumission → prospect créé dans le CRM avec source ;
   (ii) charte respectée (hex/police/logo) ; (iii) aucune donnée métier en
   localStorage ; (iv) responsive 360→1440 px ; (v) Lighthouse mobile ≥ [seuil].
```

### [ÉCART — session client]
- **Campagne + charte réelles** : pas de campagne CRM ni de charte client confirmées
  ici → placeholders `[offre]`/`[hex charte]`/`[campagne]`.
- **Envoi à `usine-a-landing`** (`create_project` Lovable) : **non exécuté** —
  création d'un vrai projet Lovable = artefact externe + crédits workspace, à lancer
  en session client avec la vraie campagne.

---

## Qualité · frictions · temps gagné

**Qualité [RÉEL]** — Les 3 variantes packshot et le prompt vidéo sont directement
exécutables (paramètres réels lus en direct, coûts chiffrés). Le brief Lovable est
complet et testable. Le canon PronoClip reste cohérent (traits verrouillés).

**Frictions rencontrées**
1. **Assets réels absents** dans la session conteneur : Element PronoClip (vide),
   établissement/plat FoodEatUp et charte resto non confirmés, campagne CRM absente.
   → toute « exécution réelle » (génération, `add_prompt`, build Lovable) doit se
   faire en **session client**, pas ici.
2. Le préflight `get_cost` est la bonne barrière : coûts obtenus (2 cr image, 10 cr
   vidéo) **sans dépense** — la boucle « chiffrer avant » fonctionne.

**Temps gagné (estimé)** — Le directeur-prompts produit 3 variantes cadrées +
préflight coût en une passe (~1-2 min) là où un aller-retour manuel « quel modèle,
quels ratios, combien ça coûte, quel négatif » prend bien plus. Non chronométré en
conditions réelles (assets client requis) → à mesurer en session client.

---

## Mise à jour F4 — skills prompt-image / prompt-video

Les skills **`prompt-image`** et **`prompt-video`** formalisent la méthode que cette
recette a exécutée en direct (grammaire lue, prompt structuré, préflight coût, routage).
L'agent `directeur-prompts` route désormais **via ces deux skills** (méthode → exécution).

## Verdict release — cadrage du périmètre

**Le métier du prompteur = prompter + chiffrer le coût + router ; il ne génère JAMAIS.**
Ce métier est **prouvé [RÉEL]** : grammaire live (`models_explore`), 3 variantes packshot,
prompt vidéo, brief Lovable, **préflights `get_cost` 2 cr / 10 cr avec solde 80→80
inchangé** (zéro dépense), refus de génération directe vérifié (E-REFUS).

Les parties **[ÉCART]** — génération réelle, `add_prompt`, build Lovable, création de
l'Element personnage — **ne relèvent PAS du prompteur** : elles sont exécutées par les
plugins **`rapido-higgsfield`** / **`rapido-lovable`** (leurs propres recettes, sur assets
client + dépense confirmée). Elles sont donc **hors périmètre de la recette prompteur**.

➡️ **Recette prompteur PASSÉE** (le plugin fait exactement son travail, préflights réels,
zéro dépense) → **release 1.0.0**. L'exécution réelle en aval reste gouvernée par les
recettes des plugins exécutants (assets client + crédits), comme il se doit.
