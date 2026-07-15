# Règles de construction d'un prompt (par média)

> **Prérequis absolu** : la grammaire du moteur cible a été **lue en direct** ce
> tour (`reference/grammaire-des-moteurs.md`). Ces règles décrivent l'**anatomie**
> d'un bon prompt ; les valeurs concrètes (ratios, résolutions, durées) viennent
> toujours de la lecture live, jamais d'ici.

## Principe transverse

- **Afficher le prompt complet** en bloc copiable — jamais « un prompt qui dirait
  à peu près… ». (Repris de la structure `prompt-engineer`, cf. `docs/IMPORTS-PROMPTEUR.md`.)
- **Données réelles uniquement** : charte, textes, noms viennent des MCP / de la
  KB / de l'utilisateur. Une donnée manquante se **signale** (« à confirmer côté
  backend Tunis »), elle ne s'invente pas.
- **Charte d'abord** : couleurs en **hex**, police, logo lus via `get_brand` ou
  `rapido-kb` avant d'écrire quoi que ce soit de visuel.

## Image — anatomie en 6 blocs

| Bloc | Contenu | Exemple de placeholder |
|---|---|---|
| **Sujet** | qui/quoi, en une phrase nette | `[sujet précis + attributs]` |
| **Action / pose** | ce que fait le sujet, cadrage | `[action]`, `[plan : gros plan / plan large]` |
| **Style** | rendu visuel générique (jamais un nom d'artiste) | `[photoréaliste / illustration flat / cinématique]` |
| **Lumière** | direction, qualité, ambiance | `[lumière douce latérale / contre-jour doré]` |
| **Caméra / optique** | objectif, angle, profondeur | `[85 mm, faible profondeur de champ]` |
| **Format** | ratio + résolution **lus en live** | `[ratio et résolution disponibles pour le modèle]` |

- Couleurs de la charte **en hex** dans le bloc positif.
- Texte incrusté → **protocole zéro faute** (voir « Délégation » ci-dessous).

## Vidéo — anatomie

| Bloc | Contenu | Placeholder |
|---|---|---|
| **Plan** | type de plan, sujet, décor | `[plan large / serré]`, `[sujet]` |
| **Mouvement** | caméra (travelling, dolly, statique) + mouvement dans le cadre | `[dolly avant lent]` |
| **Rythme** | découpe, temps forts, énergie | `[1 temps fort à 2 s, montée à 5 s]` |
| **Durée** | secondes — **dans la plage lue en live** pour le modèle | `[durée ∈ plage du modèle]` |
| **Son** (si le modèle le gère) | ambiance / voix / SFX | `[ambiance]`, `[voix off : "…"]` |

- Pour le **hook** (0-2 s) et la rétention, voir le pattern `hooks-viraux` et le
  skill `rapido-higgsfield:analyse-video-virale` — le prompteur **cadre**, il ne
  double pas l'analyse virale.

## Web / app (Lovable, mode B) — anatomie

| Bloc | Contenu | Placeholder |
|---|---|---|
| **Rôle / objectif** | ce que l'app doit accomplir, pour qui | `[objectif]`, `[audience]` |
| **Pages / écrans** | liste des vues et leur contenu | `[page : rôle]` |
| **Design system** | charte (hex, police), ton, références de style génériques | `[hex]`, `[police]`, `[ambiance]` |
| **Data / logique** | entités, sources, intégrations | `[entité]`, `[connecteur]` |

- Décrire en **langage naturel** ; préférences de stack dans le message initial.
- `plan_mode` pour cadrer avant génération de code.

## Prompt négatif — DÉLÉGUÉ (pas de doublon ici)

La **bibliothèque de négatifs** (base commune + négatifs par type de visuel) et le
**protocole ZÉRO FAUTE** (texte incrusté, correction chirurgicale via `images_to_image`)
sont maintenus **une seule fois**, dans le skill **`rapidocms:prompts-visuels-pro`**.

> Le directeur de prompts **appelle** ce skill pour la couche négatif/texte — il
> **ne recopie pas** sa bibliothèque (règle anti-doublon maison). Idem pour la
> structure 6 blocs et la capitalisation : `rapidocms:prompt-engineering-visuel`
> et `rapidocms:bibliotheque-prompts`.

## INTERDITS encodés (non négociables)

1. **Aucune IP tierce** — pas de marque, franchise, produit ou logo d'un tiers
   dans un prompt (ex. « façon Star Wars », « packaging Coca-Cola »). Exception
   unique : la **marque du client** (ou une IP dont les droits sont détenus).
2. **Aucun « style de [artiste vivant] »** — jamais « in the style of [réalisateur/
   artiste] ». On **décrit l'effet visuel générique** (« symétrie, palette pastel,
   plans larges statiques ») au lieu de nommer l'auteur.
3. **Aucun personnage sous licence** — pas de héros, mascotte ou personnage de
   fiction protégé, même « inspiré de ».
4. **Texte incrusté → protocole zéro faute** de `rapidocms:prompts-visuels-pro`
   (texte exact entre guillemets, validation orthographique avant génération,
   5 mots max, vérification après génération, correction chirurgicale).

> Ces interdits sont **doublés par un garde automatique** : le hook PreToolUse
> `anti-ip.py` scanne les prompts sortants (liste maison `reference/ip-a-risque.md`)
> et demande confirmation avec avertissement en cas de détection. Le garde ne
> remplace pas la règle — il rattrape les oublis.

### Formulation de remplacement (au lieu de nommer une IP / un artiste)

| À éviter | À écrire à la place |
|---|---|
| « in the style of Wes Anderson » | « composition symétrique frontale, palette pastel, décors façon maison de poupée » |
| « ambiance Blade Runner » | « néons saturés, pluie nocturne, brume, contrastes bleu/magenta » |
| « packaging façon Apple » | « produit épuré sur fond neutre, lumière studio douce, minimalisme premium » |
| « un héros type super-héros Marvel » | « personnage original en costume [couleurs charte], posture héroïque » |
