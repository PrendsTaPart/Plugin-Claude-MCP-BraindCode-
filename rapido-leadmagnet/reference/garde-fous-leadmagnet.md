# Garde-fous — rapido-leadmagnet

Encodés (hook déterministe + règles de skill), indépendants du modèle. Les seuils
client vivent dans `./rapido-kb/` (défauts prudents ici).

## 1. RGPD capture

- **Consentement explicite** au formulaire : checkbox **non pré-cochée**, mention
  claire de l'échange (« recevez le guide + nos conseils »).
- **Double opt-in** proposé **par défaut** (email de confirmation AVANT le lien) —
  activable/désactivable en `rapido-kb/marketing/`.
- **Désinscription honorée immédiatement** : retrait de séquence + tag CRM. Un
  contact désinscrit n'est jamais re-sollicité.

## 2. Gate délivrabilité OBLIGATOIRE

Avant **tout** envoi de séquence de nurturing : passer le gate
`rapido-marketing:delivrabilite-email` (mode newsletter). Aucun lot n'est envoyé
sans ce feu vert.

## 3. LinkedIn « commente pour recevoir » — SEMI-AUTO (décision LM0 : GO)

Claude prépare les **réponses aux commentaires** et les **DM** (avec le lien) **en
brouillons** ; l'**humain envoie**. Dédup des commentaires traités dans une **table
n8n** (`memoire-operationnelle`). **Jamais** d'Unipile ni d'automatisation d'envoi
LinkedIn (CGU). Cohérent avec `rapidocms:social-selling-linkedin` /
`rapido-marketing` selon le canal.

## 4. Vidéos IA sur Meta

`self_ai_disclosure` **activé** pour toute vidéo générée diffusée sur Meta (règle
`rapido-higgsfield:usine-video-marketing`).

## 5. Budget ads confirmé

Campagnes Meta créées en **PAUSED**, **coût max récapitulé**, **activation sur
confirmation écrite** dans un tour séparé — imposé par le hook `garde-budget-ads`
(en plus des hooks de `rapido-meta-ads`).

## 6. Attribution MIT

Frameworks francisés/réimplémentés de dépôts MIT (content-vault, copy-thief,
hormozi-offer-audit, lead-magnet-responder, pdf-ebook-generator) → `NOTICE.md`.
Aucun corps de texte copié ; le code GPL (AI-eBook) n'est **jamais** fusionné.

## 7. Focus — un seul lead magnet en production à la fois

Jamais plus d'**un** lead magnet en production simultanée **sans confirmation**
explicite (évite la dispersion). L'agent `chef-usine-leadmagnet` le fait respecter.

## 8. Rien d'inventé

Preuve/chiffre sur une landing = **donnée réelle du CRM uniquement**. Stats de
mesure **par script**, sources citées. Une donnée absente reste absente.
